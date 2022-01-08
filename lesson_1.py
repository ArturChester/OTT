import requests


def test_check_status():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    status = data.get('status')
    assert status == 'success'


def check_country(country):
    if 'T'.isupper():
        return True
    elif 'u'.islower():
        return True

def test_check_country():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    country = data.get('country')
    assert check_country(country)

def test_check_countryCode():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    countryCode = data.get('countryCode')
    assert countryCode == 'TR'


def check_region(region):
        if region != '07':
            return False
        elif region == '08':
            return False
        return True

def test_check_region():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    region = data.get('region')
    assert check_region(region)

def test_check_regionName():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    regionName = data.get('regionName')
    assert regionName == 'Antalya'


def test_check_city():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    city = data.get('city')
    assert city == 'Antalya'


def check_query(query):
    numbers = query.split('.')
    numbers = [int(a) for a in numbers]
    for b in numbers:
        if b > 0 and b < 185:
            return False
        return True

def test_check_query():
    result = requests.get('http://ip-api.com/json')
    data = result.json()
    query = data.get('query')
    assert len(query) > 0
    assert query > ''
    assert check_query(query)