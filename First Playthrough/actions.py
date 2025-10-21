from tools import waiting_harvest, can_afford_item, need_item, get_entity_from_item
from factory import create_tilling_function, create_planting_function
from movement import traverse_farm

def get_item_if_needed(plant):
	item_needed = need_item(plant["item"], plant["min"])
	
	if (not item_needed):
		return false
		
	quick_print("Item ", plant["name"], " Needed")
	
	while (item_needed):
		if (not can_afford_cost(plant["entity"])):
			return False
		
		if(plant["ground"] != get_ground_type()):
			traverse_farm(create_tilling_function(plant["ground"]))
		
		traverse_farm(create_planting_function(plant["entity"], plant["water"]))
		traverse_farm(waiting_harvest)	
		return True

	
def get_item_if_needed_special(item, min_item_count, planting_function):
	item_needed = need_item(item, min_item_count)
		
	if (not item_needed):
		return False	
	
	quick_print("Need Item ", item)
	
	entity_to_plant = get_entity_from_item(item)
		
	while (item_needed):		
		if (not can_afford_cost(entity_to_plant)):
			quick_print("Can't Afford Seeds: ", entity_to_plant)
			return False
	
		if (item != Items.Hay and get_ground_type() != Grounds.Soil):
			traverse_farm(create_tilling_function(Grounds.Soil))
		
		traverse_farm(planting_function)
		harvest()		
		item_needed = need_item(item, min_item_count)
		
	return True