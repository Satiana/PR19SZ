firstLine    = ""
originalFile = "2013"
written = 0
with open(originalFile + ".csv", "r") as original, open(originalFile + "_1.csv", "a") as new1, open(originalFile + "_2.csv", "a") as new2, open(originalFile + "_3.csv", "a") as new3, open(originalFile + "_4.csv", "a") as new4, open(originalFile + "_5.csv", "a") as new5, open(originalFile + "_6.csv", "a") as new6, open(originalFile + "_7.csv", "a") as new7, open(originalFile + "_8.csv", "a") as new8, open(originalFile + "_9.csv", "a") as new9, open(originalFile + "_10.csv", "a") as new10, open(originalFile + "_11.csv", "a") as new11, open(originalFile + "_12.csv", "a") as new12:
    firstLine = original.readline()
    for line in original:
        splt = line.split(";")
        if len(splt) < 54:
            continue
            """
        try:
            dt = splt[2].split(".")
        except:
            continue
            """
        dt = splt[2].split(".")
        if dt[1] == "1":
            if written < 1:
                new1.write(firstLine)
                written += 1
            new1.write(line)
        elif dt[1] == "2":
            if written < 2:
                new2.write(firstLine)
                written += 1
            new2.write(line)
        elif dt[1] == "3":
            if written < 3:
                new3.write(firstLine)
                written += 1
            new3.write(line)
        elif dt[1] == "4":
            if written < 4:
                new4.write(firstLine)
                written += 1
            new4.write(line)
        elif dt[1] == "5":
            if written < 5:
                new5.write(firstLine)
                written += 1
            new5.write(line)
        elif dt[1] == "6":
            if written < 6:
                new6.write(firstLine)
                written += 1
            new6.write(line)
        elif dt[1] == "7":
            if written < 7:
                new7.write(firstLine)
                written += 1
            new7.write(line)
        elif dt[1] == "8":
            if written < 8:
                new8.write(firstLine)
                written += 1
            new8.write(line)
        elif dt[1] == "9":
            if written < 9:
                new9.write(firstLine)
                written += 1
            new9.write(line)
        elif dt[1] == "10":
            if written < 10:
                new10.write(firstLine)
                written += 1
            new10.write(line)
        elif dt[1] == "11":
            if written < 11:
                new11.write(firstLine)
                written += 1
            new11.write(line)
        else:
            if written < 12:
                new12.write(firstLine)
                written += 1
            new12.write(line)
    