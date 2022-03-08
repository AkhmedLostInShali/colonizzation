import os

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


@app.route('/success')
@app.route('/astronaut_selection')
def anketa():
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
                  <body align=center>
                    <div class="card text-white bg-danger mb-3" style="max-width: 44rem; margin-left: auto;
                     margin-right: auto;" align=left>
                      <div class="mb-3">
                        <input class="form-control" id="exampleFormControlInput1" rows="1"
                        placeholder="Введите фамилию"></input>
                        <input class="form-control" id="exampleFormControlInput1" type=text rows="1"
                        placeholder="Введите имя"></input>
                        <label for="exampleFormControlInput1" class="form-label"></label>
                        <input type="email" class="form-control" id="exampleFormControlInput1"
                        placeholder="Введите адрес почты"></input>
                        <label for="exampleFormControlInput1" class="form-label">Какое у вас образование?</label>
                        <select class="form-select" aria-label="Default select example">
                          <option selected>Начальное</option>
                          <option value="2">Среднее</option>
                          <option value="3">Высшее</option>
                        </select>
                      </div>   
                      <label for="exampleFormControlInput1" class="form-label">Какие у вас есть профессии?</label>
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                        <label class="form-check-label" for="flexCheckChecked">
                          Пилот
                        </label>
                      </div>   
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                        <label class="form-check-label" for="flexCheckChecked">
                          Инженер
                        </label>
                      </div>   
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                        <label class="form-check-label" for="flexCheckChecked">
                          Врач
                        </label>
                      </div>   
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                        <label class="form-check-label" for="flexCheckChecked">
                          Таргетолог
                        </label>
                      </div>   
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
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
                          <textarea class="form-control" aria-label="With textarea" rows="4"></textarea>
                        </div>
                        </br>
                        <label for="input-group">Приложите фотографию</label>
                        <div class="input-group mb-3">
                          <input type="file" class="form-control" id="inputGroupFile02">
                          <label class="input-group-text" for="inputGroupFile02">Upload</label>
                        </div>
                      <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                      </div>
                      <button type="submit" class="btn btn-primary" style="max-width: 8rem;">Отправить</button>
                      </div>
                    </div>
                  </body>
                </html>"""


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


@app.route("/carousel/<int:slide>")
@app.route("/carousel/")
def carousel(slide=0):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <script type="text/javascript" src="//code.jquery.com/jquery.min.js"></script>
                    <script type="text/javascript" src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
                    <title>галерея!</title>
                  </head>
                  <body>
                      <header>
                        <div id="carouselExampleIndicators" class="carousel slide" data-mdb-ride="carousel" style="width: 800px; height: 400">
                          <div class="carousel-inner">
                            <div class="carousel-item {'active' if slide == 0 else ''}" id="0">
                              <img src="{url_for('static', filename='img/landscapes/1.jpg')}" style="width: 800px; height: 400" alt="...">
                            </div>
                            <div class="carousel-item {'active' if slide == 1 else ''}" id="1">
                              <img src="{url_for('static', filename='img/landscapes/2.jpg')}" style="width: 800px; height: 400" alt="...">
                            </div>
                            <div class="carousel-item {'active' if slide == 2 else ''}" id="2">
                              <img src="{url_for('static', filename='img/landscapes/3.jpg')}" style="width: 800px; height: 400" alt="...">
                            </div>
                            <div class="carousel-item {'active' if slide == 3 else ''}" id="3">
                              <img src="{url_for('static', filename='img/landscapes/4.jpg')}" style="width: 800px; height: 400" alt="...">
                            </div>
                          </div>
                          <a class="carousel-control-prev" href="{(slide - 1) % 4}" role="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon bg-primary" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="{(slide + 1) % 4}" role="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                            <span class="carousel-control-next-icon bg-primary" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                      </header>
                  </body>
                </html>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/load_photo', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        if os.path.exists('static/img/to_show.jpg'):
            os.remove('static/img/to_show.jpg')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                              <label for="photo">Приложите фотографию</label>
                              <label></label>
                              <input class="form-control" type="file" class="form-control-file" id="photo" name="file">
                              <label></label>
                              <button class="btn btn-primary" type="submit" class="btn btn-primary">Отобразить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        if f:
            f.save('static/img/to_show.jpg')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                              <label for="photo">Приложите фотографию</label>
                              <label></label>
                              <input class="form-control" type="file" class="form-control-file" id="photo" name="file">
                              <label></label>
                              <img class="form-control" src="{url_for('static', filename="img/to_show.jpg")}" alt="">
                              <label></label>
                              <button class="btn btn-primary" type="submit" class="btn btn-primary">Отобразить</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    if os.path.exists('static/img/to_show.jpg'):
        os.remove('static/img/to_show.jpg')
