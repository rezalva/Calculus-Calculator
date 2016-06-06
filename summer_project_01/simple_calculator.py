from stack import *

"""
For containing numbers with multiple digits. Only for integers
Will be used to contain negative numbers as well.
Will be used to contain floats.
"""
class Number(object):
    __slots__ = ["number"]

    def __init__(self, number):
        self.number = number


"""
calculator:
-Does calculation for five operators.
-assumes that num is integer.           Make it float later
"""
def calc(num1, num2,op):
    if op == "+":
        return num2 + num1
    elif op == "-":
        return num2 - num1
    elif op == "*":
        return num2 * num1
    elif op == "/":
        return num2 / num1
    elif op == "^":
        return num2 ** num1


"""
order of operation
"""
def rank_checker(operations):
    op = top(operations)            # assumes that the operations parameter is a stack
    if op == "+":
        return 1
    elif op == "-":
        return 1
    elif op == "*":
        return 2
    elif op == "/":
        return 2
    elif op == "^":
        return 3
    elif op == "(":
        return 0

"""
String to list
"""
def stringToList(string):
    lst = []
    for x in string:
        lst.append(x)
    return lst

def operate(num,op):
    num1 = int(top(num).number)
    number = pop(num)
    num2 = int(top(number).number)
    number = pop(number)
    opp = top(op)
    op = pop(op)
    result = int(calc(num1, num2, opp))

    node = Number(str(result))
    num = push(number, node)

    return num, op


"""
compute
parameter - string
"""
def simple_compute(equation):
    if equation.isdigit():
        return float(equation)
    rank = {}
    rank["+"] = 1
    rank["-"] = 1
    rank["*"] = 2
    rank["/"] = 2
    rank["^"] = 3
    rank["("] = 0
    stackR = {}
    stackR["num"] = None                 # **Not sure if I really need to use dictionary to store stack
    stackR["op"] = None
    tempNum = ""                            # in string. used to hold the value after while loop. Same with others
                                            # I could change it to list but then I would have to make it so each append is a single string.

    eList = stringToList(equation)          # This is the equation in list form for each character.

    while 0 < len(eList):                   # designed so I can take account to multiple digits in numbers.
        o = stackSting(stackR["op"])        #these two are there for debugging
        n = stackSting2(stackR["num"])
        #print("op: ", o)
        #print("num: ", n)

        if eList[0].isdigit():
            temp = ""
            while eList[0].isdigit():       # only evaluates if eList[0] has character. does not work if there is nothing.
                temp += eList[0]
                eList.pop(0)
                tempNum = temp
                if eList == []:
                    break                   #That is why break is here
            node = Number(tempNum)
            stackR["num"] = push(stackR["num"],node)

        elif eList[0] == "+" or eList[0] == "-" or eList[0] == "*" or eList[0] == "/" or eList[0] == "^":
            if size(stackR["op"]) != 0:
                while rank_checker(stackR["op"]) >= rank[eList[0]]:


                    stackR["num"], stackR["op"] = operate(stackR["num"], stackR["op"])

                    if stackR["op"] == None:
                        break

                stackR["op"] = push(stackR["op"], eList[0])
                eList.pop(0)
            else:
                stackR["op"] = push(stackR["op"], eList[0])
                eList.pop(0)

        elif eList[0] == "(":
            stackR["op"] = push(stackR["op"], eList[0])
            eList.pop(0)

        elif eList[0] == ")":
            while top(stackR["op"]) != "(":
                stackR["num"], stackR["op"] = operate(stackR["num"], stackR["op"])

            stackR["op"] = pop(stackR["op"])
            eList.pop(0)

    while size(stackR["op"]) != 0:
        stackR["num"], stackR["op"] = operate(stackR["num"], stackR["op"])

    return int(top(stackR["num"]).number)


def test():
    a = '24+412345678000'
    b = '10/2'
    c = '4-3'
    d = '5*7'
    e = '10^3'
    f = "2+5*(10-2)/4"
    g = "2+5*(10-2)/4"
    print("Testing...")
    print(simple_compute(a) == 412345678024)
    print(simple_compute(b) == 5)
    print(simple_compute(c) == 1)
    print(simple_compute(d) == 35)
    print(simple_compute(e) == 1000)
    print(simple_compute(f) == 12)
    print(simple_compute(g) == 12)

if __name__ == '__main__':
    test()
    #a = "3"
    #print(a.isdigit())
    #print(isinstance(a,str))