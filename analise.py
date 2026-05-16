import pandas as pd
from collections import Counter
from itertools import combinations
from math import comb

# ==========================================================
# LEITURA DOS RESULTADOS
# ==========================================================

df = pd.read_excel("Lotofácil.xlsx")

# Ajuste caso suas colunas sejam diferentes
colunas_numeros = df.columns[2:17]

# ==========================================================
# ANÁLISE DE FREQUÊNCIA
# ==========================================================

frequencia = Counter()

for _, linha in df.iterrows():

    numeros = linha[colunas_numeros].tolist()

    frequencia.update(numeros)

# ==========================================================
# ANÁLISE DOS PARES
# ==========================================================

pares = Counter()

for _, linha in df.iterrows():

    numeros = sorted(linha[colunas_numeros].tolist())

    for par in combinations(numeros, 2):

        pares[par] += 1

# ==========================================================
# JOGO SUGERIDO
# ==========================================================

mais_frequentes = [num for num, _ in frequencia.most_common(15)]

# ==========================================================
# DADOS OFICIAIS
# ==========================================================

dados_apostas = {

    15: {
        "valor": 3.50,
        "chance_15": 3268760
    },

    16: {
        "valor": 56.00,
        "chance_15": 204298
    },

    17: {
        "valor": 476.00,
        "chance_15": 24035
    },

    18: {
        "valor": 2856.00,
        "chance_15": 4006
    },

    19: {
        "valor": 13566.00,
        "chance_15": 843
    },

    20: {
        "valor": 54264.00,
        "chance_15": 211
    }
}

# ==========================================================
# 50 JOGOS GERADOS
# ==========================================================

jogos = [

[1, 2, 3, 4, 5, 7, 8, 9, 11, 15, 16, 19, 22, 24, 25],
[1, 2, 3, 5, 6, 8, 9, 10, 12, 14, 16, 18, 21, 23, 25],
[1, 3, 4, 6, 7, 8, 10, 11, 13, 15, 17, 18, 20, 22, 24],
[2, 4, 5, 6, 7, 9, 11, 12, 13, 15, 16, 18, 19, 23, 25],
[1, 2, 4, 5, 7, 8, 10, 12, 14, 15, 17, 19, 21, 24, 25],
[2, 3, 5, 6, 8, 9, 11, 13, 14, 16, 17, 20, 22, 23, 25],
[1, 3, 4, 5, 7, 9, 10, 11, 13, 15, 18, 19, 20, 24, 25],
[1, 2, 4, 6, 7, 8, 9, 12, 13, 14, 16, 18, 21, 22, 25],
[2, 3, 4, 5, 6, 8, 10, 11, 14, 15, 17, 19, 20, 23, 24],
[1, 2, 3, 5, 7, 9, 11, 12, 13, 16, 18, 20, 21, 24, 25],

[1, 4, 5, 6, 8, 9, 10, 12, 14, 15, 17, 19, 22, 23, 25],
[2, 3, 4, 6, 7, 8, 11, 13, 15, 16, 18, 20, 21, 24, 25],
[1, 2, 5, 6, 7, 9, 10, 11, 14, 15, 17, 18, 20, 22, 24],
[1, 3, 4, 5, 8, 9, 12, 13, 14, 16, 18, 19, 21, 23, 25],
[2, 3, 4, 6, 7, 10, 11, 12, 13, 15, 17, 20, 22, 24, 25]

]

# ==========================================================
# GERAÇÃO DO TXT
# ==========================================================

with open(
    "Analise_Lotofacil.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        " ANÁLISE ESTATÍSTICA LOTOFÁCIL\n"
    )

    arquivo.write(
        "==================================================\n\n"
    )

    # ======================================================
    # NÚMEROS MAIS SORTEADOS
    # ======================================================

    arquivo.write(
        "NÚMEROS MAIS SORTEADOS:\n\n"
    )

    for numero, freq in frequencia.most_common():

        arquivo.write(
            f"Número {numero}: {freq} vezes\n"
        )

    arquivo.write("\n")

    # ======================================================
    # PARES MAIS FREQUENTES
    # ======================================================

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        "PARES MAIS FREQUENTES:\n\n"
    )

    for par, freq in pares.most_common(20):

        arquivo.write(
            f"{par}: {freq} vezes\n"
        )

    arquivo.write("\n")

    # ======================================================
    # JOGO SUGERIDO
    # ======================================================

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        "JOGO SUGERIDO:\n\n"
    )

    arquivo.write(
        f"{sorted(mais_frequentes)}\n\n"
    )

    # ======================================================
    # CUSTO BENEFÍCIO
    # ======================================================

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        "CUSTO BENEFÍCIO:\n\n"
    )

    for qtd, info in dados_apostas.items():

        arquivo.write(
            f"{qtd} números -> "
            f"Valor: R$ {info['valor']:.2f} | "
            f"15 pontos: 1 em {info['chance_15']:,}\n"
        )

    arquivo.write("\n")

    # ======================================================
    # EXPLICAÇÃO DAS PROBABILIDADES
    # ======================================================

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        "COMO FUNCIONAM AS PROBABILIDADES:\n\n"
    )

    arquivo.write(
        "As probabilidades NÃO são baseadas em\n"
    )

    arquivo.write(
        "quantidade de pessoas jogando.\n\n"
    )

    arquivo.write(
        "Elas são calculadas matematicamente\n"
    )

    arquivo.write(
        "usando análise combinatória.\n\n"
    )

    arquivo.write(
        "Exemplo:\n"
    )

    arquivo.write(
        "Uma aposta simples de 15 números possui:\n\n"
    )

    arquivo.write(
        "1 chance em 3.268.760\n\n"
    )

    # ======================================================
    # 50 JOGOS
    # ======================================================

    arquivo.write(
        "==================================================\n"
    )

    arquivo.write(
        "SUGESTÕES DE JOGOS:\n\n"
    )

    for i, jogo in enumerate(jogos, start=1):

        arquivo.write(
            f"{i}. {jogo}\n"
        )

