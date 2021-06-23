import csv

#data start

raw_pixels = []

zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

#data end

#Read data

with open('C:\\Users\\hacky\\Python\\kaggle\\digit-recognizer\\train.csv', newline='') as csvfile:
    pixelreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in pixelreader:
        raw_pixels.append(row)

#print(raw_pixels[1])

#End read data

#Setup

def initialconditions():
    for i in range(783):
        zero.append(128)
        one.append(128)
        two.append(128)
        three.append(128)
        four.append(128)
        five.append(128)
        six.append(128)
        seven.append(128)
        eight.append(128)
        nine.append(128)

initialconditions()
print(len(zero))

#End setup

#Training

raw_pixels = raw_pixels[1:] #trimming headers

for pixel in raw_pixels:
    initlist = pixel[0]
    listdata = list(initlist.split(","))
    for i in range(len(listdata)):
        listdata[i] = int(listdata[i])
    #print(listdata)
    training(listdata[1:],listdata[0])

print(one)
print(two)
print(three)
print(four)
print(five)
#End training


