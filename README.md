#loginform_kivy
Este é um projeto simples de formulário de login desenvolvido com o framework Kivy, que é uma biblioteca Python de código aberto para o desenvolvimento de aplicações móveis e desktop. O projeto utiliza uma interface gráfica (GUI) para permitir a criação de contas de usuários e o login em uma aplicação fictícia. A aplicação possibilita interações de cadastro, login e exibição de informações de conta.

- Funcionalidades:
  Tela de Login: O usuário pode fazer login inserindo um email e senha. O login é validado e, se correto, a aplicação redireciona o usuário para a tela principal.

- Tecnologias Utilizadas
Kivy: Framework para criação de interfaces gráficas.
Python: Linguagem de programação utilizada para o desenvolvimento.

-Arquitetura do Projeto
Main.py: Arquivo principal que contém a lógica do aplicativo, incluindo a implementação das telas de criação de conta, login e a tela principal.
My.kv: Arquivo de design, onde a interface gráfica é definida utilizando a linguagem de marcação do Kivy.
Database.py: Módulo (caso implementado) para gerenciamento de banco de dados e armazenamento de informações de usuários.

#Como Executar
Instale as dependências necessárias:
pip install kivy

-Para rodar a aplicação, execute o arquivo app.py:

bash
Copiar
Editar
python app.py
Estrutura de Diretórios
scss
Copiar
Editar
loginform_kivy/
├── app.py
├── my.kv
├── database.py  (se implementado)
└── README.md
