import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric.kernel_regression import KernelReg
from statsmodels.robust.robust_linear_model import RLM
from statsmodels.tools.tools import add_constant

from CONFIG import FILE_PATH_RELATIVE


class FuzzyRDD:
    def __init__(self, data, threshold_date):
        self.data = data
        self.threshold_date = threshold_date
        self.threshold_index = (self.data['date'] >= threshold_date).idxmax()

    def preprocess_data(self):
        self.data['treatment'] = (self.data['date'] >= self.threshold_date).astype(int)
        self.data['T_centered'] = (self.data['date'] - self.threshold_date).dt.days
        self.data['T_standardized'] = (self.data['T_centered'] - self.data['T_centered'].mean()) / self.data['T_centered'].std()

    def fit_rdd(self):
        Y = self.data['time']
        T = self.data['T_standardized']
        D = self.data['treatment']
        X = add_constant(np.column_stack((D, T)))
        rdd_model = RLM(Y, X).fit(cov='H3')
        return rdd_model

    def kernel_regression(self):
        kr = KernelReg(self.data['time'], self.data['T_centered'], var_type='c')
        y_pred, _ = kr.fit(self.data['T_centered'])
        return y_pred

    def estimate_density(self):
        below_threshold = self.data[self.data['date'] < self.threshold_date]['time']
        above_threshold = self.data[self.data['date'] >= self.threshold_date]['time']

        kde_below = KDEUnivariate(below_threshold)
        kde_below.fit()

        kde_above = KDEUnivariate(above_threshold)
        kde_above.fit()

        return kde_below, kde_above

    def test_discontinuity(self):
        kde_below, kde_above = self.estimate_density()
        threshold_time = self.data.loc[self.threshold_index, 'time']

        density_below = kde_below.evaluate(threshold_time)
        density_above = kde_above.evaluate(threshold_time)

        return density_below != density_above

    def plot_rdd(self, rdd_model):
        plt.figure(figsize=(10, 6))
        plt.scatter(
            self.data['T_standardized'],
            self.data['time'],
            color='blue',
            label='Observed Data'
        )
        T_predict = np.linspace(
            self.data['T_standardized'].min(),
            self.data['T_standardized'].max(),
            1000
        )
        D_predict = (T_predict >= 0).astype(int)
        X_predict = add_constant(np.column_stack((D_predict, T_predict)))
        y_predict = rdd_model.predict(X_predict)

        plt.plot(
            T_predict,
            y_predict,
            color='red',
            label='Fitted Line'
        )
        plt.axvline(
            0,
            color='gray',
            linestyle='--',
            label='Threshold'
        )
        plt.xlabel('Standardized Date (from threshold)')
        plt.ylabel('Mile Record Time (seconds)')
        plt.title('Fuzzy Regression Discontinuity Design')
        plt.legend()
        plt.show()


THRESHOLD_DATE = pd.Timestamp('1954-05-06')

data = pd.read_csv(FILE_PATH_RELATIVE, sep=";")
data['date'] = pd.to_datetime(data['date'])

fuzzy_rdd = FuzzyRDD(data, THRESHOLD_DATE)
fuzzy_rdd.preprocess_data()

rdd_model = fuzzy_rdd.fit_rdd()
print(rdd_model.summary())

fuzzy_rdd.plot_rdd(rdd_model)

y_pred_kernel = fuzzy_rdd.kernel_regression()

bunching_test = fuzzy_rdd.test_discontinuity()
print("Discontinuity Detected:", bunching_test)
