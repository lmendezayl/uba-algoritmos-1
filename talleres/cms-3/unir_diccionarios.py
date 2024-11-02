from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[int]]:
  resultado = {}
  for diccionario in a_unir:
    for clave, valor in diccionario.items():
        if clave in resultado:
            resultado[clave].append(valor)
        else:
            resultado[clave] = [valor]
  return resultado


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))