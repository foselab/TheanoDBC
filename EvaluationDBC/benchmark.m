function print_statistics(mean, median, std, min, max)
    fprintf('\tAverage: %.2f\n', mean);
    fprintf('\tMedian: %.2f\n', median);
    fprintf('\tStandard Deviation: %.2f\n', std);
    fprintf('\tMin: %.2f\n', min);
    fprintf('\tMax: %.2f\n', max);
end

function print_boxplot(filename, data, group, means)
    blue = [0, 114, 178]/255;
    red = [230, 159, 0]/255;
    gray = [187, 187, 187]/255;

    figure;
    h = boxplot(data, group);
    hold on; % keep the boxplot

    set(gca, 'FontSize', 14); % set font size
        
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
    set(gca, 'XTickLabel', {'Safe', 'Unsafe'});
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

% Read data from files
M1 = readmatrix('.\results\safe.txt');
M2 = readmatrix('.\results\unsafe.txt');

% Exclude EUL
E1 = M1(1:450, :);
E2 = M2(1:450, :);

% All data
data = [E1; E2];

% Grouping
group = [ones(size(E1)); 2*ones(size(E2))];

% Statistics
means = [mean(E1), mean(E2)];
medians = [median(E1), median(E2)];
std_devs = [std(E1), std(E2)];
mins = [min(E1), min(E2)];
maxs = [max(E1), max(E2)];

% Print statistics for each experiment
fprintf('Statistics for each experiment (EUL excluded):\n');
for i = 1:2
    print_statistics(means(i), medians(i), std_devs(i), mins(i), maxs(i));
end

% Statistics for all the experiements
mean_all = mean(data);
median_all = median(data);
std_devs_all = std(data);
min_all = min(data);
max_all = max(data);

% Print statistics for all the experiments
fprintf('\nStatistics for all the experiments (EUL excluded):\n');
print_statistics(mean_all, median_all, std_devs_all, min_all, max_all);
print_boxplot('results/boxplot', data, group, means);

% Only EUL
E1 = M1(451:500, :);
E2 = M2(451:500, :);

% All data
data = [E1; E2];

% Grouping
group = [ones(size(E1)); 2*ones(size(E2))];

% Statistics
means = [mean(E1), mean(E2)];
medians = [median(E1), median(E2)];
std_devs = [std(E1), std(E2)];
mins = [min(E1), min(E2)];
maxs = [max(E1), max(E2)];

% Print statistics for each experiment
fprintf('Statistics for each experiment (only EUL):\n');
for i = 1:2
    print_statistics(means(i), medians(i), std_devs(i), mins(i), maxs(i));
end

% Statistics for all the experiements
mean_all = mean(data);
median_all = median(data);
std_devs_all = std(data);
min_all = min(data);
max_all = max(data);

% Print statistics for all the experiments
fprintf('\nStatistics for all the experiments (only EUL):\n');
print_statistics(mean_all, median_all, std_devs_all, min_all, max_all);
print_boxplot('results/boxplot_eul', data, group, means);
