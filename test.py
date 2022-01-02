import json
import os

for i in range(0, 15):
    here = os.path.dirname(os.path.abspath(__file__))
    filename_1 = os.path.join(here, "data-54518-2021-12-20-" + str(i) + ".json")
    with open(filename_1, "r") as f1:
        l1 = json.load(f1)
        for j in range(len(l1)):
            if l1[j]['ShortName'] == "ГБОУ школа № 626":
                print(l1[j]['geoData']['coordinates'][0][0])