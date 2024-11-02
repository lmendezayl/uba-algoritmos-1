import sys

def fibonacciNoRecursivo(n: int) -> int:
   if n == 0:
      return 0
   if n == 1: 
      return 1
   
   b = 0
   a = 1
   fibonacciActual = 0

   for i in range (n-1): 
      fibonacciActual = b + a
      b = a
      a = fibonacciActual

   return fibonacciActual

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))