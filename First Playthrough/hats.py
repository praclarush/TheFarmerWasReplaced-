from utilities import sleep

for hat in Hats:
	if (num_unlocked(hat) == 1):
		change_hat(hat)	
		print(hat)
		sleep(4)