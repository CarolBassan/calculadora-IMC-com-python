altura = float(input ('Qual é a sua altura em cm: '))
peso = float(input ('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2

print ('O seu IMC é: ', IMC)

if IMC < 18.5:
    print ('Você está abaixo do peso')

elif IMC >= 18.5 and IMC < 25:
    print ('Você está no peso ideal')

elif IMC >= 25 and IMC < 30:
    print ('Você está com sobrepeso')

elif IMC >= 30 and IMC < 35:
    print ('Você está com obesidade grau I')

else:
    print ('Pode parar de comer e começar a malhar pois o negócio esta feio! Obesidade Grave')