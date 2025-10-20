ALL_DIRECTIONS = [North, South, East, West]

MIN_POWER_REQ = 500

# ---------------------------------------------------------	#
# name - The Name of the Plant 								#
# entity - The Entity to Plant 								#
# item - The Item Farmed 									#
# fertilize - Use Furtilizer when Planting 					#
# ground - Water the plant when Planting 					#
# min - The Miniumn amount of the Item to maintain 			#
# badEntity - if the Plant has an Invalid Entity state		#
# worldSize - sets the size of the False					#
# enabled - Enable farming of the Plant 					#
# ---------------------------------------------------------	#
PLANTS = [	
	{
		"name":"sunflower",
		"entity":Entities.Sunflower,
		"item":Items.Power,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Soil,
		"power": False,
		"min":5000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": True
	},
	{
		"name":"tree",
		"entity":Entities.Tree,
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Soil,		
		"power": True,
		"min":5500000,
		"badEntity": None,
		"worldSize": 16,		
		"enabled": True
	},
	{
		"name":"hay",
		"entity":Entities.Grass,
		"item":Items.Hay,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":1750000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": True
	},	
	{
		"name":"carrot",
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":150000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": True
	},
	{
		"name":"pumpkin",
		"entity":Entities.Pumpkin,
		"item":Items.Pumpkin,
		"ground": Grounds.Soil,
		"fertilize": True,
		"water": False,
		"power": True,
		"min":400000,
		"badEntity": Entities.Dead_Pumpkin,
		"worldSize": 16,
		"enabled": True
	},
	{
		"name":"cactus",
		"entity":Entities.Cactus,
		"item":Items.Cactus,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True, 
		"min":75000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": True		
	},
	{	
		"name":"maze",
		"entity":Entities.Bush,
		"item":Items.Gold,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":110000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": True		
	},
	{	
		"name":"dinos",
		"entity":Entities.Apple,
		"item":Items.Bone,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":75000,
		"badEntity": None,
		"worldSize": 16, #farm can't work if not even
		"enabled": True		
	}
]

# Weird_substance
WAITING_PLANTS = [	
	{	
		"name":"WeirdSubstance",
		"entity":Entities.Bush,
		"item":Items.Weird_Substance,
		"ground": Grounds.Grassland,
		"fertilize": True,
		"water": False,
		"power": True,
		"min":500000,
		"badEntity": None,
		"worldSize": 16,
		"enabled": False		
	}
]


def get_plant_by_item(item):
	for plant in PLANTS:
		if (plant["item"] == item):
			return plant
	return None

def get_plant_by_entity(entity):
	for plant in PLANTS:
		if (plant["entity"] == entity):
			return plant
	return None
	
