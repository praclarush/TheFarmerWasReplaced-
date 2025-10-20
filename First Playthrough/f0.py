def pumpkin():
		item_needed = tools.need_item(farm["item"], farm["min"])
		
		if (not item_needed):
			return True
			
		quick_print("Item ", farm["name"], " Needed")		

		while (item_needed):
			if (farm["power"] and num_items(Items.Power) < static.MIN_POWER_REQ):
				print("Out of Power")
				return False
				
			if (not tools.can_afford_item(farm["entity"])):
				print("Cannot afford: ", farm["entity"])
				return False
						
			movement.traverse_farm(factory.create_planting_function(farm))
			
			def check_pumpkin_is_good():
				if ((get_entity_type() == Entities.Dead_Pumpkin) or (not can_harvest())):
					return False
				return True							

			def look_for_bad_pumpkins():
				if (check_pumpkin_is_good()):
					return (get_pos_x(), get_pos_y())

			suspect_pumpkins = movement.traverse_farm_returns(look_for_bad_pumpkins)
			while (len(suspect_pumpkins) != 0):				
				cords = bad_pumpkin_list.pop()
				
				if (cords == None):
					break
				else:
					movement.move_to_location(cords[0], cords[1])
					if (not check_pumpkin_is_good()):
						if (get_entity_type() == Entities.Dead_Pumpkin):							
							harvest()
							plant(farm["entity"])
							suspect_pumpkins.append(cords)
						else:
							suspect_pumpkins.append(cords)																				
							pet_the_piggy()
												
			movement.move_to_origin()
			harvest()
			
			item_needed = tools.need_item(farm["item"], farm["min"])
			
		return True