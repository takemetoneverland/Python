
'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''
file_path = 'C:/test/points.txt'

try:
    f = open(file_path, 'r')
    text = f.read()
    # print(text)
except:
    print('파일 로드 실패!')
finally:
    f.close() # 파일 읽기 끝

list = text.split() # 텍스트를 리스트에 넣기
# print(list)

# 리스트의 자료는 str이므로 연산을 위해 숫자형으로 형변환
points = [] 
for l in list:
    points.append(int(l))
# print(points)

# 총점 구하기
total = 0
for p in points:
    total += p
# print(total)

# 평균 구하기
avg = total / len(points)

# 저장할 텍스트
# print(f'총점: {total}, 평균: {avg:0.1f}')
result = f'총점: {total}, 평균: {avg:0.1f}'

# result.txt 파일에 저장
new_path = 'C:/test/result.txt'
try:
    f = open(new_path, 'w')
    f.write(result)
    print('파일 저장 성공!')
except:
    print('파일 저장 실패!')
finally:
    f.close()