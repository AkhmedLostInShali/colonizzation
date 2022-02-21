from flask import Flask, url_for, redirect, render_template, request, session
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<title>')
@app.route('///<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!',
                         'Присоединяйся!'])


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div>Вот она какая, красная планета</div>
                  </body>
                </html>"""


@app.route('/success')
@app.route('/promotion_image')
def prom_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def prom_choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h4>Моё предложение: {planet_name}</h4>
                    <h2>Прекрасный выбор!</h2>
                    <div class="alert alert-primary" role="alert">
                      {planet_name} находится где-то в космосе
                    </div>
                    <div class="alert alert-success" role="alert" width=400px>
                      Мы предлагаем насладиться пейзажами {planet_name}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Билет до {planet_name} будет стоить {len(planet_name) ** 6} миллионов
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <form method="post" class="login_form">
                        <div class="mb-3">
                          <input class="form-control" name="surname" rows="1"
                          placeholder="Введите фамилию"></input>
                          <input class="form-control" name="name" type=text rows="1"
                          placeholder="Введите имя"></input>
                          <label class="form-label"></label>
                          <input type="email" class="form-control" name="email"
                          placeholder="Введите адрес почты"></input>
                          <label class="form-label">Какое у вас образование?</label>
                          <select class="form-select" name="grade" aria-label="Default select example">
                            <option selected value="Начальное">Начальное</option>
                            <option value="Среднее">Среднее</option>
                            <option value="Высшее">Высшее</option>
                          </select>
                        </div>   
                        <label class="form-label">Какие у вас есть профессии?</label>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="Пилот" id="flexCheckChecked" name="job">
                          <label class="form-check-label" for="flexCheckChecked">
                            Пилот
                          </label>
                        </div>   
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="Инженер" id="flexCheckChecked" name="job">
                          <label class="form-check-label" for="flexCheckChecked">
                            Инженер
                          </label>
                        </div>   
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="Врач" id="flexCheckChecked" name="job">
                          <label class="form-check-label" for="flexCheckChecked">
                            Врач
                          </label>
                        </div>   
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="Таргетолог" id="flexCheckChecked" name="job">
                          <label class="form-check-label" for="flexCheckChecked">
                            Таргетолог
                          </label>
                        </div>   
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="Суетолог" id="flexCheckChecked" name="job">
                          <label class="form-check-label" for="flexCheckChecked">
                            Суетолог
                          </label>
                        </div>
                          </br>
                          <label for="form-check">Укажите пол</label>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                            <label class="form-check-label" for="male">
                              Мужской
                            </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                            <label class="form-check-label" for="female">
                              Женский
                            </label>
                          </div>
                          </br>
                          <label for="input-group">Почему вы хотите принять участие в миссии?</label>
                          <div class="input-group">
                            <textarea class="form-control" aria-label="With textarea" rows="4" name="reason"></textarea>
                          </div>
                          </br>
                          <label for="input-group">Приложите фотографию</label>
                          <div class="input-group mb-3">
                            <input type="file" class="form-control" id="inputGroupFile02">
                            <label class="input-group-text" for="inputGroupFile02">Upload</label>
                          </div>
                        <div class="form-group form-check">
                          <input type="checkbox" class="form-check-input" id="acceptRules" name="ready">
                          <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                        </div>
                        <button type="submit" class="btn btn-primary" style="max-width: 8rem;">Отправить</button>
                        </div>
                    </form>
                  </body>
                </html>"""
    elif request.method == 'POST':
        session["form"] = request.form.copy()
        print(session['form'])
        return redirect("/auto_answer")


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h4>Результаты отбора</h4>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {str(level)} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                      составляет {str(rating)}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    form = session.get('form')
    data = {'title': 'анкета', 'surname': form.get('surname'), 'name': form.get('name'),
            'education': form.get('grade'), 'profession': form.get('job'),
            'sex': form.get('sex'), 'motivation': form.get('reason'),
            'ready': form.get('ready')}
    return render_template('auto_answer.html', data=data)


@app.route('/training/<prof>')
def scheme(prof):
    return render_template('scheme.html', profession=prof)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('cabin_table.html', sex=sex, age=age)


@app.route('/list_prof/<marker>')
def list_maker(marker):
    prof = ['врач', "доктор", "медик", "лекарь", "цирюльник"]
    return render_template('lister.html', professions=prof, mark=marker)


@app.route('/distribution')
def cabins():
    people = ['Ридли Скотт', "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('caiuta.html', stuff=people)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
