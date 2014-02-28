
def sum(vekt1,hoyde1):
	x = hoyde1 / 100 
	z = vekt1 / (x * x)
	y = round(z,1)
	
	print "BMI: ", y

	if y <= 18.4:
		print "Undervektig > 18,5"

	elif y >= 18.5 and y <= 24.9:
		print "Normal kroppsvekt fra 18,5 til 24,9"

	elif y >= 25 and y <= 29.9:
		print "Overvektig fra 25 til 29,9"

	elif y >= 30 and y <= 34.9:
		print "Fedme fra 30 til 34,9"

	elif y >= 35 and y <= 39.9:
		print "Fedme, klasse II fra 35 til 39,9"

	elif y >= 40:
		print "Fedme, klasse III (ekstrem fedme) > 40"


print "BMI Kalkulator"

vekt = float(raw_input("vekt(kg): "))
hoyde = float(raw_input("Hoyde(cm): "))

sum(vekt,hoyde)
