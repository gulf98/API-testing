import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="url to check status code"
    )
    parser.addoption(
        "--status_code", action="store", type=int, default=200, help="expected status code"
    )


@pytest.fixture
def url(request) -> str:
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request) -> int:
    return request.config.getoption("--status_code")
