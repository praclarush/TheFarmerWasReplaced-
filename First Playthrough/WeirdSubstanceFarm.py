import farm

from movement import move_to_origin, harvest_column
from utilities import is_even, sleep, world_loop, plant_crop
from factory import build_func1
from DroneUtil import create_drone

def plant_column(entity):
	for y in range(get_world_size()):
		if (not is_even(get_pos_x()) and (is_even(get_pos_y()))):
			plant_crop(entity)
			use_item(Items.Weird_Substance)		
		elif (is_even(get_pos_x()) and (not is_even(get_pos_y()))):
			plant_crop(entity)
			use_item(Items.Weird_Substance)			
		move(North)

def treeFarm():		
	move_to_origin()

	def action():
		drone_function = build_func1(plant_column, Entities.Tree)
		for _ in range(get_world_size()):
			create_drone(drone_function)			
			move(East)

		for _ in range(get_world_size()):
			create_drone(harvest_column)			
			move(East)
			
		return True
	world_loop(action)

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("WeirdSubstanceFarm")
	farm_config["min"] = num_items(Items.Weird_Substance) + 1
	farm.init(farm_config)
	set_world_size(farm.World_Size)
	treeFarm()
	