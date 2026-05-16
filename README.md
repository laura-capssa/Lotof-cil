````markdown id="k7m2qp"
# Lotofácil Analyzer

Sistema desenvolvido em Python para análise estatística da Lotofácil utilizando o histórico oficial de resultados.  
O projeto realiza processamento de dados, cálculos probabilísticos, análise histórica e geração de sugestões de apostas com base em estatísticas dos concursos anteriores.

---

## Objetivo

O objetivo do projeto é fornecer uma ferramenta de apoio para análise matemática e estatística da Lotofácil, permitindo:

- Identificar padrões históricos;
- Verificar frequência dos números sorteados;
- Calcular probabilidades oficiais;
- Comparar custo-benefício entre tipos de apostas;
- Gerar sugestões automáticas de jogos;
- Executar análises personalizadas.

---

# Funcionalidades

## Análise Estatística

- Frequência histórica dos números;
- Ranking dos números mais sorteados;
- Identificação de pares recorrentes;
- Distribuição histórica de acertos.

## Probabilidades Oficiais

Cálculo baseado em análise combinatória oficial da Lotofácil:

| Quantidade de números | Probabilidade de 15 pontos |
|---|---|
| 15 números | 1 em 3.268.760 |
| 16 números | 1 em 204.298 |
| 17 números | 1 em 24.035 |
| 18 números | 1 em 4.006 |
| 19 números | 1 em 843 |
| 20 números | 1 em 211 |

## Análise Personalizada

O usuário pode:

- Escolher entre 15 e 20 números;
- Inserir manualmente os números da aposta;
- Consultar:
  - frequência histórica dos números;
  - ranking estatístico;
  - probabilidade de 14 pontos;
  - probabilidade de 15 pontos;
  - valor oficial da aposta;
  - desempenho histórico da combinação.

## Geração de Relatório

O sistema gera automaticamente um arquivo `.txt` contendo:

- números mais sorteados;
- pares mais frequentes;
- sugestões de jogos;
- análise probabilística;
- estatísticas históricas.

---

# Estrutura do Projeto

```text
lotofacil/
│
├── analise.py
├── Lotofácil.xlsx
├── Analise_Lotofacil.txt
├── .gitignore
└── README.md
```

---

# Tecnologias Utilizadas

## Linguagem

- Python 3

## Bibliotecas

- Pandas
- OpenPyXL
- Collections
- Math
- Itertools

---

# Instalação

## Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/lotofacil.git
```

---

## Acessar a pasta do projeto

```bash
cd lotofacil
```

---

## Criar ambiente virtual

```bash
python3 -m venv venv
```

---

## Ativar ambiente virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install pandas openpyxl
```

---

# Execução

Execute o sistema com:

```bash
python3 analise.py
```

---

# Funcionamento

O sistema realiza a leitura automática da planilha `.xlsx` contendo os resultados históricos da Lotofácil.

Durante a execução são realizadas:

1. Leitura dos concursos;
2. Processamento estatístico;
3. Contagem de frequências;
4. Análise de combinações;
5. Cálculo de probabilidades;
6. Geração do relatório;
7. Execução da análise personalizada interativa.

---

# Sobre as Probabilidades

As probabilidades apresentadas NÃO são baseadas em comportamento humano ou quantidade de jogadores.

Todos os cálculos utilizam:

- análise combinatória;
- estatística matemática;
- probabilidades oficiais da Lotofácil.

---

# Melhorias Futuras

- Interface gráfica;
- Dashboard estatístico;
- Exportação em PDF;
- Geração automática avançada de jogos;
- Visualizações gráficas;
- API REST;
- Machine Learning para padrões estatísticos.

---

# Licença

Projeto desenvolvido para fins educacionais, acadêmicos e de estudo estatístico.
````
