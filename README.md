# Flask parte 1: Crie uma webapp com Python 3

# Aulas

## Curso ['Flask parte 1: Crie uma webapp com Python 3'](https://cursos.alura.com.br/course/flask-rotas-templates-autenticacao)

<details>
    <summary>Criando uma aplicação web super rápido</summary>
    <ul>
        <li>Introdução</li>
        <li>Primeira aplicação</li>
        <li>A ferramenta PIP</li>
        <li>Adicionando um pacote ao projeto</li>
        <li>Para saber mais: Definindo versões com o PIP</li>
        <li>Mostrando página HTML</li>
        <li>Criação de aplicação com página web</li>
        <li>Para saber mais: Definindo portas para aplicação</li>
        <li>Mãos na massa: Criando uma aplicação</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Listando jogos usando Flask</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Adicionando conteúdo dinâmico</li>
        <li>Passando variáveis para o HTML</li>
        <li>Pegando lista do servidor</li>
        <li>Deixando valores dinâmicos</li>
        <li>Deixando mais orientado à objetos</li>
        <li>Mostrando atributos na view</li>
        <li>Executando lógicas na view</li>
        <li>Para saber mais: Filtrando dados de templates</li>
        <li>Mãos na massa: Mostrando jogos do servidor</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Criação de um novo Jogo</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Criar um novo Jogo</li>
        <li>Montando um formulário no flask</li>
        <li>Criando o formulário</li>
        <li>Resolvendo um POST no servidor</li>
        <li>Configurando o servidor para as requisições</li>
        <li>Recarregando automaticamente</li>
        <li>Mãos na massa: Adicionando jogos</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Melhorando o código e a usabilidade</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Redirecionando para outra página</li>
        <li>Redirecionando</li>
        <li>Estilizando com Bootstrap</li>
        <li>Adicionando CSS</li>
        <li>Reutilizando partes do template</li>
        <li>Evitando re-trabalho</li>
        <li>Gerando URLs dinâmicas</li>
        <li>Melhorando mais o projeto</li>
        <li>Mãos na massa: Reduzindo a duplicação nos templates</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Autenticando usuários com sessão do Flask</summary>
    <ul>
        <li>Preparando o ambiente</li>
        <li>Criando tela de Login</li>
        <li>Criando um formulário de login</li>
        <li>Guardando dados na sessão</li>
        <li>Colocando dados em sessão</li>
        <li>Recuperando dados da sessão na view</li>
        <li>Deslogar da sessão</li>
        <li>Mãos na massa: Fazendo autenticação</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Implementando autorização para criar Jogos</summary>
    <ul>
        <li>Preparando o ambiente</li>
        <li>Protegendo uma rota</li>
        <li>Bloqueando quem não estiver logado.</li>
        <li>Melhorando o fluxo de login</li>
        <li>Recuperando dados da query string</li>
        <li>Mais URLs dinâmicas</li>
        <li>Usando urls dinâmicas para as rotas</li>
        <li>Múltiplos usuários</li>
        <li>Mãos na massa: Autorização de usuários</li>
        <li>O que aprendemos?</li>
        <li>Download do projeto final</li>
        <li>Conclusão</li>
    <ul>
</details>

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

🚀 :clap: Para visualizar o sistema basta acessar no navegador no endereço: [localhost:3000](http://localhost:3000)


# Referências utilizadas

[1° Containerized Python Web App(conteinerização de aplicação Web em Python)](https://github.com/claudimf/containerized_python_web_app) 

[2° Docker Compose with Flask Apps](https://runnable.com/docker/python/docker-compose-with-flask-apps)

[3° Flask](https://github.com/pallets/flask)