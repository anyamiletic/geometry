import naive
import dlt
import modified_dlt

def main():
	M1 = [1,2,3]
	M2 = [2,-3,5]
	M3 = [6,1,-2]
	M4 = [-12,8,8]
	M5 = [4,-2,1]
	M6 = [1,1,1]

	M1p = [14,29,-2]
	M2p = [13,18,23]
	M3p = [42,19,12]
	M4p = [-60,32,-60]
	M5p = [25,11,21]
	M6p = [10,13.9,0]

	# M1 = [20,10,5]
	# M2 = [10,2,1]
	# M3 = [14,10,1]
	# M4 = [6,24,30]
	# M5 = [-3,3,1]
	# M6 = [-7,7,7]

	# M1p = [16,4,1]
	# M2p = [18,2,1]
	# M3p = [24,6,1]
	# M4p = [20,6,1]
	# M5p = [2.3,05,0.1]
	# M6p = [0.6,0.2,0.1]

	original = [M1,M2,M3,M4,M5,M6]
	images = [M1p,M2p,M3p,M4p,M5p,M6p]

	print("Naive algorithm:")
	print(naive.algorithm(M1,M2,M3,M4,M1p,M2p,M3p,M4p))
	print("DLT algorithm")
	print(dlt.dlt(original, images))
	print("modified dlt:")
	print(modified_dlt.func(original, images))

if __name__ == "__main__":
	main()