import farms
import movement
import static
import tools
import factory

clear()
plant = static.get_plant_by_item(Items.Wood)
farm = farms.create_farm_function(plant)
farm()


