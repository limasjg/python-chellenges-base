#Lists

lista = [1,2,3,4,5,6,7,8,9,10]
lista.append(11)
lista.remove(5)
lista[1] = 20

#print(lista)

#Tuplas

tupla = (10, 20)

#tupla[10] = 100
#print(tupla)


#Sets
conjunto = {1,2,3,2,4,4,5}

conjunto.add(6)
conjunto.add(2)
conjunto.remove(3)

#print(conjunto)


#Dict
dicionario = {"nome": "João", "idade": 32, "cidade": "cwb"}

dicionario["idade"] = 26
dicionario["profissão"] = "arquiteto"
del dicionario["cidade"]
#cidade = dicionario.pop("cidade")
print(dicionario)
