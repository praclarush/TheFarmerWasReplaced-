
flowers = []
flowers.append(((0,1), 10))
flowers.append(((1,0), 15))
flowers.append(((1,1), 7))
flowers.append(((1,1), 7))

for petals_counter in range(15, 6, -1):
	for sunflower in range(len(flowers)):
		if flowers[sunflower][1] == petals_counter:
			quick_print(flowers[sunflower])