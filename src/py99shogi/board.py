from py99shogi.koma import *
class Board:
	def __init__(self):
		self.arr = [
			-ky,-ke,-gi,-ki,-ou,-ki,-gi,-ke,-ky,
			emp,-hi,emp,emp,emp,emp,emp,-ka,emp,
			-fu,-fu,-fu,-fu,-fu,-fu,-fu,-fu,-fu,
			emp,emp,emp,emp,emp,emp,emp,emp,emp,
			emp,emp,emp,emp,emp,emp,emp,emp,emp,
			emp,emp,emp,emp,emp,emp,emp,emp,emp,
			+fu,+fu,+fu,+fu,+fu,+fu,+fu,+fu,+fu,
			epm,+ka,emp,emp,emp,emp,emp,+hi,emp,
			+ky,+ke,+gi,+ki,+ou,+ki,+gi,+ke,+ky
		]
	def __iter__()
	def __getitem__(self,index):
		if isinstance(index,slice):
			s = [index.start,index.stop,index.step]
			isint = None
			length = None
			for i,v in enumerate(s):
				if v is not None:
					if hasattr(v,'__iter__'):
						if isint is not None:
							throw TypeError
					else:
						if hasattr(v,'__index__')and isint is not False:
							isint=True
					if not hasattr(v,'__len__'):
						v = s[i] = list(v)
					if length is None:
						length = len(v)
					elif length != len(v):
							throw TypeError
			return self.arr[index]if isint else self[zip(s)]
		if hasattr(index,'__iter__'):
			if hasattr(index,'__next__'):
				index = list(index)
			if all(hasattr(v,'__iter__')for v in index):
				return self[v]for v in index
			else:
				length = len(index)
				if length == 1:
					return self[index[0]]
				if length == 2:
					return self.arr[index[0]*9+index[1]]
				if length == 3:
					return self[9-index[0],9-index[1]]if index[2] < 0 else self[index[0],index[1]]
				throw TypeError
		if hasattr(index,'__index__'):
			return self.arr[int(index)]
	def __setitem__(self,index,value):
		if isinstance(index,slice):
			s = [index.start,index.stop,index.step]
			isint = None
			length = None
			for i,v in enumerate(s):
				if v is not None:
					if hasattr(v,'__iter__'):
						if isint is not None:
							throw TypeError
					else:
						if hasattr(v,'__index__')and isint is not False:
							isint=True
					if not hasattr(v,'__len__'):
						v = s[i] = list(v)
					if length is None:
						length = len(v)
					elif length != len(v):
						throw TypeError
			if isint:
				self.arr[index] = value
			else:
				self[zip(s)] = value
		elif hasattr(index,'__iter__'):
			if hasattr(index,'__next__'):
				index = list(index)
			length = len(index)
			if length == 1:
				self[index[0]] = value
			elif length == 2:
				self.arr[index[0]*9+index[1]] = value
			elif length == 3:
				self[9-index[0],9-index[1]]if index[2] < 0 else self[index[0],index[1]] = value
			else:
				throw TypeError
		elif hasattr(index,'__index__'):
			return self.arr[int(index)]
board=Board()
