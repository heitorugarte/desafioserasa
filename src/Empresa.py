class Empresa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.pontuacao = 50
        self.notasFiscais = 0
        self.debitos = 0

    def carregarDados(self, notasFiscais, debitos):
        self.addNotasFiscais(notasFiscais)
        self.addDebitos(debitos)
        self.calcularPontuacao()
        return
    
    def setNotasFiscais(self, quantidade):
        self.notasFiscais = quantidade
        return

    def setDebitos(self, quantidade):
        self.debitos = quantidade
        return

    def addNotasFiscais(self, quantidade):
        self.notasFiscais += quantidade
        return
    
    def addDebitos(self, quantidade):
        self.debitos += quantidade
        return

    def calcularPontuacao(self):
        pontuacaoAtual = 50
        notasFiscaisCalculadas = 0
        debitosCalculados = 0

        while notasFiscaisCalculadas < self.notasFiscais:
            pontuacaoAtual += pontuacaoAtual * 0.02
            notasFiscaisCalculadas += 1
        
        while debitosCalculados < self.debitos:
            pontuacaoAtual -= pontuacaoAtual * 0.04
            debitosCalculados += 1 

        if pontuacaoAtual > 100:
            pontuacaoAtual = 100
        elif pontuacaoAtual < 1:
            pontuacaoAtual = 1
        
        pontuacaoAtual = round(pontuacaoAtual)
        self.pontuacao = pontuacaoAtual
        print("Pontuação da empresa (" + self.nome + ") calculada em: " + str(self.pontuacao))
        return self.pontuacao
    
    def getConfiabilidade(self):
        return str(self.pontuacao + "%")
    
    def getPontuacao(self):
        return self.pontuacao