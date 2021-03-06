class Pessoa:
    def __init__(self):
        self.nome = "CRISTIANO"

    @property
    def nome(self):
        return f"{self._nome} - do Getter"

    @nome.setter
    def nome(self, nome):
        if(nome != ""):
            self._nome = nome.title()


p1 = Pessoa()
print(p1.nome)
p1.nome = "CUNHA"
print(p1.nome)
