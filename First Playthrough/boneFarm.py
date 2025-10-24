import farm
from movement import move_to_origin, move_to_x_position, move_to_y_position
from utilities import world_loop, is_even

def boneFarm():
	move_to_origin()	

	def action():		
		if (not is_even(farm.World_Size)):
			quick_print("World Size must be even")
			return False

		world_size = get_world_size()

		change_hat(Hats.Dinosaur_Hat)
		can_move = True
		half_world_size = world_size / 2
		while (can_move):
			for x in range(half_world_size):
				result = move_to_y_position(world_size - 1)
				if ((not move(East)) or (not result)):
					can_move = False
					break

				result = move_to_y_position(1)
				if (not result):
					can_move = False
					break

				if (x != half_world_size - 1):
					if (not move(East)):
						can_move = False
						break
			
			if (not can_move):
				break

			if (not move_to_y_position(0)):
				can_move = False
			
			if (not move_to_x_position(0)):
				can_move = False
		change_hat(farm.Current_Hat)
		return True
	
	world_loop(action)
	

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("DinoFarm")
	farm_config["min"] = num_items(Items.Bone) + 1
	farm.init(farm_config)
	set_world_size(farm.World_Size)
	boneFarm()

