from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')