import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from static.Helpers import DataLoader


class SpilloverAnalysis:
    def __init__(self, data, threshold_date):
        self.data = data
        self.threshold_date = threshold_date

    def preprocess_data(self):
        self.data['treatment'] = (self.data['date'] >= self.threshold_date).astype(int)

    def difference_in_differences(self):
        treated_group = self.data[self.data['date'] >= self.threshold_date]
        control_group = self.data[self.data['date'] < self.threshold_date]

        treated_mean = treated_group.groupby('date')['time'].mean()
        control_mean = control_group.groupby('date')['time'].mean()

        return treated_mean, control_mean

    def calculate_counterfactual_trends(self, treated_mean, control_mean):
        did_difference = treated_mean - control_mean
        counterfactual_treated_mean = treated_mean - did_difference
        counterfactual_control_mean = control_mean + did_difference

        return counterfactual_treated_mean, counterfactual_control_mean


#FILE_PATH = '../data/mile_records.csv'
# All times around Th
THRESHOLD_DATE = pd.Timestamp('1954-05-06')

data = DataLoader.load_data(FILE_PATH)
data = DataLoader.process_data(data)

spillover_analysis = SpilloverAnalysis(data, THRESHOLD_DATE)
spillover_analysis.preprocess_data()

treated_mean, control_mean = spillover_analysis.difference_in_differences()

# Ensure the full date range is covered
min_date = min(treated_mean.index.min(), control_mean.index.min())
max_date = max(treated_mean.index.max(), control_mean.index.max())
full_date_range = pd.date_range(start=min_date, end=max_date)

# Interpolate missing values
treated_mean = treated_mean.reindex(full_date_range).interpolate(method='linear')
control_mean = control_mean.reindex(full_date_range).interpolate(method='linear')

counterfactual_treated_mean, counterfactual_control_mean = \
    spillover_analysis.calculate_counterfactual_trends(treated_mean, control_mean)

# Smooth the data with a rolling average
window_size = 7  # Adjust as needed
treated_mean_smoothed = treated_mean.rolling(window=window_size, min_periods=1).mean()
control_mean_smoothed = control_mean.rolling(window=window_size, min_periods=1).mean()
counterfactual_treated_mean_smoothed = counterfactual_treated_mean.rolling(window=window_size, min_periods=1).mean()
counterfactual_control_mean_smoothed = counterfactual_control_mean.rolling(window=window_size, min_periods=1).mean()

plt.figure(figsize=(10, 6))
plt.plot(treated_mean_smoothed.index, treated_mean_smoothed.values, color='blue', label='Treated Group')
plt.plot(control_mean_smoothed.index, control_mean_smoothed.values, color='red', label='Control Group')
plt.plot(counterfactual_treated_mean_smoothed.index, counterfactual_treated_mean_smoothed.values,
         color='green', linestyle='--', label='Counterfactual Treated Group')
plt.plot(counterfactual_control_mean_smoothed.index, counterfactual_control_mean_smoothed.values,
         color='orange', linestyle='--', label='Counterfactual Control Group')
plt.axvline(spillover_analysis.threshold_date, color='gray', linestyle='--', label='Threshold Date')

plt.title('Difference-in-Differences (DiD) Analysis')
plt.xlabel('Date')
plt.ylabel('Mean Mile Record Time')
plt.legend()
plt.grid(True)
plt.show()
