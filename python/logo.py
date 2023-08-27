GSD_LOGO = """
 _____  _____ ______ 
|  __ \/  ___||  _  \\
| |  \/\ `--. | | | |
| | __  `--. \| | | |
| |_\ \/\__/ /| |/ / 
 \____/\____/ |___/                   
"""

CS_STUDY_LOGO = """
 _____  _____        _               _        
/  __ \/  ___|      | |             | |       
| /  \/\ `--.   ___ | |_  _   _   __| | _   _ 
| |     `--. \ / __|| __|| | | | / _` || | | |
| \__/\/\__/ / \__ \| |_ | |_| || (_| || |_| |
 \____/\____/  |___/ \__| \__,_| \__,_| \__, |
                                         __/ |
                                        |___/ 
"""

HOW_TO_USE = """
#################################################################
 발표할 타이틀을 한개씩 입력해주세요.
 맨 뒤에 "= 숫자"를 쓰면 그 숫자만큼 반복해서 생성합니다.
 ex) 데이터베이스 = 2 -> 데이터베이스(1/2), 데이터베이스(2/2)
 스터디 세팅 변경은 0을 입력해주세요
 챕터가 새로 시작되었다면 1을 입력해주세요
 임시 날짜 변경은 2를 입력해주세요
 중단하시려면 exit를 입력해주세요
#################################################################
"""

def logo():
    print(GSD_LOGO + "\n" + CS_STUDY_LOGO + "\n" + HOW_TO_USE)