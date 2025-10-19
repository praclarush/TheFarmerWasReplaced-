ALL_DIRECTIONS = [North, South, East, West]

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
		"enabled": False
	},
	{
		"name":"tree",
		"entity":Entities.Tree,
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Soil,		
		"power": True,
		"min":5000000,
		"badEntity": None,
		"enabled": False
	},
	{
		"name":"hay",
		"entity":Entities.Grass,
		"item":Items.Hay,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":1500000,
		"badEntity": None,
		"enabled": False
	},	
	{
		"name":"carrot",
		"entity":Entities.Carrot,
		"item":Items.Carrot,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":100000,
		"badEntity": None,
		"enabled": False
	},
	{
		"name":"pumpkin",
		"entity":Entities.Pumpkin,
		"item":Items.Pumpkin,
		"ground": Grounds.Soil,
		"fertilize": True,
		"water": False,
		"power": True,
		"min":100000,
		"badEntity": Entities.Dead_Pumpkin,
		"enabled": False
	},
	{
		"name":"cactus",
		"entity":Entities.Cactus,
		"item":Items.Cactus,
		"ground": Grounds.Soil,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":500000,
		"badEntity": None,
		"enabled": True		
	}
]

WAITING_PLANTS = [	
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
	
