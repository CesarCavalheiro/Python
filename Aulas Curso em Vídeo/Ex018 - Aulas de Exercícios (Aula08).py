from math import sin,cos,tan,radians
angulo = float(input('Digite seu ângulo: '))
print(f"""Para o ângulo de {angulo}º 
seu seno é: {sin(radians(angulo)):.2f}
seu cosseno é: {cos(radians(angulo)):.2f}
e sua tangente é: {tan(radians(angulo)):.2f}""")