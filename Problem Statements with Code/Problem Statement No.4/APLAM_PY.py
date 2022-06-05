'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code APLAM_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			APLAM_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Import reduce module
from functools import reduce


# Function to calculate Euclidean distance between two points
#def generate_AP(a1, d, n):
T = int(input())
for j in range(T):
  s = input()
  p=""
  c=0
  for l in s:
    if l == " ":
      
      if c == 0:
        a = int(p)
        p=""
      elif c==1:
        d= int(p)
        p=""
      c = c+1 
    else:
      p=p+l

  for l in s:
    if l ==" ":
      p= ""
    else:
      p=p+l
  n = int(p) 
  r =0
  if 1<=a<= 20:
    r=0
  elif 1<=d<=20:
    r=0
  elif 1<=n<= 20:
    r=0
  elif 1<= T <= 25:
    r=0
  else:
    print("error")


  i = 0
  s = ""
  sq = ""
  sum = 0
  while i < n:
     x = a + (i*d)
     s = s + str(x) + " "
     q = x**2
     sq = sq + str(q) + " "
     sum = sum + q
     i = i + 1
  print(s)
  print(sq)
  print(sum)
	#AP_series = []

	# Complete this function to return A.P. series


	#return AP_series


# Main function
#if __name__ == '__main__':
	
	# take the T (test_cases) input
	#test_cases = int(input("enter number of cases: "))

	# Write the code here to take the a1, d and n values


		# Once you have all 3 values, call the generate_AP function to find A.P. series and print it
		#AP_series = generate_AP(a1, d, n)

		# Using lambda and map functions, find squares of terms in AP series and print it
		#sqr_AP_series = 

		# Using lambda and reduce functions, find sum of squares of terms in AP series and print it
		#sum_sqr_AP_series = 

