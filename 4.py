from flask import Flask, render_template, request

app = Flask(__name__)
list = []


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training(profession):
    return render_template('2.html', profession=profession.lower())


@app.route('/list_prof/<list>')
def lst(list):
    prf_lst = ['Инженер', 'Строитель', 'Врач', 'Юрист']
    return render_template('3.html', list=lst, professions=prf_lst)


@app.route('/auto_answer') # страница выдает результат из формы ниже
def display_results():
    global list
    return render_template('auto_answer.html', list=list, title='Итоги')


@app.route('/answer', methods=['POST', 'GET'])  # форма принимает данные
def auto_answer():
    global list
    if request.method == 'GET':
        return render_template('4.html')
    if request.method == 'POST':
        for i in request.form:
            list += i


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
