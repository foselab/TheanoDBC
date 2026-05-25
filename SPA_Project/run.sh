#!/usr/bin/env bash

# Detect OS and set Python command
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OS" == "Windows_NT" ]]; then
    python_cmd="py -3"
    FIND_EXEC="find"
else
    python_cmd="python3"
    FIND_EXEC="find"
fi

# Command
cmd=(java -jar ../Theano.jar)

print_usage() {
    cat <<EOF
Usage: bash run.sh [OPTIONS]

Options:
  -k, --keep             keep generated files in LM_Challenges folder on exit
  -i N, --iterations N   run each OTA N times (default: 50)
  -h, --help             show this help message
EOF
}

# SETTINGS
CLEAN_ON_EXIT=true
ITERATIONS=50

while [[ $# -gt 0 ]]; do
    case "$1" in
        -k|--keep)
            CLEAN_ON_EXIT=false
            shift
            ;;
        -i)
            if [[ -z "$2" || "$2" == -* ]]; then
                echo "Error: -i requires a numeric argument."
                print_usage
                exit 1
            fi
            if ! [[ "$2" =~ ^[0-9]+$ ]]; then
                echo "Error: iterations must be a positive integer."
                exit 1
            fi
            ITERATIONS="$2"
            shift 2
            ;;
        --iterations)
            if [[ -z "$2" || "$2" == -* ]]; then
                echo "Error: --iterations requires a numeric argument."
                print_usage
                exit 1
            fi
            if ! [[ "$2" =~ ^[0-9]+$ ]]; then
                echo "Error: iterations must be a positive integer."
                exit 1
            fi
            ITERATIONS="$2"
            shift 2
            ;;
        --iterations=*)
            ITERATIONS="${1#*=}"
            if ! [[ "$ITERATIONS" =~ ^[0-9]+$ ]]; then
                echo "Error: iterations must be a positive integer."
                exit 1
            fi
            shift
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            print_usage
            exit 1
            ;;
    esac
done

if [[ "$ITERATIONS" -lt 1 ]]; then
    echo "Error: iterations must be at least 1."
    exit 1
fi

# PATHS TO SAVE RESULTS
RESULT_PATH="./results"
mkdir -p "$RESULT_PATH"
SAFE_OTA_RESULTS="$RESULT_PATH/safe.csv"
UNSAFE_OTA_RESULTS="$RESULT_PATH/unsafe.csv"

# PATH TO ALL CONFIGURATIONS
LMCHALLENGES_FOLDER="../LM_Challenges"

# INITIAL CONFIGURATION FILES
INIT_CONFIG=("TSM_v1" "FSM_v1" "TUI_v1" "REG_v1" "NLG_v1" "NN_v1" "EB_v1" "AP_v1" "SWIM_v1" "EUL_v1")
UNSAFE_UPDATES=("TSM_v2" "FSM_v2" "TUI_v3" "REG_v2" "NLG_v2" "NN_v2" "EB_v2" "AP_v2" "SWIM_v2" "EUL_v2")
SAFE_UPDATES=("TSM_v3" "FSM_v3" "TUI_v2" "REG_v3" "NLG_v3" "NN_v3" "EB_v3" "AP_v3" "SWIM_v3" "EUL_v3")
#INIT_CONFIG=("EUL_v1")
#UNSAFE_UPDATES=("EUL_v2")
#SAFE_UPDATES=("EUL_v3")

# CLEANUP FUNCTION
cleanup_files() {
	find "$LMCHALLENGES_FOLDER" -type f \( -name "*.py" -o -name "*.bak" -o -name "*_refinement.rt" -o -name "*_composition.rt" -o -name "*.smt" \) -delete
}

get_result() {
	local input_str="$1"
	if [[ "$input_str" == *"unsat"* ]]; then
		echo "safe"
	elif [[ "$input_str" == *"sat"* ]]; then
		echo "unsafe"
	else
		echo "unknown"
	fi
}

