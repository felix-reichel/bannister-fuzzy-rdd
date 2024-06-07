import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# File path and threshold date for 10k
FILE_PATH_RELATIVE = '../data/10k_records.csv'
# first date of time < 27 mins
BANNISTER_LIKE_THRESHOLD_DATE = pd.Timestamp('1993-07-10')

from static.Helpers import DataLoader

data = DataLoader.load_data(FILE_PATH_RELATIVE)
data = DataLoader.process_data(data, '1993-07-10')


def fit_rdd(data):
    Y = data['time']
    T = data['T_standardized']
    D = data['treatment']
    X = sm.add_constant(np.column_stack((D, T)))
    model = sm.OLS(Y, X).fit()
    return model


rdd_model = fit_rdd(data)
print(rdd_model.summary())


def plot_rdd(data, model):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['T_standardized'], data['time'], color='blue', label='Observed Data')

    T_predict = np.linspace(data['T_standardized'].min(), data['T_standardized'].max(), 1000)
    D_predict = (T_predict >= 0).astype(int)
    X_predict = sm.add_constant(np.column_stack((D_predict, T_predict)))
    y_predict = model.predict(X_predict)

    plt.plot(T_predict, y_predict, color='red', label='Fitted Line')
    plt.axvline(0, color='gray', linestyle='--', label='Threshold')
    plt.xlabel('Standardized Date (from threshold)')
    plt.ylabel('10k Record Time (seconds)')
    plt.title('Regression Discontinuity Design - 10k')
    plt.legend()
    plt.show()


plot_rdd(data, rdd_model)
