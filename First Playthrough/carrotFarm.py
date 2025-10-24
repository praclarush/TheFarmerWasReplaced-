import farm

from movement import move_to_origin, harvest_column
from utilities import sleep, plant_crop, world_loop
from DroneUtil import create_drone

def plant_column():
	for _ in range(get_world_size()):
		if (get_ground_type() == Grounds.Grassland):
			till()

		plant_crop(Entities.Carrot)		
		move(North)

def carrotFarm():	
	move_to_origin()	

	def action():
		for _ in range(get_world_size()):
			create_drone(plant_column)			
			move(East)		
		
		for _ in range(get_world_size()):
			create_drone(harvest_column)			
			move(East)
		
		return True

	world_loop(action)

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("CarrotFarm")
	farm_config["min"] = num_items(Items.Carrot) + 1
	farm.init(farm_config)
	set_world_size(farm.World_Size)
	carrotFarm()
