ALL_DIRECTIONS = [North, South, East, West]

MIN_POWER_REQ = 500

# ---------------------------------------------------------	#
# name - The Name of the Plant 								#
# farm - The Entity to use	 								#
# entity - The Entity to Plant 								#
# item - The Item Farmed 									#
# fertilize - Use Furtilizer when Planting 					#
# ground - Water the plant when Planting 					#
# min - The Miniumn amount of the Item to maintain 			#
# badEntity - if the Plant has an Invalid Entity state		#
# worldSize - sets the size of the False					#
# enabled - Enable farming of the Plant 					#
# ---------------------------------------------------------	#
Farms = [	
	{
		"name":"SunflowerFarm",
		"farm": "Sunflower",
		"entity":Entities.Sunflower,
		"item":Items.Power,
		"fertilize": False,
		"water": True,
		"ground": Grounds.Soil,
		"power": False,
		"min":5000,
		"badEntity": None,
		"worldSize": 7,
		"enabled": True
	},
	{
		"name":"TreeFarm",
		"farm": "Tree",
		"entity":Entities.Tree,
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Grassland,		
		"power": True,
		"min":5500000,
		"badEntity": None,
		"worldSize": 12,		
		"enabled": False
	},
	{
		"name":"BushFarm",
		"farm": "Bush",
		"entity":Entities.Bush,
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Grassland,		
		"power": True,
		"min":5500000,
		"badEntity": None,
		"worldSize": 12,		
		"enabled": False
	},
	{
		"name":"HayFarm",
		"farm": "Hey",
		"entity":Entities.Grass,
		"item":Items.Hay,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":2000000,
		"badEntity": None,
		"worldSize": 3,
		"enabled": False
	},	
	{
		"name":"CarrotFarm",
		"farm": "Carrot",
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":260000,
		"badEntity": None,
		"worldSize": 12,
		"enabled": False
	},
	{
		"name":"PumpkinFarm",
		"farm": "Pumpkin",
		"entity":Entities.Pumpkin,
		"item":Items.Pumpkin,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":4100000,
		"badEntity": Entities.Dead_Pumpkin,
		"worldSize": get_world_size(),
		"enabled": False
	},
	{
		"name":"CactusFarm",
		"farm": "Cactus",
		"entity":Entities.Cactus,
		"item":Items.Cactus,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True, 
		"min":2600000,
		"badEntity": None,
		"worldSize": 12,
		"enabled": True		
	},
	{	
		"name":"MazeFarm",
		"farm": "Maze",
		"entity":Entities.Bush,
		"item":Items.Gold,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":256000,
		"badEntity": None,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"DinoFarm",
		"farm": "Dino",
		"entity":Entities.Apple,
		"item":Items.Bone,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":1000000,
		"badEntity": None,
		"worldSize": 12, #farm can't work if not even
		"enabled": False		
	},
	{	
		"name":"PolycultureHeyFarm",
		"farm": "Polyculture",	
		"entity":Entities.Grass, 
		"item":Items.Hay,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":5000000,
		"badEntity": None,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"PolycultureBushFarm",
		"farm": "Polyculture",	
		"entity":Entities.Bush, 
		"item":Items.Wood,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":5000000,
		"badEntity": None,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"PolycultureCarrotFarm",	
		"farm": "Polyculture",	
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":260000,
		"badEntity": None,
		"worldSize": get_world_size(),
		"enabled": False		
	},
	{	
		"name":"WeirdSubstance",
		"farm": "WeirdSubstance",	
		"entity":Entities.Tree,
		"item":Items.Weird_Substance,
		"ground": Grounds.Grassland,
		"fertilize": True,
		"water": False,
		"power": True,
		"min":500000,
		"badEntity": None,
		"worldSize": 12,
		"enabled": True		
	}
]

def get_farm_by_item(item):
	for farm in Farms:
		if (farm["item"] == item):
			return farm
	return None

def get_farm_by_entity(entity):
	for farm in Farms:
		if (farm["entity"] == entity):
			return farm
	return None

def get_farm_by_name(name):
	for farm in Farms:
		if (farm["name"] == name):
			return farm
	return None