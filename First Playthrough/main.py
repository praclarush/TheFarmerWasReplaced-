from movement import move_to_origin
from static import Farms
from farmUtil import create_farm_function

def main():	
	is_running = True
	check_loop = False
	
	clear()
	move_to_origin()
	
	while (is_running or check_loop):	
		all_good = list()
		if (check_loop):
			check_loop = False
		else:
			check_loop = True
			
		for farm in Farms:
			quick_print("Checking ", farm["name"])						
			if (farm["enabled"]):
				config_world_size = farm["worldSize"]
				set_world_size(config_world_size)			
				farmFunc = create_farm_function(farm)
						
				if (farm == None):
					quick_print("Invalid Farm:", farm["farm"])
			
				result = farmFunc()	
				all_good.append(result)
				move_to_origin()
				quick_print("Farm Run Finished")
		is_running = (False in all_good)	
		
	print("Done Gathering")
	
if (__name__ == "__main__"):
	main()