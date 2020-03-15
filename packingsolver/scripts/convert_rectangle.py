import os
import os.path
import csv

def words(filename):
    f = open(os.path.join("data", "rectangle_raw", filename), "r")
    for line in f:
        for word in line.split():
            yield word

def write_dict(dic, filename):
    p = os.path.join("data", "rectangle", filename.replace(" ", "_"))
    d = os.path.dirname(p)
    if not os.path.exists(d):
        os.makedirs(d)
    print("Create " + p)
    f = open(p, "w")
    for i in range(-1, len(dic[next(iter(dic))])):
        if i == -1:
            f.write("ID")
        else:
            f.write(str(i))
        for k in dic.keys():
            if i == -1:
                f.write("," + k)
            else:
                f.write("," + str(dic[k][i]))
        f.write("\n")

################################################################################

def convert_generic(filename, s1 = "nwh", s2 = "whpc"):
    w = words(filename)

    bins = {"WIDTH": [], "HEIGHT": []}
    for c in s1:
        if c == 'n':
            itemtype_number = int(next(w))
        elif c == 'w':
            bins["WIDTH"].append(int(next(w)))
        elif c == 'h':
            bins["HEIGHT"].append(int(next(w)))
        elif c == 'x':
            next(w)
    write_dict(bins, filename + "_bins.csv")

    items = {}
    for c in s2:
        if c == 'w':
            items["WIDTH"] = []
        elif c == 'h':
            items["HEIGHT"] = []
        elif c == 'p':
            items["PROFIT"] = []
        elif c == 'c':
            items["COPIES"] = []
    for i in range(0, itemtype_number):
        for c in s2:
            if c == 'w':
                items["WIDTH"].append(int(next(w)))
            elif c == 'h':
                items["HEIGHT"].append(int(next(w)))
            elif c == 'p':
                items["PROFIT"].append(int(next(w)))
            elif c == 'c':
                items["COPIES"].append(int(next(w)))
            elif c == 'x':
                next(w)
    write_dict(items, filename + "_items.csv")

def convert_berkey1987(filename):
    w = words(filename)
    batches = []
    for instance_number in range(0, 50):
        bins = {"WIDTH": [], "HEIGHT": []}
        items = {"WIDTH": [], "HEIGHT": []}
        for _ in range(3):
            next(w)
        itemtype_number = int(next(w))
        for _ in range(3):
            next(w)
        instance_relative_number = int(next(w))
        for _ in range(7):
            next(w)
        bins["HEIGHT"].append(int(next(w)))
        bins["WIDTH"].append(int(next(w)))
        next(w)
        for i in range(0, itemtype_number):
            items["HEIGHT"].append(int(next(w)))
            items["WIDTH"].append(int(next(w)))
            if i == 0:
                next(w)
        suffix = "_" + str(itemtype_number) + "_" + str(instance_relative_number);
        write_dict(bins, filename + suffix + "_bins.csv")
        write_dict(items, filename + suffix + "_items.csv")

def convert_beasley2004(filename):
    w = words(filename)
    instance_number = int(next(w))
    for instance in range(0, instance_number):
        bins = {"WIDTH": [], "HEIGHT": []}
        items = {"WIDTH": [], "HEIGHT": [], "PROFIT": [], "COPIES": []}
        itemtype_number = int(next(w))
        bins["WIDTH"].append(int(next(w)))
        bins["HEIGHT"].append(int(next(w)))
        for i in range(0, itemtype_number):
            items["WIDTH"].append(int(next(w)))
            items["HEIGHT"].append(int(next(w)))
            next(w)
            items["COPIES"].append(int(next(w)))
            items["PROFIT"].append(int(next(w)))
        suffix = "_" + str(instance + 1);
        write_dict(bins, filename + suffix + "_bins.csv")
        write_dict(items, filename + suffix + "_items.csv")

def convert_cintra2008(filename):
    w = words(filename)

    bins = {"WIDTH": [], "HEIGHT": []}
    items = {"WIDTH": [], "HEIGHT": [], "COPIES": []}

    next(w)
    platetype_number = int(next(w))
    itemtype_number = int(next(w))

    for _ in range(3):
        next(w)

    bins["WIDTH"].append(int(next(w)))
    bins["HEIGHT"].append(int(next(w)))
    next(w)

    for _ in range(1, platetype_number):
        for _ in range(3):
            next(w)

    for i in range(0, itemtype_number):
        items["WIDTH"].append(int(next(w)))
        items["HEIGHT"].append(int(next(w)))
        items["COPIES"].append(int(next(w)))
        next(w)

    write_dict(bins, filename + "_bins.csv")
    write_dict(items, filename + "_items.csv")

