from tools import get_current_pos, is_even, water_ground, fertilize

def call_func(f, arg):
	def g():
		f(arg)
	return g

def create_harvest_and_plant_function(entity):
	def harvest_and_replant():
		harvest()
		create_planting_function(entity)()
	return harvest_and_replant
	
def create_replanting_function(entity):
	def replant_function():
		if (not can_harvest()):			
			if (entity["badEntity"] != None and get_entity_type() == entity["badEntity"]):			
				harvest()
				if (entity["water"]):
					water_ground()
				if (entity["fertilize"]):
					fertilize()		
				plant(entity["entity"])				
				return get_current_pos()		
		return None
	return replant_function
	
def create_messured_planting_function(entity):
	def mesured_planting_function():
		if (get_ground_type() != entity["ground"]):
			till()			
		if (entity["water"]):
			water_ground()	
		if (entity["fertilize"]):
			fertilize()		
		plant(entity["entity"])		
		return (get_current_pos(), measure())
	return mesured_planting_function

def create_planting_function(entity):
	def planting_function():	
		if (get_ground_type() != entity["ground"]):
			till()			
		if (entity["water"]):
			water_ground()						
		plant(entity["entity"])				
		if (entity["fertilize"]):
			fertilize()	
		return get_current_pos()
	return planting_function
	
def create_tilling_function(ground_type):
	def set_ground_type():
		if get_ground_type() != ground_type:
			till()
	return set_ground_type		
	
def create_plant_tree_function(entity, plant_bush_in_gaps):
	def plant_tree():
		current_X = get_pos_x()
		current_Y = get_pos_y()

		if (entity["water"]):
			water_ground()									
		
		if ((is_even(current_X) and not is_even(current_Y)) or (is_even(current_Y) and not is_even(current_X))):
			plant(Entities.Tree)		
		else:
			if (plant_bush_in_gaps):
				plant(Entities.Bush)	
			
		if (entity["fertilize"]):
			use_item(Items.Fertilizer)	
			
	return plant_tree
	
