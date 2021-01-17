s = input()

result = ''
op = []

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        result += s[i]

    else:
        if s[i] == ')':
            while len(op) != 0 and op[-1] != '(':
                result += op.pop()
            op.pop()

        elif s[i] == '*' or s[i] == '/':
            while len(op) != 0 and (op[-1] == '*' or op[-1] == '/'):
                result += op.pop()
            op.append(s[i])

        elif s[i] == '+' or s[i] == '-':
            while len(op) != 0 and op[-1] != '(':
                result += op.pop()
            op.append(s[i])

        elif s[i] == '(':
            op.append(s[i])

while len(op) != 0:
    result += op.pop()

print(result)
