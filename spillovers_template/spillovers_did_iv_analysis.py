import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant

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

        treated_diff = treated_group['time'].diff()
        control_diff = control_group['time'].diff()

        did_estimate = (treated_diff.mean() - control_diff.mean())
        return did_estimate, treated_diff, control_diff

    def instrumental_variables(self):
        self.data['date_diff'] = (self.data['date'] - self.threshold_date).dt.days
        X = add_constant(self.data['date_diff'])
        y = self.data['time']
        model_iv = OLS(y, X).fit()
        iv_estimate = model_iv.params.iloc[1]  # Coefficient of date_diff (instrument)
        iv_p_value = model_iv.pvalues.iloc[1]  # p-value of the coefficient
        return iv_estimate, iv_p_value, model_iv.summary()


#FILE_PATH = '../data/mile_records.csv'
# All times around Th
THRESHOLD_DATE = pd.Timestamp('1954-05-06')

#data = DataLoader.load_data(FILE_PATH)
#data = DataLoader.process_data(data)

spillover_analysis = SpilloverAnalysis(data, THRESHOLD_DATE)
spillover_analysis.preprocess_data()

did_estimate, treated_diff, control_diff = spillover_analysis.difference_in_differences()
print("Difference-in-Differences (DiD) Estimate:", did_estimate)

iv_estimate, iv_p_value, iv_summary = spillover_analysis.instrumental_variables()
print("Instrumental Variables (IV) Estimate:", iv_estimate)
print("Instrumental Variables (IV) p-value:", iv_p_value)
print("Instrumental Variables (IV) Summary:")
print(iv_summary)
