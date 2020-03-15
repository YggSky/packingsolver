import sys
import os
import os.path
import json

################################################################################

datas = {}

datas["roadef2018_A"] = ["roadef2018/A" + str(i) for i in range(1, 21)]
datas["roadef2018_B"] = ["roadef2018/B" + str(i) for i in range(1, 16)]
datas["roadef2018_X"] = ["roadef2018/X" + str(i) for i in range(1, 16)]

datas["christofides1977"] = ["christofides1977/cgcut" + str(i) + ".txt" for i in range(1, 4)]

datas["wang1983"] = ["wang1983/" + i for i in ["WANG1", "WANG2", "WANG3", "W"]]

datas["beasley1985"] = ["beasley1985/gcut" + str(i) + ".txt" for i in range(1, 14)]

datas["berkey1987"] = ["berkey1987/Class_" + "{:02d}".format(c) + ".2bp_" + str(n) + "_" + str(i) \
        for c in range(1, 7) \
        for n in [20, 40, 60, 80, 100] \
        for i in range(1, 11)]

datas["oliveira1990"] = ["oliveira1990/" + i for i in ["OF1", "OF2"]]

datas["tschoke1995_cw"] = ["tschoke1995/" + i for i in ["STS2", "STS4"]]
datas["tschoke1995_cu"] = ["tschoke1995/" + i for i in ["STS2s", "STS4s"]]

datas["hadjiconstantinou1995"] = ["hadjiconstantinou1995/" + i for i in ["HADCHR3", "HADCHR11"]]

datas["kroger1995"] = ["kroger1995/KR-" + "{:02d}".format(i) + ".txt" for i in range(1, 13)]

datas["jakobs1996"] = ["jakobs1996/" + i for i in ["j1", "j2", "JAKOBS1", "JAKOBS2", "JAKOBS3", "JAKOBS4", "JAKOBS5"]]

datas["fekete1997"] =  ["fekete1997/okp" + str(i) for i in range(1, 6)]

datas["lai1997"] = ["lai1997/" + i for i in ["1", "2", "3"]]

datas["hifi1997a_cw"] = ["hifi1997a/" + i for i in ["2", "3", "A1", "A2"]]
datas["hifi1997a_cu"] = ["hifi1997a/" + i for i in ["2s", "3s", "A1s", "A2s", "A3", "A4", "A5", "HH"]]

datas["fayard1998_cw"] = ["fayard1998/CW" + str(i) for i in range(1, 12)]
datas["fayard1998_cu"] = ["fayard1998/CU" + str(i) for i in range(1, 12)]

datas["martello1998"] = ["martello1998/Class_" + "{:02d}".format(c) + ".2bp_" + str(n) + "_" + str(i) \
        for c in range(7, 11) \
        for n in [20, 40, 60, 80, 100] \
        for i in range(1, 11)]

datas["cung2000_cw"] = ["cung2000/" + i for i in ["CHL1", "CHL2", "CHL3", "CHL4",
    "Hchl1", "Hchl2", "Hchl9"]]
datas["cung2000_cu"] = ["cung2000/" + i for i in ["CHL1s", "CHL2s", "CHL3s", "CHL4s",
    "CHL5", "CHL6", "CHL7", "Hchl3s", "Hchl4s", "Hchl5s", "Hchl6s", "Hchl7s", "Hchl8s"]]

datas["hifi2001_cu"] = ["hifi2001/" + i for i in ["U4", "LU1", "LU2", "LU3", "LU4"]]
datas["hifi2001_cw"] = ["hifi2001/" + i for i in ["W4", "MW1", "MW2", "MW3", "MW4", "MW5", "LW1", "LW2", "LW3", "LW4"]]

datas["hopper2001a"] = ["hopper2001a/C" + str(i) + "_" + str(j) \
        for i in range(1, 8) \
        for j in range(1, 4)]

datas["alvarez2002_cu"] = ["alvarez2002/ATP3" + str(i) for i in range(0, 10)]
datas["alvarez2002_cw"] = ["alvarez2002/ATP4" + str(i) for i in range(0, 10)]

datas["leung2003"] = ["leung2003/" + i for i in ["P9", "P10"]]

