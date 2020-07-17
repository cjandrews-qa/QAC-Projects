def quest():
    fname = "chris" # input('What is your first name: ')
    sname = "andrews" #input(f'What is your surname {fname}: ')
    hw = 26 #int(input('What did you get in your homework: '))
    ass = 23 # int(input('What did you get in your Assesment: '))
    fe = 97 #int(input('What did you get in your Final Exam: '))
    mark = hw + ass + fe
    return fname, sname, str(mark)


def calc(total):
    calc = int(total)/175*100
    grade = ""
    if calc >= 70:
        grade = "A"
    elif clac >= 60:
        grade = "B"
    elif calc >= 50:
        grade = "C"
    else:
        grade = "Fail"
    return grade



test = quest()
grade = calc(test[2])
print(f'{test[0]} {test[1]} got an {grade}!!')   
