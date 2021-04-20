import os

userID = 273474320544694274

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Storage'
C1 = open(os.path.join(dir_path, "C1-Clearance-List.txt"), "r", encoding="utf-8")

for line in C1:
    print(type(line))
    if userID == int(line.strip()):
        C1.close()
        print('c1')
        break

C2 = open(os.path.join(dir_path, "C2-Clearance-List.txt"), "r", encoding="utf-8")
for line in C2:
    if userID == int(line.strip()):
        C2.close()
        print('c2')
        break