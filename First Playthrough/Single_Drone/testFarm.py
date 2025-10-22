import farmUtil
import movement
import static
import tools
import factory

def test_single_farm(farmName):
	clear()
	farm = static.get_farm_by_name(farmName)

	quick_print("Testing ", farm["name"])
	#farm["min"] = num_items(farm["item"]) + 1
	farm["min"] = 512000
	#config_world_size = farm["worldSize"]
	config_world_size = 12
	set_world_size(config_world_size)

	farmFunction = farmUtil.create_farm_function(farm)
	farmFunction()
	movement.move_to_origin()

def test_all_farms():
	clear()

	for farm in static.Farms:
		quick_print("Testing ", farm["name"])
		farm["min"] = num_items(farm["item"]) + 1

		config_world_size = 6
		set_world_size(config_world_size)

		farmFunction = farmUtil.create_farm_function(farm)
		farmFunction()
		movement.move_to_origin()

test_single_farm("MazeFarm")
#test_all_farms()