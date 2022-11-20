import pytest
import requests

host = 'https://api.openbrewerydb.org'


def test_list_breweries():
    response = requests.get(url=f'{host}/breweries')
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize('obdb_id', ['10-56-brewing-company-knox', '10-barrel-brewing-co-bend-1'])
def test_single_brewery(obdb_id):
    response = requests.get(url=f'{host}/breweries/{obdb_id}')
    assert response.status_code == 200
    assert response.json()['id'] == obdb_id


@pytest.mark.parametrize('city', ['Costa Mesa', 'Gilbert', 'Williamsville'])
def test_by_city(city):
    response = requests.get(url=f'{host}/breweries', params={'by_city': city})
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery['city'] == city


@pytest.mark.parametrize('name', ['10-56 Brewing Company', '10 Barrel Brewing Co - Bend Pub'])
def test_by_name(name):
    response = requests.get(url=f'{host}/breweries', params={'by_name': name})
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery['name'] == name


@pytest.mark.parametrize('brewery_type', ['micro', 'nano', 'regional', 'brewpub'])
def test_by_type(brewery_type):
    response = requests.get(url=f'{host}/breweries', params={'by_type': brewery_type})
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery['brewery_type'] == brewery_type
