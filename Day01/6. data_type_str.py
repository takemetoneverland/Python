
'''
* 문자열 (String)

- 단일 문자들을 따옴표('', "")로 감싸서
 나열한 문자 데이터의 집합형태이다.
- 따옴표 안에 어떤 형태의 데이터가 들어가도 문자로 인식.
- 전 세계의 모든 문자를 저장할 수 있고, 길이에도 제한이 없다. (파이썬3 utf-8 지원)
'''

# 나는 그에게 "도와줘!" 라고 말했다.
# 탈출문자를 적용해서(\) 따옴표를 문자로 표현할 수 있다.
s1 = "나는 그에게 \"도와줘!\" 라고 말했다."

# Let's get together!
s2 = 'Let\'s get together!'

file1 = 'C:\\temp\\new.jpg'
print(file1)

# 문자열 앞에 r이라는 접두어를 붙이면
# 해당 문자열은 탈출 문자를 적용하지 않는다.(raw char sequence)
file2 = r'C:\temp\new.jpg'
print(file2)

anthem = '''
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
'''
print(anthem)

# \를 문장 끝에 붙여주면 line continue 효과가 있다.
anthem2 = '''
동해물과 백두산이 마르고 닳도록 \
하느님이 보우하사 우리나라만세 \
무궁화 삼천리 화려강산 \
대한사람 대한으로 길이 보전하세
'''
print(anthem2)

'''
* 문자열 연산

- 파이썬은 문자열의 덧셈 연산과 곱셈 연산을 지원한다.
- 덧셈 연산은 문자열을 서로 연결하여 결합한다.
'''
s3 = '오늘 저녁은 '
s4 = '치킨입니다!'
print(s3 + s4 + ' 와 맛있겠다~')

'''
- 파이썬에서는 문자열의 곱셈 연산 또는 지원하고 있다.
- 곱셈 연산자 (*)로 문자열을 정해진 수 만큼 반복 연결한다.
'''

print('배고파' * 4)
print('-' * 30)

# print(s3 * 1.7) (x)
# print(s3 * s4) (x)