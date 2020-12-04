cnt = 0
for i in range(int(input())):
    word = input()
    cnt += list(word) == sorted(word, key=word.find) #발견하는 문자 순서대로 정렬
print(cnt)

