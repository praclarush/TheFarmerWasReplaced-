PLANTS = [	
	{
		"name":"sunflower",
		"entity":Entities.Sunflower,
		"item":Items.Power,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Soil,
		"power": False,
		"min":1000,
		"badEntity": None
	},
	{
		"name":"tree",
		"entity":Entities.Tree,
		"item":Items.Wood,
		"fertilize": False,
		"water": False,
		"ground": Grounds.Soil,		
		"power": True,
		"min":50000000,
		"badEntity": None
	},
	{
		"name":"hay",
		"entity":Entities.Grass,
		"item":Items.Hay,
		"ground": Grounds.Grassland,
		"fertilize": False,
		"water": False,
		"power": True,
		"min":5000000,
		"badEntity": None
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
		"badEntity": None
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
		"badEntity": Entities.Dead_Pumpkin
	}	
]

WAITING_PLANTS = [

	{
		"name":"cactus",
		"entity":Entities.Cactus,
		"item":Items.Cactus,
		"ground": Grounds.Soil,
		"min":100000
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
	