print("\nArquivo TXT gerado com sucesso!")
print("Arquivo: Analise_Lotofacil.txt")

# ==========================================================
# PARTE INTERATIVA
# ==========================================================

print("\n==================================================")
print(" ANÁLISE PERSONALIZADA ")
print("==================================================\n")

qtd_aposta = int(
    input("Quantos números deseja apostar? (15 a 20): ")
)

# ==========================================================
# VALIDAÇÃO
# ==========================================================

if qtd_aposta < 15 or qtd_aposta > 20:

    print("Quantidade inválida!")
    exit()

# ==========================================================
# ENTRADA DOS NÚMEROS
# ==========================================================

numeros_usuario = []

print("\nDigite os números da aposta:\n")

while len(numeros_usuario) < qtd_aposta:

    numero = int(
        input(f"{len(numeros_usuario)+1}º número: ")
    )

    # ======================================================
    # VALIDAÇÕES
    # ======================================================

    if numero < 1 or numero > 25:

        print("Número inválido!")
        continue

    if numero in numeros_usuario:

        print("Número repetido!")
        continue

    numeros_usuario.append(numero)

    # ======================================================
    # MOSTRA ESTATÍSTICAS DO NÚMERO
    # ======================================================

    freq = frequencia[numero]

    ranking = list(
        dict(frequencia.most_common()).keys()
    ).index(numero) + 1

    print(
        f"Número {numero} apareceu "
        f"{freq} vezes."
    )

    print(
        f"Ranking histórico: "
        f"{ranking}º mais sorteado.\n"
    )

# ==========================================================
# CÁLCULO DAS PROBABILIDADES
# ==========================================================

total_combinacoes = comb(25, 15)

# ==========================================================
# CHANCE DE 15 ACERTOS
# ==========================================================

prob_15 = 1 / dados_apostas[qtd_aposta]["chance_15"]

# ==========================================================
# CHANCE DE 14 ACERTOS
# ==========================================================

acertos_14 = (
    comb(qtd_aposta, 14)
    * comb(25 - qtd_aposta, 1)
)

prob_14 = acertos_14 / total_combinacoes

# ==========================================================
# RESULTADO FINAL
# ==========================================================

print("\n==================================================")
print(" RESULTADO DA ANÁLISE ")
print("==================================================\n")

print("Números escolhidos:\n")

print(sorted(numeros_usuario))

print("\n--------------------------------------------------")

print("Chance de 15 pontos:\n")

print(
    f"1 em "
    f"{dados_apostas[qtd_aposta]['chance_15']:,}"
)

print(f"{prob_15 * 100:.10f}%")

print("\n--------------------------------------------------")

print("Chance estimada de 14 pontos:\n")

print(f"1 em {int(1 / prob_14):,}")

print(f"{prob_14 * 100:.8f}%")

print("\n--------------------------------------------------")

print("Valor da aposta:\n")

print(
    f"R$ "
    f"{dados_apostas[qtd_aposta]['valor']:.2f}"
)

# ==========================================================
# ANÁLISE HISTÓRICA
# ==========================================================

contador_acertos = []

for _, linha in df.iterrows():

    sorteados = set(
        linha[colunas_numeros].tolist()
    )

    acertos = len(
        set(numeros_usuario) & sorteados
    )

    contador_acertos.append(acertos)

maior = max(contador_acertos)

print("\n==================================================")
print(" ANÁLISE HISTÓRICA ")
print("==================================================\n")

print(
    f"Maior quantidade de acertos "
    f"já registrada: {maior}"
)

print("\nDistribuição histórica:\n")

for i in range(max(contador_acertos), 0, -1):

    qtd = contador_acertos.count(i)

    if qtd > 0:

        print(f"{i} acertos -> {qtd} concursos")

print("\n==================================================")
print(" FIM DA ANÁLISE ")
print("==================================================")