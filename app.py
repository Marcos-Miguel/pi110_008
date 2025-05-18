from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pi110.sqlite3.db"

# initialize the app with the extension
db = SQLAlchemy(app)

class Cadastros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable = False)
    telefone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    historico_resumido = db.Column(db.String(600), nullable = False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable = False)

    def __init__(self, nome, telefone, email, historico_resumido):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.historico_resumido = historico_resumido

class Contatos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable = False)
    telefone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    mensagem = db.Column(db.String(600), nullable = False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable = False)

    def __init__(self, nome, telefone, email, mensagem):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.mensagem = mensagem

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#Neste estágio do aplicativo a leitura dos dados inseridos
#no banco de dados poderá ser feito pelo software: sqlitestudio.
@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        historico = request.form['historico_resumido']
        cadastro = Cadastros(nome, telefone, email, historico)
        db.session.add(cadastro)
        db.session.commit()
        status = "Cadastro registrado"
    return render_template('cadastro.html')

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        mensagem = request.form['mensagem']
        contato = Contatos(nome, telefone, email, mensagem)
        db.session.add(contato)
        db.session.commit()
        status = "Mensagem registrada"
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)