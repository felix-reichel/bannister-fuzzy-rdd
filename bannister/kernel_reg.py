import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.nonparametric.kernel_regression import KernelReg

from static.Helpers import DataLoader

file_path = '../data/mile_records.csv'
data = DataLoader.load_data(file_path)

threshold_date = pd.Timestamp('1954-05-06')
data['treatment'] = (data['date'] >= threshold_date).astype(int)
data['T_centered'] = (data['date'] - threshold_date).dt.days
data['T_standardized'] = (data['T_centered'] - data['T_centered'].mean()) / data['T_centered'].std()


def kernel_regression(data):
    kr = KernelReg(data['time'], data['T_centered'], var_type='c')
    y_pred, _ = kr.fit(data['T_centered'])
    return y_pred


data['y_pred_kernel'] = kernel_regression(data)

plt.figure(figsize=(10, 6))
plt.scatter(
    data['date'],
    data['time'],
    color='blue',
    label='Observed Data'
)
plt.plot(
    data['date'],
    data['y_pred_kernel'],
    color='red',
    linewidth=2,
    label='Kernel Regression'
)
plt.axvline(
    threshold_date,
    color='green',
    linestyle='--',
    label='Threshold date (1954-05-06)'
)
plt.title('Kernel Regression for Robustness Check')
plt.xlabel('Date')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()

# Examine bunching
plt.figure(figsize=(10, 6))
plt.hist(data[data['date'] < threshold_date]['time'], bins=10, color='blue', alpha=0.7, label='Before Threshold')
plt.hist(data[data['date'] >= threshold_date]['time'], bins=10, color='red', alpha=0.7, label='After Threshold')
plt.axvline(x=data[data['date'] < threshold_date]['time'].mean(), color='blue', linestyle='--')
plt.axvline(x=data[data['date'] >= threshold_date]['time'].mean(), color='red', linestyle='--')
plt.xlabel('Mile Record Time (seconds)')
plt.ylabel('Frequency')
plt.title('Bunching Examination')
plt.legend()
plt.show()
