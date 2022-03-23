from requests import get, post, delete, put

print(get('http://localhost:8080/api/v2/users').json())  # просмотр всех | ошибиться сложно...


print(get('http://localhost:8080/api/v2/users/1').json())  # рабочий просмотр по id
print(get('http://localhost:8080/api/v2/users/199').json())  # нерабочий просмотр по id | нет такого id


print(post('http://localhost:8080/api/v2/users',  # рабочее добавление с указанием id
           json={'id': 10, 'age': 23, 'email': 'neadmin@gmail.com', 'city_from': 'Moscow',
                 'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                 'speciality': 'Python teacher', 'surname': 'Hasaev',
                 'address': 'module_1', 'password': 'aboba', 'password_again': 'aboba'}).json())

print(post('http://localhost:8080/api/v2/users',  # рабочее добавление без указания id, добавляется в конец
           json={'age': 23, 'email': 'tester@gmail.com', 'city_from': 'Moscow',
                 'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                 'speciality': 'Python teacher', 'surname': 'Hasaev',
                 'address': 'module_1', 'password': 'aboba', 'password_again': 'aboba'}).json())

print(get('http://localhost:8080/api/v2/users').json())  # проверка

print(post('http://localhost:8080/api/v2/users',  # нерабочее добавление | указание уже имеющегося id = 10
           json={'id': 10, 'age': 23, 'email': 'tozhe_tester@gmail.com', 'city_from': 'Moscow',
                 'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                 'speciality': 'Python teacher', 'surname': 'Hasaev',
                 'address': 'module_1', 'password': 'aboba', 'password_again': 'aboba'}).json())

print(post('http://localhost:8080/api/v2/users',  # нерабочее добавление | указание уже имеющегося admin@gmail.com
           json={'age': 23, 'email': 'admin@gmail.com', 'city_from': 'Moscow',
                 'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                 'speciality': 'Python teacher', 'surname': 'Hasaev',
                 'address': 'module_1', 'password': 'aboba', 'password_again': 'aboba'}).json())

print(post('http://localhost:8080/api/v2/users',  # нерабочее добавление | пароли не совпадают
           json={'age': 23, 'email': 'unique@gmail.com', 'city_from': 'Moscow',
                 'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                 'speciality': 'Python teacher', 'surname': 'Hasaev',
                 'address': 'module_1', 'password': 'aboba', 'password_again': 'ne_aboba'}).json())

print(post('http://localhost:8080/api/v2/users',  # нерабочее добавление | указание не всех нужных данных
           json={'position': 'BOSS of the BOSS', 'city_from': 'Moscow',
                 'speciality': 'Python teacher', 'surname': 'Hasaev'}).json())

print(post('http://localhost:8080/api/v2/users',  # нерабочее добавление | не указаны данные
           json={}).json())


print(put('http://localhost:8080/api/v2/users/10',  # рабочее изменение
          json={'id': 9,
                'name': 'Ibrah', 'position': 'BOSS',
                'speciality': 'teacher', 'surname': 'Hasanov'}).json())

print(get('http://localhost:8080/api/v2/users').json())  # проверка

print(put('http://localhost:8080/api/v2/users/10',  # нерабочее изменение | нет такого id = 10
          json={'age': 11}).json())

print(put('http://localhost:8080/api/v2/users/9',  # нерабочее изменение | указание уже имеющегося id = 1
          json={'id': 1, 'age': 11}).json())

print(put('http://localhost:8080/api/v2/users/9',  # нерабочее изменение | указание уже имеющегося admin@gmail.com
          json={'age': 11, 'email': 'admin@gmail.com'}).json())

print(put('http://localhost:8080/api/v2/users/9',  # нерабочее изменение | пароли не совпадают
          json={'password': 'aboba', 'password_again': 'ne_aboba'}).json())

print(put('http://localhost:8080/api/v2/users/9',  # нерабочее изменение | отсутствует повторение пароля
          json={'password': 'aboba'}).json())

print(put('http://localhost:8080/api/v2/users/9',  # нерабочее изменение | отсутствуют данные
          json={}).json())


print(delete('http://localhost:8080/api/v2/users/11').json())  # рабочее удаление
print(delete('http://localhost:8080/api/v2/users/9').json())  # рабочее удаление
print(delete('http://localhost:8080/api/v2/users/199').json())  # нерабочее удаление | нет такого id
print(delete('http://localhost:8080/api/v2/users/1').json())  # нерабочее удаление | нельзя удалить капитана id = 1
