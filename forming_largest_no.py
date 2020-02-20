s,c=list(map(str,input().split())),[]
for i in s:
	for j in i:
		c.append(j)
print("".join(sorted(c,reverse=True)))


