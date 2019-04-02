from glob import glob
from csv import DictReader
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy

path = ".\\Podatki"

files = [f for f in glob(path + "**/*.csv")]

readers = []

date             = []

for fl in files:
    date.append(fl.split("\\")[2].split(".")[0])
    reader = DictReader((x.replace("\0", "") for x in open(fl, "rt", encoding="latin-1")), delimiter=";")
    readers.append(reader)
    
averageMalePow   = []
averageFemalePow = []

femalePow     = []
femalePowDate = []

malePow     = []
malePowDate = []

numOfMaleCarUsers   = []
numOfFemaleCarUsers = []

numOfMaleCarUsersPerBrand   = []
numOfFemaleCarUsersPerBrand = []

interestingBrands = ["AUDI", "PEUGEOT", "VOLKSWAGEN", "BMW"]


for reader in readers:
    sumMalePow = 0
    sumFemalePow = 0
    counterMale = 0
    counterFemale = 0

    maleCarUsersPerBrand   = defaultdict(int)
    femaleCarUsersPerBrand = defaultdict(int)

    for row in reader:
        try:
            if row["C-Spol uporabnika (ce gre za fizicno osebo)"] == "M":
                mp = float(row["P.1.2-Nazivna moc"].replace(",", "."))
                sumMalePow += mp
                maleCarUsersPerBrand[row["D.1-Znamka"]] += 1
                if mp < 700:
                    malePow.append(mp)
                    dt = row["2A-Datum prve registracije vozila v SLO"].strip("\"").split(".")
                    malePowDate.append(int(dt[0]) + int(dt[1]) * 30 + int(dt[2]) * 365)
                counterMale += 1
            elif row["C-Spol uporabnika (ce gre za fizicno osebo)"] == "Z":
                mp = float(row["P.1.2-Nazivna moc"].replace(",", "."))
                sumFemalePow += mp
                femaleCarUsersPerBrand[row["D.1-Znamka"]] += 1
                if mp < 700:
                    femalePow.append(mp)
                    dt = row["2A-Datum prve registracije vozila v SLO"].strip("\"").split(".")
                    femalePowDate.append(int(dt[0]) + int(dt[1]) * 30 + int(dt[2]) * 365)
                counterFemale += 1
        except:
            if row["Spol uporabnika"] == "M":
                mp = float(row["NajveCja neto moC"].replace(",", "."))
                sumMalePow += mp
                maleCarUsersPerBrand[row["Znamka"]] += 1
                if mp < 700:
                    malePow.append(mp)
                    dt = row["Datum prve registracije Slo"].strip("\"").split(".")
                    malePowDate.append(int(dt[0]) + int(dt[1]) * 30 + int(dt[2]) * 365)
                counterMale += 1
            elif row["Spol uporabnika"] == "C":
                mp = float(row["NajveCja neto moC"].replace(",", "."))
                sumFemalePow += mp
                femaleCarUsersPerBrand[row["Znamka"]] += 1
                if mp < 700:
                    femalePow.append(mp)
                    dt = row["Datum prve registracije Slo"].strip("\"").split(".")
                    femalePowDate.append(int(dt[0]) + int(dt[1]) * 30 + int(dt[2]) * 365)
                counterFemale += 1

    averageMalePow.append(sumMalePow/counterMale)
    averageFemalePow.append(sumFemalePow/counterFemale)

    if len(numOfMaleCarUsers) == 0:
        numOfMaleCarUsers.append(counterMale)
        numOfFemaleCarUsers.append(counterFemale)
    else:
        numOfMaleCarUsers.append(numOfMaleCarUsers[len(numOfMaleCarUsers)-1] + counterMale)
        numOfFemaleCarUsers.append(numOfFemaleCarUsers[len(numOfFemaleCarUsers)-1] + counterFemale)
    
    numOfFemaleCarUsersPerBrand.append(femaleCarUsersPerBrand)
    numOfMaleCarUsersPerBrand.append(maleCarUsersPerBrand)

"""
for i in range(len(numOfFemaleCarUsersPerBrand)):
    keys = []
    for key, value in numOfFemaleCarUsersPerBrand[i].items():
        if value < 10:
            keys.append(key)
    for key in keys:
        numOfFemaleCarUsersPerBrand[i].pop(key)
    keys = []
    for key, value in numOfMaleCarUsersPerBrand[i].items():
        if value < 10:
            keys.append(key)
    for key in keys:
        numOfMaleCarUsersPerBrand[i].pop(key)
"""

datesToUse = [date[x] for x in range(len(date)) if x%6 == 0]
ticks = [x*6 for x in range(len(datesToUse))]

plt.figure()
plt.title("Mesecna povprecja moci motorjev")
plt.plot(averageFemalePow)
plt.plot(averageMalePow)
plt.legend(["Zenske", "Moski"])
plt.xticks(ticks)
plt.gca().set_xticklabels(datesToUse, rotation=45)
plt.ylabel("Moc motorja")
plt.xlabel("Datum")
plt.show()

yearlyAverageMalePow   = []
yearlyAverageFemalePow = []
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018"]

for i in range(len(years)):
    temp1 = 0
    temp2 = 0
    for j in range(12):
        temp1 += averageMalePow[i*12+j]
        temp2 += averageFemalePow[i*12+j]
    yearlyAverageMalePow.append(temp1/12)
    yearlyAverageFemalePow.append(temp2/12)

ticks = range(len(years))

plt.figure()
plt.title("Letna povprecja moci motorjev")
plt.plot(yearlyAverageFemalePow)
plt.plot(yearlyAverageMalePow)
plt.legend(["Zenske", "Moski"])
plt.xticks(ticks)
plt.gca().set_xticklabels(years, rotation=45)
plt.ylabel("Moc motorja")
plt.xlabel("Leto")
plt.show()

plt.figure()
plt.plot(malePowDate, malePow, "b.")
plt.plot(femalePowDate, femalePow, "r.")
plt.show()

ticks = [x*6 for x in range(len(datesToUse))]

plt.figure()
plt.title("Stevilo novih uporabnikov avtomobilo (kumulativno)")
plt.plot(numOfFemaleCarUsers)
plt.plot(numOfMaleCarUsers)
plt.plot([numOfMaleCarUsers[x] - numOfFemaleCarUsers[x] for x in range(len(numOfMaleCarUsers))])
plt.legend(["Zenske", "Moski", "Razlika"])
plt.xticks(ticks)
plt.gca().set_xticklabels(datesToUse, rotation=45)
plt.ylabel("Stevilo uporabnikov")
plt.xlabel("Datum")
plt.show()

"""
for x in numOfFemaleCarUsersPerBrand:
    print(x)
"""



"""
fl = open("Podatki/2014_1.csv", "rt", encoding="latin-1")
myCsv = (x.replace("\0", "") for x in fl)
"""

"""
allLines = []

fl = open(files[0], "r")
allLines.append(fl.readline())
fl.close()

for f in files:
    print(f)
    fl = open(f, "r", encoding="latin-1")
    fl.readline()
    for line in fl:
        if len(line.split(";")) < 54:
            continue
        allLines.append(line)

fl = open("cela.csv", "a", encoding="latin-1")
for line in allLines:
    fl.write(line)
"""