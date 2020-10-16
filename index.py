import json, requests, codecs, os

def getEstatisticas(pais):
  url = "https://covid-193.p.rapidapi.com/statistics?country="+pais
  headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "BF3VktHr4RmshMmOUbrOu2PrFhRgp1FUfeNjsnWVqJzqUF7I5j"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = response.json()
  return jsonData["response"][0]

def getPaises():
  url = "https://covid-193.p.rapidapi.com/countries"
  headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "BF3VktHr4RmshMmOUbrOu2PrFhRgp1FUfeNjsnWVqJzqUF7I5j"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = response.json()
  return jsonData["response"]

def printEstatisticas(pais):
  estatistica = getEstatisticas(pais)

  print('\n__________________________________\n')
  print('-> Continente:.....', estatistica["continent"])
  print('-> País:...........', estatistica["country"])
  print('-> População:......', estatistica["population"], ' Habitantes')
  print('-> Casos:          ')
  print('   -> Novos:.......', estatistica["cases"]["new"])
  print('   -> Ativos:......', estatistica["cases"]["active"])
  print('   -> Críticos:....', estatistica["cases"]["critical"])
  print('   -> Recuperados:.', estatistica["cases"]["recovered"])
  print('   -> Total:.......', estatistica["cases"]["total"])
  print('-> Mortes:     ')
  print('   -> Novos:.......', estatistica["deaths"]["new"])
  print('   -> Total:.......', estatistica["deaths"]["total"])
  print('-> Testes:         ')
  print('   -> Total:.......', estatistica["tests"]["total"])
  print('-> Data:...........', estatistica["time"])
  print('\n__________________________________\n')

def printPaises():
  paises = getPaises()

  print('\n__________________________________\n')
  for pais in paises:
    print(pais)
    
  print('\n__________________________________\n')

def salvarInfoTxt(pais):

  # Objeto com as estatisticas do pais
  estatistica = getEstatisticas(pais)

  # Informações do pais
  continente = estatistica["continent"]
  pais = estatistica["country"]
  populacao = estatistica["population"]
  
  # Informações do caso
  casosNovos = estatistica["cases"]["new"]
  casosAtivos = estatistica["cases"]["active"]
  casosCriticos = estatistica["cases"]["critical"]
  casosRecuperados = estatistica["cases"]["recovered"]
  casosTotal = estatistica["cases"]["total"]

  # Informações de morte
  mortesNovos = estatistica["deaths"]["new"]
  mortesTotal = estatistica["deaths"]["total"]

  # Informações de testes
  testesTotal = estatistica["tests"]["total"]

  # Informação da data
  data = estatistica["time"]

  # Imprimindo a estatistica de um determinado país
  # no arquivo txt
  with codecs.open(f'{pais}.txt', "w", "utf-8-sig") as temp:
    temp.write(f'Dados COVID-19 {data}\n')
    temp.write(f'├── Continente: {continente}\n')
    temp.write(f'├── Pais: {pais}\n')
    temp.write(f'├── Populacao: {populacao}\n')
    temp.write(f'├── Casos\n')
    temp.write(f'│   ├── Novos casos: {casosNovos}\n')
    temp.write(f'│   ├── Casos Ativos: {casosAtivos}\n')
    temp.write(f'│   ├── Casos criticos: {casosCriticos}\n')
    temp.write(f'│   ├── Casos recuperados: {casosRecuperados}\n')
    temp.write(f'│   └── Total: {casosTotal}\n')
    temp.write(f'├── Mortes\n')
    temp.write(f'│   ├── Novas mortes: {mortesNovos}\n')
    temp.write(f'│   └── Total: {mortesTotal}\n')
    temp.write(f'└── Testes\n')
    temp.write(f'    └── Total: {testesTotal}\n')

def menuRecursivo(menu1):
 
  # Menu de opções
  print('Seja bem vindo ao nosso sistema de contagem de casos, escolha a opção desejada', '''\n[1] Paises \n[2] Estatistica \n[3] Salvar estatistica \n[4] Fechar programa''')

  # Caso o input seja algo diferente de um inteiro o valor será 0
  try: menu1 = int(input("Qual a sua escolha?"))
  except: menu1 = 0

  # Caso ocorra algum erro
  try:
    if menu1 == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      printPaises()
      menuRecursivo(0)
      
    elif menu1 == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      printEstatisticas(input("Qual o seu país?"))
      menuRecursivo(0)
      
    elif menu1 == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      salvarInfoTxt(input("Qual o seu país?"))
      menuRecursivo(0)

    # Condição de parada
    elif menu1 == 4:
      print("Consulta finalizada com sucesso, volte sempre.")
    
    else:
      # Limpando o console
      os.system('cls' if os.name == 'nt' else 'clear')
      menuRecursivo(0)
  except:
    print("Ocorreu algum erro, tente novamente")
    menuRecursivo(0)

def init():
  menuRecursivo(0)
  
# Iniciando o programa
init()
