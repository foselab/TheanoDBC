#!/bin/bash

# SETTINGS
CLEAN_ON_EXIT=true
ITERATIONS=50
LOGGING=true

# PATHS TO SAVE RESULTS
RESULT_PATH="./results"
mkdir -p "$RESULT_PATH"
SAFE_OTA_RESULTS="$RESULT_PATH/safe.txt"
UNSAFE_OTA_RESULTS="$RESULT_PATH/unsafe.txt"

# PATH TO ALL CONFIGURATIONS
LMCHALLENGES_FOLDER="../LM_Challenges"

# INITIAL CONFIGURATION FILES
INIT_CONFIG=("TSM_v1" "FSM_v1" "TUI_v1" "REG_v1" "NLG_v1" "NN_v1" "EB_v1" "AP_v1" "SWIM_v1" "EUL_v1")
UNSAFE_UPDATES=("TSM_v2" "FSM_v2" "TUI_v2" "REG_v2" "NLG_v2" "NN_v2" "EB_v2" "AP_v2" "SWIM_v2" "EUL_v2")
SAFE_UPDATES=("TSM_v3" "FSM_v3" "TUI_v3" "REG_v3" "NLG_v3" "NN_v3" "EB_v3" "AP_v3" "SWIM_v3" "EUL_v3")

# CLEANUP FUNCTION
cleanup_files() {
	find "$LMCHALLENGES_FOLDER" -type f \( -name "*.py" -o -name "*.bak" -o -name "*_refinement.rt" -o -name "*_composition.rt" \) -delete
}

# Run refinement, it takes as input the name of the OTA and the file to save the results
run_refinement() {
	local ota=$1
	local refinement_time_file=$2

	model_name="${ota/_v[0-9]/}" # e.g. TSM
	model_path="${LMCHALLENGES_FOLDER}/${model_name}" # e.g. TSM
	
	system_name="${model_name}_v1" # e.g TSM_v1
	system_name_path="${model_path}/${system_name}.rt" # e.g. TSM_v1.rt
	ota_file_path="${model_path}/${ota}.rt" # e.g. TSM_v3.rt
	refinement_file_path="${model_path}/${ota}_refinement.rt" # e.g. TSM_v3_refinement.rt
	refinement_script_path="${model_path}/${ota}_refinement.py" # e.g. TSM_v3_refinement.py

	# Check if required files exist
	if [[ ! -f "$system_name_path" || ! -f "$ota_file_path" ]]; then
		echo "Missing required file(s) for $ota, skipping..." >> "$refinement_time_file"
		return
	fi

	# Get tables 
	system_file_content=$(cat "$system_name_path")
	ota_file_content=$(cat "$ota_file_path")
	
	# Create refinement file
	echo "table ${system_name}" > "$refinement_file_path"
	echo "$system_file_content" >> "$refinement_file_path"
	echo "endtable" >> "$refinement_file_path"

	echo "table ${ota}" >> "$refinement_file_path"
	echo "$ota_file_content" >> "$refinement_file_path"
	echo "endtable" >> "$refinement_file_path"

	# Check if refinement file exists
	if [ -f "$refinement_file_path" ]; then
		for ((i = 1; i <= ITERATIONS; i++)); do
			
			if [ "$LOGGING" = true ]; then
				echo "Running $ota, iteration $i..."
			fi

			# if the OTA is FSM then we need to run composition first
			if [[ "$ota" == *"FSM"* ]]; then
				composition_file_path="${model_path}/${ota}_composition.rt" # e.g. FSM_v1_composition.rt
				
				start_time_comp=$(date +%s.%N)

				# Create composition file
				if ! timeout 100 java -jar ./Theano.jar -i "$ota_file_path" -o "$composition_file_path" -t composition -e BeUfFs -t composition -b 6 -a > /dev/null 2>&1; then
					echo "$ota,$i,CompositionFailed" >> "$refinement_time_file"
					continue
				fi

				end_time_comp=$(date +%s.%N)
				elapsed_comp=$(python -c "print($end_time_comp-$start_time_comp)")

				# Create refinement file with composition
				echo "table ${system_name}" > "$refinement_file_path"
				echo "$system_file_content" >> "$refinement_file_path"
				echo "endtable" >> "$refinement_file_path"
				echo "table ${ota}" >> "$refinement_file_path"
				echo $(cat "$composition_file_path") >> "$refinement_file_path"
				echo "endtable" >> "$refinement_file_path"

				start_time=$(date +%s.%N)

				# Run Java and Python scripts
				if ! java -jar ./Theano.jar -i "$refinement_file_path" -o "$refinement_script_path" -t refinement > /dev/null 2>&1; then
					echo "$ota,$i,JavaFailed" >> "$refinement_time_file"
					continue
				fi

				if ! timeout 100 python "$refinement_script_path" > /dev/null 2>&1; then
					echo "$ota,$i,PythonFailed" >> "$refinement_time_file"
					continue
				fi

				end_time=$(date +%s.%N)
				elapsed=$(python -c "print($end_time-$start_time)")
				tot_elapsed=$(python -c "print($elapsed+$elapsed_comp)")

				#echo "$ota,$i,$tot_elapsed" >> "$refinement_time_file"
				echo "$tot_elapsed" >> "$refinement_time_file"

			else
				start_time=$(date +%s.%N)

				# Run Java and Python scripts
				if ! java -jar ./Theano.jar -i "$refinement_file_path" -o "$refinement_script_path" -t refinement > /dev/null 2>&1; then
					echo "$ota,$i,JavaFailed" >> "$refinement_time_file"
					continue
				fi

				if ! timeout 100 python "$refinement_script_path" > /dev/null 2>&1; then
					echo "$ota,$i,PythonFailed" >> "$refinement_time_file"
					continue
				fi

				end_time=$(date +%s.%N)
				elapsed=$(python -c "print($end_time-$start_time)")

				#echo "$ota,$i,$elapsed" >> "$refinement_time_file"
				echo "$elapsed" >> "$refinement_time_file"

			fi
		done
	else
		echo "FAIL TO CREATE FILE for $ota" >> "$refinement_time_file"
	fi
}

trap 'echo -e "\nCtrl+C detected. Exiting..."; [ "$CLEAN_ON_EXIT" = true ] && cleanup_files; exit 0' SIGINT

#echo "OTA,Iteration,ElapsedTime(s)" > "$SAFE_OTA_RESULTS"
: > "$SAFE_OTA_RESULTS"
#echo "OTA,Iteration,ElapsedTime(s)" > "$UNSAFE_OTA_RESULTS"
: > "$UNSAFE_OTA_RESULTS"
echo "Running OTA..."

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

echo -e "OTA times results saved to $SAFE_OTA_RESULTS and $UNSAFE_OTA_RESULTS"
