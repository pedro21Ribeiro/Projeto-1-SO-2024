class processo:
  def __init__(self, nome, tempoComeco, tempoExec):
    self.nome = nome
    self.tempoComeco = tempoComeco
    self.tempoFim = 0
    self.tempoExec = tempoExec
    self.tempoRes = tempoExec
    
  

listInicial = []
x = 1

while(x==1):
  nome = input("\nDigite o nome do processo: ")
  tempoComeco = int(input("Digite o tempo de começo: "))
  tempoExec = int(input("Digite o tempo de execução: "))

  listInicial.append(processo(nome, tempoComeco, tempoExec))

  x = int(input("Deseja continuar? (1 para continuar):"))


listInicial.sort(key=lambda x: x.tempoComeco)

listAtivo = [o for o in listInicial if o.tempoComeco == listInicial[0].tempoComeco]

for processo in listAtivo:
  listInicial.remove(processo)

timer = listAtivo[0].tempoComeco

listAtivo.sort(key=lambda x: x.tempoExec)

listaFin = []


while(len(listAtivo) > 0):
  if listInicial:
    if listInicial[0].tempoComeco <= timer:
      novo = [o for o in listInicial if\
      o.tempoComeco ==\
      listInicial[0].tempoComeco]
      listAtivo.extend(novo)
      for processo in novo:
        listInicial.remove(processo)
      listAtivo.sort(key=lambda x: x.tempoRes)
      pass

  listAtivo[0].tempoRes -= 1
  timer += 1

  if listAtivo[0].tempoRes == 0:
    listAtivo[0].tempoFim = timer
    listaFin.append(listAtivo[0])
    listAtivo.pop(0)

turnRoundG = 0
TEPG = 0
for i in listaFin:
  turnaroud = i.tempoFim - i.tempoComeco
  turnRoundG += turnaroud

  tempoEspera = i.tempoFim - i.tempoExec - i.tempoComeco
  TEPG += tempoEspera

  print(f"processo {i.nome} tempo de turnaroud\
  {turnaroud} tempo de espera {tempoEspera}\
  Começa em {i.tempoComeco} e termina em {i.tempoFim}")

turnRoundG /= len(listaFin)
TEPG /= len(listaFin)

print(f"Turnaround medio: {turnRoundG}")
print(f"Tempo de espera medio: {TEPG}")