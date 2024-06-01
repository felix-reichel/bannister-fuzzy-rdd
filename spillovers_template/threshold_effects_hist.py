import matplotlib.pyplot as plt

from CONFIG import FILE_PATH_RELATIVE, THRESHOLD_DATE
from static.Helpers import DataLoader


#FILE_PATH_RELATIVE = '../data/mile_records.csv'
# All times around Th
data = DataLoader.load_data(FILE_PATH_RELATIVE)

threshold_date = THRESHOLD_DATE
data = DataLoader.process_data(data)


def analyze_threshold_effects(data):
    before_threshold = data[data['date'] < threshold_date]
    after_threshold = data[data['date'] >= threshold_date]

    print("Summary Statistics - Before Threshold:")
    print(before_threshold.describe())
    print("\nSummary Statistics - After Threshold:")
    print(after_threshold.describe())

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.hist(before_threshold['time'], bins=10, color='blue', alpha=0.7, label='Before Threshold')
    plt.axvline(x=before_threshold['time'].mean(), color='blue', linestyle='--')
    plt.xlabel('Mile Record Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Mile Record Time - Before Threshold')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.hist(after_threshold['time'], bins=10, color='red', alpha=0.7, label='After Threshold')
    plt.axvline(x=after_threshold['time'].mean(), color='red', linestyle='--')
    plt.xlabel('Mile Record Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Mile Record Time - After Threshold')
    plt.legend()

    plt.tight_layout()
    plt.show()


analyze_threshold_effects(data)
