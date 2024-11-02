from queue import Queue
from typing import List, Dict, Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  pedidos_procesados = []
  
  while not pedidos.empty():
    pedido = pedidos.get()

    pedido_procesado = procesar_pedido(pedido, stock_productos, precios_productos)
    pedidos_procesados.append(pedido_procesado)

  return pedidos_procesados

def procesar_pedido(pedido: Queue,
                    stock_productos: Dict[str, int],
                    precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  # Defino cada apartado del pedido
  id_pedido = pedido['id']
  cliente = pedido['cliente']
  productos = pedido['productos']
  precio_total = 0.0
  estado = 'completo'
  
  # Itero entre productos del pedido para ver si hay o no stock
  for producto, cantidad in productos.items():                                    
    if stock_productos[producto] >= cantidad:   # Verifico que haya suficiente stock de tal producto
      stock_productos[producto] -= cantidad   # Resto la cantidad de productos que saque del stock
      precio_total += precios_productos[producto] * cantidad   # Sumo al precio total 
      
    else:
      estado = 'incompleto'  
      cantidad_disponible = stock_productos[producto]  # Defino la cantidad de productos disponibles para sacar el precio total
      stock_productos[producto] = 0 
      precio_total += precios_productos[producto] * cantidad_disponible

  # Defino al pedido procesado como un diccionario por cliente
  pedido_procesado = {'id': id_pedido, 'cliente': cliente, 'productos': productos, 'precio_total': precio_total, 'estado': estado}

  return pedido_procesado

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input
# pedidos = [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos = {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}

