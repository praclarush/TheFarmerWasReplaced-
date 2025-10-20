import movement
import static
import actions
import factory
import tools
import farmUtil

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
		
	for farm in static.Farms:
			quick_print("Checking ", farm["name"])						
			if (farm["enabled"]):
				config_world_size = farm["worldSize"]
				if ((farm["item"] == Items.Bone) and (not tools.is_even(config_world_size))):
					print("Invalid World Size, Must be even - Skipping")
				else:			
					set_world_size(config_world_size)			
					farmFunc = farmUtil.create_farm_function(farm)
					
					if (farm == None):
						quick_print("Invalid Farm:", farm["farm"])
					
					result = farmFunc()	
					all_good.append(result)
					movement.move_to_origin()
					quick_print("Farm Run Finished")
	is_running = (False in all_good)	
	
print("Done Gathering")