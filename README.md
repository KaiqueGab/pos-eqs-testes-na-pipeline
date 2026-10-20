# Testes da Calculadora na Pipeline

Projeto utilizado na disciplina de Estratégias Modernas de Teste de Software
da PUC Minas. O projeto contém uma calculadora simples em Python, testes
automatizados com `pytest` e geração de relatórios com Allure.

[![CI - Testes Automatizados](https://github.com/KaiqueGab/pos-eqs-testes-na-pipeline/actions/workflows/ci.yaml/badge.svg)](https://github.com/KaiqueGab/pos-eqs-testes-na-pipeline/actions/workflows/ci.yaml)

## Estrutura do projeto

```text
calculadora/
├── app.py
└── test_calculadora.py
allure-results/
README.md
```

## Pré-requisitos

- Python 3.13 ou superior
- Java instalado, necessário para executar o Allure
- Node.js e npm, necessários para instalar o Allure Commandline

Verifique as instalações:

```powershell
python --version
java -version
node --version
npm.cmd --version
```

## Instalação das dependências

Na raiz do projeto, execute:

```powershell
python -m pip install --upgrade pip
python -m pip install pytest allure-pytest
```

O código da calculadora não possui dependências externas. Os pacotes acima são
usados pelos testes e pela geração dos resultados do Allure.

### Instalação do Allure Commandline

Instale o Allure Commandline globalmente com npm:

```powershell
npm.cmd install --global allure-commandline
```

Confirme a instalação:

```powershell
allure --version
```

> No Windows, o PowerShell pode bloquear o arquivo `npm.ps1` por causa da
> política de execução de scripts. Nesse caso, use `npm.cmd` nos comandos npm.

## Executando os testes

Para executar os testes sem gerar relatório Allure:

```powershell
python -m pytest calculadora\test_calculadora.py
```

Para executar os testes e gerar os resultados do Allure:

```powershell
python -m pytest calculadora\test_calculadora.py --alluredir=allure-results
```

## Visualizando o relatório Allure

Depois de gerar os resultados, inicie um servidor temporário e abra o relatório
no navegador:

```powershell
allure serve allure-results
```

Se o comando `allure` não for reconhecido, use:

```powershell
allure.cmd serve allure-results
```

Para gerar um relatório permanente na pasta `reports`:

```powershell
allure generate allure-results --clean -o reports
allure open reports
```

## Execução rápida

Com Python, Java, Node.js, pytest, allure-pytest e Allure Commandline já
instalados:

```powershell
python -m pytest calculadora\test_calculadora.py --alluredir=allure-results
allure serve allure-results
```

## Integração contínua

O workflow do GitHub Actions executa automaticamente os testes em eventos de
`push`, `pull_request` para a branch `main` e execução manual. Consulte o
arquivo [ci.yaml](.github/workflows/ci.yaml) para mais detalhes.
    