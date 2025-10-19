#Sunflowers
	
flowers = []
flowers.append(((0,1), 1))
flowers.append(((1,0), 3))
flowers.append(((1,1), 2))

quick_print(flowers)

petal_count = 3
for i in range(len(flowers)):
	quick_print("harvesting: ", petal_count)
	if (flowers[i][1] == petal_count):
		#move and harvest
		quick_print("Moving: ", flowers[i][0])
	petal_count -= 1	
	