
# **loginform_kivy**

Este projeto é uma implementação simples de um **formulário de login** utilizando o framework **Kivy**. O Kivy é uma biblioteca Python de código aberto que facilita o desenvolvimento de aplicações móveis e desktop com interfaces gráficas (GUI). Este exemplo permite que os usuários criem contas, façam login e visualizem as informações de sua conta.

## **Funcionalidades**

- **Tela de Login**: O usuário pode realizar o login inserindo seu email e senha. A aplicação valida os dados fornecidos e, em caso de sucesso, redireciona o usuário para a tela principal.
- **Tela de Criação de Conta**: Permite que o usuário cadastre um novo nome, email e senha.
- **Tela Principal**: Exibe informações da conta do usuário, como nome, email e data de criação da conta.
- **Validação de Entrada**: Validação de email e senha durante o login, além de mensagens de erro caso algum campo não seja preenchido corretamente.

## **Tecnologias Utilizadas**

- **Kivy**: Framework para a criação de interfaces gráficas ricas e multi-touch.
- **Python**: Linguagem de programação utilizada para o desenvolvimento da aplicação.
- **SQLite** (opcional): Banco de dados utilizado para armazenar informações dos usuários (caso implementado).

## **Arquitetura do Projeto**

- **app.py**: Arquivo principal contendo a lógica do aplicativo, incluindo a implementação das telas de criação de conta, login e a tela principal.
- **my.kv**: Arquivo de layout que define a interface gráfica da aplicação usando a linguagem de marcação do Kivy.
- **database.py** (opcional): Módulo responsável pela manipulação de dados, armazenamento de informações de usuários e gerenciamento do banco de dados (caso implementado).

## **Como Executar**

### Instalação

1. Instale as dependências necessárias utilizando o `pip`:
   ```bash
   pip install kivy
   ```

2. Clone este repositório ou faça o download do código.

3. Para rodar a aplicação, execute o arquivo `app.py` com o comando:
   ```bash
   python app.py
   ```

## **Estrutura de Diretórios**

A estrutura de arquivos do projeto é a seguinte:

```
loginform_kivy/
├── app.py              # Lógica principal da aplicação
├── my.kv               # Layout da interface gráfica
├── database.py         # Gerenciamento de banco de dados (se implementado)
└── README.md           # Documentação do projeto
```


