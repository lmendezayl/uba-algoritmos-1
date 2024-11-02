from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  res = []
  while pedidos.empty() == False:
    pedido_en_proceso = pedidos.get()
    producto_procesado = {}
    productos = pedido_en_proceso["productos"]
    precio_total = 0
    estado = 'completo'
    id_cliente = pedido_en_proceso["id"]
    nombre_cliente = pedido_en_proceso["cliente"]
    for producto, cantidad in productos.items():
      if producto in stock_productos and cantidad <= stock_productos[producto]:
        precio_total += cantidad * precios_productos[producto]
        stock_productos[producto] -= cantidad
        producto_procesado[producto] = cantidad
      else:
        estado = 'incompleto'
        precio_total += precios_productos.get(producto, 0) * stock_productos.get(producto, 0)
        producto_procesado[producto] = stock_productos.get(producto, 0)
        stock_productos[producto] = 0
    
    pedidoTerminado = {'id': id_cliente,'cliente': nombre_cliente,'productos': producto_procesado,'precio_total': precio_total,'estado': estado}
    res.append(pedidoTerminado)
  return res

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))