import math

def main():
	while True:
		a = float(input("Enter a number>0: "))
		if a>0:
			a=math.sqrt(a)
			with open('output.txt', 'w') as file:
				file.write(str(a))
				break
		else:
			print("Error. Enter number>0")
				
if __name__=="__main__":
	main()		
