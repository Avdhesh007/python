import json

json_file = open('rec1-master/F5_Week1.txt')
data = json.load(json_file)
json_file.close()
# lst=data["people"]
print(len(data))
for p in data:
    for q in p:

        for k, v in q.items():
            if (k == "dow"):
                print("day of work:" + v)
            elif (k == "time"):
                print("Time:" + v)
            elif (k == "conference-categories-count"):
                for x, y in v.items():
                    if (x == "Small"):
                        print("Small:" + str(y))
                    elif (k == "Phone Booth"):
                        print("Phone Booth:" + y)
                    elif (k == "Medium"):
                        print("Medium:" + y)
                    elif (k == "Large"):
                        print("Large:" + y)
