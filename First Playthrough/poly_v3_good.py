import movement
import static
import actions
import factory
import tools
import farms

#set_world_size(5)
compainion_list = {} # (x, y):companion

def plant_poly():	
	pos = (get_pos_x(), get_pos_y())
	if (compainion_list and (pos in compainion_list)):	
		entity = compainion_list[pos]		
		if (entity == Entities.Carrot):
			till()			
		plant(entity)
	else:
		plant(Entities.Bush)
		companion = get_companion()
		if (not companion[0] in compainion_list):			
			compainion_list[companion[1]] = companion[0]	

			
	
movement.traverse_farm_returns(plant_poly)
movement.traverse_farm(tools.waiting_harvest)
