#Conjuntos da matemática = set(Estrutura de dados)
#A estrutura set tem valores únicos(Não pode repetir.)
conjunto_a = {1, 2, 2, 3, 1}
print(conjunto_a)
conjunto_b = {4, 5, 6}
conjunto_c = {2, 3, 5}
conjunto_d = {2, 3}
print(conjunto_a.union(conjunto_b)) #soma de conjuntos
print(conjunto_a.intersection(conjunto_c)) #Intersecção de conjuntos
print(conjunto_a.intersection(conjunto_b)) #Diferença de conjuntos
print(conjunto_a.difference(conjunto_c))
print(conjunto_a.symmetric_difference(conjunto_c)) #Soma do conjunto - Sua intersecção
print(conjunto_a.issubset(conjunto_d)) #Indica se um(Base) é subconjunto do outro(Argumento)
print(conjunto_d.issubset(conjunto_a))
print(conjunto_a.issuperset(conjunto_d)) #Inverte, indica se o argumento é subconjunto do conjunto primeiro
print(conjunto_d.issuperset(conjunto_a))
print(conjunto_a.isdisjoint(conjunto_b)) #Indica se os dois conjuntos são disjuntos, isso é, não possuem interseção
print(conjunto_a.isdisjoint(conjunto_c))
conjunto_a.add(7) #Caso o elemento a ser adicionado não exista no conjunto, ele o adiciona
conjunto_a.discard(2) #Exclui um valor do conjunto(Se o valor não estiver no conjunto ele não faz nada)
conjunto_a.remove(3) #Exclui um valor do conjunto(Se o valor não estiver no conjunto ele retorna um erro)
conjunto_a.clear() #Limpa o conjunto
conjunto_b.pop() #exclui o primeiro valor do conjunto