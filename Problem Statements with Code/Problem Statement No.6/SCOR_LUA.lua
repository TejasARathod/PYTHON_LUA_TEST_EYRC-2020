testcase = tonumber(io.read())
if 1>testcase or testcase>25 then
os.exit()
end
for i=1,testcase do
t = tonumber(io.read())
if 2>t or t>100 then
os.exit()
end
i=1
a = {}
for i = 1,t do
  line = io.read()
  a[i]= line
  if 0>tonumber(string.match(a[i],"%d+")) or tonumber(string.match(a[i],"%d+"))>100 then
os.exit()
end
end
for i= 1,t do
for j= i+1 ,t do
if string.match(a[i],"%d+")<string.match(a[j],"%d+") then
c=a[i]
a[i]=a[j]
a[j]=c
else do 
r= 0
end
end
end 
end
d={}
for i = 1, t do 
if string.match(a[i],"%d+")==string.match(a[i+1],"%d+") then
d[i]=a[i]
print(d[i])
else do
print(a[1])
os.exit()
end
end
end
for i= 1,len(d) do
for j= i+1 ,len(d) do
if string.match(d[i],"%w+")<string.match(d[j],"%w+") then
c=d[i]
d[i]=d[j]
d[j]=c
else do 
r= 0
end
end
end 
for i =1,len(d) do 
    print(d[i])
    end
    
end


end