def convert_roadef2018(filename):
    bins = {"WIDTH": [], "HEIGHT": []}
    for _ in range(100):
        bins["WIDTH"].append(6000)
        bins["HEIGHT"].append(3210)
    write_dict(bins, filename + "_bins.csv")

    with open(os.path.join("data", "rectangle_raw", filename + "_batch.csv"), newline='') as csvfile:
        items = {"WIDTH": [], "HEIGHT": [], "NEWSTACK": []}
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        first_line = True
        row_prec = None
        for row in spamreader:
            if first_line:
                first_line = False
                continue
            items["WIDTH"].append(int(row[1]))
            items["HEIGHT"].append(int(row[2]))
            if len(items["NEWSTACK"]) == 0:
                new_stack = True
            else:
                new_stack = (row_prec[3] != row[3])
            items["NEWSTACK"].append(int(new_stack))
            row_prec = row
        write_dict(items, filename + "_items.csv")

    with open(os.path.join("data", "rectangle_raw", filename + "_defects.csv"), newline='') as csvfile:
        defects = {"BIN": [], "X": [], "Y": [], "WIDTH": [], "HEIGHT": []}
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        first_line = True
        for row in spamreader:
            if first_line:
                first_line = False
                continue
            defects["BIN"].append(int(row[1]))
            defects["X"].append(int(float(row[2])))
            defects["Y"].append(int(float(row[3])))
            defects["WIDTH"].append(int(float(row[4])))
            defects["HEIGHT"].append(int(float(row[5])))
        write_dict(defects, filename + "_defects.csv")

def convert_martin2019b(filename):
    # Note: the files contain values for number of copies, but they are not
    # used in the corresponding paper.
    w = words(filename)
    items = []

    bins = {"WIDTH": [], "HEIGHT": []}
    bins["WIDTH"].append(int(next(w)))
    bins["HEIGHT"].append(int(next(w)))
    write_dict(bins, filename + "_bins.csv")
    itemtype_number = int(next(w))

    items = {"WIDTH": [], "HEIGHT": [], "COPIES": []}
    for i in range(0, itemtype_number):
        items["WIDTH"].append(int(next(w)))
        items["HEIGHT"].append(int(next(w)))
        items["PROFIT"].append(int(next(w)))
        int(next(w))
        write_dict(items, filename + "_items.csv")

    defect_number = int(next(w))
    defects = {"BIN": [], "X": [], "Y": [], "WIDTH": [], "HEIGHT": []}
    for i in range(0, defect_number):
        x1 = int(next(w))
        y1 = int(next(w))
        x2 = int(next(w))
        y2 = int(next(w))
        defects["BIN"].append(0)
        defects["X"].append(x1)
        defects["Y"].append(y1)
        defects["WIDTH"].append(x2 - x1)
        defects["HEIGHT"].append(y2 - y1)
    write_dict(defects, filename + "_defects.csv")

################################################################################

