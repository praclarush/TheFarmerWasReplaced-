import farm
from movement import move_to_origin
from utilities import fertilize_harvest, plant_crop, world_loop
from factory import build_func1
from DroneUtil import wait_for_drones, create_drone


def plant_column():
	for _ in range(get_world_size()):
		if (get_ground_type() != Grounds.Soil):
			till()
		
		plant_crop(Entities.Sunflower)		
		move(North)

def harvest_sunflowers(petalCount):
	for _ in range(get_world_size()):
		if (measure() == petalCount):			
			fertilize_harvest()
		move(North)

def sunflowerFarm():
	move_to_origin()	

	def action():
		drones = []
		for _ in range(get_world_size()):
			drones.append(create_drone(plant_column))
			move(East)		
			
		wait_for_drones(drones)

		drones = []
		for petalCount in range(15, 6, -1):
			for _ in range(get_world_size()):
				func = build_func1(harvest_sunflowers, petalCount)
				drones.append(create_drone(func))
				move(East)		
			wait_for_drones(drones)
		return True
		
	
	world_loop(action)

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("SunflowerFarm")
	farm_config["min"] = num_items(Items.Power) + 1
	farm.init(farm_config)
	set_world_size(farm.World_Size)
	sunflowerFarm()