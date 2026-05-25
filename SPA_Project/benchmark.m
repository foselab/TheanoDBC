function print_statistics(mean, median, std, min, max)
    fprintf('\tAverage: %.3f\n', mean);
    fprintf('\tMedian: %.3f\n', median);
    fprintf('\tStandard Deviation: %.3f\n', std);
    fprintf('\tMin: %.3f\n', min);
    fprintf('\tMax: %.3f\n', max);
end

function print_boxplot(filename, d, labels, fig_title)
    blue = [0, 114, 178]/255;
    red = [230, 159, 0]/255;
    gray = [187, 187, 187]/255;

    figure;
    h = boxplot(d);
    hold on; % keep the boxplot

    set(gca, 'FontSize', 14); % set font size
    set(gcf, 'Name', fig_title); % figure name

    means = mean(d);

    % Add rhombus to the boxplot
    for i = 1:length(means)
        plot(i, means(i), 'd', 'MarkerSize', 10, 'Color', gray);
    end
    
    grid on;
    
    % Thickness
    set(findobj(gca, 'Type', 'Line'), 'LineWidth', 2);

    % White background
    set(gcf, 'Position', [200, 200, 350, 350], 'Color', 'w');
    
    % Labels
    set(gca, 'XTickLabel', labels);
    ylabel('Time [s]');
    
    % Get objects
    boxes = findobj(h, 'Tag', 'Box');
    medians = findobj(h, 'Tag', 'Median');
    whiskers = findobj(h, 'Tag', 'Whisker');
    caps = findobj(h, 'Tag', 'Cap');
    outliers = findobj(h, 'Tag', 'Outliers');
    
    set(boxes, 'Color', blue, 'LineWidth', 2);
    set(medians, 'Color', red, 'LineWidth', 2);
    set(whiskers, 'Color', red, 'LineWidth', 2);
    set(caps, 'Color', red, 'LineWidth', 2);
    set(outliers, 'Color', red, 'LineWidth', 2);
    set(outliers, 'MarkerEdgeColor', red, 'MarkerSize', 6); 
    
    print(filename,'-dpng','-r300');  % -dpng = PNG format, -r300 = 300 dpi
    
    hold off;
end

clear; clc; close all;

% Read data from files
T_safe = readtable('results/safe.csv');
T_unsafe = readtable('results/unsafe.csv');

T1 = T_safe(strcmp(T_safe.Solver, 'Theano_DC'), :);
T2 = T_unsafe(strcmp(T_unsafe.Solver, 'Theano_DC'), :);
T3 = T_safe(strcmp(T_safe.Solver, 'Theano_SC'), :);
T4 = T_unsafe(strcmp(T_unsafe.Solver, 'Theano_SC'), :);
T5 = T_safe(strcmp(T_safe.Solver, 'z3'), :);
T6 = T_unsafe(strcmp(T_unsafe.Solver, 'z3'), :);
T7 = T_safe(strcmp(T_safe.Solver, 'cvc5'), :);
T8 = T_unsafe(strcmp(T_unsafe.Solver, 'cvc5'), :);

idx_EUL_1 = startsWith(string(T1.OTA), "EUL"); M1_EUL = T1(idx_EUL_1, :); M1 = T1(~idx_EUL_1, :);
idx_EUL_2 = startsWith(string(T2.OTA), "EUL"); M2_EUL = T2(idx_EUL_2, :); M2 = T2(~idx_EUL_2, :);
idx_EUL_3 = startsWith(string(T3.OTA), "EUL"); M3_EUL = T3(idx_EUL_3, :); M3 = T3(~idx_EUL_3, :);
idx_EUL_4 = startsWith(string(T4.OTA), "EUL"); M4_EUL = T4(idx_EUL_4, :); M4 = T4(~idx_EUL_4, :);
idx_EUL_5 = startsWith(string(T5.OTA), "EUL"); M5_EUL = T5(idx_EUL_5, :); M5 = T5(~idx_EUL_5, :);
idx_EUL_6 = startsWith(string(T6.OTA), "EUL"); M6_EUL = T6(idx_EUL_6, :); M6 = T6(~idx_EUL_6, :);
idx_EUL_7 = startsWith(string(T7.OTA), "EUL"); M7_EUL = T7(idx_EUL_7, :); M7 = T7(~idx_EUL_7, :);
idx_EUL_8 = startsWith(string(T8.OTA), "EUL"); M8_EUL = T8(idx_EUL_8, :); M8 = T8(~idx_EUL_8, :);

time_column=3;

E1 = M1{:, time_column}; E1_EUL = M1_EUL{:, time_column};
E2 = M2{:, time_column}; E2_EUL = M2_EUL{:, time_column};
E3 = M3{:, time_column}; E3_EUL = M3_EUL{:, time_column};
E4 = M4{:, time_column}; E4_EUL = M4_EUL{:, time_column};
E5 = M5{:, time_column}; E5_EUL = M5_EUL{:, time_column};
E6 = M6{:, time_column}; E6_EUL = M6_EUL{:, time_column};
E7 = M7{:, time_column}; E7_EUL = M7_EUL{:, time_column};
E8 = M8{:, time_column}; E8_EUL = M8_EUL{:, time_column};

% All data
data = [E1, E2, E3, E4, E5, E6, E7, E8];
data_eul = [E1_EUL, E2_EUL, E3_EUL, E4_EUL, E5_EUL, E6_EUL, E7_EUL, E8_EUL];

% Statistics
means = mean(data); means_eul = mean(data_eul);
medians = median(data); medians_eul = median(data_eul);
stds = std(data); stds_eul = std(data_eul);
mins = min(data); mins_eul = min(data_eul);
maxs = max(data); maxs_eul = max(data_eul);

labels = {'DC (s)', 'DC (u)', 'SC (s)', 'SC (u)', 'z3 (s)', 'z3 (u)', 'cvc5 (s)', 'cvc5 (u)'};

if ~all(isnan(means(:)))
    fprintf('Statistics for each experiment (EUL excluded):\n');
    for i = 1:length(means)
        fprintf('%s\n', labels{i});
        print_statistics(means(i), medians(i), stds(i), mins(i), maxs(i));
    end

    print_boxplot('results/boxplot', data, labels, 'Results for all the models (EUL excluded)');
end

if ~all(isnan(means_eul(:)))
    fprintf('Statistics for each experiment (only EUL):\n');
    for i = 1:length(means_eul)
        fprintf('%s\n', labels{i});
        print_statistics(means_eul(i), medians_eul(i), stds_eul(i), mins_eul(i), maxs_eul(i));
    end

    print_boxplot('results/boxplot_eul', data_eul, labels, 'Results for the EUL model');
end
