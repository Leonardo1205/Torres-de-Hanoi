def torre_hanoi(n, origem, destino, auxiliar, contador):
    if n == 1:
        print(f"➡️  Mova o disco 1 de {origem} para {destino}")
        contador[0] += 1
        return
    torre_hanoi(n - 1, origem, auxiliar, destino, contador)
    print(f"➡️  Mova o disco {n} de {origem} para {destino}")
    contador[0] += 1
    torre_hanoi(n - 1, auxiliar, destino, origem, contador)

if __name__ == '__main__':
    print("🎮 Bem-vindo ao Jogo das Torres de Hanoi! 🎮")
    print("""
    🏰 Regras do Jogo:
    - Mova todos os discos da torre de origem para a torre de destino.
    - Apenas um disco pode ser movido por vez.
    - Um disco maior nunca pode ser colocado sobre um menor.
    - Utilize a torre auxiliar para ajudar nas movimentações.
    """)
    try:
        n = int(input("Digite o número de discos (positivo): "))
        if n <= 0:
            print("❌ Erro: O número de discos deve ser um inteiro positivo.")
            exit()

        torres_validas = {'A', 'B', 'C'}

        origem = input("Digite a torre de origem (A, B ou C): ").strip().upper()
        if origem not in torres_validas:
            print("❌ Erro: A torre de origem deve ser A, B ou C.")
            exit()

        destino = input("Digite a torre de destino (A, B ou C): ").strip().upper()
        if destino not in torres_validas:
            print("❌ Erro: A torre de destino deve ser A, B ou C.")
            exit()

        auxiliar = input("Digite a torre auxiliar (A, B ou C): ").strip().upper()
        if auxiliar not in torres_validas:
            print("❌ Erro: A torre auxiliar deve ser A, B ou C.")
            exit()

        if len({origem, destino, auxiliar}) != 3:
            print("❌ Erro: As torres de origem, destino e auxiliar devem ser distintas.")
            exit()

        print(f"\n🚀 Iniciando a resolução das Torres de Hanoi com {n} discos...\n")
        contador = [0] 
        torre_hanoi(n, origem, destino, auxiliar, contador)
        print(f"\n✅ Parabéns! Resolução concluída! Total de jogadas: {contador[0]}")

    except ValueError:
        print("❌ Erro: Entrada inválida. Por favor, digite um número inteiro para a quantidade de discos.")
