from asyncio.windows_events import NULL
import os
import random
from PIL import Image

#data
id = 'image_'
imgType = '.png'

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
layers = os.listdir('layers')
count = len(layers)

total = 1
TraitCounts = []
traits = []


#Load traits and calculate total possible NFTs
print('### Traits ###')
for i in range(count):
    trait = os.listdir('layers/'+layers[i])
    traits.append(trait)
    
    TraitCount = len(traits)

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

#generate
print('### Generating ###')
print('')
for y in range(nftReq):

    #initial background
    nft = Image.open(f'./layers/'+layers[0]+'/'+traits[0][0]).convert('RGBA')
    nft.putalpha(0)

    for i in range(count):
        img = Image.open(f'./layers/'+layers[i]+'/'+traits[i][combinations[y][i]]).convert('RGBA')
        nft = Image.alpha_composite(nft , img)
        id = 'image_' + "".join(map(str,combinations[y]))

    nftName = id + imgType
    nft.save("NFT/" + nftName)
    print(y+1)

print('')
print('### Done ###')