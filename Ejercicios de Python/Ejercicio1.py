#Escribe un programa en Python que imprime los números del 1 a 100 pero aplicando lo siguiente:

#Si el número es multiplo de 3, imprime "Fizz" en lugar del número.

#Si el número es multiplo de 5, imprime "Buzz" en lugar del número.

#Si el número es multiplo de 3 y 5 al mismo tiempo, imprime "FizzBuzz".

#En cualquier otro caso, imprima el número.

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
    
    else:
      print(i)