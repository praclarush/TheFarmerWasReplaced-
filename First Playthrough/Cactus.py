import movement

def farm_catus():
	world_edge = get_world_size() - 1
	
	loop_count = 15
	
	while(loop_count != 0):
		#plant cactus
		for x in range (get_world_size()):
			for y in range(get_world_size()):
				if (get_ground_type() == Grounds.Grassland):
					till()
				if (get_entity_type() != Entities.Cactus):
					plant(Entities.Cactus)
				move(North)
			move(East)
				
		# Bubble Sort 
		highest_x_swap = world_edge
		highest_y_swap = world_edge
		while(True):
			x_travel_length_range = range(highest_x_swap+1)
			y_travel_length_range = range(highest_y_swap+1)
			
			highest_x_swap = 0
			highest_y_swap = 0
			
			for x in x_travel_length_range:
				for y in y_travel_length_range:
					swapped = False
						
					if(y != world_edge):
						if(measure() > measure(North)):
							swap(North)
							swapped = True
					
					if(x != world_edge):
						if(measure() > measure(East)):
							swap(East)
							swapped = True
					
					if(swapped):
						if(x > highest_x_swap):
							highest_x_swap = x
						
						if(y > highest_y_swap):
							highest_y_swap = y
				
					move(North)
					
				move(East)
				movement.move_to_location(get_pos_x(), 0)

			movement.move_to_location(0, get_pos_y())			
			
			if(highest_x_swap == 0 and highest_y_swap == 0):
				harvest()
				break
		loop_count -= 1






def sort_horizontally():
	for x in range(get_world_size()):
		sort_collumn(x)
		
def sort_collumn(x):
	is_sorted = False
	move_to_position(x, get_world_size()-1)
	while not is_sorted:
		changes = list()

		for i in range(get_world_size()):
			changes.append(is_next_cactus_bigger(East))
			
		is_sorted = is_changes_made(changes)

def sort_vertically():
	for y in range(get_world_size()):
		sort_row(y)
		
def sort_row(y):
	is_sorted = False
	move_to_position(get_world_size()-1, y)
	while not is_sorted:
		changes = list()
		for i in range(get_world_size()):
			changes.append(is_next_cactus_bigger(North))
			
		is_sorted = is_changes_made(changes)

def is_changes_made(changes):
	if True in changes:
		return False
	return True

def is_next_cactus_bigger(direction):
	answer = False
	if (measure(direction) > measure()):
		swap(direction)
		answer = True
	move(direction)
	return answer

def is_prev_cactus_bigger(check, direction):
	answer = False
	if (measure(check) < measure()):
		swap(check)
		answer = True
	move(direction)
	return answer