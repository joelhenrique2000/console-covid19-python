import json, requests

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

  print('\n\n\n\n\n\n__________________________________\n')
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
  print('\n__________________________________\n\n\n\n\n\n')

def printPaises():
  paises = getPaises()

  print('\n\n\n\n\n\n__________________________________\n')
  for pais in paises:
    print(pais)
    
  print('\n__________________________________\n\n\n\n\n\n')

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
  mortesNovos = estatistica["deaths"]["new"])
  mortesTotal = estatistica["deaths"]["total"])

  # Informações de testes
  testesTotal = estatistica["tests"]["total"])

  # Informação da data
  data = estatistica["time"])

  # Aqui vai fazer a lógica para imprimir em um txt

def init():
  printEstatisticas("brazil")
  printPaises()

  # Aqui vai ter o menu
  # Ele sempre vai está rodando, vai ser apresentado as opções
  # para o usuário. Elas são:
  # 1. Ver paises (vai imprimir paises)
  # 2. Ver estatistica de um pais (vai peguntar qual pais é e imprimir)
  # 3. Salvar estatisticas de um pais no arquivo txt (vai perguntar qual pais)
  # 4. Sair (Se o usuário quiser sair vai fechar o programa)

  # A dica é usar uma variavel de parada, se ele for True é pq o programa
  # precisa continuar rodando, caso não o programa fecha
  # Para isso o While vai ser util, sua condição é a variavel de parada 
  # é a variavel de parada.

# Iniciando a função
init()





# print(response.text)