from Empresa import Empresa
from Empresas import Empresas
import unittest

class ValidarAplicacao(unittest.TestCase):
    def testeCriarEmpresa(self):
        empresa = Empresa(0, "Teste")

        self.assertEqual(0, empresa.id)
        self.assertEqual("Teste", empresa.nome)
    
    def testeSetAddNota(self):
        empresa = Empresa(0, "Teste")
        empresa.setNotasFiscais(5)

        self.assertEqual(5, empresa.notasFiscais)

        empresa.addNotasFiscais(2)

        self.assertEqual(7, empresa.notasFiscais)
    
    def testeSetAddDebito(self):
        empresa = Empresa(0, "Teste")
        empresa.setDebitos(5)

        self.assertEqual(5, empresa.debitos)

        empresa.addDebitos(2)

        self.assertEqual(7, empresa.debitos)

    def testeCalculaPontuacao(self):
        empresa = Empresa(0, "Teste")

        empresa.setNotasFiscais(3)

        self.assertEqual(53, empresa.calcularPontuacao())

        empresa.setDebitos(1)

        self.assertEqual(51, empresa.calcularPontuacao())

        empresa.setNotasFiscais(0)
        empresa.setDebitos(1000)

        self.assertEqual(1, empresa.calcularPontuacao())

        empresa.setNotasFiscais(1000)
        empresa.setDebitos(0)

        self.assertEqual(100, empresa.calcularPontuacao())

    def testeAdicionarEmpresa(self):
        empresas = Empresas()      
        empresas.adicionarEmpresa("Empresa Teste")

        self.assertEqual(1, len(empresas.empresas))

    def testeEncontrarEmpresa(self):
        empresas = Empresas()
        empresaAdicionada = empresas.adicionarEmpresa("Empresa Teste")

        empresaEncontrada = empresas.encontrarEmpresa(0)

        self.assertEqual(empresaAdicionada, empresaEncontrada)

    def testeInicializarEmpresas(self):
        empresas = Empresas()
        empresas.InicializarEmpresas()

        self.assertEqual(18, len(empresas.empresas))