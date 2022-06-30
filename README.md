# Projeto API Log | Desafio de Programação Zedia

API REST desenvolvida em Linguagem Python versão 3.9.1, com os seguinte Frameworks: 

    - Django==3.2.13 (LTS)
    - django_filters
    - djangorestframework==3.13.1

+ Lista completa de dependencias, encontra-se no arquivo **requirements.txt**
+ A Pasta *core* corresponde a pasta do APP e a pasta *log* do projeto

## Autenticação
*API Log* permite autenticação via Token e Via sessão com algumas restrições a seguir:

    - A usuários anônimos permite somente leitura metodo:[GET].
    - Para os métodos [POST, UPDATE, DELETE] está habilitado a usuários autenticados.

Para fins de acesso fácil e avaliação da API REST, segue abaixo o nome de usuário SuperUser e Senha. Assim como seu respectivo Token.

    + usuário: admin
    + senha: 123a456b789c
    + Token: 35c88acea4cd16261767da65df9b53844e7f873d

## Autorização
Está autorizada as requisições a API à usuários:
+ anônimos: 5/minuto 
+ autenticados: 10/minuto

## Versionamento
A API fora versionada em dois paradigmas:

    /api/v1/{ENDPOINT} -> Abordagem e por métodos
    /api/v2/{ENDPOINT} - Abordagem a Objetos

### *IMPORTANTE*
RECOMENDAMOS A UTILIZAÇÃO DA **VERSÃO 2** /api/v2/, POIS CONTEMPLA MAIS FUNCIONALIDADES. 

E POR ESSE MOTIVO, ABORDAREMOS SOMENTE A UTILIZAÇÃO DESTA ÚLTIMA VERSÃO.

## Porta do Servidor

Está configurada na porta 8008 assim como mostrada a URL Abaixo:

    http://127.0.0.1:8008

# API Root [/]
Pontos de entrada da API
## URI/End Points

    /api/v2/visits/ -> Retorna todas as visitas [GET]
    
    /api/v2/workspaces/ -> Retorna todos workspaces [GET] - PERMITE métodos [POST, HEAD, OPTIONS] 
    
    /api/v2/workspaces/{workspace_id} -> Retorna workspace pelo id [GET].PERMITE: [GET, PUT, PATCH, DELETE, HEAD, OPTIONS] a partir deste endpoint
    /api/v2/workspaces/1/{visits_id}

    /api/v2/workspaces/{workspace_id}/visits -> Retorna todas as visitas daquele determinado {workspace_id}.

    /api/v2/visits/?data=2022-06-28 -> Retorna todas as visitas daquela determinada data especificada.

    /api/v2/visits/?depth=1 -> Configura o retorno do JSON no campo workspace da tabela visits. Para detalhamento sobre aquele determinado workspace. Caso queria fazer um POST, UPDATE ou DELETE; necessário depth=0

    /admin/ -> Administração Django

# Modo de Utilização.

Depois de ter clonado o repositório em sua máquina:
Execute o comando no Terminal, dentro da pasta do repositório:

    1. source venv/bin/activate -> Ativar o ambiente virtual
    2. python manage.py runserver -> Rodar o Servidor local
    3. Acessar o endereço desejado. Exemplo:
        http://127.0.0.1:8008/api/v2/workspaces/