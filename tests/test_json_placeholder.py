import random

import pytest
import requests
import uuid

host = 'https://jsonplaceholder.typicode.com'


def test_listing_all_resources():
    response = requests.get(url=f'{host}/posts')
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize('resource_id', [i for i in range(1, 4)])
def test_getting_a_resource(resource_id):
    response = requests.get(url=f'{host}/posts/{resource_id}')
    assert response.status_code == 200
    assert response.json()['id'] == resource_id


@pytest.mark.parametrize('user_id', [i for i in range(1, 4)])
def test_creating_a_resource(user_id):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    request_body = {
        'title': str(uuid.uuid4()),
        'body': str(uuid.uuid4()),
        'userId': user_id,
    }
    response = requests.post(url=f'{host}/posts', json=request_body, headers=headers)
    response_body = response.json()
    assert response.status_code == 201
    assert response_body['title'] == request_body['title']
    assert response_body['body'] == request_body['body']
    assert response_body['userId'] == user_id


@pytest.mark.parametrize('resource_id', [i for i in range(1, 4)])
def test_updating_a_resource(resource_id):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    request_body = {
        'id': resource_id,
        'title': str(uuid.uuid4()),
        'body': str(uuid.uuid4()),
        'userId': random.randint(1, 5),
    }
    response = requests.put(url=f'{host}/posts/{resource_id}', json=request_body, headers=headers)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['id'] == resource_id
    assert response_body['title'] == request_body['title']
    assert response_body['body'] == request_body['body']
    assert response_body['userId'] == request_body['userId']


@pytest.mark.parametrize('resource_id', [i for i in range(1, 4)])
def test_deleting_a_resource(resource_id):
    response = requests.delete(url=f'{host}/posts/{resource_id}')
    assert response.status_code == 200
