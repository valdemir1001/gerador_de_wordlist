import hashlib


texto = input('Digite o texto a ser gerado a hashe: ')

menu = int(input(''' ### Menu - ESCOLHA O TIPO DE HASH ###
                1 - MD5
                2 - SHA1
                3 - SHA256
                4 - SHA512
    Digite o número do HASH a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print("A hash MD5 da string: ",texto," é: ", resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print("A hash SHA1 da string: ", texto, " é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print("A hash SHA256 da string: ", texto, " é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print("A hash SHA512 da string: ", texto, " é: ", resultado.hexdigest())
else:
    print('Algo de errado não deu certo, tente novamente')