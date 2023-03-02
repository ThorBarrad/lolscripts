import json
import urllib.request
import time
import os

with open("item.json") as fp:
    data = json.load(fp)
fp.close()

data = data["data"]

stopword = [
    '''<rarityLegendary>Fire at Will</rarityLegendary><br>
    <subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>''',
    '''<rarityLegendary>Death's Daughter</rarityLegendary><br>
    <subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>''',
    '''<rarityLegendary>Raise Morale</rarityLegendary><br>
    <subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>''']

for value in data.values():

    if value["name"] in stopword:
        continue

    elif not value["maps"]["12"]:
        continue

    elif not value["gold"]["purchasable"]:
        continue

    else:
        print(value["name"])

        request = urllib.request.urlopen(
            "http://ddragon.leagueoflegends.com/cdn/13.3.1/img/item/" + value["image"]["full"])

        filename = "./Images/items/" + value["name"] + ".png"
        with open(filename, 'wb') as file:
            file.write(request.read())
        file.close()
