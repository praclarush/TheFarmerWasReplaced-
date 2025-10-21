from movement import move_to_location

#bubble sort ref = https://en.wikipedia.org/wiki/Bubble_sort

def bubble_sort(x_edge, y_edge):	
	x_edge -= 1
	y_edge -= 1
	max_x_swap = x_edge
	max_y_swap = y_edge

	while (True):
		x_travel_range = range(max_x_swap + 1)
		y_travel_range = range(max_y_swap + 1)	

		max_x_swap = 0
		max_y_swap = 0

		for x in x_travel_range:
			for y in y_travel_range:
				swapped = False

				if (y != y_edge):
					if (measure() > measure(North)):
						swap(North)
						swapped = True

				if (x != x_edge):
					if (measure() > measure(East)):
						swap(East)
						swapped = True

				if (swapped):
					if (x > max_x_swap):
						max_x_swap = x

					if (y > max_y_swap):
						max_y_swap = y

				move(North)
			move(East)
			move_to_location(get_pos_x(), 0)
		move_to_location(0, get_pos_y())

		if (max_x_swap == 0 and max_y_swap == 0):
			return True

#TODO: explor A* 