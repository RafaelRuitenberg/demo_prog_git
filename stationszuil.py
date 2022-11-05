from datetime import datetime
import random
import csv
while True:
    bericht = str(input(
        'U kunt hier een bericht van maximaal 140 karakters schrijven: \n'))  # Laat de gebruiker een bericht schrijven
    print('----------------------------------------------------------------')
    if len(bericht) > 140:
        print('Dit bericht heeft te veel karakters, maak het korter.')
        continue
    elif len(bericht) == 0:
        print('U kunt geen leeg bericht invullen.')
        continue
    else:
        break
with open('stationszuil.txt', 'a') as stationszuil:  # Open de file van de 'database'
    stationszuil.write(f'{bericht};')

naam = str(input(
    'Wat is uw naam? (Als u geen naam wil opgeven, laat dit dan leeg)\n'))  # Laat de gebruiker een naam invoeren, of niet
print('----------------------------------------------------------------')
if naam == '':  # Als de gebruiker niks invult bij naam,
    naam = 'anoniem'  # Dan wordt de 'naam' anoniem
with open('stationszuil.txt', 'a') as stationszuil:  # Open de file van de 'database'
    stationszuil.write(f'{naam};')

now = datetime.now()
datum = now.strftime("%d/%m/%Y %H:%M")  # Zo voeg je de datum en tijd toe
with open('stationszuil.txt', 'a') as stationszuil:
    stationszuil.write(f'{datum};')


with open('stations.txt', 'r') as file:  # Open de file stations met alle stadnamen
    station = file.readlines()  # Lees elke regel
    stationlijst = []   # Maakt een lege list
    for i in station:
        stationlijst.append(i.strip())  # Haalt de \n weg
    het_station = random.choice(stationlijst)   # Dit kiest een random station
    with open('stationszuil.txt', 'a') as stationszuil:
        stationszuil.write(f'{het_station}')

moderatie = [bericht, naam, het_station, datum]
with open('moderatie.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(moderatie)

if __name__ == '__main__':
    print(bericht)
    print(datum)
    print(het_station)