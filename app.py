from flask import Flask, request, render_template
from main import get_clientes,Post_DadosApi
import pyodbc
app = Flask(__name__)
formData = {}
DadosApi ={}



server = "srv-dev-sql-acquasoft.database.windows.net"
database = "BackupBolinho"
username = "saadmin"
password = "hw7CsBhUALD-n6!"

cnxn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";ENCRYPT=no;UID="
    + username
    + ";PWD="
    + password
)
print("Conexão Bem Sucedida")
dadosapi = list()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
      
        DadosApi = {
            "Token": request.form['Token'],
            "Instancia": request.form['Instancia'], 
            "Registros": request.form['Registros'],
            "DataLigar": request.form['DataLigar'],}
        Post_DadosApi(DadosApi)
    if request.method == 'GET':
     dadosapi.clear()
     cursor = cnxn.cursor()
     GetDadosAPI  =f"select Id,Token,Instancia, Registros, DataliGar from DadosAPI"
     cursor.execute(GetDadosAPI)
     data = cursor.fetchall()
     for dados in data:
         dadosapi.append({
             "Id":dados[0],
             "Token":dados[1],
             "Instancia":dados[2],
             "Registros":dados[3],
         })
   
     headings = ("ID","Token","Instancia","Registros")
    
     return render_template('home.html', headings=headings, data = dadosapi) 

        
       
    else:
        return render_template('home.html')


     
@app.route('/EnviarMsg', methods=['POST'])
def EnviarMsg():
    get_clientes()
    status = "Enviando"
    return render_template('home.html', status=status)


if __name__ == "__main__":
    app.run(debug=True)
