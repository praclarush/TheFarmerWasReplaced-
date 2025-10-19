import movement
import static
import actions
import factory
import tools
import farms

is_running = True
check_loop = False
movement.move_to_origin()

clear()

while (is_running or check_loop):	
	all_good = list()
	if (check_loop):
		check_loop = False
	else:
		check_loop = True
		
	for plant in static.PLANTS:
			quick_print("Checking ", plant["name"])					
			farm = farms.create_farm_function(plant)
			if (plant["enabled"]):
				result = farm()	
				all_good.append(result)

	is_running = (False in all_good)
	
print("Done Gathering")