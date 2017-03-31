import argparse
def can_play_today (temp_day, match):
    for i in temp_day:
        if ((i[0][0] is match[0]) or (i[0][0] is match[1]) or (i[0][1] is match[0]) or (i[0][1] is match[1])):
            return 0
    return 1
def match_programed (program, match):
    for day in program:
        for temp_match in day:
            if (temp_match[0] == match):
                return 1
    return 0

def flatten (program):
    final = []
    for day in program:
        for match in day:
            final.append(match)
    return final

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of input file")
args = parser.parse_args()

matches = []
with open(args.filename) as inputData:
    for line in inputData:
        match = line.split()
        matches.append(match)
program = []
flag = 0
for match in matches:
    if (match_programed(program, match)):
        continue
    counter = 0
    for day in program:
        if (can_play_today(day, match)):
            day.append((match, counter))
            flag = 1
            break
        counter +=1
    if (flag == 0):
        temp_day = []
        temp_day.append((match, counter))
        program.append(temp_day)
    flag = 0
final = []
final = flatten(program)
for match in final:
    if match[0][0] > match[0][1]:
        temp = match[0][0]
        match[0][0] = match[0][1]
        match[0][1] = temp
final.sort()

for match in final:
    print( "(",match[0][0],",",match[0][1],") ", match[1])
