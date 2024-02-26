def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    
print('start')

def convertToArray():
    import ast

    # A string fornecida
    minha_string = '("4",("2","3","*"),"+")'
    minha_string = minha_string.replace('(', '[').replace(')', ']')
    #minha_string = '["4",["2","3","*"],"+"]'

    # Removendo os caracteres não numéricos e convertendo para uma lista
    lista_simplificada = ast.literal_eval(minha_string)
    print(lista_simplificada)
convertToArray()

expressions = []
expressions.append(['2', '3', '+'])
expressions.append(['2', '3', '-'])
expressions.append(['2', '3', '*'])
expressions.append(['2', '3', '/'])
expressions.append(['3', 'MEM'])
expressions.append(['MEM', '3', '+'])
expressions.append(['3', 'RES', '2', '+'])
expressions.append([[['2.0', '3.0', '+']], [['2.0', '3.0', '+']], '+'])

def calculateSubExpression(array):
    if type(array) == list:
        return calculateExpressions(array)
    else: return None
    
finalResults = [] 

def calculateExpressions(expressions):
    memory = 0
    stack = []
    
    for expression in expressions:
        result = calculateSubExpression(expression[0])
        if result != None:
            expression[0] = result

        result = calculateSubExpression(expression[1])
        if result != None:
            expression[1] = result

        if (expression[0].replace('.', '', 1).isdigit() and expression[1].replace('.', '', 1).isdigit()):
            result = calculate(float(expression[0]), float(expression[1]), expression[2])
            stack.append(result)
            finalResults.append(result)

        elif expression[1] == 'MEM':
            memory = float(expression[0])
            stack.append(memory)

        elif expression[0] == 'MEM':
            result = calculate(memory, float(expression[1]), expression[2])
            stack.append(result)
            finalResults.append(result)

        elif expression[1] == 'RES':
            result = calculate(float(stack[int(expression[0])]), float(expression[2]), expression[3])
            finalResults.append(result)
            stack.append(result)
    
    return str(result)

calculateExpressions(expressions)
print(finalResults)