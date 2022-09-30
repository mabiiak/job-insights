# Boas-vindas ao projeto Job Insights

  Projeto feito durante o curso de desenvolvimento web na trybe.
  
  Neste projeto foi implementado análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python).

  ## Habilidades a serem trabalhadas:

 - Utilizar o terminal interativo do Python.
    
 - Utilizar estruturas condicionais e de repetição.
    
- Utilizar funções built-in do Python.
    
- Utilizar tratamento de exceções.
    
- Realizar a manipulação de arquivos.
    
- Escrever funções.
    
- Escrever testes com Pytest.
    
- Escrever seus próprios módulos e importá-los em outros códigos.


# Desenvolvimento
<details>
  <summary>
    <h3>
      Antes de começar a desenvolver
    </h3>
    </summary>

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:mabiiak/job-insights.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd job-insights`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `main`

  - Verifique que você está na branch `main`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `main`
    - Exemplo: `git checkout main`
  - Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
    - Exemplo: `git checkout -b nome-job-insights`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'descrição do commit'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin nome-job-insights`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/mabiiak/job-insights/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/mabiiak/job-insights/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong> Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

## Requisitos

    ✅ 1 - Implemente a função `read`

    ✅ 2 - Implemente a função `get_unique_job_types`

    ✅ 3 - Implemente a função `get_unique_industries`

    ✅ 4 - Implemente a função `get_max_salary`

    ✅ 5 - Implemente a função `get_min_salary`

    ✅ 6 - Implemente a função `filter_by_job_type`

    ✅ 7 - Implemente a função `filter_by_industry`

    ✅ 8 - Implemente a função `matches_salary_range`

    ❌ 9 - Implemente a função `filter_by_salary_range`

    ✅ 10 - Implemente um teste para a função `count_ocurrences`

    ✅ 11 - Implemente um teste para a função `read_brazilian_file`

    ❌ 12 - Implemente um teste para a função `sort_by`

## Bônus

    ❌ 13 - (`Bônus`) Implemente a página de um job
          13.1 - Crie a rota /job recebendo o parâmetro index

          13.2 - Crie a view job, recebendo o parâmetro index

          13.3 - Implemente view job para que ela retorne status code 200 para jobs válidos

          13.4 - Implemente view job de forma a retornar o HTML exato de uma página de job
