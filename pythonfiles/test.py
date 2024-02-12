print("Hello World! ") 

name="Mohammed"
age=24
print(f"my name is {name} and i have {age} years old")


#Dictionnaire(objet):

donnees={"name":['Mohammed','Iqbal'],
         "surname":['Harnoufi','Abdou Ali'],
         "age":['24',22]}

personne_id1 = donnees["name"][0]
print(personne_id1)

#conditionner un programme:
soleil=True
neige=False

if soleil:
    print("on va à la plage !")
elif neige:
    print("on va faire une bataille de neige")
else:
    print("on reste à la maison ")

soleil=True
en_semaine=False
if soleil and not en_semaine:
    print("on part en week end")
else:
    print("on reste à la maison")

neige=True
sun=True
semaine=False
if neige and sun and not semaine:
    print("On part au ski")
elif sun and not neige and not semaine:
    print ("On part à la piscine")
else:
    print("on reste dormir")

#match cases:
animal="chat"
match animal:
    case "chien":
        print("wouaf")
    case "chat":
        print("miaou")
    case "oiseau":
        print("piou piou") 
        #valeur par defaut:
    case _:
        print("animal inconnu")

#boucle for:
        
for x in range(5):
    print(x)

for x in range(3):
    print(f"{x} bouteilles de bières au mur !")

#boucle while:

capacite_avion=150
capacite_actuelle=50
while capacite_actuelle < capacite_avion:
    capacite_actuelle+=1
print(capacite_actuelle)

#break:
for i in range(10):
    print(i)
    if i==3:
        break
    
#continue:
for i in range(10):
    if i==3:
        continue
    print(i)
#lorsque i=3 le continue retourne a for i ignorant ainsi le print(i) pour 3

#FONCTION

def message():
    print("Hello Bonjour Comment ça va?")   

message()

def addition(a, b):
    resultat= a+b
    return resultat

num1=48
num2=52
print(addition(num1,num2))


#try/expect

numerateur=input("Entrer le numerateur : ")
denominateur=input("Entrer le denominateur : ")

try:
    resultat=int(numerateur)/int(denominateur)
    print(f"Le resultat est {resultat}")
except ZeroDivisionError: 
    print("Erreur : division par zero !")
except ValueError:    
    print("Erreur: Conversion de type incorrecte")
