# import theater_module
    
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 영화 보러 갔을 때
# theater_module.price_soldier(5) # 군인 5명

# import theater_module as mv # as뒤에 변수선언 하듯이 약어 설정 가능

# mv.price_soldier(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # 다 사용하겠다.
# from random import *

# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price, price_morning
from travel import thailand
price(5)
price_morning(6)
#price_soldier(6) 오류쓰

from theater_module import price_soldier as price
price(5)

# 패키지
# travel 패키지 확인
# import travel.thailand #이렇게 임포트 뒤에 바로 쓰는건 패키지나 모듈만 가능하다 위랑 비교해봐. from ~ import 구문은 가능
# from travel.thailand import ThailandPackage << 요건 가능해
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detaiil()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

from travel import *  #<<오류난다. 왜냐하면 개발자가 문법상에서 공개범위를 설정을 안했기 때문. import 될 것만 공개할 수 있음. __init__.py 설정해줘서 오류 안남
#trip_to3 = vietnam.VietnamPackage()
trip_to3 = thailand.ThailandPackage()
trip_to3.detail()

# 모듈 직접 실행 타일랜드.py 참고

# 패키지, 모듈 위치 파이썬 lib 경로 혹은 같은 폴더(같은 패키지)안에 있으면 사용가능하다.

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# pip install

# pypi 검색
# 터미널에서 pip install 패키지이름
# pip list <현재 설치된 패키지 확인
# pip show 패키지 < 패키지 정보를 알려줌
# pip intall --upgrade 패키지 <<업그레이드
# pip uninstall 패키지 << 삭제

# 내장함수 <list of python builtins 검색
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir()) < 현재쓸 수 있는 패키지 등등
# import pickle
# print(dir()) <피클 추가됨
# print(dir(random)) < 랜덤에서 뭐 쓸 수 있는지
# lst = [1, 2, 3]
# print(dir(lst))  
# name = "Jim"
# print(dir(name))

# 외장함수

# list of python modules 검색
# glob : 경로 내의 폴더 / 파일 목록 조회(dir 명령어와 같음)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일
# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리 표시
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir()) # 글롭이랑 비슷함
# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M;%S"))
import datetime
# print("오늘 날짜는",datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난 지 100일은",today+td) #오늘부터 100일 후


