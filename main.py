import circular
import sjf

#sjf.init()
#circular.init()
opcao = 0

while (opcao != 3):
  print("\t MENU ")
  print("1 - SJF")
  print("2 - Circular")
  print("3 - SAIR")
  opcao = int(input("Digite uma opcao: "))

  match opcao:
    case 1:
      sjf.init()
    case 2:
      circular.init()
    case 3:
      print("Bye Bye!")
    case _:
      print("Opcao invalida!")
    

