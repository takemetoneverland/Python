
# 리스트를 이용한 간단한 연락처 관리 프로그램

# namelist에 이름, phonelist에 전화번호를 저장해서
# 이름과 전화번호 리스트의 인덱스가 동일하게 증가할 수 있도록 조작.

namelist = []
phonelist = []

while True:
    print('\n---------- 연락처 관리 프로그램 ----------')
    print('1. 연락처 등록')
    print('2. 연락처 검색')
    print('3. 연락처 삭제')
    print('4. 모든 연락처 조회')
    print('5. 프로그램 종료')
    print('------------------------------------------')

    menu = int(input('메뉴를 입력하세요: '))

    # pass: if문 비워져있을 때 에러나서 씀. 통과 키워드 나중에 지우면 됨
    if menu == 1:
        print('-' * 20)
        print('연락처 등록을 시작합니다.')
        name = input('이름: ')
        phone = input('전화번호: ')

        # 입력받은 이름과 전화번호 데이터를 각각의 리스트에 추가하세요.
        # 추가 완료 시 "XXX님 연락처 저장 완료!" 를 출력하세요.
        namelist.append(name)
        phonelist.append(phone)
        print(f'{name}님 연락처 저장 완료!')

    elif menu == 2:
        name = input('찾을 이름을 입력하세요: ')
        # 입력한 이름이 리스트 내부에서 발견된다면 해당 이름을 통해
        # 인덱스 번호를 추출하여 인덱스를 통해 리스트의 전화번호를 얻어옵니다.
        # 출력예시: "홍길동의 전화번호는 010-1234-5678입니다."
        if name in namelist:
            idx = namelist.index(name)
            print(f'{name}님의 전화번호는 {phonelist[idx]}입니다.')
        else:
            print(f'{name}님은 연락처 목록에 없습니다.')

    elif menu == 3:
        # 이름을 입력받아서 해당 이름과 전화번호를 동시에 삭제해 주세요.
        # 이름이 없다면 없다고도 얘기 해 주세요.
        name = input('삭제할 이름을 입력하세요: ')

        if name in namelist:
            idx = namelist.index(name)            
            del namelist[idx]
            del phonelist[idx]
            print(f'{name}님의 정보가 정상적으로 삭제되었습니다.')
        else:
            print(f'{name}님은 연락처 목록에 없습니다.')

    elif menu == 4:
        # for문을 통해 리스트 내부의 모든 인덱스에 접근하여 모든 이름과
        # 연락처 정보를 출력하는 코드를 작성합니다.
        # 홍길동 : 010-1234-5678
        # 김철수 : 010-5678-1234...
        
        # for name in namelist:
        #    print(f'{name} : {phonelist[phonelist.index(name)]}')

        for idx in range(len(namelist)):
            print(f'{namelist[idx]} : {phonelist[idx]}')

    elif menu == 5:
        print('프로그램을 종료합니다.')
        break # while True break
    else:
        print('메뉴를 다시 입력해 주세요.')