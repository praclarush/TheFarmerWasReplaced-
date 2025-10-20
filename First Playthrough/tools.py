def generate_maze(size):	
	plant(Entities.Bush)
	substance = size * num_unlocked(Unlocks.Mazes)
	use_item(Items.Weird_Substance, substance)

def is_even(n):
	return n % 2 == 0
	
def get_current_pos():
	return (get_pos_x(), get_pos_y())

def water_ground():
	water_level = get_water()
	if (water_level < 0.25):
		while (get_water() < 0.75):
			use_item(Items.Water)	

def get_entity_from_item(item = Items.Hay):
	if (item == Items.Hay):
		return Entities.Grass
	elif(item == Items.Wood):
		return Entities.Bush
	elif(item == Items.Carrot):
		return Entities.Carrot
	elif(item == Items.Pumpkin):
		return Entities.Pumpkin
	else:
		return None
			
def need_item(item, min_count):
	return num_items(item) < min_count
	

def can_afford_item(entity):
	cost = get_cost(entity)
	for item in cost:
		if (num_items(item) < cost[item]):
			quick_print ("Not enough ", item, " to plant ", entity)
			return False
	return True
	
def waiting_harvest():
	while not can_harvest():
		do_a_flip()
	harvest()