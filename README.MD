# Gerador de CPF Aleatório

Este é um programa em Python que gera CPFs aleatórios com e sem marcação. O CPF é um número de identificação utilizado no Brasil.

## Como usar

1. Certifique-se de ter o Python instalado em seu computador.
2. Abra o arquivo do código-fonte em um editor de texto ou ambiente de desenvolvimento Python.

### Executando o programa

1. Execute o código-fonte e aguarde a exibição do menu.
2. Digite o número correspondente à opção desejada:
   - Digite `1` para gerar um CPF com marcação.
   - Digite `2` para gerar um CPF sem marcação.
   - Digite `3` para sair do programa.
3. Após fazer sua escolha, o programa irá gerar e exibir um CPF aleatório de acordo com a opção selecionada.
4. Repita os passos 2 e 3 para gerar CPFs adicionais ou sair do programa.

## Detalhes do código

O código utiliza a biblioteca `random` do Python para gerar números aleatórios. Ele possui um loop infinito que exibe um menu e aguarda a entrada do usuário. Dependendo da opção selecionada, o programa gera um CPF com ou sem marcação. O CPF gerado é exibido na tela.

### Opção 1 - Gerar CPF com marcação

Nesta opção, o código itera sobre os 11 dígitos do CPF e adiciona pontos (`.`) e um traço (`-`) nos locais corretos para criar a marcação padrão do CPF brasileiro.

### Opção 2 - Gerar CPF sem marcação

Nesta opção, o código simplesmente gera 11 dígitos aleatórios para criar um CPF sem marcação.

### Opção 3 - Sair

Esta opção encerra a execução do programa.

Se uma opção inválida for digitada, o programa exibirá uma mensagem de erro.

**Observação:** Este programa gera CPFs aleatórios e não garante a validade ou unicidade dos mesmos.