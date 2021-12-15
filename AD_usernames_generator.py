#!/bin/env python3

import argparse

# create the parser
arg_parser = argparse.ArgumentParser(
    prog='AD_usernames_generator.py',
    description="Generate a list of possible usernames for AD Enumeration",
    usage="./AD_usernames_generator.py -u users.txt -o possibleusers.txt -a A -p A -an 0 -pn 2005"
)

# add the CLI flags/options
arg_parser.add_argument(
    "-o", "--output",
    default="possibleusernames.txt",
    type=str,
    help="specify outfile name",
)

# CLI flag for usernames.txt input file
arg_parser.add_argument(
    "-u", "--usernames",
    # default="usernames.txt",
    type=str,
    help="specify path to usernames.txt file",
)

# l33t usernames
# Yet to Implement 
# arg_parser.add_argument(
#     "-leet", "--leet-speak",
#     default=False,
#     type=bool,
#     help="specify if you want L337 US3RN4M3S",
# )

# append string to usernames
arg_parser.add_argument(
    "-a", "--append",
    default="",
    type=str,
    help="specify what you want to append",
)

# prepend string to usernames
arg_parser.add_argument(
    "-p", "--prepend",
    default="",
    type=str,
    help="specify what you want to prepend",
)

# append numbers to usernames
arg_parser.add_argument(
    "-an", "--append-number",
    default="",
    type=str,
    help="specify what you want to append",
)

# prepend numbers to usernames
arg_parser.add_argument(
    "-pn", "--prepend-number",
    default="",
    type=str,
    help="specify what you want to prepend",
)


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
print(" ")
prLightPurple("==============================")
prLightPurple("    AD Usernames Generator")
prLightPurple("==============================")
print(" ")


# parse cli arguments
args = arg_parser.parse_args()
print(args)

# set usernames variable value to the usernames.txt input file
usernamesFile = str(args.usernames)
# output file name
outputFile = str(args.output)

appendNumber= str(args.append_number)
prependNumber = str(args.prepend_number)
appendStr = str(args.append)
prependStr = str(args.prepend)

# username format (for now it can handle both username types by default)
# nameformat = str(args.format)

finalNames = []

def nameToString(name):
    # print("inside nameToString")
    namestring = ""
    for i in name:
        namestring += i
    # print("namestr:", namestring)
    return namestring

def addSymbols(string1, string2, string3):
    symbols = ["", ".", "-", "_"]
    for i in range(len(symbols)):
        if string2 == None:
            finalNames.append(string1 + symbols[i] + string3)
            finalNames.append(string3 + symbols[i] + string1)
        else:
            reverseSymbols = ["_", "-", ".", ""]
            finalNames.append(string1 + string2 + symbols[i] + string3)
            finalNames.append(string1 + symbols[i] + string2 + string3)
            finalNames.append(string3 + symbols[i] + string1 + string2)
            for j in range(len(reverseSymbols)):
                finalNames.append(string1 + symbols[i] + string2 + symbols[i] + string3)
                finalNames.append(string1 + symbols[i] + string2 + symbols[j] + string3)
                finalNames.append(string1 + symbols[j] + string2 + symbols[i] + string3)
                finalNames.append(string1 + symbols[j] + string2 + symbols[j] + string3)
                finalNames.append(string3 + symbols[i] + string1 + symbols[i] + string2)
                finalNames.append(string3 + symbols[i] + string1 + symbols[j] + string2)
                finalNames.append(string3 + symbols[j] + string1 + symbols[i] + string2)
                finalNames.append(string3 + symbols[j] + string1 + symbols[j] + string2)
                # mercer_alex-j

def firstLetterMutations(name):

    nameclass = name.split()
    if len(nameclass) == 2:
        firstName = nameclass[0]
        lastName = nameclass[1]
        middleName = None
        firstLetterFirstName = nameclass[0][0]
        firstLetterLastName = nameclass[1][0]
        
        addSymbols(firstLetterFirstName, middleName, lastName)
        addSymbols(firstLetterLastName, middleName, firstName)
        addSymbols(lastName, middleName, firstLetterFirstName)
        addSymbols(firstName, middleName, firstLetterLastName)


def joinFirstLastName(name):
    nameclass = name.split()
    if len(nameclass) == 2:
        firstName = nameclass[0]
        lastName = nameclass[1]
        middleName = None
        # pattern = re.compile(r'\s+')
        # print(re.sub(pattern, "", name))
        addSymbols(firstName, middleName, lastName)

def handle3wordNames(name):
    # print(name)
    nameclass = name.split()
    string1 = nameclass[0]
    string2 = nameclass[1]
    string3 = nameclass[2]

    addSymbols(string1, string2, string3)

try:
    file_name = usernamesFile
    with open(file_name) as f:
        names = f.readlines()
        # print("names type:", type(names), "names:", names)
        for name in names:
            name = name.rstrip()
            namestring = nameToString(name)
            # print("namestring", type(namestring), namestring)
            firstLetterMutations(namestring)
            numberOfWordsInName = len(namestring.split())
            if numberOfWordsInName == 1:
                finalNames.append(namestring)
            elif numberOfWordsInName == 2:
                for name in names:
                    joinFirstLastName(name)
            elif numberOfWordsInName == 3:
                handle3wordNames(namestring)            
        f.close()
except IOError:
    print("No username input file specified...")


# print(finalNames)

def removeLastSpecialCharacter():
    specialChars = [".", "-", "_"]
    for i in finalNames:
        for j in specialChars:
            if i[-1] == str(j):
                finalNames.append(i[:-1])
removeLastSpecialCharacter()

# ==================================================
# Append Prepend Strings and Numbers to Usernames 
# ==================================================

# output='possibleusernames.txt', usernames='users.txt', 
# leet_speak=None, append=None, prepend=None, 
# append_number=None, prepend_number=None

def appendStringToUsernames():
    # print("appendStr", appendStr)
    if appendStr:
        # print("appendStr", appendStr)
        appendedNames = []
        for i in finalNames:
            appendedNames.append(i + appendStr)
        finalNames.extend(appendedNames)
        # print(finalNames)
appendStringToUsernames()

def prependStringToUsernames():
    # print("prependStr", prependStr)
    if prependStr:
        # print("prependStr", prependStr)
        prependedNames = []
        for i in finalNames:
            prependedNames.append(prependStr + i)
        finalNames.extend(prependedNames)
        # print(finalNames)
prependStringToUsernames()

def appendNumbersToUsernames():
    # print("appendNumber", appendNumber)
    if appendNumber:
        # print("appendNumber", appendNumber)
        appendedNumbers = []
        for i in finalNames:
            appendedNumbers.append(i + appendNumber)
        finalNames.extend(appendedNumbers)
        # print(finalNames)
appendNumbersToUsernames()

def prependNumbersToUsernames():
    # print("prependNumber", prependNumber)
    if prependNumber:
        # print("prependNumber", prependNumber)
        prependedNumbers = []
        for i in finalNames:
            prependedNumbers.append(prependNumber + i)
        finalNames.extend(prependedNumbers)
        # print(finalNames)
prependNumbersToUsernames()

# print(finalNames)
# finalNames.sort()

with open(outputFile, 'w') as f:
    f.writelines("%s\n" % i for i in finalNames)
    f.close()


# Deduplicate the output file 

def deduplicate():
    with open(outputFile, 'r+') as f:
        lines_seen = set()
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
        f.truncate()
        # print(lines_seen)
deduplicate()
