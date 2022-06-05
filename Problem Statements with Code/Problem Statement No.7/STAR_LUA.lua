--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code STAR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			STAR_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- generatePattern function to print the pattern of start(*) and hash(#)
t = io.read()
r = 0 
if 1<= tonumber(t) then 
r = 1
else
os.exit()
end
if 25>=tonumber(t) then 
r = 1
else
os.exit()
end
if r==1 then
for i=t,0,-1 
do
  l = tonumber(io.read())
if l == nil then
os.exit()
end
  p=0
if 100>= l then 
p = 1
else
os.exit()
end
if 1<=l then 
p = 1
else
os.exit()
end
if p==1 then
  for j=l,0,-1 
  do 
  s = ""
    for k=1,j,1 do
      if k%5 == 0 then
      s=s.."#"
      else 
      s=s.."*"
      end
    end
    print(s)
  end
end
end
end