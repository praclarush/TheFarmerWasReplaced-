import farm
from movement import explore_path, ALL_DIRECTIONS
from utilities import world_loop

def generate_maze():
	weird_substance = get_world_size() * 2 **num_unlocked(Unlocks.Mazes)

	if (num_items(Items.Weird_Substance) < weird_substance):
		quick_print("unable to generate maze")
		return False

	plant(Entities.Bush)
	return use_item(Items.Weird_Substance, weird_substance)

def goldFarm():
	def action():
		if (not generate_maze()):
			return False
		
		for direction in ALL_DIRECTIONS:
			if (explore_path(direction, Entities.Treasure)):
				break #found treasure so break for loop to restart maze

		return True
	
	world_loop(action)
	

if (__name__ == "__main__"):
	farm_config = farm.get_config_by_name("MazeFarm")
	farm_config["min"] = num_items(Items.Gold) + 1
	farm.init(farm_config)
	set_world_size(farm.World_Size)
	goldFarm()