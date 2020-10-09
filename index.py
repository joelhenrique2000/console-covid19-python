import json, requests

def estatisticas(pais):
  url = "https://covid-193.p.rapidapi.com/statistics?country="+pais
  headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "BF3VktHr4RmshMmOUbrOu2PrFhRgp1FUfeNjsnWVqJzqUF7I5j"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = response.json()
  return jsonData["response"][0]

def paises():
  url = "https://covid-193.p.rapidapi.com/countries"
  headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "BF3VktHr4RmshMmOUbrOu2PrFhRgp1FUfeNjsnWVqJzqUF7I5j"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = response.json()
  return jsonData["response"])

def init():

  paises = paises()

  estatistica = estatisticas("brazil")

  print(estatistica["continent"])
  print(estatistica["country"])
  print(estatistica["population"])
  print(estatistica["cases"])
  print(estatistica["deaths"])
  print(estatistica["tests"])
  print(estatistica["time"])

init()





# print(response.text)