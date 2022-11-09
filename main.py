def soma(x,y,z):
  return (x+y+z)

def media(nota):
  return nota/3

def menu():
  x = int(input('Digite a nota da AV1: '))
  y = int(input('Digite a nota da AV2: '))
  z = int(input('Digite a nota da AVD: '))
  
  print('Soma: ', soma(x,y,z))
  print('Media: ', media(soma(x,y,z)))

while True:
    menu()