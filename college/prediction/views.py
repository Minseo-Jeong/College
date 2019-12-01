from django.shortcuts import render

# Create your views here.

'''
class 대학이니셜():

    caculate_list_1 = [] 
    caculate_list_2 = []
    caculate_list_3 = []
    caculate_list_4 = [] # 계산식이 같은 학과 리스트
    
    def major_caculate(list, math_select, disquisition_slect, major):
        if major in(caculate_list_1):
            _MATH_SELECT = 1 # 0, 1, 2 // 0=only 나형 1=only 가형 2=중복
            _DISQUISITION_SELECT = 0, 1, 2 // 0=only 사탐 1=only 과탐 2=중복

        else if major in(caculate_list_1):

        else if major in(caculate_list_2):

        else if major in(caculate_list_3):

    
    

def caculate(list, math_select, disquisition_slect, major):

    #매개 변수
    list = 성적리스트 국 영 수 탐1 탐2 영어 한국사   # Type = list
    math_select = 수학 선택 과목 True = 가형, False = 나형   # Type = boolean
    disquisition_slect = 탐구 선택 과목 True = 과탐, False = 사탐  
    major = 학과 식별 번호

    # 가산점 및 반영 비율을 반영하여 계산한 값 반환
    if major == 0:
        if math_select:

            if disquisition_select:
                # 가형 + 과탐
                
            else:
                # 가형 + 사탐

        else:

            if disquisition_select:
                # 나형 + 과탐

            else:
                # 나형 + 사탐
    
    elif major == 1:
        
return result
'''
class GradeAnalysis():

    def setGrade(*grade,):


    def EngPoint(self, grade, NS_LA): #영어 점수 변환
        g = grade[4]
        if NS_LA:
            if g == 1:
                return 100
            elif g == 2:
                return 97
            elif g == 3:
                return 92
            elif g == 4:
                return 86
            elif g == 5:
                return 75
            elif g == 6:
                return 64
            elif g == 7:
                return 58
            elif g == 8:
                return 53
            elif g == 9:
                return 50  

        else:
            if g == 1:
                return 100
            elif g == 2:
                return 98
            elif g == 3:
                return 95
            elif g == 4:
                return 92
            elif g == 5:
                return 86
            elif g == 6:
                return 75
            elif g == 7:
                return 64
            elif g == 8:
                return 58
            elif g == 9:
                return 50
    
    def HisPoint(self, grade): #한국사 점수 변환
        g = grade[5]

        if g >= 4:
            return 10
        else:
            return 14-g

    def Caculate_NaturalSciences(self, grade): # 0:국어 1:수학 2:탐구1 3: 탐구2 4:영어 5:한국사
        return round(grade[0]*1.25,3) + round(grade[1]*2.0,3) + round((grade[2]+grade[3])*1.75,3) + self.EngPoint(grade, 0) + self.HisPoint(grade)

    def Caculate_LiberalArts(self, grade): 
        return round(grade[0]*2.0,3) + round(grade[1]*2.0,3) + (grade[2]+grade[3]) +self.EngPoint(grade, 1) + self.HisPoint(grade)



