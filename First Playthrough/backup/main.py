import actions
import factory
import helpers

min_num_items = 200000
is_running = True

max_loop_count = 100
loop_count = 0
clear()	
while (is_running):
	#actions.get_item_if_needed(Items.Hay, min_num_items)
	actions.get_item_if_needed(Items.Wood, min_num_items)
	#actions.get_item_if_needed(Items.Carrot, min_num_items)
	#actions.get_item_if_needed_special(Items.Pumpkin, min_num_items, factory.create_plant_pumpkin_function(True, True))
	
	if (max_loop_count >= loop_count):
		loop_count += 1
		quick_print("Loop: ", loop_count)
	else:
		is_running = False
	
		
	
	
