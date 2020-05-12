# ToDo List
# Features:
# - Permitir crear listas de tareas ordenadas o desordenadas
#   * Listas numeradas
#   * Listas no numeradas
# - Permitir agregar elementos a la lista en cualquier parte
# - Permitir modificar los elementos de la lista
# - Permitir eliminar cualquier elemento de la lista
# - Status de elementos (tareas terminadas o pendientes)
# - Eliminar una lista completa ===> TAREA
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

# ---- Creador de listas de tareas v.1.0 ----
# 1) Crear una lista
# 2) Modificar una lista
# 3) Eliminar una lista

# Para la opción 1:
# ---- Crear una lista ----
# ¿Qué tipo de lista deseas crear? 
# ...

# Para la opción 2:
# ---- Modificar lista ----
# 1) Agregar una nueva tarea a una lista
# 2) Cambiar el status de una tarea
# 3) Cambiar el nombre de una tarea
# 4) Eliminar una tarea
# 5) Regresar al menú principal


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
  print('=== Listas de tareas ===')
  for lista in listasTareas:
    print(str(n)+'.',lista[0])
    n +=1
  return

def mostrarTareas(lista):
  vineta = '' 
  if lista[1] == 'o' or lista[1] == 'O':
    vineta = 1
  else:
    vineta = '-'
  for elemento in lista[2:]:
    print (str(vineta)+'.',elemento[0])
    print('\t',elemento[1])
    if type(vineta) == int:
      vineta += 1
  return

def cambiaStatus():
  mostrarLista()
  i = int(input('A qué lista deseas hacerle cambios?'))
  lista = listasTareas[i-1]
  mostrarTareas(lista)
  j = int(input('A qué tarea deseas cambiar el status?'))
  lista[j+1][1] = input('Escribe el nuevo status para la tarea: ')
  mostrarTareas(lista)

def agregaTarea():
  mostrarLista()
  i = int(input('Elige una lista para agregar un elemento: '))
  lista = listasTareas[i-1]
  mostrarTareas(lista)
  tarea = input('Escribe la tarea a agregar: ')
  status = 'PENDIENTE'
  posicion = int(input('En qué posición deseas agregar la nueva tarea?'))
  lista.insert(posicion+1, [tarea, status])
  mostrarTareas(lista)
  return

def modificaTarea():
  

crearLista()
# crearLista()
# print (listasTareas)
# mostrarLista()
cambiaStatus()
# agregaTarea()
modificaTarea()