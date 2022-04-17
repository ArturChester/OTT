import requests
import json
import time

#track time function
def decorator_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time() - start_time
        print(f"Функция выполнила работу {end_time}")
        return func

    return wrapper

@decorator_time
def st_code():
    result = requests.get('http://ip-api.com/json')
    data = json.loads(result.text)

    print('Response status code:', result.status_code)
    print('Country:', data['country'])
    print('IP:', data['query'])
    print('City', data['city'])


st_code()
