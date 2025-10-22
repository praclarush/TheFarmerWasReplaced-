def navigateMaze(action = harvest, moveDirection = None, cache = {}):
	isFound = False
	if get_entity_type() == Entities.Treasure:
		action()
		return True
	
	while get_entity_type() != Entities.Hedge:
		size = get_world_size() * get_world_size()
		plant(Entities.Bush)
		substance = size * num_unlocked(Unlocks.Mazes)
		use_item(Items.Weird_Substance, substance)

	
	x = get_pos_x()
	y = get_pos_y()
	
	directions = {
		North: {
			"target": (x, y+1),
			"opposite": South
		},
		South: {
			"target": (x, y-1),
			"opposite": North
		},
		East: {
			"target": (x+1, y),
			"opposite": West
		},
		West: {
			"target": (x-1, y),
			"opposite": East
		},
	}
	
	for key in directions:
		if moveDirection != directions[key]["opposite"] and not directions[key]["target"] in cache:
			if move(key):
				cache[directions[key]["target"]] = True
				isFound = navigateMaze(action, key, cache)
				if not isFound:
					move(directions[key]["opposite"])
	return isFound

def harvest_final_maze():
	size = get_world_size() * get_world_size()
	substance = size * num_unlocked(Unlocks.Mazes)
	res = use_item(Items.Weird_Substance,)	
	if (not res):
		harvest()
	
#clear()
while True:
	navigateMaze(harvest_final_maze)
	