from Empresa import Empresa

class Empresas:
    def __init__(self):
        self.contador = 0
        self.empresas = []
    
    def adicionarEmpresa(self, nomeEmpresa):
        novaEmpresa = Empresa(self.contador, nomeEmpresa)
        self.empresas.append(novaEmpresa)
        self.contador += 1
        return novaEmpresa
    
    def InicializarEmpresas(self):
        self.adicionarEmpresa("Phillips")
        self.adicionarEmpresa("LG")
        self.adicionarEmpresa("Samsung")
        self.adicionarEmpresa("Apple")
        self.adicionarEmpresa("Dell")
        self.adicionarEmpresa("AOC")
        self.adicionarEmpresa("Intel")
        self.adicionarEmpresa("Motorola")
        self.adicionarEmpresa("Spotify")
        self.adicionarEmpresa("Deezer")
        self.adicionarEmpresa("iFood")
        self.adicionarEmpresa("Uber")
        self.adicionarEmpresa("SpaceX")
        self.adicionarEmpresa("Sony")
        self.adicionarEmpresa("Microsoft")
        self.adicionarEmpresa("Eletrolux")
        self.adicionarEmpresa("SEMP")
        self.adicionarEmpresa("Kalunga")
    
    def encontrarEmpresa(self, idEmpresa):
        for empresa in self.empresas:
            if empresa.id == idEmpresa:
                return empresa
        return None

    def gerarListaDeEmpresas(self):
        listaNomes = []
        for empresa in self.empresas:
            listaNomes.append(empresa.nome)
        return listaNomes

    def consultarEmpresas(self):
        saida = ""
        def ordenar(e):
            return e.pontuacao
        listaOrdenada = self.empresas.copy()
        listaOrdenada.sort(reverse = True, key=ordenar)
        ranking = 1
        for empresa in listaOrdenada:
            saida += str(ranking) + "º - " + empresa.nome + ": " + str(empresa.getPontuacao()) + " --> (notas fiscais: " + str(empresa.notasFiscais) + " / debitos: " + str(empresa.debitos) +")\n"
            ranking += 1
        return saida
