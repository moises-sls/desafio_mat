import random
import time

OPERATORS = ['+', '-', "*"]
MIN_OPERAND = 1
MAX_OPERAND = 15
TOTAL_PROBLEMS = 5


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) # escolhe um elemento aleatório da lista


    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) # calcula a expressao 
    return expr, answer



wrong = 0

input("Pressione enter para começar!")
print("-----------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()

    while True:
        guess = input("Problema #" + str(i+1) + ": " + expr + " = ")
        
        if guess == str(answer): # transformamos o resultado da expressao em 
            break                #string, ja que esse valor sempre sera numérico
                                 # se tentarmos transformar a resposta em int
                                 # poderiamos encontrar erros, se o input for uma letra, por exemplo
        wrong += 1
            

end_time = time.time()
total_time = round(end_time-start_time, 2)

print("-----------------------------")
print("Você terminou em", total_time, "segundos! A quantidade de erros foi:", wrong)