class Carro:
    def __init__(self):
        self.chassi = None
        self.motor = None
        self.rodas = None

    def __str__(self):
        return f"Carro com chassi: {self.chassi}, motor: {self.motor}, rodas: {self.rodas}"


class ConstrutorDeCarro:
    def __init__(self):
        self.carro = Carro()

    def construir_chassi(self, chassi):
        self.carro.chassi = chassi
        return self

    def construir_motor(self, motor):
        self.carro.motor = motor
        return self

    def construir_rodas(self, rodas):
        self.carro.rodas = rodas
        return self

    def obter_carro(self):
        return self.carro


#Exemplo de Uso
carro_esportivo = ConstrutorDeCarro().construir_chassi("Fibra de carbono").construir_motor("V8").construir_rodas("Magnésio").obter_carro()
carro_popular = ConstrutorDeCarro().construir_chassi("Aço").construir_motor("4 cilindros").construir_rodas("Aço").obter_carro()

print(carro_esportivo)
print(carro_popular)