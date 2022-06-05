'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code DIST_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            DIST_PY.py
*  Created:             02/10/2020
*  Last Modified:       02/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Import any required module/s


T = int(input())
for j in range(T):
  s = input()
  n=""
  c=0
  for l in s:
    if l == " ":
      
      if c == 0:
        x1 = int(n)
        
        n=""
      elif c==1:
        y1= int(n)
        
        n=""
      elif c==2:
       x2= int(n)
       
       n=""  
      c = c+1 
    else:
      n=n+l

  for l in s:
    if l ==" ":
      n= ""
    else:
      n=n+l
  y2 = int(n) 
  

  r =0
  if -20<=x1<= 20:
    r=0
  elif -20<=x2<=20:
    r=0
  elif -20<=y1<= 20:
    r=0
  elif -20<=y2<= 20:
    r=0
  elif 1<= T <= 25:
    r=0
  else:
    print("error")
  
  dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
  
  print("Distance:",format(dist, '.2f'))


# Function to calculate Euclidean distance between two points
#def compute_distance(x1, y1, x2, y2):

    #distance = 0

    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places


# Main function
#if __name__ == '__main__':
    
    # Take the T (test_cases) input
    #test_cases = int(input())

    # Write the code here to take the x1, y1, x2 and y2 values
    
    
    	# Once you have all 4 values, call the compute_distance function to find Euclidean distance
		#compute_distance(x1, y1, x2, y2)
