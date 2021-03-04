def thorwError(throw):
    if(throw.lower() == "true"):
        raise Exception('Eu sou um erro')


thorwErrorNow = input('Mostar Erro[true/false]: ')

try:
    thorwError(thorwErrorNow)
    print("Não deu erro!")
except:
    print("Deu erro")
