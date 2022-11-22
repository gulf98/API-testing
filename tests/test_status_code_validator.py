import requests


def test_status_code_validator(url, status_code):
    assert requests.get(url=url).status_code == status_code
