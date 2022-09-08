def get_ir(p, n=1):
	if (n == 0):
		print("The total is %s" % p)
	else:
		p += p * 0.3
		x = int(p / 500)
		p = x * 500
		print("Month %s is %s" % (n, p))
		n -= 1
		get_ir(p, n)

##if "__name__" == "__main__":
##     get_ir(p, n)
