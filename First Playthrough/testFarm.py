import farms
import movement
import static
import tools
import factory

clear()
plant = static.get_plant_by_item(Items.Bone)

config_world_size = plant["worldSize"]
if (not tools.is_even(config_world_size )):
	print("Invalid World Size, Must be even - Skipping")
else:
	set_world_size(plant["worldSize"])
	farm = farms.create_farm_function(plant)
	farm()
	movement.move_to_origin()
	print("Farm Run Finished")

