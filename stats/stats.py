from typing import Dict, List, Union

import statistics


class Stats:

    def __init__(self, names: List[str], values: List[int]) -> None:
        self._names = names
        self._values = values

    def __getitem__(self, index: int) -> int:
        return self._values[index]

    def __len__(self) -> int:
        return len(self._values)

    @property
    def names(self) -> List[str]:
        return self._names

    def mean(self) -> float:
        return statistics.mean(self)

    def min(self) -> int:
        return min(self)

    def max(self) -> int:
        return max(self)

    def median(self) -> float:
        return statistics.median(self)

    def variance(self) -> float:
        return statistics.variance(self)

    def all(self) -> Dict[str, Union[int, float]]:
        return {
            "berries_names": self.names,
            "mean_growth_time": self.mean(),
            "min_growth_time": self.min(),
            "max_growth_time": self.max(),
            "median_growth_time": self.median(),
            "variance_growth_time": self.variance()
        }