def solution(code):
    stack = []
    str_list = []
    for i in range(len(code)):
        if code[i] == "{":
            stack.append("{")
        elif code[i] == "}":
            while True:
                tmp = stack.pop()
                if tmp == "{":
                    str_list.reverse()
                    result = ''.join(code for code in str_list)
                    break
                str_list.append(tmp)
            result = result * stack.pop()
            stack.append(result)
            str_list = []
        elif i != len(code) - 1 and code[i].isdigit and code[i + 1] == "{":
            stack.append(int(code[i]))
        else:
            stack.append(code[i])
    answer = ''.join(stack)
    return answer