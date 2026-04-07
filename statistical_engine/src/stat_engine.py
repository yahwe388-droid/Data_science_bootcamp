import math
from collections import Counter


class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("Dataset is empty after cleaning.")

    def _clean_data(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Data must be a list or tuple.")

        clean = []
        for x in data:
            if isinstance(x, (int, float)):
                clean.append(float(x))
            else:
                raise TypeError(f"Invalid data type detected: {type(x)}")

        return clean

    # ------------------------
    # Central Tendency
    # ------------------------

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        counts = Counter(self.data)
        max_count = max(counts.values())

        if max_count == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in counts.items() if v == max_count]
        return modes

    # ------------------------
    # Dispersion
    # ------------------------

    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        if is_sample:
            if n < 2:
                raise ValueError("Sample variance requires at least 2 data points.")
            denominator = n - 1
        else:
            denominator = n

        return sum((x - mean) ** 2 for x in self.data) / denominator

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # ------------------------
    # Outliers
    # ------------------------

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        return [x for x in self.data if abs(x - mean) > threshold * std]