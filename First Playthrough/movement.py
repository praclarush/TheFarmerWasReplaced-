import static

def get_opposite_direction(direction):
	if (direction == North):
		return South
	elif(direction == South):
		return North
	elif(direction == East):
		return West
	elif(direction == West):
		return East
		
#Depth First Search ref - https://en.wikipedia.org/wiki/Depth-first_search
def explore_path(direction, target):
	if (not move(direction)):
		return False

	if (get_entity_type() == target):
		harvest()
		return True

	for explore_direction in static.ALL_DIRECTIONS:
		if (get_opposite_direction(explore_direction) == direction):
			continue

		if (explore_path(explore_direction, target)):
			return True

	move(get_opposite_direction(direction))

def set_grid_size(size):
	set_world_size(size)
		
def get_grid_size():
	return [get_world_size(), get_world_size()]
	
def traverse_farm_returns(cell_function):
	move_to_origin()
	grid = get_grid_size()
	list = []	
	
	for x in range(grid[0]):
		for y in range(grid[1]):
			result = cell_function()
			if (result != None):
				list.append(result)
			move(North)	
		move_to_location(get_pos_x(), 0)
		move(East)		
	move_to_origin()	
	return list		

def traverse_farm(cell_function):
	move_to_origin()
	grid = get_grid_size()
	for x in range(grid[0]):
		for y in range(grid[1]):			
			cell_function()
			move(North)
		move_to_location(get_pos_x(), 0)
		move(East)		
	move_to_origin()
	return True	
	
def move_to_origin():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
		
def move_to_x_position(x):
	current_x = get_pos_x()
	moves = x - current_x
	if (moves < 0):
		direction = West
	else:
		direction = East

	for i in range(abs(moves)):
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
	for i in range(abs(moves)):
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