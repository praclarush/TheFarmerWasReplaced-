import movement
import static
import actions
import factory
import tools
import farms

is_running = True

movement.move_to_origin()

clear()

while (is_running):
	for plant in static.PLANTS:
			quick_print("Checking ", plant["name"])					
			farm = farms.create_farm_function(plant)
			farm()	
			
	is_running = False

print("Done Gathering")