import farm
from movement import move_to_origin
from utilities import can_afford_crop, fertilize, world_loop, plant_crop, waiting_harvest
from factory import build_func1
from DroneUtil import wait_for_drones, create_drone


def check_pumpkin():
	left_id = measure()
	move(West)
	right_id = measure()
	move(East)
	return left_id == right_id

def plant_pumpkin():
	if (can_afford_crop(Entities.Pumpkin)):
		plant_crop(Entities.Pumpkin)
		return True
	return False

def plant_column(first_pass):	
	for _ in range(get_world_size()):
		if (get_entity_type() != Entities.Pumpkin):
			if (get_ground_type() != Grounds.Soil):
				till()

			if (not plant_pumpkin()):
				return
				
			if (not first_pass):
				while (not can_harvest()):
					if (get_entity_type() == Entities.Dead_Pumpkin):
						if (not plant_pumpkin()):
							return
						fertilize()
		move(North)

def plant_pumpkins(first_pass):	
	drones = []
	
	plant_Func = build_func1(plant_column, first_pass)
	for _ in range(get_world_size()):
		drones.append(create_drone(plant_Func))				
		move(East)
	
	wait_for_drones(drones)

def pumpkinFarm():    	
	move_to_origin()
	
	def action():
		first_pass = True
		plant_pumpkins(first_pass)
		first_pass = False
		if (check_pumpkin()):
			waiting_harvest() #some how, pumpkin at 0,0 was dead, and this should we don't hit here
			first_pass = True	
		return True
	
	world_loop(action)
			
if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("PumpkinFarm")
	farm_config["min"] = num_items(Items.Pumpkin) + 1
	farm.init(farm_config)
	pumpkinFarm()
	set_world_size(farm.World_Size)