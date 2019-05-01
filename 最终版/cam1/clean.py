import os
for i in range(3,7):
	print(i-3,":")
	for j in range(1,121):
		filename=str(i)+"/"+str(j)+".png"
		if not os.path.exists(filename):
			print(j)
			k=j-1
			tmpfile=str(i)+"/"+str(k)+".png"
			while not os.path.exists(tmpfile):
				k-=1
				tmpfile=str(i)+"/"+str(k)+".png"
			os.system("cp "+tmpfile+" "+filename)
