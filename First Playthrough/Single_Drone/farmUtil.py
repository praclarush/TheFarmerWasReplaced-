from movement import *
from tools import need_item, is_even, can_afford_item, generate_maze, waiting_harvest, fertilize
from factory import create_planting_function, create_plant_tree_function, create_messured_planting_function
from sorting import bubble_sort
from static import MIN_POWER_REQ

def create_farm_function(farm):
	if (farm["farm"] == "Hey"):
		return create_basic_farm(farm)
	elif(farm["farm"] == "Bush"):
		return create_basic_farm(farm)
	elif(farm["farm"] == "Tree"):
		return create_tree_farm(farm)
	elif(farm["farm"] == "Pumpkin"):
		return create_pumpkin_farm(farm)
	elif(farm["farm"] == "Carrot"):
		return create_carret_farm(farm)		
	elif(farm["farm"] == "Sunflower"):
		return create_sunflower_farm(farm)
	elif(farm["farm"] == "Cactus"):
		return create_cactus_farm(farm)
	elif(farm["farm"] == "Maze"):
		return create_maze_farm(farm)
	elif(farm["farm"] == "Dino"):
		return create_dino_farm(farm)
	elif(farm["farm"] == "Polyculture"):
		return create_polyculture_farm(farm)
	elif(farm["farm"] == "WeirdSubstance"):
		return create_weird_substance_farm(farm)
	else:
		return None

