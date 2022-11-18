import pytest

from pokeclient import PokeClient
from stats import Stats


@pytest.fixture(scope="session")
def client():
    client = PokeClient()
    client.limit = 5
    return client


@pytest.fixture(scope="session")
def stats(client):
    client.limit = 10
    return Stats(client.times)
