import pytest
import random
import requests


def test_get_status200(base_url, request_method, code=200):
    """Проверяем статус get запроса"""
    post_number = random.randint(1, 100)
    base_url = base_url + f"/{post_number}"
    response = request_method(url=base_url)
    assert response.status_code == code


@pytest.mark.parametrize('post_number', [0, 101, -1, '-1'], ids=["zero", "bondary_up", "bondary_down", "negative"])
def test_get_status404(base_url, request_method, post_number, code=404):
    """Проверяем статус get запроса с некорректными данными"""
    base_url = base_url + f"/{post_number}"
    response = request_method(url=base_url)
    assert response.status_code == code


def test_get(base_url, request_method):
    """Проверяем, что get возвращает не пустые данные"""
    response = request_method(url=base_url)
    assert response.json() != []


def test_post(base_url, request_method):
    """Добавляем новую запись"""
    response_for_len = request_method(url=base_url).json()
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }

    response = requests.post(
        base_url,
        headers=headers,
        json=body,
        verify=False).json()

    assert response['id'] == len(response_for_len) + 1


@pytest.mark.parametrize('post_number', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_update(base_url, post_number):
    """Обновляем запись"""
    base_url = base_url + f"/{post_number}"
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    body = {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.put(
        base_url,
        headers=headers,
        json=body,
        verify=False).json()
    assert response['id'] == post_number
