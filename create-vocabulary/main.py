out_file = open('vocabulary.txt', 'w')

while True:
	english_word = input("영어 단어를 입력하세요:")

	if(english_word == 'q'):
		break

	korean_work = input("한국어 뜻을 입력하세요:")

	out_file.write(f'{english_word}:{korean_work}\n')

out_file.close()
