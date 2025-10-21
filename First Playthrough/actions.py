import tools
import factory
import movement

def get_item_if_needed(plant):
	item_needed = tools.need_item(plant["item"], plant["min"])
	
	if (not item_needed):
		return false
		
	quick_print("Item ", plant["name"], " Needed")
	
	while (item_needed):
		if (not tools.can_afford_cost(plant["entity"])):
			return False
		
		if(plant["ground"] != get_ground_type()):
			movement.traverse_farm(factory.create_tilling_function(plant["ground"]))
		
		movement.traverse_farm(factory.create_planting_function(plant["entity"], plant["water"]))
		movement.traverse_farm(tools.waiting_harvest)	
		return True

	
def get_item_if_needed_special(item, min_item_count, planting_function):
	item_needed = tools.need_item(item, min_item_count)
		
	if (not item_needed):
		return False	
	
	quick_print("Need Item ", item)
	
	entity_to_plant = tools.get_entity_from_item(item)
		
	while (item_needed):		
		if (not tools.can_afford_cost(entity_to_plant)):
			quick_print("Can't Afford Seeds: ", entity_to_plant)
			return False
	
		if (item != Items.Hay and get_ground_type() != Grounds.Soil):
			movement.traverse_farm(factory.create_tilling_function(Grounds.Soil))
		
		movement.traverse_farm(planting_function)
		harvest()		
		item_needed = tools.need_item(item, min_item_count)
		
	return True