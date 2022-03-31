import pytest
import random


def test_get_status200(base_url, request_method, code=200):
    """Проверяем статус get запроса"""
    response = request_method(url=base_url)
    assert response.status_code == code


@pytest.mark.parametrize("type_param", ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract',
                                        'proprietor', 'closed'])
def test_get(base_url, request_method, type_param, code=200):
    """Проверяем статус для get запроса с параметризацией параметра type"""
    response = request_method(url=base_url, params={'by_type': type_param})
    if type_param == 'proprietor':
        assert response.status_code == 400
    else:
        assert response.status_code == code


@pytest.mark.parametrize('name_ls', ['asc', 'desc'])
def test_get_full(base_url, request_method, name_ls, code=200):
    """Проверяем, что для заданных параметров by_state, sort возвращается валидный код"""
    response = request_method(url=base_url).json()
    response_len = len(response)
    while response_len > 0:
        for state in response:
            by_state_ls = state.get('city')
            param = f"sort=type,name:{name_ls}"
            response = request_method(url=base_url, params={'by_state': by_state_ls, 'sort': param})
            assert response.status_code == code
            response_len -= 1


def test_get_per_page(base_url, request_method):
    """Проверяем, что на странице отображается заданное число записей"""
    some_page = random.randint(1, 50)
    response = request_method(url=base_url, params={'per_page': some_page}).json()
    len_response = len(response)
    assert len_response == some_page


@pytest.mark.parametrize('some_page', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_get_page(base_url, request_method, some_page):
    """Проверяем, что страницы возвращаются с данными"""
    response = request_method(url=base_url, params={'page': some_page})
    for row in response.json():
        res = row['id']
        assert res != []
