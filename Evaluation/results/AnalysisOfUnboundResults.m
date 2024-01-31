clear
close all;


filters=["UeUfFs" "UeUfVs" "UeArFs" "UeArVs" ];
tables=["Table1" "Table2" "Table3" "Table4"];

val=input("Which results do you want to analyze? Type \n 1 - for completeness\n 2 - for consistency\n");

if val==1
    check="completeness";
    filePath='./unboundedResults_completeness.csv';
    averageTablePath='./.unboundedResults_completeness.csv';

elseif val==2 
    check="consistency";
    filePath='./unboundedResults_consistency.csv';
    averageTablePath='./.unboundedResults_consistency.csv';
else
    disp("intput not valid")
end

Table = readtable(filePath); 

checkStatistics(Table,check,tables,filters);

computeAverageTable(filePath,averageTablePath);

AverageTable = readtable(averageTablePath); 

disp('--------------------------')
disp('Generic statistics')


if val==1
    disp(strcat("*****Completeness ", check, "*****"));
    for filter = filters
        rf=rowfilter(Table);
        FilteredTable2=Table(rf.check==check & rf.encoding==filter & rf.result=="Complete" & rf.expectedResult=="Complete", :);
        Time1=FilteredTable2(:,"time");
        timeValues1=Time1{:,1};
    
        FilteredTable3=Table(rf.check==check & rf.encoding==filter & rf.result=="Incomplete" & rf.expectedResult=="Incomplete", :);
        Time2=FilteredTable3(:,"time");
        timeValues2=Time2{:,1};
        timeValues=[timeValues1; timeValues2];
        disp(strcat("check: ", check, "   encoding: ", filter, "       mean: ", num2str(mean(timeValues)), "      min: ", num2str(min(timeValues)), "      max: ", num2str(max(timeValues)),"      std: ", num2str(std(timeValues))));
    end
end

if val==2 
    disp(strcat("*****Consistency ", check, "*****"));
    for filter = filters
        rf=rowfilter(Table);
        FilteredTable3=Table(rf.check==check & rf.encoding==filter & rf.result=="Inconsistent" & rf.expectedResult=="Inconsistent", :);
        Time2=FilteredTable3(:,"time");
        timeValues2=Time2{:,1};
        timeValues=timeValues2;
        disp(strcat("check: ", check, "   encoding: ", filter, "       mean: ", num2str(mean(timeValues)), "      min: ", num2str(min(timeValues)), "      max: ", num2str(max(timeValues)),"      std: ", num2str(std(timeValues))));
    end
end

function [] = checkStatistics(Table,check,tables,filters)
   
       for filter = filters
          filterfinalcount=0;
          filterfinalcorrect=0;
          for table = tables
            
                rf=rowfilter(Table);
                %filter the entries that have the same result
                FilteredTable=Table(rf.encoding==filter & rf.table==table & rf.check==check,:);
        
                Result=FilteredTable(:,"result");
                result=Result{:,1};
                ExpectedResult=FilteredTable(:,"expectedResult");
                expectedResult=ExpectedResult{:,1};
            
                count=0;
                for i=1:1:size(result,1)
                    filterfinalcount=filterfinalcount+1;
                    if(strcmp(result{i,1},expectedResult{i,1})==1)
                        count=count+1;
                        filterfinalcorrect=filterfinalcorrect+1;
                    else
                        if(strcmp(result{i,1},"Unknown")~=1)
                            disp(strcat("error!!!: table: ", table,"  check: ",check, "  encoding: ", filter, " inputFile: ", FilteredTable{i,"inputfile"}, " Result: ", result{i,1}, " Expected Result: ",expectedResult{i,1}));
                        else
                            %disp(strcat("difference!!!: table: ", table,"  check: ",check, "  encoding: ", filter, " inputFile: ", FilteredTable{i,"inputfile"}, " Result: ", result{i,1}, " Expected Result: ",expectedResult{i,1}));
                        end
                    end
                end
                disp(strcat("table: ", table,"  check: ",check, "  encoding: ", filter, "  correct verdicts: ", num2str(count/size(result,1)*100), '%'));
          end
          disp(strcat("check: ",check, "  encoding: ", filter, "  correct verdicts: ", num2str(filterfinalcorrect/filterfinalcount*100), '%'))
       end
       idx = isnan(Table.time);
       not_nan_time = sum(Table.time(~idx))/60;
       is_nan_time=sum(idx)*2*60;
      disp(strcat("Total Time (min): ",num2str(not_nan_time+is_nan_time)));
end


function [] = computeAverageTable(filePath,averageTablePath)
    disp("Wait... Computing the average results..");
    faverageTable=fopen(averageTablePath,'w');
    fid = fopen(filePath, 'r');
    initline=fgetl(fid);
    fprintf(faverageTable,'%s\n',initline);
    tline = fgetl(fid);
    visited=[];
    counter=0;
    while ischar(tline)
       ret=split(tline,',',2);
       [tablePath, TableName, encoding, check, result, expectedResult, time]=ret{:};

       if(strcmp(result,expectedResult)==1 && ~any(strcmp(visited,strcat(tablePath,encoding))))
           fid2 = fopen(filePath, 'r');
           tline2 = fgetl(fid2);
           tline2 = fgetl(fid2);
    
           numresults=0;
           timeresults=0;
           while ischar(tline2)
                if(fid2>fid)
                    if(~any(strcmp(visited,strcat(tablePath,encoding))))
                        ret2=split(tline2,',',2);
                        [tablePath2, TableName2, encoding2, check2, result2, expectedResult2, time2]=ret2{:};
                        if(strcmp(result2,expectedResult2)==1 && strcmp(tablePath2,tablePath)==1  && strcmp(TableName2,TableName)==1 && strcmp(encoding2,encoding)==1 &&  strcmp(check2,check)==1)
                            numresults=numresults+1;
                            timeresults=timeresults+str2num(time2);
                        end
                    end
                end
                tline2 = fgetl(fid2);
           end
           visited = cat(2, visited, {strcat(tablePath,encoding)});
           avgtime=timeresults/numresults;
           fprintf(faverageTable,'%s,%s,%s,%s,%s,%s,%s,%f\n',tablePath, TableName, encoding,  check, result, expectedResult,avgtime);
       end
       counter=counter+1;
       tline = fgetl(fid);
    end
    fclose(fid);
end
