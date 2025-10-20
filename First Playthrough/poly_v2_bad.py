import movement
import static
import actions
import factory
import tools
import farms

set_world_size(5)
world_size = get_world_size() * get_world_size()
count = 0

planted_list = {} # (x, y):companion

def plant_poly2():
	pos = (get_pos_x(), get_pos_y())
	if (planted_list and (pos in planted_list)):	
		entity = planted_list[pos]		
		if (entity == Entities.Carrot):
			till()			
		plant(entity)
	else:
		companion_result = get_companion()
		if (not companion_result[0] in planted_list):			
			planted_list[companion_result[1]] = companion_result[0]	
			

			
	
while (len(planted_list) != world_size):
	movement.traverse_farm_returns(plant_poly)
	count += 1
	quick_print("Pass: ", count)
	
movement.traverse_farm(harvest)
