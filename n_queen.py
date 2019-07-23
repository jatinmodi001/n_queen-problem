def valid_move(chess,col,row):
	c=1
	for i in range(col-1,-1,-1):
		if chess[i]==row:
			return False
		if chess[i]==row-c:
			return False
		if chess[i]==row+c:
			return False
		c+=1
	return True

def solve(chess,col,size):
	if col==size:
		return True
	for i in range(size):
		if valid_move(chess,col,i):
			chess[col]=i
			if solve(chess,col+1,size):
				return True
	chess[col]=None
	return False

def solve_nqueen(size):
	chess=[None]*size
	if solve(chess,0,size):
		print("solved")
		print(chess)
		for i in chess:
			arr=[0]*size
			for j in range(0,size):
				if i==j:
					arr[size-1-j]='Q'
				else:
					arr[size-1-j]='.'
			print(arr)
		return True
	else:
		print("No solution")
		return False
	
if __name__=='__main__':
	size=int(input("enter the size: "))
	solve_nqueen(size)

