
'''
* 파일 입/출력

- 프로그램이 생성한 정보를 좀 더 오래 저장할 때는
파일에 기억해야 한다.

- 메모리는 속도는 빠르지만 전원이 끊어지면 정보를 잃어버릴 수
있기 때문에, 하드디스크에 저장해야 데이터를 오래 보관할 수
있다.

- 파일은 정보를 저장하는 기본 단위이며
문서, 이미지, 멀티미디어 자료도 모두 파일 형태로 보관할 수
있다.

- 파이썬에서는 파일 입/출력을 할 때
open()이라는 함수를 사용한다.
ex) open('파일 경로', 모드)

- 파일 경로는 입/출력 대상의 파일 경로이다.
디렉터리 경로를 포함시킵니다.

- 모드는 읽기, 쓰기, 추가 등 무엇을 할 지
결정하는 인수이다.

- 모드의 종류
1. r: 파일을 읽어들인다. 읽어들일 파일이 없으면
예외가 발생한다.

2. w: 파일에 데이터를 저장한다.
파일이 이미 존재한다면 덮어쓴다.

3. a: 파일에 데이터를 추가한다. (이미 존재하는 파일의 내용에 이어 붙임. \n으로 줄개행 필요함)
파일이 존재하지 않는다면 새롭게 생성도 해 준다. (w모드의 역할도 함)
'''

try:
    # 파일 저장 기능 (write, append)
    file_path = 'C:/test/test2.txt'

    # 파일 입출력을 실행하는 내장 함수 open()
    # 반환값으로 파일 입출력을 담당하는 객체를 리턴한다.
    # 첫번째 인수로 파일 경로를, 두번째 인수로 모드를 설정.
    f = open(file_path, 'a')

    text = 'a모드는 저장경로에 명시한 파일이 존재하지 않을 경우에는 하나 만들어 줍니다.'

    # 파일을 저장할 때는 f.write() 메서드를 사용한다.
    # 저장할 데이터를 인수로 전달한다.
    f.write(text)
    print('파일 저장 완료!')

except:
    print('파일 저장 실패!')
finally:
    # 파일 입출력은 하드디스크 자원을 사용하는 코드이므로
    # 반드시 사용 후 그 자원을 해제하여 메모리 누수를 방지한다.
    f.close()