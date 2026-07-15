import random as r

firstnames = []
lastnames = []

with open("lastnames.txt", 'r') as i:
    for line in i:
        lastnames.append(line.strip())

with open("firstnames.txt", 'r') as i:
    for line in i:
        firstnames.append(line.strip())


def options():
    choiceslist = {"1": "first name",
                   "BLANK": "",
                   "2": "last name",
                   "BLANK1": "",
                   "3": "full name",
                   "BLANK2": "",
                   "--OPTIONS": "to bring this menu up",
                   "BLANK3": "",
                   "Q": "to quit",
                   "BLANK4": ""}

    for k, v in choiceslist.items():
        if "BLANK" not in k:
            print(f"{k}: {v}")
        else:
            print()

print(r"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$@WbrxrfffjrrjrLMB@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$@LvjffffjffjrJQ@@@@@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$@BmczzzXXzzzzzcrjrjjL%@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@@$$$$%Qmqqq0XzzzzzzzzzzccvcvJ8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$Mpbm#8LMMMMMMWMqXzzzzzzzzzzx@kvY@$$$$$$$$$$$$$$$$$$
$$$$$$$$@OkbkkZbWWWMMMMMMWoQzzzzzzzzzz*$8o$$$$$$$$$$$$$$$$$$
$$$$$$$@@dkkkkkbUuuvXaWWWMWWWqzzzzzzzzv>,`.$$$$$$$$$$$$$$$$$
$$$$$$$$@mkQkkkkkkkkkkpUUw*qxYwLzzzzzzzv>..f$$$$$$$$$$$$$$$$
$$$$$$$$$OkkZkkkkkkkkkkr!lir*[':~jnczzzzct`+$$$$$$$$$$$$$$$$
$$$$$$$$$#qkpwkqJf^.;(||\||\;|>.^`...I/jjj(jmQw%$$$$$$$$$$$$
$$$$$$$$$@abkd~......^l\||||!,:.-j ...`1\|)~bkbm@$$$$$$$$$$$
$$$$$$$$$$@(............<|||,...}kq:....:<~qwbkbM$$$$$$$$$$$
$$$$$$$$@UI....')x!.......~||1i.{bbkqwwjcqbkbkkb0$$$$$$$$$$$
$$$$$$@|.. -tYubbbk<....... (|+;bbbbZbbM0bkkkkkkka@$$$$$$$$$
$$$$$$$a...@0zXvYbkkq_.......?ObbbbmdbbB8qbkkkkkkk@$$$$$$$$$
$$$$$$$$$X0$bruXXzrwbkkkkbkkkkkkkkkkL@@$$@qkkkkkkpM@$$$$$$$$
$$$$$$$$$$$$@JrnzYXXXuxUmkkkkbkdmObB$$$$$$@wbkkkkbm@$$$$$$$$
$$$$$$$$$$$$$$xxxnXXvCbkkkkbbbdbkQ@$$$$$$$$@kbkkkkkO$$$$$$$$
$$$$$$$$$$$$$@OrxrrxzYuYbkkkkkkkkkL@$$$@@MZkbkkkkkpq$$$$$$$$
$$$$$$$$$$$$$$$fjrrrrrxcvdkkkkkkkkbh@@kbdkkkkkbkkwB$$$$$$$$$
$$$$$$$$$$$$$$$b(]jrrrrrrrqkkkkkkkkmpkkkkkkkkbqq@$$$$$$$$$$$
$$$$$$$$$$$$&q&aQ\]{rrxnrrvpkkkkkkbkQbkkkkk0bM$$$$$$$$$$$$$$
$$$$$$$$$$$@okbLpw|][trLUnr0kkkkkkkkbJZpB@@$$$$$$$$$$$$$$$$$
$$$$$$$$$@hwOqkd0bQ\]]/vQbCvbkkbbkkkkdb@$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@mkdqkkk0kZ/]]nOCkJbkkbqkkkkkw8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$8Zbkpkm0ZOJ(]uCQbbkkkbqdkkkkm&$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$@B0kb0pkkbkCnqkkpmbkkkpmkkkkd8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$WwCkkkkkkCLkbkqObkkkkwmkkbq8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$BJmkkkkkbbkkkO0bkkkkkqmkbmZQk@$$$$$$$$$$$$$$$$$
$$$$$$$$$$@@bpkbZOwwwwqmQbkpOkkkkkbZpbQZmmmh@$$$$$$$$$$$$$$$
$$$$$$$$$$@*pkkkkkkkbkkkkkkkUbkkkkkbQ0ZmmmmZo$$$$$$$$$$$$$$$
$$$$$$$$$$@Jbkkkkkkkkkkkkkkkk0kkkkkkkLmmmmmmwB$$$$$$$$$$$$$$
""")
options()
while True:
    inputchoice = input("select choice: ").upper()
    match inputchoice:
        case "1":
            while True:
                loopbreak = "Q"
                intvalinput = input("input amount here: ").upper()
                if intvalinput.isdigit():
                    for i in range(int(intvalinput)):
                        print(r.choice(firstnames), end='\n')
                elif intvalinput == loopbreak:
                    break
                else:
                    print(f"no integer value found {loopbreak} to return to selection '--OPTIONS' for options", end='\n')
        case "2":
            while True:
                loopbreak = "Q"
                intvalinput = input("input amount here: ").upper()
                if intvalinput.isdigit():
                    for i in range(int(intvalinput)):
                        print(r.choice(lastnames), end='\n')
                elif intvalinput == loopbreak:
                    break
                else:
                    print(f"no integer value found {loopbreak} to return to selection '--OPTIONS' for options", end='\n')
        case "3":
            while True:
                loopbreak = "Q"
                intvalinput = input("input amount here: ").upper()
                if intvalinput.isdigit():
                    for i in range(int(intvalinput)):
                        fullfirstname = r.choice(firstnames)
                        fulllastname = r.choice(lastnames)
                        print(f"{fullfirstname} {fulllastname}", end='\n')
                elif intvalinput == loopbreak:
                    break
                else:
                    print(f"no integer value found {loopbreak} to return to selection '--OPTIONS' for options", end='\n')
        case "--OPTIONS":
            options()
        case "Q":
            break
        case _:
            print("invalid input", end='\n')