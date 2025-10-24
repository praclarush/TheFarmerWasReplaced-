import __builtins__

from utilities import waiting_harvest

ALL_DIRECTIONS = [North, South, East, West]

def move_to_origin():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def get_opposite_direction(direction):
	if (direction == North):
		return South
	elif(direction == South):
		return North
	elif(direction == East):
		return West
	elif(direction == West):
		return East

def rotateCardinalDirection(direction):
	if (direction == North):
		return East
	elif(direction == East):
		return South 
	elif(direction == South):
		return West
	elif(direction == West):
		return North

def move_to_x_position(x):
	current_x = get_pos_x()
	moves = x - current_x
	if (moves < 0):
		direction = West
	else:
		direction = East

	for _ in range(abs(moves)):
		if (not move(direction)):
			return False
	return True

def move_to_y_position(y):
	current_y = get_pos_y()
	moves = y - current_y
	if (moves < 0):
		direction = South
	else:
		direction = North
	for _ in range(abs(moves)):
		if (not move(direction)):
			return False
	return True

def move_to_location(x, y):
	current_X = get_pos_x()
	current_Y = get_pos_y()
	
	while current_Y != y:
		if (current_Y <= y):
			move(North)
			current_Y += 1
		else:
			move(South)
			current_Y -= 1

	while (current_X != x):
		if (current_X <= x):
			move(East)
			current_X += 1
		else:
			move(West)
			current_X -= 1

def harvest_column():
	for _ in range(get_world_size()):
		if (get_entity_type() != None):
			waiting_harvest()
		move(North)
	
def harvest_row():
	for _ in range(get_world_size()):
		waiting_harvest()
		move(East)

def traverse_farm(cell_function):
	move_to_origin()	
	for _ in range(get_world_size):
		for _ in range(get_world_size):			
			cell_function()
			move(North)		
		move(East)			
	return True	

def traverse_farm_returns(cell_function):
	list = []		
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			result = cell_function()
			if (result != None):
				list.append(result)
			move(North)			
		move(East)			
	return list	

#Depth First Search ref - https://en.wikipedia.org/wiki/Depth-first_search
def explore_path(direction, target):
	if (not move(direction)):
		return False

	if (get_entity_type() == target):
		harvest()
		return True

	for explore_direction in ALL_DIRECTIONS:
		if (get_opposite_direction(explore_direction) == direction):
			continue

		if (explore_path(explore_direction, target)):
			return True

	move(get_opposite_direction(direction))

