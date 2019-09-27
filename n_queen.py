def valid_move(chess,col,row):				# finding the place for new queen if available
	c=1
	for i in range(col-1,-1,-1):	
		if chess[i]==row:
			return False
		if chess[i]==row-c:			# to check that the position is safe from 1st diagonal
			return False
		if chess[i]==row+c:			# to check that the position is safe from 2nd diagonal
			return False
		c+=1
	return True

def solve(chess,col,size):
	if col==size:
		return True
	for i in range(size):
		if valid_move(chess,col,i):
			chess[col]=i 				# if position found than storing it in an array
			if solve(chess,col+1,size):		# Recursize call for second row
				return True
	chess[col]=None
	return False

def solve_nqueen(size):
	chess=[None]*size
	if solve(chess,0,size):
		print("Solved")
		print(chess)
		for val in chess:
			arr=[0]*size					# declaring new array
			for j in range(0,size):			
				if val==j:	
					arr[j]='Q'			# save 'Q' for the position of queen in that row
				else:
					arr[j]='.'
			print(arr)					# print array
		return True
	else:
		print("No Solution")
		return False
	
if __name__=='__main__':
	size=int(input("Enter the size: "))
	solve_nqueen(size)
