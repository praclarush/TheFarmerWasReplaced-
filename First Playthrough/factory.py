def build_func(f):
	def g():
		f()
	return g		

def build_func1(f, arg):
	def g():
		f(arg)
	return g
	
def build_func2(f, arg1, arg2):
	def g():
		f(arg1, arg2)
	return g

def call_func(f, arg):
	def g():
		f(arg)
	g()