def create_basic_farm(farm):
	def basic():
		item_needed = need_item(farm["item"], farm["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", farm["name"], " Needed")
		clear() #reset the farm, quicker then retilling grounds
	
		while (item_needed):		
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False
					
			if (farm["item"] != Items.Hay):		
				traverse_farm(create_planting_function(farm))		
			traverse_farm(harvest)	
			
			item_needed = need_item(farm["item"], farm["min"])		
				
		return True		
	return basic
	
def create_weird_substance_farm(farm):
	def substance():
		item_needed = need_item(farm["item"], farm["min"])		

		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")			
			
		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return	False	 	
				
			traverse_farm(create_plant_tree_function(farm, False))
			traverse_farm(harvest)
								
			item_needed = need_item(farm["item"], farm["min"])			
			
		return True
	return substance		
			
def create_tree_farm(farm):
	def wood():
		item_needed = need_item(farm["item"], farm["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", farm["name"], " Needed")
		
		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return	False	 	
			
			traverse_farm(create_plant_tree_function(farm, True))
			traverse_farm(harvest)
			
			item_needed = need_item(farm["item"], farm["min"])
			
		return True
	return wood
	
def create_carret_farm(farm):
	def carret():
		item_needed = need_item(farm["item"], farm["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", farm["name"], " Needed")
			
		while (item_needed):		
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return	False
			
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
				
			traverse_farm(create_planting_function(farm))						
			traverse_farm(harvest)				
				
			item_needed = need_item(farm["item"], farm["min"])		
				
		return True
	return carret

def create_pumpkin_farm(farm):
	def pumpkin():
		item_needed = need_item(farm["item"], farm["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")		
	
		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False
					
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
							
			traverse_farm(create_planting_function(farm))
				
			def check_pumpkin_is_good():
				if ((get_entity_type() == Entities.Dead_Pumpkin) or (not can_harvest())):
					return False
				return True							
	
			def look_for_bad_pumpkins():
				if (not check_pumpkin_is_good()):
					return (get_pos_x(), get_pos_y())
	
			suspect_pumpkins = traverse_farm_returns(look_for_bad_pumpkins)
			while (len(suspect_pumpkins) != 0):				
				cords = suspect_pumpkins.pop()
					
				if (cords == None):
					break
				else:
					move_to_location(cords[0], cords[1])
					if (not check_pumpkin_is_good()):
						if (get_entity_type() == Entities.Dead_Pumpkin):							
							harvest()
							plant(farm["entity"])
							if (farm["fertilize"]):
								fertilize()
							suspect_pumpkins.insert(0, cords)
						else:
							suspect_pumpkins.insert(0, cords)
							pet_the_piggy()
													
			move_to_origin()
			harvest()			
			item_needed = need_item(farm["item"], farm["min"])			
		return True
	return pumpkin

def create_sunflower_farm(farm):
	def sunflower():
		item_needed = need_item(farm["item"], farm["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", farm["name"], " Needed")
		
		sunflower_list = []
		
		while (item_needed):		
			result = traverse_farm_returns(create_messured_planting_function(farm))
			
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False			
			
			sunflower_list = result
			
			for i in (range(15, 6, -1)): #shouldn't this be 6?
				for sunflower in range(len(sunflower_list)):
					if (sunflower_list[sunflower][1] == i):
						location = sunflower_list[sunflower][0]
						move_to_location(location[0], location[1])
						
						while (not can_harvest()):
							do_a_flip()						
						harvest()			
						
			item_needed = need_item(farm["item"], farm["min"])		
			
		return True
	return sunflower

def create_cactus_farm(farm):
	def cactus():
		item_needed = need_item(farm["item"], farm["min"])

		if (not item_needed):
			return True

		quick_print("Item ", farm["name"], " Needed")

		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return	False
				
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False	

			traverse_farm(create_planting_function(farm))
			grid_size = get_grid_size()
			if (bubble_sort(grid_size[0], grid_size[0])):
				harvest()
				
			item_needed = need_item(farm["item"], farm["min"])
			
		return True
	return cactus
	
def create_maze_farm(farm):
	def maze():
		item_needed = need_item(farm["item"], farm["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")
		
		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
				
			if (get_entity_type() != Entities.Hedge):
				grid = get_grid_size()
				generate_maze(grid[0] * grid[1])
				
			for direction in ALL_DIRECTIONS:
				if (explore_path(direction, Entities.Treasure)):
					break					
		
			item_needed = need_item(farm["item"], farm["min"])
		return True
	return maze
	
def create_dino_farm(farm):
	def dinos():
		if (not is_even(farm["worldSize"])):
			print("Invalid World Size, Must be even")			
			return True #returning True here indicates that the 
						#function will not run again, so the program 
						#doesn't get stuck in a loop, trying to run a farm thats invalid
		
		item_needed = need_item(farm["item"], farm["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")
		
		while(item_needed):
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
			
			world_size = get_world_size()
			can_move = True
			
			move_to_origin()

			change_hat(Hats.Dinosaur_Hat)
				
			while can_move:
				for x in range(world_size / 2):
					result = move_to_y_position(world_size - 1)
					if ((not move(East)) or (not result)):
						can_move = False
						break
			
					result = move_to_y_position(1)
					if (not result):
						can_move = False
						break
				
					if (x != world_size / 2 - 1):
						if not move(East):
							can_move = False
							break
			
				if (not can_move):
					break
			
				if (not move_to_y_position(0)):
					can_move = False
			
				if (not move_to_x_position(0)):
					can_move = false
			change_hat(Hats.Brown_Hat)
			item_needed = need_item(farm["item"], farm["min"])
			return True
	return dinos
	
def create_polyculture_farm(farm):
	def poly():
		item_needed = need_item(farm["item"], farm["min"])
	
		if (not item_needed):
			return True

		quick_print("Item ", farm["name"], " Needed")
		clear() #reset the farm, quicker then retilling grounds

		compainion_list = {} # (x, y):companion
		def plant_poly():
			pos = (get_pos_x(), get_pos_y())
			if (compainion_list and (pos in compainion_list)):	
				entity = compainion_list[pos]		
				if (entity == Entities.Carrot):
					till()			
				plant(entity)
			else:
				plant(farm["entity"])
				companion = get_companion()
				if (not companion[0] in compainion_list):			
					compainion_list[companion[1]] = companion[0]	

		while (item_needed):		
			if (farm["power"] and num_items(Items.Power) < MIN_POWER_REQ):
				print("Out of Power")
				return False

			traverse_farm(plant_poly)
			traverse_farm(waiting_harvest)
			compainion_list = {} #clear list for next run			
			item_needed = need_item(farm["item"], farm["min"])
		return True	
	return poly

