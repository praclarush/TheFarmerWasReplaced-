def get_entity_from_item(item = Items.Hay):
	if (item == Items.Hay):
		return Entities.Grass
	elif(item == Items.Wood):
		return Entities.Bush
	elif(item == Items.Carrot):
		return Entities.Carrot
	elif(item == Items.Pumpkin):
		return Entities.Pumpkin
	else:
		return None

def need_item(item, min_count):
	return num_items(item) < min_count

	
def can_afford_cost(entity):
	cost = get_cost(entity)
	
	if (entity == Entities.Carrot):
		if ((num_items(Items.Hay) < cost[Items.Hay]) or (num_items(Items.Wood) < cost[Items.Wood])):
			return False
	elif(entity== Entities.Pumpkin):
		if (num_items(Items.Carrot) < cost[Items.Carrot]):
			return False
	
	return True