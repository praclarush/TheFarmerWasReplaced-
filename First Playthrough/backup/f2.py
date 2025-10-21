import farmUtil
import movement
import static
import tools
import factory

set_world_size(6)

def plantTest():
	func = factory.call_func(plant, Entities.Bush)
	movement.traverse_farm(func)

def infect():
	x = get_pos_x()
	y = get_pos_y()

	if ((tools.is_even(x) and not tools.is_even(y)) or (tools.is_even(y) and not tools.is_even(x))):
		use_item(Items.Weird_Substance)

plantTest()
count = 0

for y in range(get_world_size()):
	for x in range(0, get_world_size(), 3):
		movement.move_to_location(x, y)
		use_item(Items.Weird_Substance)
		count += 1

quick_print(count)
while (True):
	pass

	