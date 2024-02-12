import requests

url = 'https://www.youtube.com/'

response = requests.get(url)
html_code = response.text

#print le code de la page google à recuperer et à convertir au format html
print(html_code)

#parser le code HTML via le package Beautiful Soup
#pip install beautifulsoup4