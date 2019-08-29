#작은 따옴표와 큰 따옴표는 차이가 없음
#하지만 쓰는 상황에 따라 적ㅈㄹ한 따옴표는 존재 ex)인용
#따옴표 세개는 긴글을 쓸 때 유용 + 따옴표 사용시 유용

string1 = '이것은 문자열'
string2 = '얘도 문자열'
string3 = '{}도, {}도, 지금도 문자열'.format(string1, string2)

print(string1, string2, string3)

quote = '나는 "직접인용한다"'
emphasize = "'문법검사기'를 인용하다고?"
# error = "엄마 친구아들이 "파이썬 좋아"라고 했대"

long_string = """이렇게
하면
되지롱"""
print(long_string)
