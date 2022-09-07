emp=  0
ou =  1
ki =  2
gi =  3
fu =  4
ke =  5
ky =  6
ka =  7
hi =  8
ng =  9
to = 10
nk = 11
ny = 12
um = 13
ry = 14

moveID = [
	[( 1, 0)],         #up
	[(-1, 0)],         #down
	[( 0, 1), ( 0,-1)],#left or right
	[( 2, 1), ( 2,-1)],#kei jump
	[( 1, 1), ( 1,-1)],#upper left or right
 	[(-1, 1), (-1,-1)],#lower left or right
]

moveKind = [
	[0,0,0,0,0,0],#emp
	[1,1,1,0,1,1],#ou
	[1,1,1,0,1,0],#ki
	[1,0,0,0,1,1],#gi
	[1,0,0,0,0,0],#fu
	[0,0,0,1,0,0],#ke
	[9,0,0,0,0,0],#ky
	[0,0,0,0,9,9],#ka
	[9,9,9,0,0,0],#hi
]
moveKind+=[moveKind[2]]*4
moveKind+=((max(z)for z in zip(x,y))for x,y in zip(moveKind[7:9],moveKind[1:2]*2))

def naru(koma):
	return koma+6 if 2<koma<9 else koma

def unNaru(koma):
	return koma-6 if 8<koma else koma
