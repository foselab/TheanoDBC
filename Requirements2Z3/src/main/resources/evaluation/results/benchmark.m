% Read data from files
E1 = readmatrix('E1.txt');
E2 = readmatrix('E2.txt');
E3 = readmatrix('E3.txt');
E4 = readmatrix('E4.txt');

% All data
data = [E1; E2; E3; E4];

% Grouping
group = [ones(size(E1)); 2*ones(size(E2)); 3*ones(size(E3)); 4*ones(size(E4))];

% Statistics
means = [mean(E1), mean(E2), mean(E3), mean(E4)];
medians = [median(E1), median(E2), median(E3), median(E4)];
std_devs = [std(E1), std(E2), std(E3), std(E4)];
mins = [min(E1), min(E2), min(E3), min(E4)];
maxs = [max(E1), max(E2), max(E3), max(E4)];

% Print
fprintf('Statistics for each experiment\n');
for i = 1:4
    fprintf('Experiment %d:\n', i);
    fprintf('\tAverage: %.2f\n', means(i));
    fprintf('\tMedian: %.2f\n', medians(i));
    fprintf('\tStandard Deviation: %.2f\n', std_devs(i));
    fprintf('\tMin: %.2f\n', mins(i));
    fprintf('\tMax: %.2f\n', maxs(i));
end

% Statistic for all the experiements
mean_all = mean(data);
median_all = median(data);
std_devs_all = std(data);
min_all = min(data);
max_all = max(data);

% Print
fprintf('\nStatistics for all the experiments:\n');
fprintf('\tAverage: %.2f\n', mean_all);
fprintf('\tMedian: %.2f\n', median_all);
fprintf('\tStandard Deviation: %.2f\n', std_devs_all);
fprintf('\tMin: %.2f\n', min_all);
fprintf('\tMax: %.2f\n', max_all);

% Boxplot
figure;
boxplot(data, group);
hold on;

% Add rhombus to the boxplot
for i = 1:length(means)
    plot(i, means(i), 'd', 'MarkerSize', 10, 'Color', [0.6, 0.6, 0.6]);
end

% Labels
ax = gca; % Get axes
ax.XTickLabel = {'E1', 'E2', 'E3', 'E4'};
ax.FontSize = 20;
ylabel('Seconds', 'FontSize', 20);

grid on;
hold off;
