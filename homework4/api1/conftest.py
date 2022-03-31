import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo/api/breeds",
        help="url for requests"
    )

    parser.addoption(
        "--method",
        default="get",
        help="method to use in requests"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
