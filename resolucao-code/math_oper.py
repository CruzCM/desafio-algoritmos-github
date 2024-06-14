numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    # Verifica se o denominador não é zero antes de realizar a divisão
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."

print("O resultado da operação é:", resultado)
