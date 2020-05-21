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
# - Agregar tareas entre el primer y último valor de la lista -CHECK
# - Permitir solamente seleccionar los valores correspondientes al número de listas disponibles 
# - SubMenú 'Agregar Nueva Tarea', 'Cambiar Status', 'Cambiar Nombre', 'Eliminar Tarea': 
#   * No pedir la posición de la tarea sólo cuando sea la primera tarea a agregar
# - SubMenú 'Cambiar Status', 'Cambiar nombre', 'Eliminar Tarea': 
#   * Permitir solamente seleccionar los valores correspondientes al número de tareas disponibles
# - Fecha/Hora de notas

import sys
import datetime

listasTareas = []

def getDate():
  date = datetime.datetime.now()
  if date.day < 10 and date.month < 10:
    return f'0{date.day}/0{date.month}/{date.year}'
  elif date.month < 10:
    return f'{date.day}/0{date.month}/{date.year}'
  elif date.day < 10:
    return f'0{date.day}/{date.month}/{date.year}'
  else:
    return f'{date.day}/{date.month}/{date.year}'

def getHour():
  hour = datetime.datetime.now()
  if hour.hour < 10 and hour.minute < 10 and hour.second < 10:
    return f'0{hour.hour}:0{hour.minute}:0{hour.second}'
  elif hour.minute < 10 and hour.second < 10:
    return f'{hour.hour}:0{hour.minute}:0{hour.second}'
  elif hour.hour < 10 and hour.second < 10:
    return f'0{hour.hour}:{hour.minute}:0{hour.second}'
  elif hour.hour < 10 and hour.minute < 10:
    return f'0{hour.hour}:0{hour.minute}:{hour.second}'
  elif hour.hour < 10:
    return f'0{hour.hour}:{hour.minute}:{hour.second}'
  elif hour.minute < 10:
    return f'{hour.hour}:0{hour.minute}:{hour.second}'
  elif hour.second < 10:
    return f'{hour.hour}:{hour.minute}:0{hour.second}'
  else:
    return f'{hour.hour}:{hour.minute}:{hour.second}'

print(getHour())
  

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
      print('*** ERROR: ¡Escribe sólo números enteros! \=< ***')
    except KeyboardInterrupt: # <---- No permitir que el programa finalice con ^C
      print('\n*** ERROR: Para salir del programa presiona 4... ***')
    except SystemExit:
      return 0 # <--- Buena práctica para finalizar un programa
    except:
      print(f'*** Ha sucedido un error inesperado: {sys.exc_info()[0]} ***')
      return 1
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
      elif opc == 5: return # menuPrincipal()     
      else:
        print('Opción no válida... selecciona 1, 2, 3, 4 o 5 \=< ')
    except ValueError:
      print('*** ERROR: ¡Escribe sólo números enteros! \=< ***')
    except KeyboardInterrupt:
      print('\n*** ERROR: Para terminar el programa, presiona 4 en el menú principal ***')
  return

def crearLista():
  tipoLista = ''
  lista = []
  print('--- Crear Listas ---')
  while True:
    try:
      opc = input('¿Qué tipo de lista deseas crear? (O = Ordenada, D = Desordenada): ')
      # transformar de mayúsculas a minúsculas
      opc = opc.lower()
      if opc == 'o' or opc == 'd':
        tipoLista = opc
        break
      else:
        print('*** ERROR: Escribe O para una lista ordenada o D para una lista desordenada... ***')
    except KeyboardInterrupt:
      print('\n*** ERROR: El proceso no puede ser cancelado ***')
  titulo = input('Título de la lista: ')
  lista.append(titulo)
  lista.append(tipoLista)
  lista.append([getDate(), getHour()])
  while True:
    try:
      tarea = input('Tarea a agregar: ')
      status = 'PENDIENTE'
      lista.append([tarea, status])
      while True:
        try:
          opc = input('¿Desea agregar otra tarea? (s/n): ')
          opc = opc.lower()
          if opc == 'n' or opc == 's':
            break
          else:
            print('Escribe sólo \'s\' ó \'n\'...')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
      if opc == 'n':
        break
    except KeyboardInterrupt:
      print('\n*** ERROR: El proceso no puede ser cancelado ***')
  listasTareas.append(lista)
  # menuPrincipal()
  return

