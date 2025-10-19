import helpers
import factory

def water_ground():
	water_level = get_water()
	if (water_level < 0.7):
		while (get_water() < 0.7):
			quick_print("Water Needed: ", water_level)
			use_item(Items.Water)		
			
def move_to_origin():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def traverse_farm(cell_function):
	move_to_origin()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			cell_function()
			move(North)
		move(East)
	return True	
	
def set_soil():
	set_ground_type(Grounds.Soil)
	
def waiting_harvest():
	while not can_harvest():
		do_a_flip()
	harvest()
	
def get_item_if_needed_special(item, min_item_count, planting_function):
	item_needed = helpers.need_item(item, min_item_count)
		
	if (not item_needed):
		return False	
	
	quick_print("Need Item ", item)
	
	entity_to_plant = helpers.get_entity_from_item(item)
		
	while (item_needed):		
		if (not helpers.can_afford_cost(entity_to_plant)):
			quick_print("Can't Afford Seeds: ", entity_to_plant)
			return False
	
		if (item != Items.Hay and get_ground_type() != Grounds.Soil):
			traverse_farm(factory.create_tilling_function(Grounds.Soil))
		
		traverse_farm(planting_function)
		harvest()		
		item_needed = helpers.need_item(item, min_item_count)
		
	return True	
	
def get_item_if_needed(item, min_item_count):	
	item_needed = helpers.need_item(item, min_item_count)
		
	if (not item_needed):
		return False	
	
	quick_print("Need Item ", item)
	
	entity_to_plant = helpers.get_entity_from_item(item)
	
	if (not helpers.can_afford_cost(entity_to_plant)):
		quick_print("Can't Afford Seeds: ", entity_to_plant)
		return False
	
		
	while (item_needed):		
		if (not helpers.can_afford_cost(entity_to_plant)):
			return False
	
		if (item != Items.Hay and get_ground_type() != Grounds.Soil):
			traverse_farm(factory.create_tilling_function(Grounds.Soil))
		
		#traverse_farm(factory.create_water_function())		
		if entity_to_plant != Entities.Grass:
			if (num_items(Items.Water) > 5000):
				traverse_farm(factory.create_planting_function(entity_to_plant, True))			
			else:
				traverse_farm(factory.create_planting_function(entity_to_plant, False))				
				
		traverse_farm(waiting_harvest)		
		item_needed = helpers.need_item(item, min_item_count)
	return True