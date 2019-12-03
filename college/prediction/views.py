from django.shortcuts import render
# from django import 
from django.http import HttpResponse
from .models import Predict_list
import numpy as np




# Create your views here.


def Test(request):
    # return HttpResponse("Hello, world!")
    return render(request, 'predictionView.html')

def posttest(request):
    # print(request.POST['college'])
    # print(request.POST['major'])
    # print(request.POST['korean'])
    # print(request.POST['math'])
    # print(request.POST['math_select'])
    # print(request.POST['English'])
    # print(request.POST['research_select'])
    # print(request.POST['research1'])
    # print(request.POST['research2'])
    # print(request.POST['history'])
    # print(type(request.POST['korean']))

    data = Predict_list.objects.get(college_name=request.POST['college'], major_name=request.POST['major'])
    print('pk='+str(data.pk))
    result = 900

    arr_grade = [
        int(request.POST['korean']),
        int(request.POST['math']),
        int(request.POST['math_select']),
        int(request.POST['English']),
        int(request.POST['research_select']),
        int(request.POST['research1']),
        int(request.POST['research2']),
        int(request.POST['history']),
    ]

    class GradeAnalysis():
        grade = np.array([])
        pk = 0
        natural_sc = True

        def setGrade(self, data, pk):
            self.grade = np.copy(data)
            self.pk = pk

        def EngPoint(self):  # 영어 점수 변환
            g = self.grade[3]
            if self.pk == 1:
                if self.natural_sc:
                    self.grade[3] = 100
                elif g == 2:
                    self.grade[3] = 97
                elif g == 3:
                    self.grade[3] = 92
                elif g == 4:
                    self.grade[3] = 86
                elif g == 5:
                    self.grade[3] = 75
                elif g == 6:
                    self.grade[3] = 64
                elif g == 7:
                    self.grade[3] = 58
                elif g == 8:
                    self.grade[3] = 53
                elif g == 9:
                    self.grade[3] = 50

            else:
                if g == 1:
                    self.grade[3] = 100
                elif g == 2:
                    self.grade[3] = 98
                elif g == 3:
                    self.grade[3] = 95
                elif g == 4:
                    self.grade[3] = 92
                elif g == 5:
                    self.grade[3] = 86
                elif g == 6:
                    self.grade[3] = 75
                elif g == 7:
                    self.grade[3] = 64
                elif g == 8:
                    self.grade[3] = 58
                elif g == 9:
                    self.grade[3] = 50

        def HisPoint(self):  # 한국사 점수 변환
            history = self.grade[7]
            if history >= 4:
                self.grade[7] = 10
            else:
                self.grade[7] = 14 - history

        def percentile(self):
            pass

        def caculate_NaturalSciences(self):  # 0:국어 1:수학 2:탐구1 3: 탐구2 4:영어 5:한국사
            # self.grade[3] = round(grade[0]*1.25,3) + round(grade[1]*2.0,3) + round((grade[2]+grade[3])*1.75,3) + self.EngPoint(grade, 0) + self.HisPoint(grade)
            pass

        def caculate_LiberalArts(self):
            # self.grade[3] = round(grade[0]*2.0,3) + round(grade[1]*2.0,3) + (grade[2]+grade[3]) +self.EngPoint(grade, 1) + self.HisPoint(grade)
            pass

        def advantage_science(self):  # 과탐가산점
            pass

        def advantage_math(self):  # 수학 가형 가산점
            pass

    class SKKU(GradeAnalysis):
        natural_sc = [3]
        liberal_arts = []

        def caculate_NaturalSciences(self):
            # print(self.grade)
            print(self.grade)
            arr = np.delete(self.grade, 4)
            arr = np.delete(arr, 2)

            tmp = arr[3] + arr[4]
            arr = np.delete(arr, 4)
            arr[3] = tmp
            print(arr)

            arr = arr * np.array([1.25, 2.0, 1, 1.75, 1])  # 국 수 영 탐 한국사
            print(arr)
            np.around(arr, 2)
            return np.sum(arr)

        def caculate_LiberalArts(self):
            print(self.grade)
            arr = np.delete(self.grade, 4)
            arr = np.delete(arr, 2)

            tmp = arr[3] + arr[4]
            arr = np.delete(arr, 4)
            arr[3] = tmp
            print(arr)

            arr = arr * np.array([2.0, 2.0, 1, 1, 1])
            print(arr)
            np.around(arr, 2)
            return np.sum(arr)

        def percentile(self, pk):  # pk1 = 과탐 pk2 = 사탐
            # tmp = self.grade[5]
            if pk:
                self.grade[5] += 4
                self.grade[6] += 4
            else:
                self.grade[5] += 1
                self.grade[6] += 1

        def advantage_math(self):
            tmp = self.grade[1]
            if tmp >= 130:
                self.grade[1] = tmp + 6
            elif tmp >= 127:
                self.grade[1] = tmp + 5
            elif tmp >= 125:
                self.grade[1] = tmp + 4
            elif tmp == 124:
                self.grade[1] = 127.85
            elif tmp == 123:
                self.grade[1] = 126.51
            elif tmp == 122:
                self.grade[1] = 124.75
            elif tmp == 121:
                self.grade[1] = 124.55
            elif tmp == 120:
                self.grade[1] = 124.33
            elif tmp == 119:
                self.grade[1] = 122.5
            elif tmp == 118:
                self.grade[1] = 121
            elif tmp == 117:
                self.grade[1] = 120
            elif tmp == 116:
                self.grade[1] = 118
            elif tmp == 115:
                self.grade[1] = 116
            elif tmp == 114:
                self.grade[1] = 115.5
            elif tmp == 113:
                self.grade[1] = 115
            elif tmp == 112:
                self.grade[1] = 113
            elif tmp == 111:
                self.grade[1] = 110.5
            elif tmp >= 109:
                self.grade[1] = tmp - 2
            elif tmp >= 106:
                self.grade[1] = tmp - 3

    SKKU = SKKU()
    pk_index = data.pk

    # print(pk_index in SKKU.natural_sc)

    if pk_index in SKKU.natural_sc:
        SKKU.setGrade(arr_grade, 1)
        SKKU.percentile(1)
        SKKU.EngPoint()
        SKKU.HisPoint()
        result = SKKU.caculate_NaturalSciences()  # 이과
    else:
        SKKU.setGrade(arr_grade, 0)
        SKKU.percentile(0)
        if SKKU.grade[2] == 1:
            SKKU.advantage_math()
        SKKU.EngPoint()
        SKKU.HisPoint()
        result = SKKU.caculate_LiberalArts()  # 문과



    # pk_index = data.pk





    context = {
        'result': result,
        'college': data.as_dict()
    }

    return render(request, 'resultView.html', context)


def ModelToDict(request):
    all_list = Predict_list.objects.all()
    # return render(request, 'predictionView.html',{'list':[item.as_dict() for item in list]})
    item_list = [item.as_dict() for item in all_list]
    filter_item = []
    for item in item_list:
        tmp = list(filter(lambda x: x['college_name'] == item['college_name'], filter_item))
        if len(tmp) == 0:
            filter_item.append(item)
    print(filter_item)
    return render(request, 'predictionView.html', {'filter_list': filter_item, 'list': item_list})
