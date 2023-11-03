def calcula_vitorias(vitorias, derrotas):
    return vitorias - derrotas


vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

resultado = calcula_vitorias(vitorias, derrotas)

if resultado < 10:
    print("Você é Ferro e o saldo de vitórias é: ", resultado)
elif 10 <= resultado < 20:
    print("Você é Bronze e o saldo de vitórias é: ", resultado)
elif 20 <= resultado < 50:
    print("Você é Prata e o saldo de vitórias é: ", resultado)
elif 50 <= resultado < 80:
    print("Você é Ouro e o saldo de vitórias é: ", resultado)
elif 80 <= resultado < 90:
    print("Você é Diamante e o saldo de vitórias é: ", resultado)
elif 90 <= resultado < 100:
    print("Você é Lendário e o saldo de vitórias é: ", resultado)
else:
    print("Você é Imortal e o saldo de vitórias é: ", resultado)
