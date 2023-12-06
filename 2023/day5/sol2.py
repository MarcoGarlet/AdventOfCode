from functools import reduce
def solve(seeds, maps):

	#print(seeds)
	di=0
	for levelMaps in maps:
		#print(f"new level ${levelMaps}")
		newSeed = []

		while (len(seeds)>0):
			#print(f"seeds = {seeds}")
			seed = seeds.pop()
			#print(f"seed poppato = ${seed}")
			srcSeed=seed[0]
			dstSeed=seed[1]
			iGame = 0
			for gameMap in levelMaps:

				#print(f"####new gameMap ${gameMap}####")
				srcMap = gameMap['src'][0]
				dstMap = gameMap['src'][1]
				srcDst = gameMap['dst'][0]
				dstDst = gameMap['dst'][1]


				if(dstSeed<srcMap or dstMap<srcSeed):
					#print(f"{seed} si rimappa su se stesso")
					if iGame==len(levelMaps)-1:
						newSeed+=[seed]
					

					

				else:
					#print(f"{seed} si rimappa in {gameMap}")
					if(srcSeed<srcMap):
						#print("nel primo if")
						
						if iGame==len(levelMaps)-1:
							newSeed+=[[srcSeed,srcMap-1]]

						else:
							seeds.append([srcSeed,srcMap-1])

						if(dstSeed<=dstMap): # dstMap>=dstSeed la destinazione di map contiene seed e la sorgente di seed è fuori da map(gestita su) srcSeed<srcMap
							#print("nel secondo if")
							newSeed+=[[srcDst,dstDst-(dstMap-dstSeed)]]
						else: # dstSeed>dstMap srcSeed<srcMap
							#print("nel secondo else") # la destinazione di map è fuori da seed
							newSeed+=[[srcDst,dstDst]]
							if iGame==len(levelMaps)-1:
								newSeed+=[[dstMap+1,dstSeed]]
							else:
								seeds.append([dstMap+1,dstSeed])	
						
						break

					else:
						#print("nel terzo else")
						if(dstMap>=dstSeed):
							#print("nel terzo if")
							newSeed+=[[srcDst+(srcSeed-srcMap),dstDst+(dstSeed-dstMap)]]
							break
						else:
							#print("nel quarto elf")
							newSeed+=[[srcDst+(srcSeed-srcMap), dstDst]]
							if iGame==len(levelMaps)-1:
								newSeed+=[[dstMap+1,dstSeed]]
								
							else:

								seeds.append([dstMap+1,dstSeed])
								#print(f"nuovo seed ({dstMap+1},{dstSeed}), seeds = {seeds}, newSeed = {newSeed}")
							break
								

				iGame+=1
					
			#print(f"new seed = {newSeed}")
		seeds = newSeed.copy()
		#print(f"newSeed = {newSeed}")
		#print(f"=> seeds = {seeds}")
		


	
		

	print(min(reduce(lambda x,y: x+y,seeds)))
			




def getSeedIntervals(seeds):
	return [ [seeds[i],seeds[i]+seeds[i+1]-1]for i in range(0,len(seeds),2)]

def getMaps(inputMaps):
	return [[[int(x) for x in el.split(' ')] for el in inputList] for inputList in inputMaps]

def convertMaps(inputMaps):
	return [[{'src':[mapFunc[1],mapFunc[1]+mapFunc[2]-1],'dst':[mapFunc[0],mapFunc[0]+mapFunc[2]-1]} for mapFunc in gameMap] for gameMap in inputMaps]


if __name__ == '__main__':
	with open('inp.txt','r') as f:
		data =''.join(f.readlines()).split('\n\n')
	seeds = [int(el) for el in data[0].split(':')[1].strip().split(' ')]
	data = [l.split(':')[1].strip().split('\n') for l in data[1:]]
	seeds = getSeedIntervals(seeds)
	maps = convertMaps(getMaps(data))
	#print(maps)
	solve(seeds, maps)
