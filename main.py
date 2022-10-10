import requests
import datetime
import time
import json

token = "78a0654f78a0654f78a0654f4b78d897d2778a078a0654f19b7d334eecc4a3b87fff1e6"
version = '5.131'
url = 'https://api.vk.com/method/'
public = input("Введите короткое имя сообщества: ")
date_example = input("Введите дату последнего визита в формате месяц/день/год (например, 8/8/2022): ")
# первод введенной даты в формат unixtime
date_format = datetime.datetime.strptime(date_example,
                                         "%m/%d/%Y")
unix_time = datetime.datetime.timestamp(date_format)


# получение id паблика
def getting_id():
    needed_id = requests.get(url + 'groups.getById', params={
        'access_token': token,
        'v': version,
        'group_id': public
    }).json()
    return needed_id['response'][0]['id']


# получение максимального значения параметра offset для нужного паблика
def getting_offset():
    public_id = getting_id()
    count_followers = requests.get(url + 'groups.getMembers', params={
        'access_token': token,
        'v': version,
        'group_id': public_id,
        'sort': 'id_desc',
        'offset': 0,
        'fields': 'last_seen'
    }).json()['response']['count']
    return count_followers // 1000


# получение всех пользователей, в зависимости от даты последнего визита с помощью цикла
def get_all_followers():
    public_id = getting_id()
    followers_ids = []
    offset = 0
    maximal_offset = getting_offset()
    while offset < maximal_offset:
        response = requests.get(url + 'groups.getMembers', params={
            'access_token': token,
            'v': version,
            'group_id': public_id,
            'sort': 'id_desc',
            'offset': offset,
            'fields': 'last_seen'
        }).json()['response']
        offset += 1
        for el in response['items']:
            try:
                if el['last_seen']['time'] >= unix_time:
                    followers_ids.append(el['id'])
            except Exception as E:
                continue
    return followers_ids


# занесение полученных id в файл, названный по имени паблика
with open(f'{public}.txt', 'w') as f:
    for el in get_all_followers():
        f.write("%s\n" % el)
