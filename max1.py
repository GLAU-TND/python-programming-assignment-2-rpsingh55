s,c=input(),[]
for i in range(len(s)):
	d=0
	if s[i] =="1":
		for j in range(i,len(s)):
			if s[j] =="1":
				d+=1
			else:
				c.append(d)
				break
print( max(c))

