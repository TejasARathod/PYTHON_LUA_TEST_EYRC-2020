'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code IFFOR_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			IFFOR_PY.py
*  Created:				19/09/2020
*  Last Modified:		21/09/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Main function
if __name__ == '__main__':
	
	# Take the T (test_cases) input
	test_cases = int(input())

	# Write your code from here
	

for j in range(test_cases):
    v = int(input())

    

    n = range(v)

    s = ""
    for i in n:
        if i == 0:
            i += 3
        else:
            if i % 2 == 0:
                i = i * 2
            else:
                i = i ** 2
        s = s + str(i)
        if i != n:
            s = s + ' '
    print(s)

