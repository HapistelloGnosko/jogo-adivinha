import random

NIVEIS = {
    "1": ("Fácil",   1, 50,  10),
    "2": ("Normal",  1, 100,  7),
    "3": ("Difícil", 1, 200,  5),
}

def jogar(minimo, maximo, tentativas_max):
    numero = random.randint(minimo, maximo)
    tentativas = 0

    print(f"\nAdivinhe um número entre {minimo} e {maximo}. Você tem {tentativas_max} tentativas.\n")

    while tentativas < tentativas_max:
        try:
            chute = int(input(f"Tentativa {tentativas + 1}/{tentativas_max}: "))
        except ValueError:
            print("Digite um número inteiro.")
            continue

        tentativas += 1

        if chute == numero:
            print(f"\nCerto! Você acertou em {tentativas} tentativa(s).")
            return True
        elif chute < numero:
            print("Muito baixo.")
        else:
            print("Muito alto.")

    print(f"\nGame over. O número era {numero}.")
    return False

def main():
    print("=== Adivinhe o Número ===")

    while True:
        print("\nNível:\n1. Fácil\n2. Normal\n3. Difícil\n0. Sair")
        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            break

        if escolha not in NIVEIS:
            print("Opção inválida.")
            continue

        nome, minimo, maximo, tentativas = NIVEIS[escolha]
        print(f"\nNível: {nome}")
        jogar(minimo, maximo, tentativas)

        novamente = input("\nJogar novamente? (s/n): ").strip().lower()
        if novamente != "s":
            break

if __name__ == "__main__":
    main()
