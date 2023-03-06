def arithmetic_arranger(problems, answers=False):

    # split into pieces of string
    def split(problem):
        pieces = problem.split()
        num1 = pieces[0].strip()
        operator = pieces[1].strip()
        num2 = pieces[2].strip()

        return num1, operator, num2

    # how to figure out different lengths
    def lengths():
        if len(num1) > len(num2):
            longestnum = len(num1)
        else:
            longestnum = len(num2)

        dashlen = longestnum + 2
        # spacelength for numbers
        len1 = dashlen - (len(num1))
        len2 = dashlen - (len(num2)) - 1
        return dashlen, len1, len2

    # function that makes the space
    def spacemaker(length):
        spaces = ""
        for i in range(length):
            spaces += " "
        return spaces

    # function for printing dashes
    def dashprinter(dashlen):
        dashes = ""
        for i in range(dashlen):
            dashes += "-"
        return dashes

    if len(problems) > 5:
        return "Error: Too many problems."

    num1_lst = list()
    operator_lst = list()
    num2_lst = list()
    dashlen_lst = list()
    len1_lst = list()
    len2_lst = list()
    solutions = list()

    for problem in problems:
        try:
            num1, operator, num2 = split(problem)
        except:
            return "formatting error"
        dashlen, len1, len2 = lengths()

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == "-" or operator == "+":
            pass
        else:
            return "Error: Operator must be '+' or '-'."
        try:
            int(num1)
            int(num2)
        except:
            return "Error: Numbers must only contain digits."

        num1_lst.append(num1)
        operator_lst.append(operator)
        num2_lst.append(num2)
        dashlen_lst.append(dashlen)
        len1_lst.append(len1)
        len2_lst.append(len2)

        if answers == True:
            if operator == "+":
                answer = int(num1) + int(num2)
            elif operator == "-":
                answer = int(num1) - int(num2)
            solutions.append(answer)
        else:
            pass

    firstline = ""
    secondline = ""
    thirdline = ""

    for i in range(len(operator_lst)):

        firstline += str(spacemaker(len1_lst[i])) + str(num1_lst[i]) + "    "

    for i in range(len(operator_lst)):

        secondline += (
            str(operator_lst[i])
            + str(spacemaker(len2_lst[i]))
            + str(num2_lst[i])
            + "    "
        )

    for i in range(len(operator_lst)):

        thirdline += str(dashprinter(dashlen_lst[i])) + "    "

    firstline = firstline.rstrip() + "\n"
    secondline = secondline.rstrip() + "\n"
    thirdline = thirdline.rstrip()
    answerline = ""

    if answers == True:
        for i in range(len(solutions)):
            answer = str(solutions[i])
            sol_len = dashlen_lst[i] - (len(answer))
            answerline += str(spacemaker(sol_len)) + answer + "    "
        thirdline = thirdline + "\n"
        answerline = answerline.rstrip()

    elif answers == False:
        pass

    return firstline + secondline + thirdline + answerline
