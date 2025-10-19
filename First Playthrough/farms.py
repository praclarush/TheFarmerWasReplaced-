import movement
import tools
import factory

min_power_req = 100

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
	

def create_hey_farm(plant):
	def hey():
		item_needed = tools.need_item(plant["item"], plant["min"])
	
		if (not item_needed):
			return True
		
		quick_print("Item ", plant["name"], " Needed")
		clear() #reset the farm, quicker then retilling grounds
	
		while (item_needed):		
			if (plant["power"] and num_items(Items.Power) < min_power_req):
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
			if (plant["power"] and num_items(Items.Power) < min_power_req):
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
			if (plant["power"] and num_items(Items.Power) < min_power_req):
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
			if (plant["power"] and num_items(Items.Power) < min_power_req):
				print("Out of Power")
				return	False
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
			if (plant["power"] and num_items(Items.Power) < min_power_req):
				print("Out of Power")
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