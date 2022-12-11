def mult(x,y):
	if ( len(y) == 2 ):
		a = x[0]*y[0]+x[1]*y[1]
		b = x[2]*y[0]+x[3]*y[1]
		return [a,b]
	a = x[0]*y[0] + x[1]*y[2]
	b = x[0]*y[1] + x[1]*y[3]
	c = x[2]*y[0] + x[3]*y[2]
	d = x[2]*y[1] + x[3]*y[3]
	return [a,b,c,d]

# Only works for positive powers!
def matrix_power( x, n ):
	if ( n == 1 ):
		return x
	if ( n%2 == 0 ):
		return matrix_power( mult(x, x), n//2 )
	return mult(x, matrix_power( mult(x, x), n//2 ) )
	
# fibonacci example:
A = [1,1,1,0]
v = [1,0]
def main():
    x = int(input('Enter the number to find the nth fibonacci: '))
    print (mult(matrix_power(A,x-1),v)[0])

if __name__=='__main__':
    main()

