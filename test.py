import re
entries = [('25/01/1990', 'AHOJKY', 31, 'NE'), ('25/02/1990', 'NEPOVIM', 31, 'NEREKNU')] #data1

entry = "AHOJKY" #data2

results = []


def checker(data1, data2):
    count = 0

    while count < len(data1):
        for each in data1[count]:
            if data2 == each:
                results.append(data1[count])
                print("yes")
            else:
                print("no")
        count += 1


entries_2 = '25/01/1990' #data1
regex = "\d" #data2

print(re.findall(regex, "30"))


def checker_2(data1, data2):
    count = 0

    while count < len(data1):
        for each in data1[count]:
            a = re.findall(data2, each)
            print(each)
            if a == each:
                results.append(data1[count])
                print("yes")
            else:
                print("no")
        count += 1

checker_2(entries, regex)
