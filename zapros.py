from requests import get, post, delete, put

# print(post('http://localhost:8080/api/v2/jobs',  # рабочее добавление жертвы
#            json={'id': 7,
#                  'job': "Заголовок",
#                  'collaborators': '1, 2, 3',
#                  'work_size': 1,
#                  'team_leader': 3,
#                  'is_finished': True}).json())
#
#
# print(get('http://localhost:8080/api/v2/jobs/7').json())
#
# print(put('http://localhost:8080/api/v2/jobs/7',  # корректное изменение жертвы
#           json={'id': 8,
#                  'job': "Заголовок был изменён",
#                  'collaborators': '1, 2, 3',
#                  'work_size': 10,
#                  'is_finished': True}).json())
#
# print(get('http://localhost:8080/api/v2/jobs').json())
#
# print(put('http://localhost:8080/api/v2/jobs/999').json())  # изменение без данных
#
# print(put('http://localhost:8080/api/v2/jobs/2',  # изменение id на уже имеющийся
#           json={'id': 1}).json())
#
# print(put('http://localhost:8080/api/v2/jobs/999',  # изменение несуществующего id
#           json={'id': 998}).json())
print(get('http://localhost:8080/api/users').json())

print(post('http://localhost:8080/api/users', json={'address': 'module_1', 'age': 23, 'email': 'neadmin@gmail.com',
                                                    'name': 'Ibrahim', 'position': 'BOSS of the BOSS',
                                                    'speciality': 'Python teacher', 'surname': 'Hasaev',
                                                    'id': 10, 'password': 'aboba', 'password_again': 'aboba'}).json())

print(get('http://localhost:8080/api/users/10').json())

print(put('http://localhost:8080/api/users/10',  # корректное изменение жертвы
          json={'id': 9,
                'name': 'Ibrah', 'position': 'BOSS',
                'speciality': 'teacher', 'surname': 'Hasanov'}).json())