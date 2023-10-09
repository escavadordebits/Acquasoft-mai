from flask import Flask, request, render_template
from main import get_clientes,Post_DadosApi
app = Flask(__name__)
formData = {}
DadosApi = list()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        Token = request.form['Token']
        Instancia = request.form['Instancia']
        Registros =request.form['Registros']
        DataLigar =request.form['DataLigar']
        DadosApi.append({Token,Instancia,Registros,DataLigar})
        Post_DadosApi(DadosApi)



        msg = "Cadastrado com Sucesso!"
        return render_template('home.html', msg=msg)

    else:
        return render_template('home.html')


@app.route('/EnviarMsg', methods=['POST'])
def EnviarMsg():
    get_clientes()
    status = "Enviando"
    return render_template('home.html', status=status)


if __name__ == "__main__":
    app.run(debug=True)
