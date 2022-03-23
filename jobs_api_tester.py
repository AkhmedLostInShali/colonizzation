from requests import get, post, delete, put

print(get('http://localhost:8080/api/v2/jobs').json())  # просмотр всех | ошибиться сложно...


print(get('http://localhost:8080/api/v2/jobs/1').json())  # рабочий просмотр по id
print(get('http://localhost:8080/api/v2/jobs/199').json())  # нерабочий просмотр по id | нет такого id


print(post('http://localhost:8080/api/v2/jobs',  # рабочее добавление с указанием id
           json={'id': 7,
                 'job': "Заголовок",
                 'collaborators': '1, 2, 3',
                 'work_size': 1,
                 'team_leader': 3,
                 'is_finished': False}).json())

print(post('http://localhost:8080/api/v2/jobs',  # рабочее добавление без указания id, добавляется в конец
           json={'job': "Заголовок 2",
                 'collaborators': '1, 2, 3',
                 'work_size': 1,
                 'team_leader': 3,
                 'is_finished': False}).json())

print(get('http://localhost:8080/api/v2/jobs').json())  # проверка

print(post('http://localhost:8080/api/v2/jobs',  # нерабочее добавление | указание уже имеющегося id = 7
           json={'id': 7,
                 'job': "Заголовок повторка",
                 'collaborators': '1, 2, 3',
                 'work_size': 1,
                 'team_leader': 3,
                 'is_finished': False}).json())

print(post('http://localhost:8080/api/v2/jobs',  # нерабочее добавление | указание не всех нужных данных
           json={'job': "недоЗаголовок"}).json())

print(post('http://localhost:8080/api/v2/jobs',  # нерабочее добавление | не указаны данные
           json={}).json())


print(put('http://localhost:8080/api/v2/jobs/7',  # рабочее изменение
          json={'job': "Заголовок изменён"}).json())

print(get('http://localhost:8080/api/v2/jobs').json())  # проверка

print(put('http://localhost:8080/api/v2/jobs/10',  # нерабочее изменение | нет такого id = 10
          json={'job': "Заголовок не изменён"}).json())

print(put('http://localhost:8080/api/v2/jobs/7',  # нерабочее изменение | указание уже имеющегося id = 1
          json={'id': 1, 'job': "Заголовок тут не причем"}).json())

print(put('http://localhost:8080/api/v2/jobs/7',  # нерабочее изменение | отсутствуют данные
          json={}).json())


print(delete('http://localhost:8080/api/v2/jobs/7').json())  # рабочее удаление
print(delete('http://localhost:8080/api/v2/jobs/8').json())  # рабочее удаление
print(delete('http://localhost:8080/api/v2/jobs/199').json())  # нерабочее удаление | нет такого id
