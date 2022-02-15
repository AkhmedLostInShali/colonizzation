from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def countdown():
    return "И на Марсе будут яблони цвести!"


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
