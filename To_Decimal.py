

#Octal to Dec

while True:
	try:
		clr_g = '\033[1;32;40m'
		number = input(clr_g+'\n Enter the Number => ')
		base = int(input(' Enter the base => '))
		digits = number.count('')
		digits = digits-2
		number= number[::-1]
		count = number.count('')
		c = 1
		dec = []
		h = []
		for i in range(0,count):
			mult = base**i	
			h.append(mult)
		a = 0		
		for k in number:	
			dect = int(h[a])*int(k)
			print(' ',h[a],'×',k,'=',dect,)
			dec.append(dect)	
			a += 1	
		decim = 0
		for i in dec:
			decim += i
		print('~~~'*count,)		
		print('  Total => ',decim,)	
		print('  Number => ',number)
		print('\a  Decimal => ',decim)
		
	except:
		print('Error Occurred !')
		
	