out_file = open('./word-quiz/vocabulary.txt', 'r')

for line in out_file:
	data = line.strip().split(': ')
	user_answer = input(f'{data[1]}')
	if(user_answer == data[0]):
		print("맞았습니다!")
	else:
		print(f"아쉽습니다. 정답은 {data[0]}입니다.")

out_file.close()