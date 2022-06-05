--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code PAL_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			PAL_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- palindrome function to check whether the input string is a palindrome or not with case insensitive
t= tonumber(io.read())
for i=t,0,-1 do
    if 1<=t then
        if t<=25 then
            
pal=io.read()
if pal == nil then
    os.exit()
    end
l = string.len(pal)
 if 2<=l then
     if l<=100 then
s = string.lower(pal)
if s == string.reverse(s) then
	print("It is a palindrome");
else
	print("It is not a palindrome");
	end
end
end
end
end
end