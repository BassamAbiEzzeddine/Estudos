import math
x= math.radians(float(input('Insira seu angulo : ')))
x1 = (math.sin(x))
x2 = (math.cos(x))
x3 = (math.tan(x))
print('O seno do seu angulo e {:.2f} \n O coseno do seu angulo e {:.2f} \n A tangente do seu angulo e {:.2f}'.format(x1,x2,x3))