def mostrarLista():
  if len(listasTareas) > 0:
    n = 1
    print('=== Listas de tareas ===')
    for lista in listasTareas:
      # Cuando no se haya modificado la lista, mostrar la fecha/hora de creación,
      # cuando la lista ya haya sido modificada, mostrar la fecha/hora de modificación
      print(f'{n}. {lista[0]} {lista[2][0]} {lista[2][1]}') # <--- formatted string o cadena formateada 
      
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
  if mostrarLista():
    if len(listasTareas) > 1:
      while True:
        try:
          i = int(input('Elige el número de la lista a modificar: '))
          if i >= 1 and i <= len(listasTareas):
            break
          else:
            print(f'*** ERROR: Escribe un número entre 1 y {len(listasTareas)} ***')
        except ValueError:
          print('*** ERROR: Escribe sólo números enteros ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
    else:
      i = 1
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      if len(lista[2:]) > 1:
        while True:
          try:
            j = int(input('¿A qué tarea deseas cambiar el status? '))
            if j >= 1 and j <= len(lista[2:]):
              break
            else:
              print(f'*** ERROR: Escribe un número entre 1 y {len(lista[2:])}')
          except ValueError:
            print('*** ERROR: Escribe sólo números enteros ***')
          except KeyboardInterrupt:
            print('\n*** ERROR: El proceso no puede ser cancelado ***')
      else:
        j = 1
      lista[j+1][1] = input('Escribe el nuevo status para la tarea: ')
      # Cuando no exista fecha y hora de modificación, agregarla,
      # cuando ya exista fecha y hora de modificación, actualizarla
      listasTareas[i-1].insert(3,[getDate(), getHour()])
      
      tareas = mostrarTareas()
      if tareas:
        while True:
          try:
            opc = input('¿Deseas cambiar otro status? (s/n): ')
            opc = opc.lower()
            if opc == 'n' or opc == 's':
              break
            else:
              print('*** ERROR: Escribe sólo \'s\' o \'n\' ***')
          except KeyboardInterrupt:
            print('*** ERROR: El proceso no puede ser cancelado ***')
      # --- Refactorizable ---
      # else:
      #   break
      elif not tareas or opc == 'n':
        break
      # ----------------------
  # menuModificar()
  return

def agregaTarea():
  print('--- Agregar Tareas ---')
  if mostrarLista():
    if len(listasTareas) > 1:
      while True:
        try:
          i = int(input('Elige una lista para agregar un elemento: '))
          if i >= 1 and i <= len(listasTareas):
            break
          else:
            print(f'*** ERROR: Escribe un número entre 1 y {len(listasTareas)}')
        except ValueError:
          print('\n*** ERROR: Escribe sólo números enteros ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
    else:
      i = 1
    lista = listasTareas[i-1]
    mostrarTareas(lista)
    while True:
      if len(lista[2:]) > 1:
        while True:
          try:
            posicion = int(input('¿En qué posición de la lista deseas agregar la nueva tarea? '))
            if posicion >= 1 and posicion <= len(lista[2:])+1:
              break
            else:
              print(f'ERROR: Escribe un número entre 1 y {len(lista[2:])+1}')
          except ValueError:
            print('*** ERROR: Escribe sólo números enteros... ***')
          except KeyboardInterrupt:
            print('\n*** ERROR: El proceso no puede ser cancelado ***')
      else:
        posicion = 1
      tarea = input('Escribe la tarea a agregar: ')
      status = 'PENDIENTE'
      lista.insert(posicion+1, [tarea, status])
      mostrarTareas(lista)
      while True:
        try:
          opc = input('¿Deseas agregar otra tarea? (s/n): ')
          opc = opc.lower()
          if opc == 'n' or opc == 's':
            break
          else:
            print('*** ERROR: Escribe \'s\' o \'n\' ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
      if opc == 'n':
        break
  # menuModificar()
  return

def modificaTarea():
  print('--- Modificar tareas ---')
  if mostrarLista():
    if len(listasTareas) > 1:
      while True:
        try:
          i = int(input('Elige una lista para modificar una tarea: '))
          if i >= 1 and i <= len(listasTareas):
            break
          else:
            print(f'*** ERROR: Escribe un número entre 1 y {len(listasTareas)} ***')
        except ValueError:
          print('*** ERROR: Escribe sólo números enteros ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
    else:
      i = 1
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      if len(lista[2:]) > 1:
        while True:
          try:
            j = int(input('Escribe el número de tarea que deseas modificar: '))
            if j >= 1 and j <= len(lista[2:]):
              break
            else:
              print(f'*** ERROR: Escribe un número entre 1 y {len(lista[2:])} ***')
          except ValueError:
            print('*** ERROR: Escribe sólo números enteros ***')
          except KeyboardInterrupt:
            print('\n*** ERROR: El proceso no puede ser cancelado ***')
      else:
        j = 1
      lista[j+1][0] = input('Escribe el nuevo nombre para la tarea: ')
      mostrarTareas(lista)
      while True:
        try:
          opc = input('¿Deseas modificar otra tarea? (s/n): ')
          opc = opc.lower()
          if opc == 'n' or opc == 's' :
            break
          else:
            print('*** ERROR: Escribe sólo \'s\' o \'n\' ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
      if opc == 'n':
        break
  # menuModificar()
  return

def eliminaTarea():
  print('--- Eliminar tareas ---')
  if mostrarLista():
    if len(listasTareas) > 1:
      while True:
        try:
          i = int(input('Elige una lista para eliminar alguna de sus tareas: '))
          if i >= 1 and i <= len(listasTareas):
            break
          else:
            print(f'*** ERROR: Escribe un número entre 1 y {len(listasTareas)} ***')
        except ValueError:
          print('*** ERROR: Escribe sólo números enteros ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
    else:
      i = 1
    lista = listasTareas[i-1]
    while mostrarTareas(lista):
      if len(lista[2:]) > 1:
        while True:
          try:
            j = int(input('Elige el número de la tarea a eliminar: '))
            if j >= 1 and j <= len(lista[2:]):
              break
            else:
              print(f'*** ERROR: Escribe un número entre 1 y {len(lista[2:])} ***')
          except ValueError:
            print('*** ERROR: Escribe sólo números enteros ***')
          except KeyboardInterrupt:
            print('\n*** ERROR: El proceso no puede ser cancelado ***')
      else:
        j = 1
      lista.pop(j+1)
      tareas = mostrarTareas(lista)
      if tareas:
        while True:
          opc = input('¿Deseas eliminar otra tarea? (s/n): ')
          opc = opc.lower()
          if opc == 'n' or opc == 's':
            break
          else:
            print('*** ERROR: Escribe sólo \'s\' o \'n\' ***')
      # --- Refactorizable ---
      elif not tareas or opc == 'n':
        break
      # ----------------------
  # menuModificar()
  return

def eliminaLista():
  print('--- Eliminar Listas ---')
  while mostrarLista():
    if len(listasTareas) > 1:
      while True:
        try:
          i = int(input('Elige una lista para eliminarla: '))
          if i >= 1 and i <= len(listasTareas):
            break
          else:
            print(f'*** ERROR: Escribe un número entre 1 y {len(listasTareas)} ***')
        except ValueError:
          print('\n*** ERROR: Escribe sólo números enteros ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
    else:
      i = 1
    listasTareas.pop(i-1)
    if not mostrarLista():
      break
    else:
      while True:
        try:
          opc = input('¿Deseas eliminar otra lista? (s/n): ')
          opc = opc.lower()
          if opc == 'n' or opc == 's':
            break
          else:
            print('*** ERROR: Escribe sólo \'s\' o \'n\' ***')
        except KeyboardInterrupt:
          print('\n*** ERROR: El proceso no puede ser cancelado ***')
      if opc == 'n':
        break
  # menuPrincipal()
  return

# menuPrincipal()

# dateFormat = '%d/%m/%Y'
# date = datetime.datetime.strptime('02/01/2020', dateFormat)
# date = datetime.datetime.now()
# print(date)
# if date.day < 10 and date.month < 10:
#   print(f'Fecha actual: 0{date.day}/0{date.month}/{date.year}')
# elif date.month < 10:
#   print(f'Fecha actual: {date.day}/0{date.month}/{date.year}')
# elif date.day < 10:
#   print(f'Fecha actual: 0{date.day}/{date.month}/{date.year}')
# else:
#   print(f'Fecha actual: {date.day}/{date.month}/{date.year}')

# print(f'Hora: {date.hour}:{date.minute}:{date.second}')
