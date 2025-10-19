import farms
import movement
import static

movement.set_grid_size(5, 5)
clear()
item = static.get_plant_by_item(Items.Pumpkin)
farm = farms.create_farm_function(item)
farm()
