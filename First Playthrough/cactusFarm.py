import farm
from utilities import plant_crop, world_loop
from movement import move_to_origin
from factory import build_func1
from sorting import sort_direction
from DroneUtil import create_drone, wait_for_drones

def plant_column():
	for _ in range(get_world_size()):
		if (get_ground_type() == Grounds.Grassland):
			till()
		
		plant_crop(Entities.Cactus)
		move(North)

def cactusFarm():	
	move_to_origin()	

	def action():
		directions = [North, East]
		#plant
		drones = []
		for _ in range(get_world_size()):
			drones.append(create_drone(plant_column))			
			move(East)		

		wait_for_drones(drones)

		#sort
		for direction in directions:
			drones = []
			func = build_func1(sort_direction, direction)			
				
			move_direction = None
			if (direction == North):
				move_direction = East
			else:
				move_direction = North

			for _ in range(get_world_size()):
				drones.append(create_drone(func))				
				move(move_direction)

			wait_for_drones(drones)		
		harvest()
		return True
	
	world_loop(action)
		

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("CactusFarm")
	farm_config["min"] = num_items(Items.Cactus) + 1
	farm.init(farm_config)	
	set_world_size(farm.World_Size)
	cactusFarm()