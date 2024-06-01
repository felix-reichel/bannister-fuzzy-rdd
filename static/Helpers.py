import pandas as pd


class DataLoader:
    @staticmethod
    def load_data(file_path):
        data = pd.read_csv(file_path, sep=";")
        data['date'] = pd.to_datetime(data['date'])
        return data

    @staticmethod
    def process_data(data):
        threshold_date = pd.Timestamp('1954-05-06')
        data['treatment'] = (data['date'] >= threshold_date).astype(int)
        data['T_centered'] = (data['date'] - threshold_date).dt.days
        data['T_standardized'] = (data['T_centered'] - data['T_centered'].mean()) / data['T_centered'].std()
        return data
