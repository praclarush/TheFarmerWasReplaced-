import movement
import tools
import factory
import sorting
import static


def create_farm_function(plant):
	if (plant["item"] == Items.Hay):
		return create_hey_farm(plant)
	elif(plant["item"] == Items.Wood):
		return create_tree_farm(plant)
	elif(plant["item"] == Items.Pumpkin):
		return create_pumpkin_farm(plant)
	elif(plant["item"] == Items.Carrot):
		return create_carret_farm(plant)		
	elif(plant["item"] == Items.Power):
		return create_sunflower_farm(plant)
	elif(plant["item"] == Items.Cactus):
		return create_cactus_farm(plant)
	elif(plant["item"] == Items.Gold):
		return create_maze_farm(plant)
	elif(plant["item"] == Items.Bone):
		return create_dino_farm(plant)
	

def create_hey_farm(plant):
	def hey():
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
	return hey
	
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

def create_pumpkin_farm(plant):
	def pumpkin():
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
						
			movement.traverse_farm(factory.create_planting_function(plant))
			bad_pumpkin_list = movement.traverse_farm_returns(factory.create_replanting_function(plant))
			
			while (len(bad_pumpkin_list) != 0):
				cords = bad_pumpkin_list.pop()
				replantFunc = factory.create_replanting_function(plant)					
				if(cords != None):
					movement.move_to_location(cords[0], cords[1])					
					bad_pumpkin_list.append(replantFunc())			
				else:
					pet_the_piggy()
					bad_pumpkin_list = movement.traverse_farm_returns(replantFunc)		
								
			movement.move_to_origin()
			harvest()
			
			item_needed = tools.need_item(plant["item"], plant["min"])
			
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
	return dinos
	
	
	
	
	
	
	
		