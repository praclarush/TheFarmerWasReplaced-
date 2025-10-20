import movement
import static
import actions
import factory
import tools
import farms

set_world_size(5)

companion_list = [] # (x, y):companion
planted_list = {} # (x, y):companion

def plant_poly1():
	entity_type = get_entity_type()
	if (companion_list):				
		companion = companion_list.pop()
		movement.move_to_location(companion[1][0], companion[1][1])
		if (companion == Entities.Carrot):
			Till()

		if (not planted_list and (not companion in planted_list)):
			plant(companion[0])			
			planted_list[companion[0]] = companion[1]
	else:
		world_size = get_world_size() * get_world_size()
		
		if (len(planted_list) == world_size):
			return False
		else:
			companion_result = get_companion()
			companion_list.append(companion_result)	
			
	if (not plant_poly()):
		return

plant_poly()		
#movement.traverse_farm_returns(plant_poly)
movement.traverse_farm(harvest)