from inspect import ArgSpec


def multi(*args):
  for arg in args:
    total = total * arg

  return total


def aplicar(*args, operador):
  if operador == "*":
    return multi(args)
  elif operador == "+":
    return sum(args)
  else:
    return "Operador não está valido para aplicação"



print(aplicar(2, 4, 6, 8, operador="+"))    