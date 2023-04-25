from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo= None, ano=None, qtdPortas=None, cilindradas = None):
        super().__init__(modelo, ano)
        self.qtdPortas = qtdPortas
        self.cilindradas = cilindradas

    def imprimirEspecifico(self):
        super().imprimir()
        print("Cilindradas: ", self.cilindradas)
