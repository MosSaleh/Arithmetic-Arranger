#def arithmetic_arranger(problems):

#split into pieces of string
def split(problem):
    pieces = problem.split()
    num1 = pieces[0].strip()
    operator = pieces[1].strip()
    num2 = pieces[2].strip()
    
    return num1, operator, num2

#how to figure out different lengths
def lengths():
    if len(num1) > len(num2):
        longestnum = len(num1)
    else:
        longestnum = len(num2)
    
    dashlen = longestnum + 2
    #spacelength for numbers
    len1 = dashlen -(len(num1))
    len2 = dashlen - (len(num2)) - 1
    return dashlen, len1, len2

#function that makes the space
def spacemaker(length):
    for i in range(length):
        print(end=' ')

#function for printing dashes
def dashprinter(dashlen):
    for i in range(dashlen):
        print('-',end='')

#inp = (input('Problems: '))
#problems = inp
problem = '1 - 3801'
problems = list()

print('(Enter problems one at a time, (max 5), if you want answers type True, else type done)')

while True:
    inp = input('Enter problems here:')
    if inp == 'done':
        break
    elif inp == 'True':
        solutions = True
        break
    else:
        problems.append(inp)

if len(problems) > 5:
    print('Error: Too many problems.')
    quit()

num1_lst = list()
operator_lst = list()
num2_lst  = list()
dashlen_lst  = list()
len1_lst = list()
len2_lst  = list()
answers = list()

for problem in problems:
    try:
        num1, operator, num2 = split(problem)
    except:
        print('formatting error')
        quit()
    dashlen, len1, len2 = lengths()
    
    if len(num1) > 4 or len(num2) > 4 :
        print('Error: Numbers cannot be more than four digits.')
        quit()
    if operator == '-' or operator == '+':
        pass
    else:
        print('Error: Operator must be \'+\' or \'-\'.')
    try:
        int(num1)
        int(num2)
    except:
        print('Error: Numbers must only contain digits.')
    
    num1_lst.append(num1)
    operator_lst.append(operator)
    num2_lst.append(num2)
    dashlen_lst.append(dashlen)
    len1_lst.append(len1)
    len2_lst.append(len2)
    
    if solutions == True:
        if operator == '+':
            answer = int(num1) + int(num2)
        elif operator == '-':
            answer = int(num1) - int(num2)
        answers.append(answer)
    else:
        pass

for i in range (len(operator_lst)):
    spacemaker(len1_lst[i]), print(num1_lst[i], end='    ')
print('')
for i in range (len(operator_lst)):
    print(operator_lst[i],end=''), spacemaker(len2_lst[i]), print(num2_lst[i], end ='    ')

print('')

for i in range (len(operator_lst)):
    dashprinter(dashlen_lst[i]), print('', end='    ')

print('')

if solutions == True:
    for i in range (len(answers)):
        answer = str (answers[i])
        sol_len = dashlen_lst[i] -(len(answer))
        spacemaker(sol_len), print(answer, end='    ') 


#spacemaker(len1), print(num1)
#print(operator, end=''), spacemaker(len2),print(num2)
#dashprinter(dashlen), print('', end =' ')










#for problem in problems:
#    return arranged_problems
