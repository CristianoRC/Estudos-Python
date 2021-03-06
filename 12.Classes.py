class Pessoa:
    def __init__(self):
        print("Construtor padrão")

    def __init__(self, nome="Cristiano"):
        print(f"Construtor modificado - {nome}")
        self.nome = nome

    def falar(self):
        print("Olá Mundo")


p1 = Pessoa()
p1.falar()
print(p1.nome)
