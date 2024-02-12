#import de requests un package via pip

import requests
if __name__ =='__main__':
    resultat3 = requests.get("https://google.fr")
    print(resultat3.content)


#package de calcul dans operations.py
    
from calculator.operations import division, multiplication

if __name__ =='__main__':

    resultat = multiplication(10,20)
    print(resultat)
    resultat2 = division(10,20)
    print(resultat2)