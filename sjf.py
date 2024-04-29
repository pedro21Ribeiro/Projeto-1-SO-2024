def init():
  class processo:
    def __init__(self, nome, tempoExec):
      self.nome = nome
      self.tempoComeco = 0
      self.tempoFim = 0
      self.tempoExec = tempoExec
  
  
  list = []
  x = 1
  

  
  while(x==1):
    nome = input("\nDigite o nome do processo: ")
    tempoExec = int(input("Digite o tempo de execução: "))
  
    list.append(processo(nome, tempoExec))
  
    x = int(input("Deseja continuar? (1 para continuar):"))
  list.sort(key=lambda x: x.tempoExec)
  
  timer = 0
  for i in list:
    timer += i.tempoExec
    i.tempoFim = timer
  
  turnRoundG = 0
  TEPG = 0
  print("\n")
  for i in list:
    turnaroud = i.tempoFim - i.tempoComeco
    turnRoundG += turnaroud
  
    tempoEspera = i.tempoFim - i.tempoExec - i.tempoComeco
    TEPG += tempoEspera

    
    print(f"processo {i.nome} tempo de turnaroud\
    {turnaroud} tempo de espera {tempoEspera}")
  
  turnRoundG /= len(list)
  TEPG /= len(list)
  
  print(f"Turnaround medio: {turnRoundG}")
  print(f"Tempo de espera medio: {TEPG}")