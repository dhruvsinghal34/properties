import random
import csv
import plotly.figure_factory as ff
import statistics as s
student_list=[]
count=[]
for i in range(0,100):
    reading = random.randint(1,100)
    writing = random.randint(1,100)
    maths = random.randint(1,100)
    marks = reading+writing+maths
    student_list.append(marks)
    count.append(i)

#print(student_list)
fiqure = ff.create_distplot([student_list],["Student Result"])
fiqure.show()
 
Mean = s.mean(student_list)
print("Mean is " + str(Mean))

Median = s.median(student_list)
print("Median is" + str(Median))

Mode = s.mode(student_list)
print("Mode is " + str(Mode))

StandardDeviation = s.stdev(student_list)
print("Standard Deviation is " + str(StandardDeviation))

firstleftStandardDeviation = Mean - StandardDeviation
print("Left Standard Deviation is " + str(firstleftStandardDeviation))

firstrightStandardDeviation = Mean + StandardDeviation
print("right Standard Deviation is" + str(firstrightStandardDeviation))

secondLeftStandardDeviation , SecondRightStandardDeviation =    Mean - 2*StandardDeviation , Mean + 2*StandardDeviation
print("SecondLeftStandardDeviation is " + str(secondLeftStandardDeviation))
print("SecondRightStandardDeviation is " + str(SecondRightStandardDeviation))

thirdLeftStandardDeviation , thirdRightStandardDeviation = Mean - 3*StandardDeviation , Mean + 3*StandardDeviation
print("thirdLeftStandardDeviation is " + str(thirdLeftStandardDeviation))
print("thirdRightStandardDeviation is " + str(thirdRightStandardDeviation))

listOfdatawithinfirststdev = []

for i in student_list:
    if i > firstleftStandardDeviation and i < firstrightStandardDeviation:
        listOfdatawithinfirststdev.append(i)


listOfdatawithinsecondstdev = []

for i in student_list:
    if i > secondLeftStandardDeviation and i < SecondRightStandardDeviation:
        listOfdatawithinsecondstdev.append(i)

listOfdatawithinthirdstdev = []

for i in student_list:
    if i > thirdLeftStandardDeviation and i < thirdRightStandardDeviation:
        listOfdatawithinthirdstdev .append(i)

percent = len(listOfdatawithinfirststdev) / len(student_list) * 100
print("the percentage of data lies in first standard Deviation " + str(percent))

percent2 = len(listOfdatawithinsecondstdev) / len(student_list) * 100
print("the percentage of data lies in second standard Deviation " + str(percent2))

percent3 = len(listOfdatawithinthirdstdev) / len(student_list) * 100
print("the percentage of data lies in second standard Deviation " + str(percent2))

