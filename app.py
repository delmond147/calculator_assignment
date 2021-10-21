def calculator():
	name = str(input('Enter your name: '))
	print(f'''
		WELCOME TO CALCULATOR {name} .... ENJOY!
		''')
	print('Choose a shape to compute it\'s area')
	print('1. Circle')
	print('2. Rectangle')
	print('3. Square\n')

	while True:
		choice = int(input('Reply with your choice: \n'))
		if choice == 1:
			pi = 3.142
			r = int(input('Enter the radius: '))
			circle = pi*r**2
			print(circle)
			print(f'Thank you {name} for using calculator.\n')
		elif choice == 2:
			length = int(input('Enter the length: '))
			width = int(input('Enter the width: '))
			rect = length*width
			print(rect)
			print(f'Thank you {name} for using calculator.\n')
		elif choice == 3:
			side = int(input('Enter the side: '))
			sqaure = side*side
			print(sqaure)
			print(f'Thank you {name} for using calculator.\n')
		else:
			print(f'I did\'t understand your command {name}')
			print(f'Thank you {name} for using calculator.\n')

if __name__ == '__main__':
	calculator()

