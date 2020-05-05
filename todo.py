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

tareasOrdenadas = []
tareasDesordenadas = []

def crearLista():
  opc = input('Qué tipo de lista deseas crear? (O = Ordenada, D = Desordenada): ')
  if opc == 'o' or opc == 'O':
    tareas = tareasOrdenadas
  elif opc == 'd' or opc == 'D':
    tareas = tareasDesordenadas
  titulo = input('Título de la lista: ')
  tareas.append(titulo)

# Desord [titulo, [ [tarea, status], [tarea,status] ] ]
# Ord [titulo, [[tarea, status], [tarea, status]] ]

  while True:
    tarea = input('Tarea a agregar: ')
    status = 'PENDIENTE'
    tareas.append([tarea, status])
    opc = input('Desea agregar otra tarea? (s/n): ')
    if opc == 'n' or opc == 'N':
      break
  return

# def mostrarLista():


# def cambiaStatus():

crearLista()
print (tareasDesordenadas)
print (tareasOrdenadas)