# # 화면에 데이터 출력하기
# print(1 + 2)
#
# # 사용자로 부터 값 받기
# # 변수 활용
# name = input("당신의 이름은 무엇입니까? ")
# print("안녕하세요, " + name)
# # print("안녕" + "하세요")
#
#
#
#
# #
# import random
#
# rlist = [1,2,3,4,5]
# print(random.choice(rlist))

# 미니과제1
# class school() :
#     def __init__(self, iname, iyear, iaddr):
#         self.name = iname
#         self.year = iyear
#         self.addr = iaddr
#
#         print(name + year + addr)
#
# school('이름' ,'1988','주소는어디' )

#과제1 맛집고르기

# import random
#
# def recommand_food() :
#     lst_kfood = ['경복궁', '장금이', '본설', '김밥천국', '소한마리']
#     lst_cfood = ['홍콩반점', '백억원', '진짜루', '자금성','마라탕']
#     lst_jfood = ['스시마루', '오토코', '오카상', '사케사케', '하코네']
#
#     food_kind = input('1.한식, 2.중식, 3.일식 중 하나를 고르시오\n')
#
#     if food_kind == '1' or food_kind == '한식' :
#         print('오늘은 ' + random.choice(lst_kfood) + '에서 식사를 하시죠')
#
#     elif food_kind == '2' or food_kind == '중식':
#         print('오늘은 ' + random.choice(lst_cfood) + '에서 식사를 하시죠')
#
#     elif food_kind == '3' or food_kind == '일식':
#         print('오늘은 ' + random.choice(lst_jfood) + '에서 식사를 하시죠')
#
#     else :
#         print('보기 중 한 가지를 골라주세요.')
#         recommand_food()
#
# recommand_food()


#과제2 회사 조직도 만들기
# class People():
#     # grade = '대리'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Colleague(People):
#     def __init__(self, name, age, gender, grade):
#         super().__init__(name, age, gender)
#         self.grade = grade
#
#
# # name = input('이름을 입력하세요\n')
# # age = input('나이를 입력하세요\n')
# # gender = input('성별을 입력하세요\n')
#
# # people1 = people(name, age, gender)
# colleague = Colleague("Song",'2','F','대리')
# print(colleague.__dict__)


#과제3 가위 바위 보 게임
import  random
def game() :
    w_count = 0
    l_count = 0
    while True :
        com_result = random.randint(1,3)
        print(com_result)
        user_result = int(input("1.가위 2.바위 3.보"))
        if com_result == 1 :
            if user_result == 2 :
                w_count += 1
            elif user_result == 3 :
                l_count += 1
        elif com_result == 2 :
            if user_result == 1 :
                l_count += 1
            elif user_result == 3 :
                w_count += 1
        elif com_result == 3 :
            if user_result == 1 :
                w_count += 1
            elif user_result == 2 :
                l_count += 1
        if w_count == 3 or l_count :
            print(str(w_count) + " , " + str(l_count) )
            break

game()