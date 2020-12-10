#THIS PROGRAM RETURN NAME IN STAR AFTER USER INPUT
def pattern():
	for i in range(len(name)):
		#PATTERN OF A
		if name[i]=="A":
			priA=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if ((col==0 or col==4) and row!=0) or (row==0 and (0<col<4)) or (row==4 and col<5):
						priA[row][col]="*"
			list2.append(priA)
		#PATTERN OF B
		if name[i]=="B":
			priB=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and col!=5 and col!=6) or (row==6 and col!=5 and col!=6) or (col==5 and(0<row<6)) or (col==0) or (row==3) and col!=6:
						priB[row][col]="*"
			list2.append(priB)
		#PATTERN OF C
		if name[i]=="C":
			priC=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and 0<col<6) or (row==6 and 0<col<6) or (col==0 and 0<row<6):
						priC[row][col]="*"
			list2.append(priC)
		#PATTERN OF C
		if name[i]=="D":
			priD=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and col!=5 and col!=6) or (row==6 and col!=5 and col!=6) or (col==5 and(0<row<6)) or (col==0):
						priD[row][col]="*"			
			list2.append(priD)
		#PATTERN OF E
		if name[i]=="E":
			priE=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and col!=6) or (row==6 and col!=6) or (col==0) or (row==3 and (col<5)):
						priE[row][col]="*"
			list2.append(priE)			
		#PATTERN OF F
		if name[i]=="F":
			priF=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 ) or (row==3 and col!=5 and col!=6) or (col==0):
						priF[row][col]="*"
			list2.append(priF)			
		#PATTERN OF G *
		if name[i]=="G":
			priG=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==0 and col<6 or row==4 and 4<col<6:
						priG[row][col]="*"
					elif col==0 or (row==6 and col<4) or (col==4 and row>3 or col==6 and row>3):
						priG[row][col]="*"
			list2.append(priG)			
		#PATTERN OF H
		if name[i]=="H":
			priH=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (col==0 or col==5) or (row==3 and (col<6)):
						priH[row][col]="*"
			list2.append(priH)		
		#PATTERN OF I
		if name[i]=="I":
			priI=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 or row==6) or (col==3):
						priI[row][col]="*"
			list2.append(priI)
		#PATTERN OF J
		if name[i]=="J":
			priJ=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 or col==3) or 4<row<6 and 1<col<4 or  3<row<5 and 0<col<2:
						priJ[row][col]="*"
			list2.append(priJ)
		#PATTERN OF K
		if name[i]=="K":
			priK=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if col==0:
						priK[row][col]="*"
					elif (row==2 and 1<col<3 and 1<row<3) or (row==3 and 0<col<2 and 2<row<4) or (row==1 and 2<col<4 and 0<row<2) or (row==0 and 3<col<5 and row<1):
						priK[row][col]="*"
					elif (row==4 and 1<col<3 and 3<row<5) or (row==5 and 2<col<4 and 4<row<6) or (row==6 and 3<col<5 and 5<row<7):
						priK[row][col]="*"
			list2.append(priK)
		#PATTERN OF L
		if name[i]=="L":
			priL=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==6 or col==0:
						priL[row][col]="*"
			list2.append(priL)
		#PATTERN OF M
		if name[i]=="M":
			priM=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (col==0 or col==6) or (0<col<2 and 0<row<2) or (1<col<3 and 1<row<3):
						priM[row][col]="*"
					elif (2<col<4 and 2<row<4) or (3<col<5 and 1<row<3) or (4<col<6 and 0<row<2):
						priM[row][col]="*"
			list2.append(priM)
		#PATERN OF N
		if name[i]=="N":
			priN=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==col:
						priN[row][col]="*"
					elif col==0 or col==6:
						priN[row][col]="*"
			list2.append(priN)
		#PATTERN OF O
		if name[i]=="O":
			priO=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and 0<col<6) or (row==6 and 0<col<6) or (col==0 and (row>0 and row<6)):
						priO[row][col]="*"
					elif (col==6 and (row>0 and row<6)):
						priO[row][col]="*"
			list2.append(priO)
		#PATTERN OF P
		if name[i]=="P":
			priP=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (col==0 and (row>0) or row==0 and (0<col<5)) or (row==3 and col<5 or (col==5 and 0<row<3)):
						priP[row][col]="*"
			list2.append(priP)
		#PATTERN OF Q
		if name[i]=="Q":
			priQ=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row==0 and 0<col<6) or (row==5 and 0<col<6) or (col==0 and (row>0 and row<5)):
						priQ[row][col]="*"
					elif (col==6 and (row>0 and row<5)):
						priQ[row][col]="*"
					elif row==col and row>3:
						priQ[row][col]="*"			
			list2.append(priQ)
		#PATTERN OF R
		if name[i]=="R":
			priR=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if col==0 or row==0 and col<6 or row==3 and col<6:
						priR[row][col]="*"
					elif col==6 and 0<row<3 or col==6 and row >3:
						priR[row][col]="*"
			list2.append(priR)
		#PATTERN OF S
		if name[i]=="S":
			priS=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if (row == 0 and col>0) or (row == 3 and (0<col<6)):
						priS[row][col]="*"
					elif col == 0 and 0<row<3:
						priS[row][col]="*"
					elif col == 6 and 3<row<6:
						priS[row][col]="*"
					elif row==6 and col<6:
						priS[row][col]="*"
			list2.append(priS)
		#PATTERN OF T
		if name[i]=="T":
			priT=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==0 or col==3:
						priT[row][col]="*"
			list2.append(priT)
		#PATTERN OF U
		if name[i]=="U":
			priU=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(5):
					if ((col==0 or col==4) and row!=6) or (row==6 and (0<col<4)):
						priU[row][col]="*"
			list2.append(priU)
		#PATTERN OF V
		if name[i]=="V":
			priV=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==col and col<4:
						priV[row][col]="*"
					elif (row==2 and 3<col<5 and 1<row<3) or (row==3 and 2<col<4 and 2<row<4):
						priV[row][col]="*"
					elif (row==1 and 4<col<6 and 0<row<2) or (row==0 and col>5 and row<1):
						priV[row][col]="*"
			list2.append(priV)
		#PATTERN OF W
		if name[i]=="W":
			priW=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if col==0 or col==6 or row==col and col>2:
						priW[row][col]="*"
					elif row==5 and col<2 and row>4:
						priW[row][col]="*"
					elif row==4 and 1<col<3 and row>3:
						priW[row][col]="*"
			list2.append(priW)
		#PATTERN OF X
		if name[i]=="X":
			priX=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==col:
						priX[row][col]="*"
					elif (row==2 and 3<col<5 and 1<row<3) or (row==3 and 2<col<4 and 2<row<4) or (row==5 and 0<col<2 and 4<row<6) :
						priX[row][col]="*"
					elif (row==1 and 4<col<6 and 0<row<2) or (row==4 and 1<col<3 and 3<row<5) or (row==0 and col>5 and row<1) or (row==6 and col<1 and row>5):
						priX[row][col]="*"
			list2.append(priX)
		#PATTERN OF Y
		if name[i]=="Y":
			priY=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==col and col<4 or col==3 and row>2:
						priY[row][col]="*"
					elif row==2 and 3<col<5 and 1<row<3:
						priY[row][col]="*"
					elif row==1 and 4<col<6 and 0<row<2:
						priY[row][col]="*"
					elif row==0 and col>5 and row<1:
						priY[row][col]="*"
			list2.append(priY)
		#PATTERN OF Z
		if name[i]=="Z":
			priZ=[[" " for i in range(7)]for j in range(7)]
			for row in range(7):
				for col in range(7):
					if row==0 or row==6:
						priZ[row][col]="*"
					elif (row==2 and 3<col<5 and 1<row<3) or (row==3 and 2<col<4 and 2<row<4) or (row==5 and 0<col<2 and 4<row<6) :
						priZ[row][col]="*"
					elif (row==1 and 4<col<6 and 0<row<2) or (row==4 and 1<col<3 and 3<row<5) or (row==0 and col>5 and row<1) :
						priZ[row][col]="*"
			list2.append(priZ)	
																														
	return list2
#PROGRAM IS STARTED FROM HERE
for abc in range(100):
	name1=input("ENTER THE NAME=")
	name=name1.upper()
	list2=[]
	list3=pattern()
	for i in range(7):
		for j in range(len(list3)):
			for k in range(7):
				print(list3[j][i][k],end="")
			print(end=" ")
		print()
	print("GOODBYE ●_●")
	print("")
