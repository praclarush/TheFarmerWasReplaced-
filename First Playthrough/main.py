import farm
from hayFarm import hayFarm
from treeFarm import treeFarm
from sunflowerFarm import sunflowerFarm
from pumpkinFarm import pumpkinFarm
from carrotFarm import carrotFarm
from cactusFarm import cactusFarm
from goldFarm import goldFarm
from boneFarm import boneFarm

def get_farm_function():	
	if (farm.farm == "Hey"):
		return hayFarm
	elif (farm.farm == "Tree"):
		return treeFarm
	elif (farm.farm == "Sunflower"):
		return sunflowerFarm
	elif (farm.farm == "Carrot"):
		return carrotFarm
	elif (farm.farm == "Pumpkin"):		
		return pumpkinFarm
	elif (farm.farm == "Cactus"):
		return cactusFarm
	elif (farm.farm == "Maze"):
		return goldFarm
	elif (farm.farm == "Dino"):
		return boneFarm
	else:
		return None		

def main():
	while (True):
		for plant in farm.Plant_Configs:			
			farm.init(plant)			
			
			if (not farm.Is_Enabled):
				continue

			change_hat(farm.Current_Hat)
			set_world_size(farm.World_Size)	

			farmFunction = get_farm_function()			
			farmFunction()

if (__name__ == "__main__"):
	main()
