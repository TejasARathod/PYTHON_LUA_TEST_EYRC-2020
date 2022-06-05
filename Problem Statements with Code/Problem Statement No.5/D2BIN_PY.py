'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code D2BIN_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			D2BIN_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Function to calculate Euclidean distance between two points
def dec_to_binary(n):

	bin_num = None

	# Complete this function to return binary equivalent output of the given number 'n' in 8-bit format

	return bin_num


# Main function
#if __name__ == '__main__':
	
	# take the T (test_cases) input
test_cases = int(input())

	# Write the code here to take the n value
	#for case in range(1,test_cases+1):
		# take the n input values
		#n = int(input())

		# print (n)

		# Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
		#bin_num = dec_to_binary(n)
		#print(bin_num)
	

for j in range(test_cases):
    v = int(input(""))
    b = 00000000
    if v > 255:
        print("invalid input, no. should be less than or equal to 255")
    else:
        while v > 0:
         if v > 255:
            print("error")



         elif v >= 128:
            b = b + 10**7
            v = v -128
         elif v >= 64:
            b = b + 10**6
            v = v - 64
         elif v >= 32:
            b = b + 10**5
            v = v - 32
         elif v >= 16:
            b = b + 10**4
            v = v - 16
         elif v >= 8:
            b = b + 10**3
            v = v - 8
         elif v >= 4:
            b = b + 10**2
            v = v - 4
         elif v >= 2:
            b = b + 10**1
            v = v - 2
         elif v >= 1:
            b = b + 1
            v = v - 1
    print(str(b).zfill(8))
