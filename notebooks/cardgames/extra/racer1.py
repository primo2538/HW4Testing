class Race_Engine(object):
	def __init__(self, horsepower):
		self.horsepower = horsepower
	
	def __str__(self):
		return "Race_Engine with " + str(self.horsepower) + " horsepower"
	#...

class Drag_Racer(object):
	def __init__(self, engine):
		self.engine = engine
	
	def __str__(self):
		return "Drag_Racer with " + str(self.engine.horsepower) + " horsepower engine"
	#...

def main():
	engine1 = Race_Engine(480)
	engine2 = Race_Engine(530)
	racer1 = Drag_Racer(engine1)
	racer2 = Drag_Racer(engine2)
	
	print "Engine 1 =", engine1
	print "Engine 2 =", engine2
	print "Racer  1 =", racer1
	print "Racer  2 =", racer2

main()
