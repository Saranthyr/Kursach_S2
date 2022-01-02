import os

for i in range(0, 14):
    here = os.path.dirname(os.path.abspath(__file__))
    filename_1 = os.path.join(here, "data-54518-2021-12-20-" + str(i) + ".json")
    filename_temp = os.path.join(here, "data-54518-2021-12-20-" + str(i+1) + "-temp.json")
    filename_2 = os.path.join(here, "data-54518-2021-12-20-" + str(i+1) + ".json")


    f1 = open(filename_1, 'r')
    s = f1.read()
    last = s.rfind(',{"ShortName"')
    buffer = '[' + s[last+1:]
    buffer_internal = s[:last] + ']'
    f1.close()
    f1_rewrite = open(filename_1, 'w')
    f1_rewrite.write(buffer_internal)
    f1_rewrite.close()


    ft = open(filename_temp, "w+")
    ft.write(buffer)
    f2 = open(filename_2, "r")
    ft.write(f2.read())
    f2.close()
    ft.close()
    os.remove(filename_2)
    os.rename(filename_temp, filename_2)

