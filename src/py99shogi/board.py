from py99shogi.koma import *
def hasindex(obj):
	return hasattr(obj,'__index__')
def hasiter(obj):
	return hasattr(obj,'__iter__')
def hasnext(obj):
	return hasattr(obj,'__next__')
def haslen(obj):
	return hasattr(obj,'__len__')
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
					if hasiter(v):
						if isint is True:
								raise TypeError
						isint = False
						if not haslen(v):
							v = s[i] = list(v)
						if length is None:
							length = len(v)
						elif length != len(v):
								raise TypeError
					else:
						if hasindex(v)and isint is not False:
							isint=True
			return self.arr[index]if isint is not False else self[slice(a,b,c)for a,b,c in zip(s)]
		if isinstance(index,str):
			koma=fromKomaName[index]
			return(i//9,i%9) for i,v in enumerate(self) if v==koma
		if isinstance(index,tuple):
			length = len(index)
				if length == 2:
					if any(isinstance(v,slice)for v in index):
						index = index[:]
						if not isinstance(index[0],slice):
							index[0] = slice(index[0],index[0]+1)
						elif not isinstance(index[1],slice):
							index[1] = slice(index[1],index[1]+1))
						return(self[i,j]for j in range(9)[index[1]])for i in range(9)[index[0]]
					return self.arr[index[0]*9+index[1]]
				if length == 3:
					if index[2] >= 0:
						return self[index[0],index[1]]
					index = index[:]
					if isinstance(index[0],slice):
						index[0] = slice(9-index[0].start,9-index[0].stop,-index[0].step)
					if isinstance(index[1],slice):
						index[1] = slice(9-index[1].start,9-index[1].stop,-index[1].step)
					return self[index]
				raise TypeError
		if hasiter(index):
			return map(self.__getitem__,index)
		if hasindex(index):
			return self.arr[int(index)]
	def __setitem__(self,index,value):
		if isinstance(index,slice):
			s = [index.start,index.stop,index.step]
			isint = None
			length = None
			for i,v in enumerate(s):
				if v is not None:
					if hasiter(v):
						if isint is not None:
							raise TypeError
					else:
						if hasindex(v)and isint is not False:
							isint=True
					if not haslen(v):
						v = s[i] = list(v)
					if length is None:
						length = len(v)
					elif length != len(v):
						raise TypeError
			if isint:
				self.arr[index] = value
			else:
				self[zip(s)] = value
		elif isinstance(index,str):
			koma = fromKomaName[index]
			self[i for i,v in enumerate(self) if v==koma] = value
		elif isinstance(index,tuple):
			length = len(index)
				if length == 2:
					if any(isinstance(v,slice)for v in index):
						i = index[:]
						if not isinstance(i[0],slice):
							i[0] = slice(i[0],i[0]+1)
						elif not isinstance(i[1],slice):
							i[1] = slice(i[1],i[1]+1))
						self[x*9+y for x in range(9)[i[0]]for y in range(9)[i[1]]] = value
					else:
						self.arr[index[0]*9+index[1]]
				elif length == 3:
					if index[2] >= 0:
						self[index[0],index[1]] = value
					else:
						index = index[:]
						if isinstance(index[0],slice):
							index[0] = slice(9-index[0].start,9-index[0].stop,-index[0].step)
						if isinstance(index[1],slice):
							index[1] = slice(9-index[1].start,9-index[1].stop,-index[1].step)
						self[index] = value
				else:
					raise TypeError
		elif hasiter(index):
			if hasiter(value)and not isinstance(value,str):
				if not haslen(index):
					index = list(index)
				if not haslen(value):
					value = list(value)
				if len(index) != len(value):
					raise TypeError
				for k,v in zip(index,value):
					self[k] = v
			else:
				for k in index:
					self[k] = value
		elif hasindex(index):
			if isinstance(value,str):
				self.arr[int(index)] = fromKomaName[value]
			elif hasindex(value):
				self.arr[int(index)] = int(value)
			else:
				raise TypeError
		else:
			raise TypeError
board=Board()