# Run refinement, it takes as input the name of the OTA and the file to save the results
run_refinement() {
	local ota=$1
	local refinement_time_file=$2

	# Model paths
	model_name="${ota/_v[0-9]/}" # e.g. TSM
	model_path="${LMCHALLENGES_FOLDER}/${model_name}" # e.g. TSM
	
	# Current system and OTA paths
	system_name="${model_name}_v1" # e.g TSM_v1
	system_name_path="${model_path}/${system_name}.rt" # e.g. TSM_v1.rt
	ota_file_path="${model_path}/${ota}.rt" # e.g. TSM_v3.rt
	refinement_file_path="${model_path}/${ota}_refinement.rt" # e.g. TSM_v3_refinement.rt

	# Paths for generated scripts
	refinement_script_path_dc="${model_path}/${ota}_refinement_dc.py" # e.g. TSM_v3_refinement.py
	refinement_script_path_sc="${model_path}/${ota}_refinement_sc.py" # e.g. TSM_v3_refinement.py
	ota_file_smtlib_path="${model_path}/${ota}.smt" # e.g. TSM_v3.smt
	smtlib_script_path="${model_path}/${ota}_smtlib.py" # e.g. TSM_v3_smtlib.py

	# Check if required files exist
	if [[ ! -f "$system_name_path" || ! -f "$ota_file_path" ]]; then
		echo "Missing required file(s) for $ota, skipping..." >> "$refinement_time_file"
		return
	fi

	# Get tables 
	system_file_content=$(cat "$system_name_path")
	ota_file_content=$(cat "$ota_file_path")
	
	# Create refinement file
	{
		echo "table ${system_name}"
		echo "$system_file_content"
		echo "endtable"
		echo "table ${ota}"
		echo "$ota_file_content"
		echo "endtable"
	} > "$refinement_file_path"

	# Check if refinement file exists
	if [ -f "$refinement_file_path" ]; then
		for ((i = 1; i <= ITERATIONS; i++)); do
			
			echo "Running $ota, iteration $i..."

			# if the OTA is FSM then we need to run composition first
			if [[ "$ota" == *"FSM"* ]]; then
				composition_file_path="${model_path}/${ota}_composition.rt" # e.g. FSM_v1_composition.rt
				
				# Create composition file
				if ! "${cmd[@]}" -i "$ota_file_path" -o "$composition_file_path" -t composition -e BeUfFs -t composition -b 6 -a > /dev/null 2>&1; then
					echo "$ota,$i,CompositionFailed" >> "$refinement_time_file"
					continue
				fi

				# Create refinement file with composition
				{
					echo "table ${system_name}"
					cat "$system_name_path"
					echo
					echo "endtable"
					echo "table ${ota}"
					cat "$composition_file_path"
					echo
					echo "endtable"
				} > "$refinement_file_path"
			fi

			# Generate refinement script with double check
			if ! "${cmd[@]}" -i "$refinement_file_path" -o "$refinement_script_path_dc" -t refinement > /dev/null 2>&1; then
				echo "$ota,$i,JavaFailed,Theano_DC" >> "$refinement_time_file"
				continue
			fi

			# Generate refinement script with single check
			if ! "${cmd[@]}" -i "$refinement_file_path" -o "$refinement_script_path_sc" -t refinement -s > /dev/null 2>&1; then
				echo "$ota,$i,JavaFailed,Theano_SC" >> "$refinement_time_file"
				continue
			fi

			# Generate SMT-LIB file (single check)
			"${cmd[@]}" -i "$refinement_file_path" -o "$smtlib_script_path" -t smtlib > /dev/null 2>&1
			$python_cmd "$smtlib_script_path" > "$ota_file_smtlib_path"

			# Measure time for refinement with double check
			start_time=$(date +%s.%N)

			# Run refinement check with double check
			theano_result_dc="$($python_cmd "$refinement_script_path_dc")"
			if [ $? -ne 0 ]; then
				echo "$ota,$i,PythonFailed,Theano_DC" >> "$refinement_time_file"
				continue
			fi
			
			end_time=$(date +%s.%N)
			elapsed=$(python -c "print($end_time-$start_time)")

			echo -e "\tTheano (Double Check): $theano_result_dc" 
			echo "$ota,$i,$elapsed,$theano_result_dc,Theano_DC" >> "$refinement_time_file"

			# Measure time for refinement with single check
			start_time=$(date +%s.%N)

			# Run refinement check with single check
			theano_result_sc="$($python_cmd "$refinement_script_path_sc")"
			if [ $? -ne 0 ]; then
				echo "$ota,$i,PythonFailed,Theano_SC" >> "$refinement_time_file"
				continue
			fi
			
			end_time=$(date +%s.%N)
			elapsed=$(python -c "print($end_time-$start_time)")

			echo -e "\tTheano (Single Check): $theano_result_sc" 
			echo "$ota,$i,$elapsed,$theano_result_sc,Theano_SC" >> "$refinement_time_file"	

			# Measure time for refinement check with SMT-LIB file with Z3
			start_time=$(date +%s.%N)
			z3_res_str=$(z3 $ota_file_smtlib_path -T:10 | head -n 1)
			end_time=$(date +%s.%N)
			z3_res=$(get_result "$z3_res_str")
			elapsed=$(python -c "print($end_time-$start_time)")
			echo -e "\tz3: $z3_res"
			echo "$ota,$i,$elapsed,$z3_res,z3" >> "$refinement_time_file"

			# Measure time for refinement check with SMT-LIB file with cvc5
			start_time=$(date +%s.%N)
			cvc5_res_str=$(cvc5 $ota_file_smtlib_path --tlimit-per=10000 | head -n 1)
			end_time=$(date +%s.%N)
			cvc5_res=$(get_result "$cvc5_res_str")
			elapsed=$(python -c "print($end_time-$start_time)")
			echo -e "\tcvc5: $cvc5_res"
			echo "$ota,$i,$elapsed,$cvc5_res,cvc5" >> "$refinement_time_file"
		done
	else
		echo "FAIL TO CREATE FILE for $ota" >> "$refinement_time_file"
	fi
}

trap 'echo -e "\nCtrl+C detected. Exiting..."; [ "$CLEAN_ON_EXIT" = true ] && cleanup_files; exit 0' SIGINT

echo "OTA,Iteration,Time,Result,Solver" > "$SAFE_OTA_RESULTS"
echo "OTA,Iteration,Time,Result,Solver" > "$UNSAFE_OTA_RESULTS"

echo -e "Running OTA...\n"

# RUN REFINEMENT FOR SAFE UPDATES
for ota in "${SAFE_UPDATES[@]}"; do
	run_refinement "$ota" "$SAFE_OTA_RESULTS"
done

# RUN REFINEMENT FOR UNSAFE UPDATES
for ota in "${UNSAFE_UPDATES[@]}"; do
	run_refinement "$ota" "$UNSAFE_OTA_RESULTS"
done

# CLEANUP FILES
if [ "$CLEAN_ON_EXIT" = true ]; then
	cleanup_files
fi

echo -e "OTA times results saved to $SAFE_OTA_RESULTS, $UNSAFE_OTA_RESULTS\n"
