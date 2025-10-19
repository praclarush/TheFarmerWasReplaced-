GRID_SIZE = [get_world_size(), get_world_size()]

def set_grid_size(x, y):
	global GRID_SIZE
	GRID_SIZE = [x, y]	
	
def get_grid_size():
	return GRID_SIZE
	
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