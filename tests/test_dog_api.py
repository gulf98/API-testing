import pytest
import requests

from jsonschema import validate

host = 'https://dog.ceo'


def test_list_all_breads():
    expected_schema = {
        'properties': {
            'message': {'type': 'object'},
            'status': {'const': 'success'}
        }
    }
    response = requests.get(url=f'{host}/api/breeds/list/all')
    assert response.status_code == 200
    validate(instance=response.json(), schema=expected_schema)


def test_single_random_image_from_all_dogs_collection():
    expected_schema = {
        'properties': {
            'message': {'type': 'string'},
            'status': {'const': 'success'}
        }
    }
    response = requests.get(url=f'{host}/api/breeds/image/random')
    assert response.status_code == 200
    validate(instance=response.json(), schema=expected_schema)


@pytest.mark.parametrize('images_count', [1, 50])
def test_multiple_random_images_from_all_dogs_collection(images_count):
    expected_schema = {
        'properties': {
            'message': {'type': 'array'},
            'status': {'const': 'success'}
        }
    }
    response = requests.get(url=f'{host}/api/breeds/image/random/{images_count}')
    response_body = response.json()
    assert response.status_code == 200
    validate(instance=response_body, schema=expected_schema)
    assert len(response_body['message']) == images_count


@pytest.mark.parametrize('breed', ['bulldog', 'bullterrier', 'corgi'])
def test_array_of_all_the_images_from_a_breed(breed):
    expected_schema = {
        'properties': {
            'message': {'type': 'array'},
            'status': {'const': 'success'}
        }
    }
    response = requests.get(url=f'{host}/api/breed/{breed}/images')
    assert response.status_code == 200
    validate(instance=response.json(), schema=expected_schema)


@pytest.mark.parametrize('breed', ['bulldog', 'bullterrier', 'corgi'])
def test_random_image_from_a_breed_collection(breed):
    expected_schema = {
        'properties': {
            'message': {'type': 'string'},
            'status': {'const': 'success'}
        }
    }
    response = requests.get(url=f'{host}/api/breed/{breed}/images/random')
    assert response.status_code == 200
    validate(instance=response.json(), schema=expected_schema)
