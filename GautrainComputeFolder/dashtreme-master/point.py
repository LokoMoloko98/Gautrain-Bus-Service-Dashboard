from math import sqrt
class Point():
#″″″A class for points in Cartesian coordinate systems.″″″
	def __init__(self, x=None, y=None, busID=None):
		self.x, self.y = x, y
		self.busID = busID

	def get_busID(self):
		return self.busID

	def __getitem__(self, i):
		if i==0: return self.x
		if i==1: return self.y
		return None
	def __len__(self):
		return 2
	def __eq__(self, other):
		if isinstance(other, Point):
			return self.x==other.x and self.y==other.y
		return NotImplemented
	def __ne__(self, other):
		result = self.__eq__(other)
		if result is NotImplemented:
			return result
		return not result
	def __lt__(self, other):
		if isinstance(other, Point):
			if self.x<other.x:
				return True
			elif self.x==other.x and self.y<other.y:
				return True
			return False
		return NotImplemented
	def __gt__(self, other):
		if isinstance(other, Point):
			if self.x>other.x:
				return True
			elif self.x==other.x and self.y>other.y:
				return True
			return False
		return NotImplemented
	def __ge__(self, other):
		if isinstance(other, Point):
			if self > other or self == other:
				return True
			else:
				return False
			return False
		return NotImplemented
	def __le__(self, other):
		if isinstance(other, Point):
			if self < other or self == other:
				return True
			else:
				return False
			return False
		return NotImplemented

	def __repr__(self):
		if type(self.x) is int and type(self.y) is int:
			return self.x, self.y
		else:
			return self.x, self.y
			
	def __str__(self):
		if type(self.x) is int and type(self.y) is int:
			return "({0:.10f},{1:.10f})".format(self.x,self.y)
		else:
			return "({0:.10f}, {1:.10f})".format(self.x,self.y)
	def distance(self, other):
		return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)