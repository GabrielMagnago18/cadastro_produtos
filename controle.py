from PyQt5 import uic, QtWidgets
# uic lê o arquivo salvo do QtDesigner, e o QtWidgets monta os elementos na tela
import mysql.connector


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro_produtos"
)


def funcao_principal():
    codigo = formulario.txt_codigo.text()
    descricao = formulario.txt_descricao.text()
    preco = formulario.txt_preco.text()
    
    categoria = ''

    print('Codigo:', codigo)
    print('Descrição:', descricao)
    print('preço:', preco)

    
    if formulario.rB_informatica.isChecked():  # verifica se o radio Button foi selecionado
        print('Categoria: informática')
        categoria = 'Informática'
    elif formulario.rB_alimentos.isChecked():
        print('Categoria: alimentos')
        categoria = 'Alimentos'
    elif formulario.rB_eletronico.isChecked():
        print('Categoria: eletrônico')
        categoria = 'Eletrônicos'

    cursor = banco.cursor()   # Comando do mysql.connector para fazer as ações no banco de dados
    comando_SQL = 'INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)'
    dados = (str(codigo), str(descricao), str(preco), categoria)
    cursor.execute(comando_SQL,dados)  # Executa os comandos
    banco.commit()

app = QtWidgets.QApplication([])  # cria a aplicação

formulario = uic.loadUi('designCadastro.ui')  # carrega o arquivo .ui

formulario.enviar.clicked.connect(funcao_principal)  # quando eu clicar no botão enviar, ele executará a função principal

formulario.show()  # mostra o formulario na tela

app.exec()
