from tkinter import *
from random import randint
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from Empresas import Empresas
import webbrowser, os

#Classe principal da aplicação, contém a janela inicial da aplicação, dados e as variaveis de controle
class Principal:
    def __init__(self,master=None):
        #Dados da aplicação
        self.empresas = Empresas()
        self.empresas.InicializarEmpresas()
        #------------------------------------------------------------

        #Variaveis de controle
        self.carregandoDados = False
        self.consultandoDados = False
        #------------------------------------------------------------

        #Interface gráfica (GUI)

        #Definição do container principal da aplicação e sua dimensão
        self.root = root
        self.root.geometry("280x200")
        #------------------------------------------------------------
        
        #Fontes padrão à serem a utilizadas pela aplicação
        self.fonteTitulo = ("Verdana", "14", "bold")
        self.fontePadrao = ("Verdana", "10")
        self.fonteBotao = ("Arial", "11")
        #--------------------------------------------------------------

        #Definições do primeiro container da janela inicial da aplicação
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 15
        self.primeiroContainer.pack()

        self.lblBemVindo = Label(self.primeiroContainer, text="Bem-vindo!")
        self.lblBemVindo["font"] = self.fonteTitulo
        self.lblBemVindo.pack()

        self.lblGuia1 = Label(self.primeiroContainer, text="O que você deseja fazer?")
        self.lblGuia1["font"] = self.fontePadrao
        self.lblGuia1.pack()
        #--------------------------------------------------------------

        #Definições do segundo container da janela inicial da aplicação
        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 15
        self.segundoContainer.pack()

        self.btnCarregarDados = Button(self.segundoContainer)
        self.btnCarregarDados["text"] = "Carregar Dados"
        self.btnCarregarDados["font"] = self.fonteBotao
        self.btnCarregarDados["width"] = 17
        self.btnCarregarDados["command"] = self.carregarDados
        self.btnCarregarDados.pack()

        self.btnConsultarRanking = Button(self.segundoContainer)
        self.btnConsultarRanking["text"] = "Consultar Ranking"
        self.btnConsultarRanking["font"] = self.fonteBotao
        self.btnConsultarRanking["width"] = 17
        self.btnConsultarRanking["command"] = self.consultarRanking
        self.btnConsultarRanking.pack()
        #--------------------------------------------------------------

    #Método para exibir mensagem de erro genérica
    def janelaDeErro(self, textoErro):
        janelaErro = Toplevel()
        janelaErro.wm_title("Erro")
        janelaErro.wm_geometry("600x50")

        lblErro = Label(janelaErro, text = textoErro)
        lblErro["font"] = self.fontePadrao
        lblErro.pack()

        btnOk = Button(janelaErro, text = "OK")
        btnOk["font"] = self.fonteBotao
        btnOk["command"] = lambda: janelaErro.destroy()
        btnOk.pack()
    #--------------------------------------------------------------
    
    #Método para exibir mensagem de sucesso genérica
    def janelaSucesso(self, textoSucesso):
        janelaSucesso = Toplevel()
        janelaSucesso.wm_title("Sucesso")
        janelaSucesso.wm_geometry("600x50")

        lblSucesso = Label(janelaSucesso, text = textoSucesso)
        lblSucesso["font"] = self.fontePadrao
        lblSucesso.pack()

        btnOk = Button(janelaSucesso, text = "OK")
        btnOk["font"] = self.fonteBotao
        btnOk["command"] = lambda: janelaSucesso.destroy()
        btnOk.pack()
    #--------------------------------------------------------------

    #Método que trata da abertura, leitura e processamento do arquivo de entrada de dados.
    def carregarDados(self):
        #Método para gerar um arquivo de entrada de dados aleatórios
        def gerarEntrada():
            saida = open("entradas/entrada-gerada.txt", "+w")
            saida.write("+" + str(randint(0, 25)) + "," + "-" + str(randint(0, 25)))
            saida.close()
            webbrowser.open(os.getcwd()+"//entradas/entrada-gerada.txt")
            self.janelaSucesso("A entrada foi gerada com sucesso! O arquivo pode ser encontrado na raiz do projeto.")
        #--------------------------------------------------------------

        #Método que processa o arquivo de entrada de dados
        def processarArquivo():
            diretorio = askopenfilename()
            if str(diretorio).endswith('.txt'):
                arquivo = open(diretorio)
                linha = arquivo.readline()
                idEmpresa = cbEmpresas.current()
                empresa = self.empresas.encontrarEmpresa(idEmpresa)
                if empresa is not None:
                    dados = linha.split(",")
                    notasFiscais = int(dados[0].replace("+",""))
                    debitos = int(dados[1].replace("-",""))

                    empresa.carregarDados(notasFiscais, debitos)
                    self.janelaSucesso("Os dados da " + empresa.nome + " foram processados com sucesso!")
                    self.carregandoDados = False
                    janelaCarregarDados.destroy()
                else:
                   self.janelaDeErro("A empresa selecionada não foi encontrada no banco!")
            else:
                self.janelaDeErro("O arquivo selecionado é inválido!")
        #--------------------------------------------------------------

        #Interface gráfica da janela de carregamento de dados
        if not self.carregandoDados: #Checa se a janela de carregar dados já está aberta
            def fechouJanela():
                self.carregandoDados = False
                janelaCarregarDados.destroy()

            self.carregandoDados = True
            janelaCarregarDados = Toplevel()
            janelaCarregarDados.wm_title("Carregar Dados")
            janelaCarregarDados.wm_geometry("400x400")
            janelaCarregarDados.protocol("WM_DELETE_WINDOW", fechouJanela)

            lblTitulo = Label(janelaCarregarDados, text = "Carregar Dados")
            lblTitulo["font"] = self.fonteTitulo
            lblTitulo.pack()

            lblGuia = Label(janelaCarregarDados, text = "Para carregar novos dados, selecione a empresa referente ao arquivo à ser carregado:")
            lblGuia["font"] = self.fontePadrao
            lblGuia.pack()

            cbEmpresas = ttk.Combobox(janelaCarregarDados)
            cbEmpresas["values"] = self.empresas.gerarListaDeEmpresas()
            cbEmpresas.pack()

            btnCarregar = Button(janelaCarregarDados)
            btnCarregar["text"] = "Carregar Dados"
            btnCarregar["font"] = self.fonteBotao
            btnCarregar["width"] = 17
            btnCarregar["command"] = processarArquivo
            btnCarregar.pack()

            lblGerarEntrada = Label(janelaCarregarDados, text = "Caso você queira gerar uma entrada com dados aleatórios,\n clique em \"Gerar Entrada\" e depois selecione o\n arquivo que será aberto através do botão \"Carregar\"")
            lblGerarEntrada["font"] = self.fontePadrao
            lblGerarEntrada.pack()

            btnGerar = Button(janelaCarregarDados)
            btnGerar["text"] = "Gerar Entrada"
            btnGerar["font"] = self.fonteBotao
            btnGerar["width"] = 17
            btnGerar["command"] = gerarEntrada
            btnGerar.pack()
        #--------------------------------------------------------------
    
    #Método que trata da consulta do ranking das empresas
    def consultarRanking(self):
        #Método para fazer a consulta das empresas e alimentar o textbox com o resultado
        def consultarDados():
            resultado = str(self.empresas.consultarEmpresas())
            textBox.config(state = NORMAL)
            textBox.delete('1.0', END)
            textBox.insert(INSERT, resultado)
            textBox.config(state = DISABLED)
        #--------------------------------------------------------------

        #Interface gráfica da tela de consulta de dados
        if not self.consultandoDados: #Checa se a janela de consulta já está aberta
            def fechouJanela():
                self.consultandoDados = False
                janelaConsultar.destroy()

            self.consultandoDados = True
            janelaConsultar = Toplevel()
            janelaConsultar.wm_title("Consultar Ranking")
            janelaConsultar.wm_geometry("600x600")
            janelaConsultar.protocol("WM_DELETE_WINDOW", fechouJanela)

            lblTitulo = Label(janelaConsultar, text = "Consultar Ranking das Empresas")
            lblTitulo["font"] = self.fonteTitulo
            lblTitulo.pack()

            lblGuia = Label(janelaConsultar, text = "Para consultar o ranking das empresas cadastradas, clique no botão \"Consultar\"")
            lblGuia["font"] = self.fontePadrao
            lblGuia.pack()

            btnConsultar = Button(janelaConsultar)
            btnConsultar["text"] = "Consultar"
            btnConsultar["font"] = self.fonteBotao
            btnConsultar["width"] = 17
            btnConsultar["command"] = consultarDados
            btnConsultar.pack()

            textBox = Text(janelaConsultar)
            
            textBox.pack()
        #--------------------------------------------------------------

if __name__ == "__main__":
    root = Tk()
    app = Principal(root)
    app.root.title("Desafio Serasa")
    root.mainloop()