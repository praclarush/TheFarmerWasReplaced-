import farmUtil
import movement
import static
import tools
import factory

clear()

a = num_items(Items.Wood)
plant(Entities.Tree)
tools.waiting_harvest()
b = num_items(Items.Wood)
quick_print(b - a)