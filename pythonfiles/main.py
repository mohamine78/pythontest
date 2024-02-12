#import de requests un package via pip

#import requests
#if __name__ =='__main__':
    #resultat3 = requests.get("https://www.google.fr/")
    #print(resultat3.content)


#package de calcul dans operations.py
    
from calculator.operations import division, multiplication

if __name__ =='__main__':

    resultat = multiplication(10,20)
    print(resultat)
    resultat2 = division(10,20)
    print(resultat2)

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

reponse=requests.get(url)
page=reponse.content
soup = BeautifulSoup(page,"html.parser")
print(soup.title)

class_name = "gem-c-document-ist__item-link"
titres= soup.find_all("a", class_=class_name)
print(titres)

titre_textes= []
for titre in titres:
    titre_textes.append(titre.string)

print(titre_textes)


#print le code de la page google à recuperer et à convertir au format html


#parser le code HTML via le package Beautiful Soup
#pip install beautifulsoup4