datas["beasley2004_ngcutap"] = ["beasley2004/ngcutap.txt_" + str(i) for i in range(1, 22)]
# datas["beasley2004_ngcutcon"] = ["beasley2004/ngcutcon.txt_" + str(i) for i in range(1, 22)]
datas["beasley2004_ngcutfs"] = ["beasley2004/ngcutfs" + str(i) + ".txt_" + str(j) \
        for i in range(1, 4) \
        for j in range(1, 211)]

datas["imahori2005"] = ["imahori2005/" + a + b + c \
        for a in ["A", "B", "C", "D"] \
        for b in ["L", "S", "V"] \
        for c in ["X", "Y", "Z", "ZZ", "ZZZ"]]

datas["hifi2008_cu"] = ["hifi2008/" + t + "T_" + i +  "H.txt" \
        for t in ["nice", "path"] \
        for i in ["25", "50", "100", "200", "500", "1000"]]
datas["hifi2008_cw"] = ["hifi2008/" + t + "T_" + i + "PH.txt" \
        for t in ["nice", "path"] \
        for i in ["25", "50", "100", "200", "500"]]

datas["cui2008"] = ["cui2008/" + str(i) for i in range(1, 21)]

datas["cintra2008"] = ["cintra2008/gcut" + str(i) + "d.txt" for i in range(1, 13)]

datas["morabito2010"] = ["morabito2010/random_class_" + str(c) + "/R_" + str(n) + "_" + t1 + "/" + str(i) + "_" + str(n) + "_100_" + t2 + ".dat" \
        for c in [1, 2, 3] \
        for t1, t2 in [("S", "10_50"), ("L", "25_75")] \
        for n in [10, 20, 30, 40, 50] \
        for i in range(1, 16)]

datas["hifi2012_cu"] = ["hifi2012/UL" + i + "H.txt" for i in ["1", "2", "3"]]
datas["hifi2012_cw"] = ["hifi2012/WL" + i + "H.txt" for i in ["1", "2", "3"]]

datas["clautiaux2018_cu"] = []
datas["clautiaux2018_cw"] = []
for wh in ["W500H1000", "W1000H2000"]:
    for n in [50, 100, 150]:
        datas["clautiaux2018_cu"] += ["clautiaux2018/a/" + f.strip() for f in open("data/rectangle_raw/clautiaux2018/A_" + wh + "I" + str(n))]
        datas["clautiaux2018_cw"] += ["clautiaux2018/p/" + f.strip() for f in open("data/rectangle_raw/clautiaux2018/P_" + wh + "I" + str(n))]

# TODO clautiaux2019

# datas["martin2019a"] = ["martin2019a/os" + o + "_is" + i + "_m" + m +  "_" + j \
        # for o in ["02", "06"]       for i in ["01", "02", "03", "04", "06", "07", "08", "11", "12", "16"] \
        # for m in ["10", "20", "40"] for j in ["01", "02", "03", "04", "05"]]
# datas["martin2019b"] = ["martin2019b/inst_" + LW + "_" + str(m) + "_"  + str(rho) + "_" + str(i) + "_" + str(d)
        # for LW in ["75_75", "125_50", "150_150", "225_100", "300_300", "450_200"] \
        # for m in [5, 10, 15, 20, 25] for rho in [6, 8, 10] for i in range(1, 16) for d in [1, 2, 3, 4]]

datas["velasco2019"] = ["velasco2019/P" + str(cl) + "_" + str(l) + "_"  + str(h) + "_" + str(m) + "_" + str(i) + ".txt"
        for cl, l, h in [(1, 100, 200), (1, 100, 400), (2, 200, 100), (2, 400, 100), \
                         (3, 150, 150), (3, 250, 250), (4, 150, 150), (4, 250, 250)] \
        for m in [25, 50] \
        for i in range(1, 6)]

datas["hopper2000_n"] = ["wei2011/N/N" + str(i) + c + ".txt" \
        for i in range(1, 8) \
        for c in ["a", "b", "c", "d", "e"]]
datas["hopper2000_t"] = ["wei2011/T/T" + str(i) + c + ".txt" \
        for i in range(1, 8) \
        for c in ["a", "b", "c", "d", "e"]]
