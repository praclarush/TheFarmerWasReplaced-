Name = None
Farm = None
Crop = None
Item = None
Use_Fertilizer = False
Use_Water = False
Required_Amount = 0
World_Size = get_world_size()
Is_Enabled = False
Min_Power_Threshold = 500
Min_Water_Threshold = 0.25
Ground_Water_Threshold = 0.75
Min_Fertilizer_Threshold = 200
Current_Hat = Hats.Purple_Hat

# ---------------------------------------------------------	#
# name - The Name of the Plant 								#
# farm - The Entity to use	 								#
# entity - The Entity to Plant 								#
# item - The Item Farmed 									#
# fertilize - Use Furtilizer when Planting 					#
# min - The Miniumn amount of the Item to maintain 			#
# worldSize - sets the size of the False					#
# enabled - Enable farming of the Plant 					#
# ---------------------------------------------------------	#
Plant_Configs = [	
	{
		"name":"HayFarm",
		"farm": "Hey",
		"entity":Entities.Grass,
		"item":Items.Hay,		
		"fertilize": False,
		"water": False,
		"min":25000000,
		"worldSize": max_drones()-1,
		"enabled": True
	},
	{
		"name":"TreeFarm",
		"farm": "Tree",
		"entity":Entities.Tree,
		"item":Items.Wood,
		"fertilize": False,
		"water": True,
		"min":25000000,
		"worldSize": max_drones()-1,		
		"enabled": True
	},	
	{
		"name":"CarrotFarm",
		"farm": "Carrot",
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"fertilize": False,
		"water": True,
		"min":25000000,
		"worldSize": max_drones()-1,
		"enabled": True
	},
	{
		"name":"SunflowerFarm",
		"farm": "Sunflower",
		"entity":Entities.Sunflower,
		"item":Items.Power,
		"fertilize": False,
		"water": True,
		"min":2000,		
		"worldSize": max_drones()-1,
		"enabled": True
	},
	{
		"name":"PumpkinFarm",
		"farm": "Pumpkin",
		"entity":Entities.Pumpkin,
		"item":Items.Pumpkin,
		"fertilize": False,
		"water": False,
		"min":25000000,
		"worldSize": max_drones()-1,
		"enabled": True
	},
	{
		"name":"CactusFarm",
		"farm": "Cactus",
		"entity":Entities.Cactus,
		"item":Items.Cactus,
		"fertilize": False,
		"water": False,
		"min":25000000,
		"worldSize": max_drones()-1,
		"enabled": True		
	},
	{	
		"name":"MazeFarm",
		"farm": "Maze",
		"entity":Entities.Bush,
		"item":Items.Gold,
		"fertilize": False,
		"water": False,
		"min":1000000,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"DinoFarm",
		"farm": "Dino",
		"entity":Entities.Apple,
		"item":Items.Bone,
		"fertilize": False,
		"water": False,
		"min":100000000,
		"worldSize": get_world_size(), #farm can't work if not even
		"enabled": True		
	},
	{	
		"name":"WeirdSubstanceFarm",
		"farm": "Tree",	
		"entity":Entities.Tree,
		"item":Items.Weird_Substance,
		"fertilize": False,
		"water": True,
		"min":6000000,
		"worldSize": max_drones()-1,
		"enabled": True		
	},
	{	
		"name":"PolycultureHeyFarm",
		"farm": "Polyculture",	
		"entity":Entities.Grass, 
		"item":Items.Hay,
		"fertilize": False,
		"water": False,
		"min":5000000,		
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"PolycultureBushFarm",
		"farm": "Polyculture",	
		"entity":Entities.Bush, 
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"min":5000000,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"PolycultureCarrotFarm",	
		"farm": "Polyculture",	
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"fertilize": False,
		"water": False,
		"min":260000,
		"worldSize": get_world_size(),
		"enabled": False		
	}
]

def get_config_by_item(item):
	for farm in Plant_Configs:
		if (farm["item"] == item):
			return farm
	return None

def get_config_by_entity(entity):
	for farm in Plant_Configs:
		if (farm["entity"] == entity):
			return farm
	return None

def get_config_by_name(name):
	for farm in Plant_Configs:
		if (farm["name"] == name):
			return farm
	return None


def init(farm_config):
	global Name
	global Farm
	global Crop
	global Item
	global Use_Fertilizer 
	global Use_Water 
	global Required_Amount
	global World_Size
	global Is_Enabled 

	Name = farm_config["name"]
	Farm = farm_config["farm"]
	Crop = farm_config["entity"]
	Item = farm_config["item"]
	Use_Fertilizer = farm_config["fertilize"]
	Use_Water = farm_config["water"]
	Required_Amount = farm_config["min"]
	World_Size = farm_config["worldSize"]
	Is_Enabled = farm_config["enabled"]
