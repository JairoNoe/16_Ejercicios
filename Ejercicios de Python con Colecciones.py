'''
Alumno :Hernandez Vega Jairo Noe 
Grupo IRD42
EJERCICIOS 
'''
#################################################################
#Contar Ocurrencias de Elementos
def conteo(palabras):
    conteo_palabras = {}
    
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
    
    return conteo_palabras
palabras = ["python", "java", "python", "c++"]
resultado = conteo(palabras)
print(resultado)

##############################################################
#Combinar Diccionarios

def comb_dicio(dic1, dic2):
    resultado = dic1.copy()

    for num, valores in dic2.items():
        if num in resultado:
            resultado[num] += valores  
        else:
            resultado[num] = valores 

    return resultado
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
resultado = comb_dicio(dic1, dic2)
print(resultado)

#################################################################
#Listas de Frecuencia
def contar_frecu(num):
    frecuencia = {}
    for num in numeros:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    return frecuencia
numeros = [1, 1, 2, 3, 3, 3]
print(contar_frecu(numeros))
#################################################################
#Filtrar Palabras Largas

def palab_largas(palabra_larg, long):
    return [palabra for palabra in palabra_larg if len(palabra) > long]

palabra_larg = ["hola", "mundo", "python", "programación"]
long = 5
print(palab_largas(palabras, long))
#################################################################
#Inversión de Tuplas en Lista

def invertir(tuplas):
    return [(b, a) for a, b in tuplas]
tuplas = [(1, 2), (3, 4), (5, 6)]
print(invertir(tuplas))
##################################################################3
#Encontrar el Valor Más Frecuente

def val_frecuente(lista):
    contador = {}
    for num in lista:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    return max(contador, key=contador.get)
numeros = [1, 2, 3, 1, 2, 1]
resultado = val_frecuente(numeros)
print(resultado)  

########################################################
#Comprobar Subconjunto
#El método issubset en Python sirve para indicar si un conjunto es un subconjunto de otro

def subconjuntos(conju1, conjun2):
    return conju1.issubset(conjun2)

conju1 = {1, 2, 3}
conjun2 = {1, 2, 3, 4, 5}
print(subconjuntos(conju1, conjun2))
######################################################
#Agrupación por Clave
def  datos(personas):
    agrupacion = {}
    for persona in personas:
        edad = persona["edad"]
        nombre = persona["nombre"]
        if edad in agrupacion:
            agrupacion[edad].append(nombre)
        else:
            agrupacion[edad] = [nombre]
    return agrupacion

personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
print(datos(personas))
##################################################
#Merge Sort utilizando Listas
def ms(listas):
    if len(listas) <= 1:
        return listas
    medio = len(listas) // 2
    izquierda = ms(listas[:medio])
    derecha = ms(listas[medio:])
    return merge(izquierda, derecha)
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
numeros = [5, 3, 8, 6, 2]
resultado = ms(numeros)
print(resultado) 
###########################################################
#Eliminar Elementos por Condición
def eliminacion(numero, limite):
    return [num for num in numero if num >= limite]

numero= [1, 2, 3, 4, 5]
limite = 3
print(eliminacion(numero, limite))
###########################################################
#Flatten List of Lists
def list(listas):
    return [elemento for sublista in listas for elemento in sublista]

listas = [[1, 2], [3, 4], [5]]
print(list(listas))

########################################################
#Cálculo de Mediana
def calculo(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    else:
        return numeros_ordenados[mitad]
numeros = [1, 3, 2, 4, 5]
print(calculo(numeros))

##########################################################
#Duplicar Elementos en una Lista
def elemento_dubli(numeros):
    return [num for num in numeros for _ in range(2)]
numeros = [1, 2, 3]
print(elemento_dubli(numeros))

########################################################
#Contar Palabras en Frases
def conteo(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
print(conteo(frases))
########################################################
#Encontrar Clave Máxima en Diccionario
def clave_max(diccionario):
    return max(diccionario, key=diccionario.get)
diccionario = {'a': 10, 'b': 20, 'c': 5}
print(clave_max(diccionario))

#######################################################
#Palíndromos en una Lista
def encontrar_palindromos(lista):
    return [palabra for palabra in lista if palabra == palabra[::-1]]
palabras = ["ana", "oso", "hola", "level"]
resultado = encontrar_palindromos(palabras)
print(resultado) 




