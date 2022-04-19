in_file = open('data-analysis/chicken.txt', 'r')

for line in in_file:
	print(line.strip())

in_file.close()