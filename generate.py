import os
import pathlib
import random
import json
from PIL import Image

#data
id = 'image_'
imgType = '.png'

# layers = os.listdir('layers')
layers = ['layer1','layer2','layer3','layer4'] #arrange layers bottom to top

#template
print('')
print('=========================================')
print('===== NFT GENERATOR [BY CHAMOD] =========')
print('=========================================')
print('')

os.system ('pause')
print('')


#load layers
print('### loading layers ####')
print('')


count = len(layers)

total = 1
TraitCounts = []
traits = []


#Load traits and calculate total possible NFTs
print('### Traits ###')
for i in range(count):
    trait = os.listdir('layers/'+layers[i])
    traits.append(trait)
    
    TraitCount = len(trait)

    TraitCounts.append(TraitCount-1) #list which contains count of traits in every layer

    total = total*TraitCount
    print(layers[i]+' =',trait)



print('')
print('Total Possible NFTs = ', total)
print('')


# input no of NFTs
while True:
  try:
    nftReq= int(input("Enter the required no of NFTs : "))
    if nftReq <= total :
        break
    else:
        print("Please input integer below than 'Total Possible NFTs'")
        print('')
  except ValueError:
      print("Please input integer below than 'Total Possible NFTs'")  
      print('')
      continue


##### generate NFT #####

#load generated combinations
# jsonContent = open("combinations.json", "r").read() #read JSON
# combinations = json.loads(jsonContent)
# comb_Count = len(combinations)
combinations = []



#get combinations
print('')
print('### Randomizing ###')
print('')
x = 0
while x < nftReq:

    combination = []

    for i in range(count):
        gen = random.randint(0, TraitCounts[i])
        combination.append(gen)

    if combination not in combinations:
        combinations.append(combination)
        x = x + 1
    
# print(combinations)

#save combinations
# with open('combinations.json', 'w') as outfile:
#     json.dump(combinations, outfile , indent=3)

#generate NFT
print('### Generating NFTs###')
print('')

nftIDlist = []
for y in range(nftReq):

    #initial background
    nft = Image.open(f'./layers/'+layers[0]+'/'+traits[0][0]).convert('RGBA')
    nft.putalpha(0)

    for i in range(count):
        img = Image.open(f'./layers/'+layers[i]+'/'+traits[i][combinations[y][i]]).convert('RGBA')
        nft = Image.alpha_composite(nft , img)
        id = 'image_' + "".join(map(str,combinations[y]))

    nftName = id + imgType
    nftIDlist.append(id)
    nft.save("NFT/" + nftName)
    print(y+1)

#generate MetaData
print('')
print('### Generating MetaData###')


for z in range(nftReq):
    MetaData = {}
    MetaData['NFT name/ID'] = nftIDlist[z]
    
    for i in range(count):
        traitName = 'layers/' + layers[i]+'/'+ traits[i][combinations[z][i]]
        MetaData[layers[i]] = pathlib.Path(traitName).stem  

    with open('MetaData/'+nftIDlist[z]+'.json', 'w') as outfile:
        json.dump(MetaData, outfile , indent=4)


print('')
print('### Done ###')