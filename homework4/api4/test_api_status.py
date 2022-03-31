import requests
import re


def test_get(base_url, request_code):
    """Проверяем статус get запроса"""
    somethink_url = re.match('https://\S{1,1000}', base_url).string

    print(somethink_url)
    if base_url == somethink_url:
        response = requests.get(url=base_url)
        assert response.status_code == int(request_code)

    else:
        response = requests.get(url=base_url)
        assert response.status_code == 404