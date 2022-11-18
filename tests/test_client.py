from pokeclient import PokeClient


def test_singleton():
    client_a = PokeClient()
    client_b = PokeClient()

    assert client_a is client_b


def test_berries(client: PokeClient):
    expected_berries = [
        "cheri",
        "chesto",
        "pecha",
        "rawst",
        "aspear"
    ]
    client.limit = len(expected_berries)
    assert client.berries == expected_berries


def test_times(client: PokeClient):
    expected_times = [3, 3, 3, 3, 3, 4]
    client.limit = len(expected_times)
    assert client.times == expected_times


def test_wrong_berry(client: PokeClient):
    try:
        client._get_growth_time("wrong")
    except RuntimeError:
        assert True
    else:
        assert False