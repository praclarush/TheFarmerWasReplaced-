import movement
import tools
import factory
import sorting
import static

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
	else:
		return None

def create_basic_farm(plant):
	def basic():
		item_needed = tools.need_item(plant["item"], plant["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
		clear() #reset the farm, quicker then retilling grounds
	
		while (item_needed):		
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
			movement.traverse_farm(harvest)	
			
			item_needed = tools.need_item(plant["item"], plant["min"])		
				
		return True		
	return basic
	
def create_bush_farm(plant):
	def wood():
		item_needed = tools.need_item(plant["item"], plant["min"])
			
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
	
		while (item_needed):				
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
			movement.traverse_farm(factory.create_planting_function(plant["entity"], plant["water"]))				
			movement.traverse_farm(harvest)	
			
			item_needed = tools.need_item(plant["item"], plant["min"])
			
		return True
	return wood

def create_tree_farm(plant):
	def wood():
		item_needed = tools.need_item(plant["item"], plant["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
		
		while (item_needed):
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return	False	 	
			
			movement.traverse_farm(factory.create_plant_tree_function())
			movement.traverse_farm(harvest)
			
			item_needed = tools.need_item(plant["item"], plant["min"])
			
		return True
	return wood
	
def create_carret_farm(plant):
	def carret():
		item_needed = tools.need_item(plant["item"], plant["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
			
		while (item_needed):		
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return	False
			
			if (not tools.can_afford_item(plant["entity"])):
				print("Cannot afford: ", plant["entity"])
				return False
				
			movement.traverse_farm(factory.create_planting_function(plant))						
			movement.traverse_farm(harvest)				
				
			item_needed = tools.need_item(plant["item"], plant["min"])		
				
		return True
	return carret

def create_pumpkin_farm(farm):
	def pumpkin():
		item_needed = tools.need_item(farm["item"], farm["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")		
	
		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
					
			if (not tools.can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
							
			movement.traverse_farm(factory.create_planting_function(farm))
				
			def check_pumpkin_is_good():
				if ((get_entity_type() == Entities.Dead_Pumpkin) or (not can_harvest())):
					return False
				return True							
	
			def look_for_bad_pumpkins():
				if (not check_pumpkin_is_good()):
					return (get_pos_x(), get_pos_y())
	
			suspect_pumpkins = movement.traverse_farm_returns(look_for_bad_pumpkins)
			while (len(suspect_pumpkins) != 0):				
				cords = suspect_pumpkins.pop()
					
				if (cords == None):
					break
				else:
					movement.move_to_location(cords[0], cords[1])
					if (not check_pumpkin_is_good()):
						if (get_entity_type() == Entities.Dead_Pumpkin):							
							harvest()
							plant(farm["entity"])
							if (farm["fertilize"]):
								use_item(Items.Fertilizer)	
							suspect_pumpkins.insert(0, cords)
						else:
							suspect_pumpkins.insert(0, cords)
							pet_the_piggy()
													
			movement.move_to_origin()
			harvest()			
			item_needed = tools.need_item(farm["item"], farm["min"])			
		return True
	return pumpkin

def create_sunflower_farm(plant):
	def sunflower():
		item_needed = tools.need_item(plant["item"], plant["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
		
		sunflower_list = []
		
		while (item_needed):		
			result = movement.traverse_farm_returns(factory.create_messured_planting_function(plant))
			
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not tools.can_afford_item(plant["entity"])):
				print("Cannot afford: ", plant["entity"])
				return False			
			
			sunflower_list = result
			
			for i in (range(15, 6, -1)): #shouldn't this be 6?
				for sunflower in range(len(sunflower_list)):
					if (sunflower_list[sunflower][1] == i):
						location = sunflower_list[sunflower][0]
						movement.move_to_location(location[0], location[1])
						
						while (not can_harvest()):
							do_a_flip()						
						harvest()			
						
			item_needed = tools.need_item(plant["item"], plant["min"])		
			
		return True
	return sunflower

def create_cactus_farm(plant):
	def cactus():
		item_needed = tools.need_item(plant["item"], plant["min"])

		if (not item_needed):
			return True

		quick_print("Item ", plant["name"], " Needed")

		while (item_needed):
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return	False
				
			if (not tools.can_afford_item(plant["entity"])):
				print("Cannot afford: ", plant["entity"])
				return False	

			movement.traverse_farm(factory.create_planting_function(plant))
			grid_size = movement.get_grid_size()
			if (sorting.bubble_sort(grid_size[0], grid_size[0])):
				harvest()
				
			item_needed = tools.need_item(plant["item"], plant["min"])
			
		return True
	return cactus
	
def create_maze_farm(plant):
	def maze():
		item_needed = tools.need_item(plant["item"], plant["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", plant["name"], " Needed")
		
		while (item_needed):
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not tools.can_afford_item(plant["entity"])):
				print("Cannot afford: ", plant["entity"])
				return False
				
			if (get_entity_type() != Entities.Hedge):
				grid = movement.get_grid_size()
				tools.generate_maze(grid[0] * grid[1])
				
			for direction in static.ALL_DIRECTIONS:
				if (movement.explore_path(direction, Entities.Treasure)):
					break					
		
			item_needed = tools.need_item(plant["item"], plant["min"])
		return True
	return maze
	
def create_dino_farm(plant):
	def dinos():
		item_needed = tools.need_item(plant["item"], plant["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", plant["name"], " Needed")
		
		while(item_needed):
			if (plant["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not tools.can_afford_item(plant["entity"])):
				print("Cannot afford: ", plant["entity"])
				return False
			
			world_size = get_world_size()
			can_move = True
			
			movement.move_to_origin()

			change_hat(Hats.Dinosaur_Hat)
				
			while can_move:
				for x in range(world_size / 2):
					result = movement.move_to_y_position(world_size - 1)
					if ((not move(East)) or (not result)):
						can_move = False
						break
			
					result = movement.move_to_y_position(1)
					if (not result):
						can_move = False
						break
				
					if (x != world_size / 2 - 1):
						if not move(East):
							can_move = False
							break
			
				if (not can_move):
					break
			
				if (not movement.move_to_y_position(0)):
					can_move = false
			
				if (not movement.move_to_x_position(0)):
					can_move = false
			change_hat(Hats.Brown_Hat)
			item_needed = tools.need_item(plant["item"], plant["min"])
			return True
	return dinos
	
def create_polyculture_farm(farm):
	def poly():
		item_needed = tools.need_item(farm["item"], farm["min"])
	
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
			if (farm["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False

			movement.traverse_farm(plant_poly)
			movement.traverse_farm(tools.waiting_harvest)
			compainion_list = {} #clear list for next run			
			item_needed = tools.need_item(farm["item"], farm["min"])
		return True	
	return poly

