import csv
import pandas as pd
from tabulate import tabulate
from colorama import init, Fore

def calcular_saldo(transacoes):
    saldo = sum(float(transacao['valor']) for transacao in transacoes)
    return saldo

def salvar_saldo_csv(saldo_total, arquivo_saida):
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Descrição', 'Valor'])
        writer.writerow(['Saldo Total das Transações', saldo_total])
    print(f"Saldo total salvo em '{arquivo_saida}'")

def ler_saldo_csv(arquivo_entrada):
    df = pd.read_csv(arquivo_entrada, encoding='utf-8')
    descricao = df.columns[0]  # Obtém o nome da primeira coluna
    saldo_total = df.iloc[0, 1]  # Obtém o valor da primeira linha, segunda coluna
    return descricao, saldo_total


def main():
    arquivo_csv = 'transacoes.csv'
    arquivo_saida = 'saldo_total.csv'

    transacoes = []
    with open(arquivo_csv, newline='') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            transacoes.append(linha)

    saldo_total = calcular_saldo(transacoes)

    salvar_saldo_csv(saldo_total, arquivo_saida)

    descricao, saldo_total_csv = ler_saldo_csv(arquivo_saida)

    tabela = [["Descrição", "Valor"],
              [Fore.BLUE + descricao, Fore.GREEN + f"R${saldo_total_csv:.2f}"]]

    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))

if __name__ == "__main__":
    init(autoreset=True)
    main()