if __name__ == "__main__":

    convert_generic("herz1972/H", "whn", "wh")

    for f in ["christofides1977/cgcut" + str(i) + ".txt" for i in range(1, 4)]:
        convert_generic(f, "nwh", "whcp")

    for f in ["wang1983/" + i for i in ["WANG1", "WANG2", "WANG3"]]:
        convert_generic(f, "xnwh", "whc")
    convert_generic("wang1983/W", "whn", "whc")

    for f in ["beasley1985/gcut" + str(i) + ".txt" for i in range(1, 14)]:
        convert_generic(f, "nwh", "whp")

    for f in ["berkey1987/Class_" + "{:02d}".format(c) + ".2bp" for c in range(1, 7)]:
        convert_berkey1987(f)

    for f in ["oliveira1990/" + i for i in ["OF1", "OF2"]]:
        convert_generic(f, "whn", "whc")

    for f in ["tschoke1995/" + i for i in ["STS2", "STS4"]]:
        convert_generic(f, "whn", "whpc")
    for f in ["tschoke1995/" + i for i in ["STS2s", "STS4s"]]:
        convert_generic(f, "whn", "whc")

    for f in ["hadjiconstantinou1995/" + i for i in ["HADCHR3", "HADCHR11"]]:
        convert_generic(f, "whn", "whcp")

    for f in ["kroger1995/KR-" + "{:02d}".format(i) + ".txt" for i in range(1, 13)]:
        convert_generic(f, "whn", "wh")

    for f in ["jakobs1996/" + i for i in ["j1", "j2", "JAKOBS1", "JAKOBS2", "JAKOBS3", "JAKOBS4", "JAKOBS5"]]:
        convert_generic(f, "nwh", "wh")

    for f in ["fekete1997/okp" + str(i) for i in range(1, 6)]:
        convert_generic(f, "whn", "whpc")

    for f in ["lai1997/" + i for i in ["1", "2", "3"]]:
        convert_generic(f, "nwh", "wh")

    for f in ["hifi1997a/" + i for i in ["2", "3"]]:
        convert_generic(f, "whnx", "whpc")
    for f in ["hifi1997a/" + i for i in ["HH", "A1", "A2"]]:
        convert_generic(f, "whn", "whpc")
    for f in ["hifi1997a/" + i for i in ["2s", "3s"]]:
        convert_generic(f, "whnx", "whc")
    for f in ["hifi1997a/" + i for i in ["A1s", "A2s", "A3", "A4", "A5"]]:
        convert_generic(f, "whn", "whc")

    for f in ["hifi1997b/" + i for i in ["W1", "W2", "W3"]]:
        convert_generic(f, "whn", "whp")
    for f in ["hifi1997b/" + i for i in ["U1", "U2", "U3"]]:
        convert_generic(f, "whn", "wh")

    for f in ["fayard1998/CW" + str(i) for i in range(1, 12)]:
        convert_generic(f, "whn", "whpc")
    for f in ["fayard1998/CU" + str(i) for i in range(1, 12)]:
        convert_generic(f, "whn", "whc")

    for f in ["martello1998/Class_" + "{:02d}".format(c) + ".2bp" for c in range(7, 11)]:
        convert_berkey1987(f)

    for f in ["cung2000/" + i for i in ["CHL2", "CHL3", "CHL4"]]:
        convert_generic(f, "whn", "whpc")
    for f in ["cung2000/" + i for i in ["CHL1", "Hchl1", "Hchl2", "Hchl9"]]:
        convert_generic(f, "whnx", "whpc")
    for f in ["cung2000/" + i for i in ["CHL1s", "CHL2s", "CHL3s", "CHL4s", "CHL5", "CHL6", "CHL7"]]:
        convert_generic(f, "whn", "whc")
    for f in ["cung2000/" + i for i in ["Hchl3s", "Hchl4s", "Hchl5s", "Hchl6s", "Hchl7s", "Hchl8s"]]:
        convert_generic(f, "whnx", "whc")

    convert_generic("hifi2001/U4", "whn", "wh")
    convert_generic("hifi2001/W4", "whn", "whp")
    for f in ["hifi2001/" + i for i in ["MW1", "MW2", "MW3", "MW4", "MW5", "LW1", "LW2", "LW3", "LW4"]]:
        convert_generic(f, "whnx", "whp")
    for f in ["hifi2001/" + i for i in ["LU1", "LU2", "LU3", "LU4"]]:
        convert_generic(f, "whnx", "wh")

    for f in ["hopper2001a/C" + str(i) + "_" + str(j) for i in range(1, 8) for j in range(1, 4)]:
        convert_generic(f, "nwh", "wh")

    for f in ["alvarez2002/ATP3" + str(i) for i in range(0, 10)]:
        convert_generic(f, "whn", "whc")
    for f in ["alvarez2002/ATP4" + str(i) for i in range(0, 10)]:
        convert_generic(f, "whn", "whpc")

    for f in ["leung2003/" + i for i in ["P9", "P10"]]:
        convert_generic(f, "nwh", "wh")

    convert_beasley2004("beasley2004/ngcutap.txt")
    for f in ["beasley2004/ngcutfs" + str(i) + ".txt" for i in range(1, 4)]:
        convert_beasley2004(f)

    for f in ["imahori2005/" + a + b + c \
            for a in ["A", "B", "C", "D"] \
            for b in ["L", "S", "V"] \
            for c in ["X", "Y", "Z", "ZZ", "ZZZ"]]:
        convert_generic(f, "whn", "whc")

    for f in ["cui2008/" + str(i) for i in range(1, 21)]:
        convert_generic(f, "nwh", "whcxp")

    for f in ["cintra2008/gcut" + str(i) + "d.txt" for i in range(1, 13)]:
        convert_cintra2008(f)

    for f in ["morabito2010/random class " + str(c) + "/R_" + str(n) + "_" + t1 + "/" + str(i) + "_" + str(n) + "_100_" + t2 + ".dat" \
            for c in [1, 2, 3] for t1, t2 in [("S", "10_50"), ("L", "25_75")] \
            for n in [10, 20, 30, 40, 50] for i in range(1, 16)]:
        convert_generic(f, "nwh", "pwhc")

    for f in ["hifi2012/UL" + i + "H.txt" for i in ["1", "2", "3"]]:
        convert_generic(f, "whnxx", "whc")
    for f in ["hifi2012/WL" + i + "H.txt" for i in ["1", "2", "3"]]:
        convert_generic(f, "whnxx", "whpc")

    for wh in ["W500H1000", "W1000H2000"]:
        for n in [50, 100, 150]:
            for f in ["clautiaux2018/a/" + f.strip() \
                    for f in open("data/rectangle_raw/clautiaux2018/A_" + wh + "I" + str(n))]:
                convert_generic(f, "whn", "whpc")
            for f in ["clautiaux2018/p/" + f.strip() \
                    for f in open("data/rectangle_raw/clautiaux2018/P_" + wh + "I" + str(n))]:
                convert_generic(f, "whn", "whpc")

    for f in ["roadef2018/A" + str(i) for i in range(1, 21)]:
        convert_roadef2018(f)
    for f in ["roadef2018/B" + str(i) for i in range(1, 16)]:
        convert_roadef2018(f)
    for f in ["roadef2018/X" + str(i) for i in range(1, 16)]:
        convert_roadef2018(f)

    # for f in ["martin2019a/os" + o + "_is" + i + "_m" + m +  "_" + j \
            # for o in ["02", "06"]       for i in ["01", "02", "03", "04", "06", "07", "08", "11", "12", "16"] \
            # for m in ["10", "20", "40"] for j in ["01", "02", "03", "04", "05"]]:
        # convert_generic(f, "whn", "whc")
    # for f in ["martin2019b/inst_" + LW + "_" + str(m) + "_"  + str(rho) + "_" + str(i) + "_" + str(d)
            # for LW in ["75_75", "125_50", "150_150", "225_100", "300_300", "450_200"] \
            # for m in [5, 10, 15, 20, 25] for rho in [6, 8, 10] for i in range(1, 16) for d in [1, 2, 3, 4]]:
        # convert_martin2019b(f)

    for f in ["velasco2019/P" + str(cl) + "_" + str(l) + "_"  + str(h) + "_" + str(m) + "_" + str(i) + ".txt"
            for cl, l, h in [(1, 100, 200), (1, 100, 400), (2, 200, 100), (2, 400, 100), \
                             (3, 150, 150), (3, 250, 250), (4, 150, 150), (4, 250, 250)] \
            for m in [25, 50] for i in range(1, 6)]:
        convert_generic(f, "whn", "whpc")

    for f in ["wei2011/N/N" + str(i) + c + ".txt" for i in range(1, 8) for c in ["a", "b", "c", "d", "e"]]:
        convert_generic(f, "whn", "wh")
    for f in ["wei2011/T/T" + str(i) + c + ".txt" for i in range(1, 8) for c in ["a", "b", "c", "d", "e"]]:
        convert_generic(f, "whn", "wh")
    for f in ["wei2011/C/lw" + str(i) + ".txt" for i in [ \
            161, 163, 172, 251, 252, 253, 281, 283, 292, 491, 492, 493, \
            731, 732, 733, 971, 972, 973, 1961, 1963, 1972]]:
        convert_generic(f, "whn", "wh")
    for f in ["wei2011/Burke/n" + str(i) + ".txt" for i in range(1, 14)]:
        convert_generic(f, "whn", "wh")
