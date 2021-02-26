def printar_nome(nome, sobrenome):
    print(f'{nome} {sobrenome}')


nome, sobrenome = "Cristiano", "Cunha"
printar_nome(nome, sobrenome)

#Podemos fazer a inversão das variáveis sem precisar de uma terceira(temporária)
nome, sobrenome = sobrenome, nome
printar_nome(nome, sobrenome)
