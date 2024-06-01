import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

from static.Helpers import DataLoader

file_path = '../data/mile_records.csv'
data = DataLoader.load_data(file_path)

threshold_date = pd.Timestamp('1954-05-06')
data['treatment'] = (data['date'] >= threshold_date).astype(int)


def fit_rdd(data):
    Y = data['time']
    T = (data['date'] - threshold_date).dt.days
    D = data['treatment']
    X = sm.add_constant(np.column_stack((D, T)))
    model = sm.OLS(Y, X).fit()
    return model


rdd_model = fit_rdd(data)
print(rdd_model.summary())


def plot_rdd(data, model):
    plt.figure(figsize=(10, 6))
    plt.scatter(
        data['date'],
        data['time'],
        color='blue',
        label='Observed Data'
    )

    date_range = pd.date_range(
        start=data['date'].min(),
        end=data['date'].max(),
        periods=1000
    )
    T = (date_range - threshold_date).days
    D = (date_range >= threshold_date).astype(int)
    X_pred = sm.add_constant(np.column_stack((D, T)))
    y_pred = model.predict(X_pred)

    plt.plot(
        date_range,
        y_pred,
        color='red',
        linewidth=2,
        label='Regression discontinuity'
    )

    plt.axvline(
        threshold_date,
        color='green',
        linestyle='--',
        label='Threshold date (1954-05-06)'
    )
    plt.title('Regression Discontinuity Design (RDD) Analysis')
    plt.xlabel('Date')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


plot_rdd(data, rdd_model)
