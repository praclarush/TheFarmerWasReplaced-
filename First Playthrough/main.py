import movement
import static
import actions
import factory
import tools
import farms

clear()
is_running = True
check_loop = False
movement.move_to_origin()
while (is_running or check_loop):	
	all_good = list()
	if (check_loop):
		check_loop = False
	else:
		check_loop = True
		
	for plant in static.PLANTS:
			quick_print("Checking ", plant["name"])						
			if (plant["enabled"]):
				config_world_size = plant["worldSize"]
				if ((plant["item"] == Items.Bone) and (not tools.is_even(config_world_size))):
					print("Invalid World Size, Must be even - Skipping")
				else:			
					set_world_size(config_world_size)			
					farm = farms.create_farm_function(plant)
					result = farm()	
					all_good.append(result)
					movement.move_to_origin()
					quick_print("Farm Run Finished")
	is_running = (False in all_good)	
	
print("Done Gathering")