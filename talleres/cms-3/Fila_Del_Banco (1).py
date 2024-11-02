from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  minutos_pasados = 0
  proximoNumero = fila.qsize() + 1

  minutosEnCaja1 = 0
  minutosEnCaja2 = 0
  minutosEnCaja3 = 0

  caja1Vacia = True
  caja2Vacia = True
  caja3Vacia = True

  while minutos_pasados <= min :
    size = fila.qsize()
    if minutos_pasados % 4 == 0:
      fila.put(proximoNumero)
      proximoNumero += 1
    if fila.empty() != True:
      if minutos_pasados == 1 or (minutosEnCaja1 % 10 == 0  and minutosEnCaja1 > 0):
        fila.get()
        minutosEnCaja1 = 0
        caja1Vacia = False
      elif minutos_pasados == 2 or (minutosEnCaja3 % 4 == 0 and minutosEnCaja3 > 0):
        personaCaja3 = fila.get()
        minutosEnCaja3 = 0
        caja3Vacia = False
      elif minutos_pasados == 3 or (minutosEnCaja2 % 4 == 0 and minutosEnCaja2 > 0):
        fila.get()
        minutosEnCaja2 = 0
        caja2Vacia = False
      if minutosEnCaja3 == 3:
        fila.put(personaCaja3)
    if caja1Vacia  != True:
      minutosEnCaja1 += 1
    if caja2Vacia != True:
      minutosEnCaja2 += 1
    if caja3Vacia != True:
      minutosEnCaja3 += 1
    minutos_pasados += 1
  
  return fila


if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

