# ToDo List
# Features:
# - Permitir crear listas de tareas ordenadas o desordenadas
#   * Listas numeradas
#   * Listas no numeradas
# - Permitir agregar elementos a la lista en cualquier parte
# - Permitir modificar los elementos de la lista
# - Permitir eliminar cualquier elemento de la lista
# - Status de elementos (tareas terminadas o pendientes)
#
# Ejemplo de lista numerada:
# Receta de café
# 1. Agregar una cucharada de café en una taza de 250ml
# 2. Agregar una cucharada de sustituto de crema
# 3. Agregar agua hirviendo a la taza
# 4. Disfrutar!
# 
# Ejemplo de lista no numerada
# Lista del súper
# - 1Kg de carne de res (Pendiente)
# - 1 manojo de cilantro (Completado)
# - 1Kg de jitomate (Pendiente)
# - Paquete de servilletas
# - 1Kg de aguacate (Pendiente)
# 
# Propiedades de la lista:
# - Título
# - Elementos de la lista
#   * Nombre
#   * Status (Completado/Pendiente)
# - Número de elemento (**listas ordenadas)

# listasTareas = 
# [ [título de la lista, [tarea1], [tarea2], [tareaN] ], [título de la lista 2, [tarea1], [tareaN] ] ]
# [
#   [
#     título de la lista,
#     tipoLista = 'o', --> LISTA ORDENADA
#     [
#       nombre de la tarea,
#       status
#     ],
#     [
#       nombre de la tarea2,
#       status
#     ], ...
#   ],
#   [
#     título de la lista2,
#     tipoLista = 'd', --> LISTA DESORDENADA
#     [
#       nombre de la tarea2,
#       status
#     ],
#     [
#       nombre de la tarea2,
#       status
#     ], ...
#   ],
# ]
# 
# Título de la lista
# --- Tareas ---
# 1. Tarea 1
#   Status
# 2. Tarea 2
#   Status
# ...
#
# Título de la lista
# --- Tareas ---
# - Tarea 1
#   Status: 
# - Tarea 2
#   Status
# ...


# tareasOrdenadas = []
# tareasDesordenadas = []

listasTareas = []

def crearLista():
  tipoLista = ''
  lista = []
  while True:
    opc = input('Qué tipo de lista deseas crear? (O = Ordenada, D = Desordenada): ')
    if opc == 'o' or opc == 'O' or opc == 'd' or opc == 'D':
      tipoLista = opc
      break
    else:
      print('Escribe O para una lista ordenada o D para una lista desordenada...')
   
  titulo = input('Título de la lista: ')
  lista.append(titulo)
  lista.append(tipoLista)

  while True:
    tarea = input('Tarea a agregar: ')
    status = 'PENDIENTE'
    lista.append([tarea, status])
    opc = input('Desea agregar otra tarea? (s/n): ')
    if opc == 'n' or opc == 'N':
      break
  listasTareas.append(lista)

  return

def mostrarLista():
  n = 1
  for lista in listasTareas:
    print(str(n)+'.',lista[0])
    n +=1
  opc = int(input('Elige el número de lista que deseas ver: '))
  lista = listasTareas[opc-1]
  tipoLista = lista[1]
  vineta = ''
  if tipoLista == 'o':
    vineta = 1
  else:
    vineta = '-'
  for elemento in lista:
    




# def cambiaStatus():

crearLista()
crearLista()
# print (listasTareas)
mostrarLista()