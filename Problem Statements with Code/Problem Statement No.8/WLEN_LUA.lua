--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code WLEN_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			WLEN_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- countChar function to count the characters in each word of given string

t = io.read()
if t ==nil then
os.exit()
end
for j = 1,t do
s=""
  line = io.read()
  line= string.gsub(line,"@","")
  a={}
  i=1
  j=0
  for token in string.gmatch(line, "[^%s]+") do
  if j == 0 then
  j=0
  else do
  s=s..","
  end
  end
  a[i]=string.len(token,"%w+")
  s= s..tostring(a[i])
  i=i+1
  j=j+1
  end
print(s)
end
