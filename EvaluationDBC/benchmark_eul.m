% Read data from files
E1 = readmatrix('Efficiency\results\safe.txt');
E2 = readmatrix('Efficiency\results\unsafe.txt');

% Only EUL
E1 = E1(451:500, :);
E2 = E2(451:500, :);

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
fprintf('Statistics for each experiment\n');
for i = 1:2
    fprintf('Experiment %d:\n', i);
    fprintf('\tAverage: %.2f\n', means(i));
    fprintf('\tMedian: %.2f\n', medians(i));
    fprintf('\tStandard Deviation: %.2f\n', std_devs(i));
    fprintf('\tMin: %.2f\n', mins(i));
    fprintf('\tMax: %.2f\n', maxs(i));
end

% Statistics for all the experiements
mean_all = mean(data);
median_all = median(data);
std_devs_all = std(data);
min_all = min(data);
max_all = max(data);

% Print statistics for all the experiments
fprintf('\nStatistics for all the experiments:\n');
fprintf('\tAverage: %.2f\n', mean_all);
fprintf('\tMedian: %.2f\n', median_all);
fprintf('\tStandard Deviation: %.2f\n', std_devs_all);
fprintf('\tMin: %.2f\n', min_all);
fprintf('\tMax: %.2f\n', max_all);

% Boxplot
figure;
boxplot(data, group);
hold on; % keep the boxplot

% Add rhombus to the boxplot
for i = 1:length(means)
    plot(i, means(i), 'd', 'MarkerSize', 10, 'Color', [0.6, 0.6, 0.6]);
end

grid on;

fontSize=14;

% Labels
ax = gca; % Get axes
set(gca, ...
        'XTickLabel', {'\textbf{\emph{SAFE}}', '\textbf{\emph{UNSAFE}}'}, ...
        'TickLabelInterpreter','latex', ...
        'FontSize', fontSize ...
);

ylabel('\textbf{\emph{SECONDS}}', 'Interpreter', 'latex', 'FontSize', fontSize);
title('\textbf{EUL OTAs}', 'Interpreter', 'latex', 'FontSize', fontSize);


% Thickness
set(findobj(gca, 'type', 'line'), 'LineWidth', 2);

% White background
set(gcf, 'Position', [200, 200, 350, 350], 'Color', 'w'); 

print('results/boxplot_eul','-dpng','-r300');  % -dpng = PNG format, -r300 = 300 dpi

hold off;