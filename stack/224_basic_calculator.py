'''
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .
'''

'''
questions: no * or / ? expression always valid? 

idea:
if there is no (), then it is simple, just go through the string, and add or substract the current number
according to the previous sign.
With (), we can use a stack to solve this:
if we see a new open (, then we create a new element in the stack, before seeing a ), 
we do calculation on the top element.
when we see a close ), then we can pop out the top element, aggregate to the new top element.
until there is no more characters in the string
'''
'''
thought: 
for each one in '()+-d', we should know what we need to do, what are the possible situations.

'''


fs = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}

def solve(s):
    s += '+'
    st, curr = [[0, '+']], 0
    for i in xrange(len(s)):
        if s[i] == '(':
            st.append([0, '+'])
        elif s[i] == ')':
            st[-1][0] = fs[st[-1][1]](st[-1][0], curr)
            curr = 0
            tmp, sign = st.pop()
            st[-1][0] = fs[st[-1][1]](st[-1][0], tmp)
        elif s[i] in '+-':
            st[-1][0] = fs[st[-1][1]](st[-1][0], curr)
            curr = 0
            st[-1][1] = s[i]
        elif s[i].isdigit():
            curr = curr*10 + int(s[i])

    return st[-1][0]

# test = ['1+1+1+1', '1+(1+1)+1', '1-(-1-1)+1', '4', '-4', '', '1+(1+(1+1))']
# for s in test:
#     print solve(s)



'''
227: Basic Calculator 2
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.
'''


'''
idea

for +-, just add/substract from the previous result.
for */, use the last number calculated.
So keep an array as we go through the string to save every number in the string, with sign
'''
def solve1(s):
    s += '+'
    nums, curr = [[0, '+']], 0
    for i in xrange(len(s)):
        if s[i].isdigit():
            curr = curr*10 + int(s[i])
            continue
        if nums[-1][1] in '*/':
            nums[-1][0] = fs[nums[-1][1]](nums[-1][0], curr)
            nums[-1][1] = s[i]
        else:
            nums.append([curr, s[i]])
        curr = 0
    result, prevSign = 0, '+'
    for n, sign in nums:
        result = fs[prevSign](result, n)
        prevSign = sign
    return result
        
            
# test1 = ['1+2*3+4*5']
# for s in test1:
#     print solve1(s)
    




# follow up, evaluate an expression which has all '()+-*/'
'''
idea

for () and nested (), we can use a stack, for every (, append a new element to the stack.
+-*/:
    check the previous sign, if it is */, then aggragate, then set the sign
digit
(:
    start a new element in the stack
):
    calculate the value in this (), set curr as the result
'''

def aggregate(elements):
    result, prevSign = 0, '+'
    for num, sign in elements:
        result = fs[prevSign](result, num)
        prevSign = sign
    return result

def solve2(s):
    s += '+'
    curr, st = 0, [[[0, '+']]]
    for i in xrange(len(s)):
        if s[i].isdigit():
            curr = curr*10 + int(s[i])
            continue
        if s[i] in '+-*/':
            if st[-1][-1][1] in '*/':
                st[-1][-1][0] = fs[st[-1][-1][1]](st[-1][-1][0], curr)
                st[-1][-1][1] = s[i]
            else:
                st[-1].append([curr, s[i]])
            curr = 0
        if s[i] == '(':
            st.append([[0, '+']])
            curr = 0
        if s[i] == ')':
            st[-1].append([curr, '+'])
            curr = aggregate(st.pop())
    return aggregate(st[-1])



test2 = ['1+(2*(3+4)*(5-6)+7)']
for s in test2:
    print solve2(s)




















