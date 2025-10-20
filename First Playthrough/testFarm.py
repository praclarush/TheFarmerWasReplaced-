import farmUtil
import movement
import static
import tools
import factory

clear()

farm = static.get_farm_by_name("PumpkinFarm")

config_world_size = farm["worldSize"]
set_world_size(config_world_size)

farmFunction = farmUtil.create_farm_function(farm)
farmFunction()
movement.move_to_origin()
