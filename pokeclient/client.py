import multiprocessing
import os
from http import HTTPStatus
from typing import List

import requests

from utils import Singleton


URL = os.getenv("POKE_URL")
if URL is None:
    raise EnvironmentError("Environment variable POKE_URL must be set!")


class PokeClient(metaclass=Singleton):
    def __init__(self):
        self._base_url: str = URL.rstrip("/")
        self._cache = {}
        self._limit = 0

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, value: int):
        self._limit = value

    @property
    def berries(self) -> List[str]:
        if (berries := self._cache.get("berries")) and len(berries) == self.limit:
            return berries

        params = {"limit": self.limit}
        body = requests.get(f"{self.base_url}/berry", params=params).json()
        self._cache["berries"] = [berry.get("name") for berry in body["results"]]
        return self._cache["berries"]

    @property
    def times(self):
        if (times := self._cache.get("times")) and len(times) == self.limit:
            return times

        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        self._cache["times"] = pool.map(self._get_growth_time, self.berries)
        pool.close()
        return self._cache["times"]

    def _get_growth_time(self, name: str):
        response = requests.get(f"{self.base_url}/berry/{name}")
        if response.status_code != HTTPStatus.OK:
            raise RuntimeError(f"Something gone wrong with berry {name}...")
        body = response.json()
        return body.get("growth_time")
