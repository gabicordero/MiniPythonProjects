import time
import random

def get_divisor(n):
    '''
    Obtener un divisor random de n
    :param n: The number
    :return: a divisor of n
    '''
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)

if __name__ == '__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    correct = 0
    questions = []
    # bucle while, mientras segundos es menos que 60
    while time.time() - start_time <= 60:
        a = random.randint(1, 99)
        op = random.choice(ops)
        if op == '/':
            # si op es '/' entonces b es un divisor de a
            b = get_divisor(a)
        else:
            b = random.randint(1, 99)
        # Obtener la respuesta correcta
        a_op_b = '{}{}{}'.format(a, op, b)
        c = int(eval(a_op_b))

        # Let user input answer
        try:
            ans = int(input('{} = '.format(a_op_b)))
        except:
            ans = ''

        # Para chequear si es correcta o no
        if time.time() - start_time <= 60:
            if c == ans:
                print('Correcto! Tiempo restante {} segundos'.format(int(60 - (time.time() - start_time))))
                correct = correct + 1
            else:
                print('Respuesta incorrecta! Tiempo restante {} segundos.'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{}={}'.format(a_op_b, ans))

    print('{} preguntas y tu puntaje actual es {:.2f}%'.format(total, correct / total * 100))
    for q in questions:
        print(q)
