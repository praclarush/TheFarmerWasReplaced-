import farm

def is_even(n):
	return n % 2 == 0
	
def get_current_pos():
	return (get_pos_x(), get_pos_y())

def waiting_harvest():
	while (not can_harvest()):
		do_a_flip()
	harvest()

def fertilize_harvest():
	while (not can_harvest()):
		fertilize()
	harvest()

def combine_arrays(arrayA, arrayB):
	for itemB in arrayB:
		arrayA.append(itemB)
	return arrayA	

def sleep(numSec):
	for _ in range(numSec):
		do_a_flip()

def can_afford_crop(entity):
	cost = get_cost(entity)
	for item in cost:
		if (num_items(item) < cost[item]):
			quick_print ("Not enough ", item, " to plant ", entity)
			return False
	return True

def need_item(item, min_count):
	return num_items(item) < min_count

def water_ground():
	water_level = get_water()
	if (water_level < farm.Min_Water_Threshold):
		while (get_water() < farm.Ground_Water_Threshold):
			use_item(Items.Water)	

def fertilize():
	if (num_items(Items.Fertilizer) < farm.Min_Fertilizer_Threshold):
		use_item(Items.Fertilizer)

def plant_crop(crop):
	if (not can_afford_crop(crop)):
		return False
	
	if (farm.Use_Water):
		water_ground()
	plant(crop)
	if (farm.Use_Fertilizer):
		fertilize()
	return True

def world_loop(action):
	while (need_item(farm.Item, farm.Required_Amount)):
		if (not can_afford_crop(farm.Crop)):
			break
			
		if (num_items(Items.Power) < farm.Min_Power_Threshold):
			break

		result = action()		
		if (not result):
			break

