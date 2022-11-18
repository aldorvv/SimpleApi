from stats import Stats


def test_all_stats(stats: Stats):
    expected_result = {
        "max_growth_time": 12,
        "mean_growth_time": 4.7,
        "median_growth_time": 3.5,
        "min_growth_time": 3,
        "variance_growth_time": 8.9,
    }
    assert stats.all() == expected_result


def test_len(stats: Stats, client):
    assert len(stats) == len(client.times)
