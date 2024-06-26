[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/seu-usuario/seu-repositorio)
[![Total Downloads](https://img.shields.io/badge/downloads-100k-blue)](https://github.com/seu-usuario/seu-repositorio)
[![Latest Stable Version](https://img.shields.io/badge/version-1.0.0-orange)](https://github.com/seu-usuario/seu-repositorio)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/seu-usuario/seu-repositorio/blob/main/LICENSE)


# Automatização Contábil

Este é um projeto Python para automatização contábil, que calcula o saldo total das transações a partir de um arquivo CSV de entrada e salva o saldo total em outro arquivo CSV.

# Exeplo gráfico
<div style='display: flex; justify-content: center;'>
  <img width=1200 src='https://github.com/lucasbezerrapro/automa-o_de_demonstra-o_contabil/blob/main/img/exemplo.jpg?raw=true'>
</div>

## Funcionalidades

- Calcula o saldo total das transações a partir de um arquivo CSV de entrada.
- Salva o saldo total em um arquivo CSV de saída.
- Exibe o saldo total formatado em uma tabela no terminal.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - [pandas](https://pandas.pydata.org/): Para manipulação de dados tabulares.
  - [tabulate](https://pypi.org/project/tabulate/): Para exibir dados tabulares formatados no terminal.
  - [colorama](https://pypi.org/project/colorama/): Para adicionar cores ao texto no terminal.

## Como Usar

1. Instale as dependências necessárias:
```bash
   pip install pandas tabulate colorama
   ```

2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

3. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```

4. Execute o script `automatiza-trabalho.py`:
   ```bash
   python automatiza-trabalho.py
   ```

5. Insira o arquivo CSV de transações quando solicitado.

6. O saldo total será calculado e salvo em um novo arquivo CSV chamado `saldo_total.csv`, e também será exibido formatado em uma tabela no terminal.

## Exemplo de Arquivo CSV de Transações

O arquivo CSV de transações deve conter duas colunas: "data" e "valor", conforme o exemplo abaixo:

```csv
data,descricao,valor
2024-05-01,Compra no supermercado,50.00
2024-05-02,Recebimento de salário,2000.00
2024-05-03,Pagamento de aluguel,800.00
2024-05-04,Compra online,120.00
2024-05-05,Depósito em conta poupança,500.00
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
