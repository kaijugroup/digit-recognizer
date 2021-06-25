import csv
import math
import Train

#data start

raw_pixels = []

#data end

#Read data

with open('C:\\Users\\hacky\\Python\\kaggle\\digit-recognizer\\train.csv', newline='') as csvfile:
    pixelreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in pixelreader:
        raw_pixels.append(row)

#print(raw_pixels[1])

#End read data

#Setup

initial = []

def ensureint(l):
    newl = []
    for i in l:
        try:
            newi = int(i)
        except:
            print("Invalid integer: "+i)
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
    pixels = ensureint(pixels)
    ans = int(pixels[0])
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


