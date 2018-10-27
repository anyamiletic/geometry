import numpy as np 

def corr1(M, Mp):
	a = M[0]
	b = M[1]
	c = M[2]
	u = Mp[0]
	v = Mp[1]
	t = Mp[2]

	correspondence1 = np.array(
		[0.0,0,0,-1*t*a,-1*t*b,-1*t*c,v*a,v*b,v*c]
		)

	# print(correspondence)
	# print(correspondence.shape)
	return correspondence1

def corr2(M, Mp):
	a = M[0]
	b = M[1]
	c = M[2]
	u = Mp[0]
	v = Mp[1]
	t = Mp[2]

	correspondence2 = np.array(
		[1.0*t*a,t*b,t*c,0,0,0,-1*u*a,-1*u*b,-1*u*c]
		)

	# print(correspondence)
	# print(correspondence.shape)
	return correspondence2

def dlt(original, images):
	#dobijena matrica

	M1,M2,M3,M4,M5,M6 = original
	M1p,M2p,M3p,M4p,M5p,M6p = images

	A = np.array([
		corr1(M1,M1p),
		corr2(M1,M1p),
		corr1(M2,M2p),
		corr2(M2,M2p),
		corr1(M3,M3p),
		corr2(M3,M3p),
		corr1(M4,M4p),
		corr2(M4,M4p),
		corr1(M5,M5p),
		corr2(M5,M5p),
		corr1(M6,M6p),
		corr2(M6,M6p)
		])	
	#np.reshape(A, (12,9))
	#print(A)
	u, s, vh = np.linalg.svd(A)
	#vh is theone we need
	result = vh[-1]
	result = np.reshape(result, (3,3))

	return result