datas["hopper2001_c"] = ["wei2011/C/lw" + str(i) + ".txt" for i in [ \
        161, 163, 172, 251, 252, 253, 281, 283, 292, 491, 492, 493, \
        731, 732, 733, 971, 972, 973, 1961, 1963, 1972]]
datas["burke2004"] = ["wei2011/Burke/n" + str(i) + ".txt" for i in range(1, 14)]

################################################################################

problem = sys.argv[1]
pdp = []
for problem in sys.argv[1:]:
    filename = os.path.join("output", problem + ".csv")
    if os.path.exists(filename):
        os.remove(filename)

    # BPPL

    if problem == "roadef2018_A":
        pdp.append((problem, ["roadef2018_A"], [
                "--objective", "bin-packing-with-leftovers",
                "--time-limit", "3600",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 1\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 1\"",
                "-q", "\"RG -p roadef2018 -s 4 --no-symmetry-2\"", "-a", "\"DPA* -s -2 -c 5\"",
            ]))
    if problem == "roadef2018_B":
        pdp.append((problem, ["roadef2018_B"], [
                "--objective", "bin-packing-with-leftovers",
                "--time-limit", "3600",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 1\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 1\"",
                "-q", "\"RG -p roadef2018 -s 4 --no-symmetry-2\"", "-a", "\"DPA* -s -2 -c 5\"",
            ]))
    if problem == "roadef2018_X":
        pdp.append((problem, ["roadef2018_X"], [
                "--objective", "bin-packing-with-leftovers",
                "--time-limit", "3600",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.33 -c 1\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 0\"",
                "-q", "\"RG -p roadef2018 -s 2\"", "-a", "\"MBA* -f 1.5  -c 1\"",
                "-q", "\"RG -p roadef2018 -s 4 --no-symmetry-2\"", "-a", "\"DPA* -s -2 -c 5\"",
            ]))

    # BPP

    elif problem == "3NEGH-BPP-O": # alvelos2009
                                   # [G-BPP-O] charalambous2011 fleszar2013 hong2014 lodi2017 cui2018
        pdp.append((problem, [
                "christofides1977",
                "beasley1985",
                "beasley2004_ngcutap",
                "berkey1987",
                "martello1998"
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 3NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "3NEGH-BPP-R": # [G-BPP-R] charalambous2011 fleszar2013 cui2015 cui2018
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 3NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "3GH-BPP-O": # puchinger2007 alvelos2009
        pdp.append((problem, [
                "christofides1977",
                "beasley1985",
                "beasley2004_ngcutap",
                "berkey1987",
                "martello1998"
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 3EHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3EHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3EHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "3HGV-BPP-O": # chen2016
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "fekete1997",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
                "alvarez2002_cu", "alvarez2002_cw",
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "5",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3HVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, [
                "imahori2005",
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3HVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, [
                "cintra2008",
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "10",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3HVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3HVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))

    elif problem == "2NEGH-BPP-O": # cintra2008 alvelos2009 cui2013 alvelos2014
        pdp.append((problem, [
                "christofides1977",
                "beasley1985",
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "fekete1997",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
                "beasley2004_ngcutap",
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["cintra2008"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "2NEGH-BPP-R": # cintra2008 cui2013 cui2016
        pdp.append((problem, ["cintra2008"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 2NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 2NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 2NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 2NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "2GH-BPP-O": # alvelos2009 cui2013
        pdp.append((problem, [
                "christofides1977",
                "beasley1985",
                "beasley2004_ngcutap",
                "berkey1987",
                "martello1998",
            ], [
                "--objective", "bin-packing",
                "--bin-infinite-copies",
                "--time-limit", "60",
                "-q", "\"RG -p 2EHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 2EHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2EHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))

    # KP

    elif problem == "3NEG-KP-O": # [G-KP-O] fayard1998 alvarez2002 chen2007
                                 #          bortfeldt2009 morabito2010 dolatabadi2012
                                 #          wei2015 (furini2016) velasco2019 (martin2019) (martin2020)
        pdp.append((problem, [
                "christofides1977",
                "wang1983",
                "beasley1985",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hadjiconstantinou1995",
                "jakobs1996",
                "fekete1997",
                "hifi1997a_cw", "hifi1997a_cu",
                "lai1997",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "10",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["hopper2001a"], [
                "--objective", "knapsack",
                "--time-limit", "10",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "knapsack",
                "--time-limit", "60",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, [
                "leung2003",
                "beasley2004_ngcutap",
            ], [
                "--objective", "knapsack",
                "--time-limit", "10",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        # pdp.append((problem, ["beasley2004_ngcutfs"], [
                # "--objective", "knapsack",
                # "--time-limit", "10",
                # "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                # "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            # ]))
        pdp.append((problem, ["morabito2010"], [
                "--objective", "knapsack",
                "--time-limit", "10",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["velasco2019"], [
                "--objective", "knapsack",
                "--time-limit", "120",
                "-q", "\"RG -p 3NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "3NEG-KP-R": # [G-KP-R] bortfeldt2009 wei2015 velasco2019
        pdp.append((problem, [
                "christofides1977",
                "wang1983",
                "hadjiconstantinou1995",
                "jakobs1996",
                "fekete1997",
                "lai1997",
                "fayard1998_cu", "fayard1998_cw",
                "hopper2001a",
                "leung2003",
                "beasley2004_ngcutap",
            ], [
                "--objective", "knapsack",
                "--time-limit", "30",
                "-q", "\"RG -p 3NAR -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAR -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["velasco2019"], [
                "--objective", "knapsack",
                "--time-limit", "120",
                "-q", "\"RG -p 3NAR -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NAR -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "3NEGV-KP-O": # cui2015
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "knapsack",
                "--time-limit", "60",
                "-q", "\"RG -p 3NVO -s 1\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3NVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "3HG-KP-O": # cui2008
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "2",
                "-q", "\"RG -p 3HAO -s 1\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cui2008"], [
                "--objective", "knapsack",
                "--time-limit", "60",
                "-q", "\"RG -p 3HAO -s 1\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cui2008"], [
                "--objective", "knapsack",
                "--time-limit", "60",
                "--unweighted",
                "-q", "\"RG -p 3HAO -s 1\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 3HAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))

    elif problem == "2NEG-KP-O": # hifi2001
        pdp.append((problem, [
                "christofides1977",
                "wang1983",
                "oliveira1990",
                "beasley1985",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cung2000_cw", "cung2000_cu"], [
                "--objective", "knapsack",
                "--time-limit", "3",
                "-q", "\"RG -p 2NAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "2NEGH-KP-O": # hifi2001 lodi2003 belov2006 hifi2006 alvarez2007 hifi2008 hifi2012 (martin2020)
        pdp.append((problem, [
                "christofides1977",
                "wang1983",
                "oliveira1990",
                "beasley1985",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cung2000_cw", "cung2000_cu"], [
                "--objective", "knapsack",
                "--time-limit", "3",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "knapsack",
                "--time-limit", "5",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["hifi2012_cu", "hifi2012_cw"], [
                "--objective", "knapsack",
                "--time-limit", "300",
                "-q", "\"RG -p 2NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "2NEGV-KP-O": # hifi2001 lodi2003 hifi2006 alvarez2007 hifi2008 hifi2012
        pdp.append((problem, [
                "christofides1977",
                "wang1983",
                "oliveira1990",
                "beasley1985",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2NVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cung2000_cw", "cung2000_cu"], [
                "--objective", "knapsack",
                "--time-limit", "3",
                "-q", "\"RG -p 2NVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "knapsack",
                "--time-limit", "5",
                "-q", "\"RG -p 2NVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["hifi2012_cu", "hifi2012_cw"], [
                "--objective", "knapsack",
                "--time-limit", "300",
                "-q", "\"RG -p 2NVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "2NEGH-KP-R": # lodi2003
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
        pdp.append((problem, ["cung2000_cw", "cung2000_cu"], [
                "--objective", "knapsack",
                "--time-limit", "3",
                "-q", "\"RG -p 2NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))

    elif problem == "2G-KP-O": # hifi2001
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2EAO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2EAO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "2GH-KP-O": # hifi2001
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2EHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2EHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))
    elif problem == "2GV-KP-O": # hifi2001
        pdp.append((problem, [
                "wang1983",
                "oliveira1990",
                "tschoke1995_cw", "tschoke1995_cu",
                "hifi1997a_cw", "hifi1997a_cu",
                "fayard1998_cw", "fayard1998_cu",
                "cung2000_cw", "cung2000_cu",
            ], [
                "--objective", "knapsack",
                "--time-limit", "1",
                "-q", "\"RG -p 2EVO -s 2\"", "-a", "\"MBA* -f 1.5 -c 4\"",
                "-q", "\"RG -p 2EVO -s 3\"", "-a", "\"MBA* -f 1.5 -c 4\"",
            ]))

    # SPP

    elif problem == "3NEGH-SPP-O": # bortfeldt2012 wei2014
        pdp.append((problem, ["kroger1995", "hopper2000_n", "hopper2000_t", "hopper2001_c"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "30",
                "-q", "\"RG -p 3NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 0\"",
            ]))
        pdp.append((problem, ["burke2004"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "30",
                "-q", "\"RG -p 3NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "60",
                "-q", "\"RG -p 3NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHO -s 2\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "3NEGH-SPP-R": # kroger1993 schneke1996 mumford2003 zhang2006 bortfeldt2006 cui2008 bortfeldt2012 cui2013 wei2014
        pdp.append((problem, ["kroger1995", "hopper2000_n", "hopper2000_t", "hopper2001_c", "burke2004"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "30",
                "-q", "\"RG -p 3NHR -s 2\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 0\"",
            ]))
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "60",
                "-q", "\"RG -p 3NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 0\"",
                "-q", "\"RG -p 3NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 3NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "2NEGH-SPP-O": # lodi2004 cintra2008 mrad2015 cui2017
        pdp.append((problem, ["cintra2008"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["alvarez2002_cu", "alvarez2002_cw"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHO -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHO -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))
    elif problem == "2NEGH-SPP-R": #
        pdp.append((problem, ["berkey1987", "martello1998"], [
                "--objective", "strip-packing",
                "--bin-infinite-height",
                "--time-limit", "10",
                "-q", "\"RG -p 2NHR -s 3\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 2\"",
                "-q", "\"RG -p 2NHR -s 4\"", "-a", "\"MBA* -f 1.5 -c 3\"",
            ]))

    elif problem == "test":
        pass

################################################################################

files = set()
main_exec = os.path.join(".", "bazel-bin", "packingsolver", "main")
for problem, data, parameters in pdp:
    print("Problem:", problem)
    print("Data:", data)
    print("Param:", parameters)
    print()

    directory_in  = os.path.join("data",   "rectangle")
    directory_out = os.path.join("output", "rectangle", problem)
    for dataset in data:
        for filename in datas[dataset]:
            instance_file = os.path.join(directory_in, filename)
            output_file   = os.path.join(directory_out, filename + ".json")
            cert_file     = os.path.join(directory_out, filename + "_solution.csv")
            if not os.path.exists(os.path.dirname(output_file)):
                os.makedirs(os.path.dirname(output_file))
            command = main_exec + " -p rectangleguillotine" \
                    + " -v" \
                    + " -e" \
                    + " -i \"" + instance_file + "\"" \
                    + " -c \"" + cert_file + "\"" \
                    + " -o \"" + output_file + "\"" \
                    + " " + " ".join(parameters)
            print(command)
            os.system(command)
            print()

            with open(output_file, "r") as read_file:
                data = json.load(read_file)

                k = 1
                while "Solution" + str(k + 1) in data.keys():
                    k += 1

                synth_file = problem + ".csv"
                if not synth_file in files:
                    files.add(synth_file)
                    with open(os.path.join("output", "rectangle", synth_file), "w") as f:
                        f.write("Instance,Parameters")
                        for key in data["Solution" + str(k)].keys():
                            f.write(";" + key)
                        f.write("\n")
                with open(os.path.join("output", "rectangle", synth_file), "a") as f:
                    f.write(filename + "," + " ".join(parameters))
                    for key, value in data["Solution" + str(k)].items():
                        f.write(";" + str(value))
                    f.write("\n")
