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
#
#Tipos de pruebas en código:
# Pruebas Alfa --> Son las primeras pruebas que hace el programador
# Pruebas Beta --> Son las que se realizan con usuarios reales del sistema
# TODO (Tareas pendientes de diseño):
# - Agregar tareas entre el primer y último valor de la lista
# - Permitir solamente seleccionar los valores correspondientes al número de listas disponibles
# - SubMenú 'Agregar Nueva Tarea', 'Cambiar Status', 'Cambiar Nombre', 'Eliminar Tarea': 
#   * No pedir la posición de la tarea sólo cuando sea la primera tarea a agregar
# - SubMenú 'Cambiar Status', 'Cambiar nombre', 'Eliminar Tarea': 
#   * Permitir solamente seleccionar los valores correspondientes al número de tareas disponibles
# - Fecha/Hora de notas

import sys
import datetime

listasTareas = []

def menuPrincipal():
  while True:
    try:
      print(
      '''
      ---- Creador de listas de tareas v.1.0 ----
      1) Crear una lista
      2) Modificar una lista
      3) Eliminar una lista
      4) Salir del sistema
      ''')
      opc = int(input('Elige una opción del menú: '))
      if opc == 1: crearLista()
      elif opc == 2: menuModificar()
      elif opc == 3: eliminaLista()
      elif opc == 4: 
        print('Sayonara! )=')
        sys.exit() # <----- Finaliza el programa
      else: print('Opción no válida... selecciona 1, 2, 3 o 4 \=< ')
    except ValueError:
      print('¡Escribe sólo números enteros! \=< ')
    except KeyboardInterrupt: # <---- No permitir que el programa finalice con ^C
      print('\nPara salir del programa presiona 4...')
    except SystemExit:
      return 0 # <--- Buena práctica para finalizar un programa
    except:
      print(f'Ha sucedido un error inesperado: {sys.exc_info()[0]}')
      return
  return

def menuModificar():
  while True:
    try:
      print('''
      ---- Modificar lista ----
      1) Agregar una nueva tarea a una lista
      2) Cambiar el status de una tarea
      3) Cambiar el nombre de una tarea
      4) Eliminar una tarea
      5) Regresar al menú principal
      ''')
      opc = int(input('Elige una opción del menú:'))
      if opc == 1: agregaTarea()
      elif opc == 2: cambiaStatus()
      elif opc == 3: modificaTarea()
      elif opc == 4: eliminaTarea()
      elif opc == 5: menuPrincipal()    
      else:
        print('Opción no válida... selecciona 1, 2, 3, 4 o 5 \=< ')
    except ValueError:
      print('¡Escribe sólo números enteros! \=< ')
  return

def crearLista():
  tipoLista = ''
  lista = []
  print('--- Crear Listas ---')
  while True:
    opc = input('¿Qué tipo de lista deseas crear? (O = Ordenada, D = Desordenada): ')
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
    while True:
      opc = input('¿Desea agregar otra tarea? (s/n): ')
      if opc == 'n' or opc == 'N' or opc == 's' or opc == 'S':
        break
      else:
        print('Escribe sólo \'s\' ó \'n\'...')
    if opc == 'n' or opc == 'N':
      break
  listasTareas.append(lista)
  menuPrincipal()
  return

def mostrarLista():
  if len(listasTareas) > 0:
    n = 1
    print('=== Listas de tareas ===')
    for lista in listasTareas:
      # print(str(n)+'. '+lista[0])
      print(f'{n}. {lista[0]}') # <--- formatted string o cadena formateada 
      n +=1
    return True
  else: 
    print('\n¡No existen listas de tareas! )\'=\n')
    return False

def mostrarTareas(lista):
  if len(lista[2:]) > 0:
    vineta = '' 
    print(f'=== Tareas de la lista "{lista[0]}" ===')
    if lista[1] == 'o' or lista[1] == 'O':
      vineta = 1
    else:
      vineta = '-'
    for elemento in lista[2:]:
      if type(vineta) == int:
        # print (str(vineta)+'.',elemento[0])
        print (f'{vineta}. {elemento[0]}')
        vineta += 1
      else:
        print (f'{vineta} {elemento[0]}')
      print(f'\t{elemento[1]}')
    return True
  else:
    print(f'\n¡La lista "{lista[0]}" no tiene tareas! )\'=\n')
    return False

def cambiaStatus():
  print('--- Cambio de status a tareas ---')
  if mostrarLista() == True:
    i = int(input('Elige el número de la lista a modificar: '))
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      j = int(input('¿A qué tarea deseas cambiar el status? '))
      lista[j+1][1] = input('Escribe el nuevo status para la tarea: ')
      if mostrarTareas(lista):
        opc = input('¿Deseas cambiar otro status? (s/n): ')
        if opc == 'n' or opc == 'N':
          break
      else:
        break
  menuModificar()
  return

def agregaTarea():
  print('--- Agregar Tareas ---')
  if mostrarLista():
    i = int(input('Elige una lista para agregar un elemento: '))
    lista = listasTareas[i-1]
    mostrarTareas(lista)
    while True:
      if len(lista[3:]) > 0:
        posicion = int(input('¿En qué posición de la lista deseas agregar la nueva tarea? '))
      else:
        posicion = 1
      tarea = input('Escribe la tarea a agregar: ')
      status = 'PENDIENTE'
      lista.insert(posicion+1, [tarea, status])
      mostrarTareas(lista)
      opc = input('¿Deseas agregar otra tarea? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  menuModificar()
  return

def modificaTarea():
  print('--- Modificar tareas ---')
  if mostrarLista():
    i = int(input('Elige una lista para modificar una tarea: '))
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      j = int(input('Escribe el número de tarea que deseas modificar: '))
      lista[j+1][0] = input('Escribe el nuevo nombre para la tarea: ')
      mostrarTareas(lista)
      opc = input('¿Deseas modificar otra tarea? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  menuModificar()

def eliminaTarea():
  print('--- Eliminar tareas ---')
  if mostrarLista():
    i = int(input('Elige una lista para eliminar alguna de sus tareas: '))
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      j = int(input('Elige el número de la tarea a eliminar: '))
      lista.pop(j+1)
      if mostrarTareas(lista):
        opc = input('¿Deseas eliminar otra tarea? (s/n): ')
        if opc == 'n' or opc == 'N':
          break
      else:
        break
  menuModificar()
  return

def eliminaLista():
  print('--- Eliminar Listas ---')
  while mostrarLista():
    i = int(input('Elige una lista para eliminarla: '))
    listasTareas.pop(i-1)
    if not mostrarLista():
      break
    else:
      opc = input('¿Deseas eliminar otra lista? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  menuPrincipal()
  return

# menuPrincipal()

date = datetime.datetime.now()
print(date)
if date.month < 10:
  print(f'Fecha actual: {date.day}/0{date.month}/{date.year}')
elif date.day < 10:
  print(f'Fecha actual: 0{date.day}/{date.month}/{date.year}')
elif date.day < 10 and date.month < 10:
  print(f'Fecha actual: 0{date.day}/0{date.month}/{date.year}')
else:
  print(f'Fecha actual: {date.day}/{date.month}/{date.year}')
