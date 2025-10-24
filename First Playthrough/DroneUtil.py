def create_drone(action):
	while (num_drones() >= max_drones()):
		pass
	return spawn_drone(action)

def wait_for_drones(drones):
	list = []
	for drone in drones:
		if (drone != None):
			list.append(wait_for(drone))
