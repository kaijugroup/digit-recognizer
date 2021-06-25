import csv
import math
import Train

#data start

trainpixels = []
testpixels = []

#data end

#Read data

with open('train.csv', newline='') as trainfile:
    trainreader = csv.reader(trainfile, delimiter=' ', quotechar='|')
    for row in trainreader:
        trainpixels.append(row)

trainfile.close()

with open('test.csv', newline='') as testfile:
    testreader = csv.reader(testfile, delimiter=' ', quotechar='|')
    for row in testreader:
        testpixels.append(row)

testfile.close()

#End read data

#Setup

initial = []

def ensurefloat(l):
    newl = []
    for i in l:
        try:
            newi = float(i)
        except:
            print("Invalid float: "+i)
            print("Index of error:"+len(newl)+1)
            break

        newl.append(newi)
    return(newl)

def initialconditions():
    for i in range(784):
        initial.append(128)

initialconditions()

zero = Train.Train()
zero.build(initial)
one = Train.Train()
one.build(initial)
two = Train.Train()
two.build(initial)
three = Train.Train()
three.build(initial)
four = Train.Train()
four.build(initial)
five = Train.Train()
five.build(initial)
six = Train.Train()
six.build(initial)
seven = Train.Train()
seven.build(initial)
eight = Train.Train()
eight.build(initial)
nine = Train.Train()
nine.build(initial)

#End setup

#Training

raw_pixels = raw_pixels[1:] #trimming headers

for i in raw_pixels:
    pixels = i[0].split(",")
    pixels = ensurefloat(pixels)
    ans = pixels[0]
    data = pixels[1:]

    if ans==0:
        zero.train(data)
    elif ans==1:
        one.train(data)
    elif ans==2:
        two.train(data)
    elif ans==3:
        three.train(data)
    elif ans==4:
        four.train(data)
    elif ans==5:
        five.train(data)
    elif ans==6:
        six.train(data)
    elif ans==7:
        seven.train(data)
    elif ans==8:
        eight.train(data)
    elif ans==9:
        nine.train(data)
    else:
        print("Invalid data detected: "+ans)

print(zero.reportstate())
#End training

#Start testing

#End testing

