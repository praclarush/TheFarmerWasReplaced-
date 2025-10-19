import actions

def create_planting_function(entity, use_water):
	def planting_function():	
		if (use_water):
			actions.water_ground()		
		plant(entity)		
	return planting_function
	
def create_tilling_function(ground_type):
	def set_ground_type():
		if get_ground_type() != ground_type:
			till()
	return set_ground_type		
	
def create_plant_pumpkin_function(use_water, use_fertilizer):
	def plant_pumpkin():	
		good_pumpkin = False
	
		while(not good_pumpkin):
			if (use_water):
				actions.water_ground()
	
			plant(Entities.Pumpkin)	
	
			if (use_fertilizer and num_items(Items.Fertilizer) > 5):
				use_item(Items.Fertilizer)			
	
			good_pumpkin = can_harvest()	
	return plant_pumpkin