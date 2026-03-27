# Treinamento HTML - Suporte

## Slide 1

Treinamento
HTML
(Suporte)

Outubro

## Slide 2

![Imagem Slide 2](assets/Treinamento_HTML_-_Suporte_slide2_a435bb.jpg)


Visão geral Arquitetura

Componentes

Análise de Erros


Objetivo

## Slide 3

AGENDA

Desenvolvimento HTML

Manutenção/Expedição FrontEnd/BackEnd

Requisição

Ferramentas

I

II

III

IV

V

Dicas

Análise de Erros

VI

## Slide 4

01

Desenvolvimento
HTML

![Imagem Slide 4](assets/Treinamento_HTML_-_Suporte_slide4_925c9f.png)

## Slide 5

DESENVOLVIMENTO HTML

Apresentação


![Imagem Slide 5](assets/Treinamento_HTML_-_Suporte_slide5_ee7aed.png)

Desenvolvimento em Camadas:



![Imagem Slide 5](assets/Treinamento_HTML_-_Suporte_slide5_36dd4e.png)

FrontEnd

BackEnd

## Slide 6

DESENVOLVIMENTO HTML

Apresentação


![Imagem Slide 6](assets/Treinamento_HTML_-_Suporte_slide6_0aedb0.png)

![Imagem Slide 6](assets/Treinamento_HTML_-_Suporte_slide6_05051e.png)

- Desenha Tela
- Componentes

- Controle da Tela
- Pequenas Validações
- Chamada Serviços

- Fachada
- API-REST
- API/DBO

## Slide 7

![Imagem Slide 7](assets/Treinamento_HTML_-_Suporte_slide7_328e56.png)

02

Requisição

## Slide 8

![Imagem Slide 8](assets/Treinamento_HTML_-_Suporte_slide8_d4ceda.png)

REQUISIÇÃO

![Imagem Slide 8](assets/Treinamento_HTML_-_Suporte_slide8_54a298.png)

Fluxo da Informação:

1

2

Menu => Nome Externo
Projeto + Nome Tela

HTML + Arquivo de Controle (TS)

## Slide 9

![Imagem Slide 9](assets/Treinamento_HTML_-_Suporte_slide9_2df5e9.png)

![Imagem Slide 9](assets/Treinamento_HTML_-_Suporte_slide9_0129ed.png)

![Imagem Slide 9](assets/Treinamento_HTML_-_Suporte_slide9_1b16fc.png)

REQUISIÇÃO

Fluxo da Informação:

Serviço + Parâmetros

3

2

Programa Progress

Dados

Dados

1

4

Não roda Progress na máquina do usuário

## Slide 10

![Imagem Slide 10](assets/Treinamento_HTML_-_Suporte_slide10_ca1087.png)

REQUISIÇÃO

Objetivo:

Mensagem


Mensagem: 
1) URL;
2) Método;
3) Corpo (envio/receb);
4) Código de Resposta.


Mensagem

## Slide 11

![Imagem Slide 11](assets/Treinamento_HTML_-_Suporte_slide11_9c184d.png)

REQUISIÇÃO

Mensagem - 1) URL:

URL: 
http://servidor:porta/dts/datasul-rest/resources/prg/área/versão/programa

Exemplos: 
http://vigia:8480/dts/datasul-rest/resources/prg/fin/v1/customer?group=10

http://vigia:8480/dts/datasul-rest/resources/prg/man/v1/machines/1/relation


## Slide 12

![Imagem Slide 12](assets/Treinamento_HTML_-_Suporte_slide12_044270.png)

REQUISIÇÃO

Mensagem - 1) URL - Programa:

http://vigia:8480/dts/datasul-rest/resources/prg/fin/v1/customer

Fachada (THF1)
ou
PRÉ-API-REST (PO-UI)

fin/api/v1/customer.p

Fixo (PO-UI)

## Slide 13

![Imagem Slide 13](assets/Treinamento_HTML_-_Suporte_slide13_d4e12a.png)

REQUISIÇÃO

Mensagem - 1) URL - Parâmetros:

URL: 
dts/datasul-rest/resources/prg/fin/v1/customer/1?fields=code,name&orderBy=name

dts/datasul-rest/resources/prg/fin/v1/accountReceivableDocument/49/executePayment




Tipos de Parâmetros:

PathParam:
Logo de depois do Programa;
Os parâmetros são separados por “/”;
Pode indicar um código ou uma Ação de Negócio.

## Slide 14

![Imagem Slide 14](assets/Treinamento_HTML_-_Suporte_slide14_36ad36.png)

REQUISIÇÃO

Mensagem - 1) URL - Parâmetros:

URL: 
dts/datasul-rest/resources/prg/fin/v1/customer/1?fields=code,name&orderBy=name

dts/datasul-rest/resources/prg/fin/v1/accountReceivableDocument/49/executePayment




Tipos de Parâmetros:

QueryParam:
Utiliza o caracter “?” para separar do PathParam;
Os parâmetros são separados por “&”;
Pode indicar filtros ou parâmetros adicionais;
Formato por: chave + valor.

## Slide 15

![Imagem Slide 15](assets/Treinamento_HTML_-_Suporte_slide15_937648.png)

REQUISIÇÃO

Mensagem - 2) Método:

Indica o Tipo de Ação que deve ser executada no BackEnd;
É uma convenção de Mercado;
Principais:



Exemplos - 1:
GET dts/datasul-rest/resources/prg/fin/v1/customer/1?fields=code,name&orderBy=name

POST dts/datasul-rest/resources/prg/fin/v1/accountReceivableDocument/49/executePayment




Regras
Exemplo:
Não deve mexer no banco de dados.

## Slide 16

![Imagem Slide 16](assets/Treinamento_HTML_-_Suporte_slide16_4d62da.png)

REQUISIÇÃO

Mensagem - 2) Método:

Indica o Tipo de Ação que deve ser executada no BackEnd;
É uma convenção de Mercado;
Principais:



Exemplos - 2:
PUT dts/datasul-rest/resources/prg/fin/v1/customer/1

DELETE dts/datasul-rest/resources/prg/fin/v1/customer/1



Regras
Exemplo:
Não deve mexer no banco de dados.

## Slide 17

![Imagem Slide 17](assets/Treinamento_HTML_-_Suporte_slide17_2d6ca0.png)

REQUISIÇÃO

Mensagem - 3) Corpo:

Envio: Informações necessário para execução do BackEnd;
Retorno: Informações de Retorno;
É opcional;
Na TOTVS utilizamos o formato “JSON” (chave + valor).



## Slide 18

![Imagem Slide 18](assets/Treinamento_HTML_-_Suporte_slide18_68997b.png)

REQUISIÇÃO

Mensagem - 3) Corpo - Exemplo:

POST dts/datasul-rest/resources/prg/fin/v1/customer



![Imagem Slide 18](assets/Treinamento_HTML_-_Suporte_slide18_23cc56.png)

## Slide 19

![Imagem Slide 19](assets/Treinamento_HTML_-_Suporte_slide19_196703.png)

REQUISIÇÃO

Mensagem - 4) Código de Resposta (Status Code):

Indica o que aconteceu no BackEnd;
É uma convenção de Mercado;
Faixas por Tipo:



## Slide 20

![Imagem Slide 20](assets/Treinamento_HTML_-_Suporte_slide20_9bd6bd.png)

![Imagem Slide 20](assets/Treinamento_HTML_-_Suporte_slide20_aa3111.png)

REQUISIÇÃO

Exemplo:

Filtros

Informações Retornadas

## Slide 21

![Imagem Slide 21](assets/Treinamento_HTML_-_Suporte_slide21_4ffda4.png)

REQUISIÇÃO

Exemplo:

![Imagem Slide 21](assets/Treinamento_HTML_-_Suporte_slide21_c36cdc.png)

![Imagem Slide 21](assets/Treinamento_HTML_-_Suporte_slide21_be758f.png)

URL + Parâmetros

Método

Código de Resposta

Corpo da Resposta

![Imagem Slide 21](assets/Treinamento_HTML_-_Suporte_slide21_860040.png)

## Slide 22

03

Manutenção/
Expedição
FrontEnd

![Imagem Slide 22](assets/Treinamento_HTML_-_Suporte_slide22_80e387.png)

## Slide 23

![Imagem Slide 23](assets/Treinamento_HTML_-_Suporte_slide23_42aac3.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Fluxo da Manutenção:

1

2

Fontes Projeto

Fontes alterados

3

4

Fontes Projeto

Compilado Projeto

## Slide 24

![Imagem Slide 24](assets/Treinamento_HTML_-_Suporte_slide24_d2c0ff.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

É o “pacote” que vai para o ambiente;
É a menor parte “expedível”;
Padrão: HTML + Módulo; (Ex: html-acr-11.5.X-SNAPSHOT.war);
Portanto, a cada liberação é necessário expedir “todo o módulo”;
A versão é do Projeto e não dos programas;
A manutenção dos arquivos é individual;



Projeto HTML - Definição - THF1:

## Slide 25

![Imagem Slide 25](assets/Treinamento_HTML_-_Suporte_slide25_bd1f37.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Fonte Aberto;
Portanto é possível alterar os arquivos HTML e Javascript diretamente no ambiente;
Também, pode ser liberado os arquivos separadamente para o cliente;




Projeto HTML - Definição - THF1:

![Imagem Slide 25](assets/Treinamento_HTML_-_Suporte_slide25_8c082c.png)

## Slide 26

![Imagem Slide 26](assets/Treinamento_HTML_-_Suporte_slide26_97b2b0.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

É o “pacote” que vai para o ambiente;
É a menor parte “expedível”;
Padrões (definido pela equipe responsável): 
TOTVS + Área + Módulo (Ex: totvs-fin-acr.war);
TOTVS + Área + Funcionalidade (Ex: totvs-fis-calendario.war);
Portanto, a cada liberação é necessário expedir “todo o módulo ou funcionalidade”;
A versão é do Projeto e não dos programas;
A manutenção dos arquivos é individual;
O fonte é compilado;
Portanto, não há como liberar ou alterar apenas um arquivo no ambiente.




Projeto HTML - Definição - PO-UI:

## Slide 27

![Imagem Slide 27](assets/Treinamento_HTML_-_Suporte_slide27_4e0d2d.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Os Fontes ficam no TFS, no caminho:
     $/Datasul/Fontes_Doc/Sustentacao/V11/V11/html



Projeto HTML - Fontes - THF1:

![Imagem Slide 27](assets/Treinamento_HTML_-_Suporte_slide27_132869.png)

## Slide 28

![Imagem Slide 28](assets/Treinamento_HTML_-_Suporte_slide28_5151d5.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Existem dois modelos de Desenvolvimento:




Projeto HTML - Fontes - PO-UI:

1) Modelo Atual: 
O gerenciamento de configuração do Projeto é de responsabilidade do GCAD;
Utiliza o mesmo repositório de fontes do Progress (TFS);
Local: $/Datasul/Fontes_Doc/Sustentacao/V11/V11/thf2





## Slide 29

![Imagem Slide 29](assets/Treinamento_HTML_-_Suporte_slide29_7b941e.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Projeto HTML - Fontes - PO-UI:

![Imagem Slide 29](assets/Treinamento_HTML_-_Suporte_slide29_01b74d.png)

## Slide 30

![Imagem Slide 30](assets/Treinamento_HTML_-_Suporte_slide30_889886.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Existem dois modelos de Desenvolvimento:




Projeto HTML - Fontes - PO-UI:

2) Novo Modelo (Devops): 
O gerenciamento de configuração do Projeto é de responsabilidade da Equipe;
Incorpora várias ferramentas de controle de aprovação de alteração, versionamento, teste unitário, validação de fonte, cobertura de código;
A proposta é que todos os projetos PO-UI sejam migrados para este modelo;
Ela está acontecendo aos poucos, conforme disponibilidade de cada equipe;
Utiliza como repositório o TFS1215 no modelo github;
Local: http://tfs2015.totvs.com.br:8080/tfs/CD-JV/



## Slide 31

![Imagem Slide 31](assets/Treinamento_HTML_-_Suporte_slide31_af53ec.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Projeto HTML - Fontes - PO-UI:

![Imagem Slide 31](assets/Treinamento_HTML_-_Suporte_slide31_3f0f5e.png)

A permissão de acesso é definida pela equipe responsável pelo projeto

## Slide 32

![Imagem Slide 32](assets/Treinamento_HTML_-_Suporte_slide32_f3cc90.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Local: http://prado:8080/view/TODOS_HTML/


Projeto HTML - Integração Contínua - THF1:

![Imagem Slide 32](assets/Treinamento_HTML_-_Suporte_slide32_2d3040.png)

## Slide 33

![Imagem Slide 33](assets/Treinamento_HTML_-_Suporte_slide33_80a4f5.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Local: http://prado:8080/view/THF2/



Projeto HTML - Integração Contínua - PO-UI – Modelo Atual:

![Imagem Slide 33](assets/Treinamento_HTML_-_Suporte_slide33_61a93b.png)

## Slide 34

![Imagem Slide 34](assets/Treinamento_HTML_-_Suporte_slide34_8a1327.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

Local: http://jenkins-gcad-ops.jv01.local/



Projeto HTML - Integração Contínua - PO-UI – Novo modelo:

![Imagem Slide 34](assets/Treinamento_HTML_-_Suporte_slide34_7e7a06.png)

Ferramentas executadas no processo

## Slide 35

![Imagem Slide 35](assets/Treinamento_HTML_-_Suporte_slide35_dbf155.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

FONTES:
Não há um diretório de Fontes na rede - Somente TFS.


Projeto HTML:

COMPILADOS:
THF1: http://laranjeiras:8081/nexus/#view-repositories;repository-snapshots~browsestorage (Ex: com/totvs/html/html-acr)

PO-UI: http://porto:8081/#browse/browse:maven-snapshots (procurar pelo projeto, ex: totvs-fin-acr)

Para o novo Framework (Tomcat) os compilados também pode ser encontrados no caminho: \\laranjeiras\nfrw_repository\





## Slide 36

![Imagem Slide 36](assets/Treinamento_HTML_-_Suporte_slide36_8f3b99.png)

MANUTENÇÃO/EXPEDIÇÃO - FRONTEND

PATH DE LIBERAÇÃO:
Expedição via console;
Compilação realizada pela equipe;
Commit dos compilado no TFS: $/Patches_Datasul



Projeto HTML:

![Imagem Slide 36](assets/Treinamento_HTML_-_Suporte_slide36_d886e3.png)

deploy - Jboss
webapps - Tomcat

## Slide 37

03

Manutenção/
Expedição
BackEnd

![Imagem Slide 37](assets/Treinamento_HTML_-_Suporte_slide37_f55ce3.png)

## Slide 38

![Imagem Slide 38](assets/Treinamento_HTML_-_Suporte_slide38_e93538.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Manutenção/Compilação/Expedição:
Não muda nada em relação ao outros programas do produto.

Programas:
THF1 - Fachada + DBO/API de Negócio;
PO-UI - PRÉ-API-REST + API-REST + DBO/API de Negócio.


Programas:

## Slide 39

![Imagem Slide 39](assets/Treinamento_HTML_-_Suporte_slide39_50dce4.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

PRE-API-REST
(PO-UI)

Fachada (THF1)
API-REST (PO-UI)

API-NEGÓCIO
OU BO

## Slide 40

![Imagem Slide 40](assets/Treinamento_HTML_-_Suporte_slide40_30ddc3.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

PRE-API-REST
(PO-UI)

Fachada (THF1)
API-REST (PO-UI)

API-NEGÓCIO
OU BO

Nome:
área/api/versão/entidade.p
Objetivo:
Porta de Entrada;
Controle de Versionamento;
Roteamento;
Executar a API-REST.

## Slide 41

![Imagem Slide 41](assets/Treinamento_HTML_-_Suporte_slide41_83bb93.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

PRE-API-REST
(PO-UI)

Fachada (THF1)
API-REST (PO-UI)

API-NEGÓCIO
OU BO

Nome:
área/api/versão/entidade.p
Objetivo:
Porta de Entrada;
Controle de Versionamento;
Roteamento;
Executar a API-REST.

Nome: 
THF1: fch/área/fch<seq>.p
PO-UI: área+api/apiEntidade.p
Objetivo:
Pegar os Parâmetros;
Transformação;
Controle dados retornados;
Pequenas lógicas de negócio;
Executar a API/BO de Negócio.

## Slide 42

![Imagem Slide 42](assets/Treinamento_HTML_-_Suporte_slide42_bf304a.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

PRE-API-REST
(PO-UI)

Fachada (THF1)
API-REST (PO-UI)

API-NEGÓCIO
OU BO

Nome:
área/api/versão/entidade.p
Objetivo:
Porta de Entrada;
Controle de Versionamento;
Roteamento;
Executar a API-REST.

Nome: 
THF1: fch/área/fch<seq>.p
PO-UI: área+api/apiEntidade.p
Objetivo:
Pegar os Parâmetros;
Transformação;
Controle dados retornados;
Pequenas lógicas de negócio;
Executar a API/BO de Negócio.

Objetivo:
Regra de Negócio;
CRUD.

## Slide 43

![Imagem Slide 43](assets/Treinamento_HTML_-_Suporte_slide43_2ac3f5.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

Exemplo:

![Imagem Slide 43](assets/Treinamento_HTML_-_Suporte_slide43_ff313b.png)

![Imagem Slide 43](assets/Treinamento_HTML_-_Suporte_slide43_f03874.png)

PRÉ-API-REST

API-REST

Com base nos parâmetros verifica se é uma Consulta, Alteração, Execução de Processo

Converte os Parâmetros e Dados e chama a API/DBO de negócio

## Slide 44

![Imagem Slide 44](assets/Treinamento_HTML_-_Suporte_slide44_36d5f7.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

1) Internas:
Utilizadas somente pelas telas internas do Produto;
Não possui documentação;
Podem ser alteradas a qualquer momento, alterando a estrutura se necessário;
Exemplo: finapi\v1\businessUnit.p - finapi\apiBusinessUnit.p


Programas:

Existem dois tipos de API-REST:


## Slide 45

![Imagem Slide 45](assets/Treinamento_HTML_-_Suporte_slide45_936b5f.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

2) Externas ou Publicas:
Utilizadas por clientes ou integrações com outros Produtos;
Deve possuir uma documentação indicando os métodos e parâmetros;
Em alterações estruturais ou drásticas é feito o controle de versão (evolução de API);
Exemplo: finapi\v1\businessUnitPublic.p - finapi\apiBusinessUnitPublic.p.

Programas:

Existem dois tipos de API-REST:


## Slide 46

![Imagem Slide 46](assets/Treinamento_HTML_-_Suporte_slide46_88f228.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND

Programas:

http://vigia:8480/dts/datasul-rest/resources/prg/fin/v1/customer



fin/api/v1/customer.p

finapi/apiCustomer.p

http://vigia:8480/dts/datasul-rest/resources/prg/fin/v2/customer



fin/api/v2/customer.p

Somente para api’s externas e quando tiver uma mudança “estrutural”

Versão da “Assinatura”
(parâmetros)

Controle de Versão:

## Slide 47

![Imagem Slide 47](assets/Treinamento_HTML_-_Suporte_slide47_248ba5.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND


TFS: $/EMS5/Fontes_Doc/Sustentacao/V11/V11/progress/src



Programas:

![Imagem Slide 47](assets/Treinamento_HTML_-_Suporte_slide47_aebd0b.png)

fch     - Fachada (THF1)
fin      - PRÉ-API-REST (PO-UI)
finapi - API-REST (PO-UI)

## Slide 48

![Imagem Slide 48](assets/Treinamento_HTML_-_Suporte_slide48_e62b91.png)

![Imagem Slide 48](assets/Treinamento_HTML_-_Suporte_slide48_c183c2.png)

MANUTENÇÃO/EXPEDIÇÃO - BACKEND


TFS: $/EMS2/Fontes_Doc/Sustentacao/V11/V11/progress/src



Programas:

fch - Fachada (THF1)

pdp/api/v1- PRÉ-API-REST (PO-UI)

rep/api/v1- PRÉ-API-REST (PO-UI)

API-REST (PO-UI)
- Verificar execução dentro da PRÉ-API-REST

## Slide 49

![Imagem Slide 49](assets/Treinamento_HTML_-_Suporte_slide49_e371ed.png)

04

Ferramentas

## Slide 50

![Imagem Slide 50](assets/Treinamento_HTML_-_Suporte_slide50_32dc8c.png)

FERRAMENTAS

F12 - Developer Tools - Console:

![Imagem Slide 50](assets/Treinamento_HTML_-_Suporte_slide50_674b58.png)

Posição:
Dock side

Console

Apresenta os erros + Logs

Limpa o Log

## Slide 51

![Imagem Slide 51](assets/Treinamento_HTML_-_Suporte_slide51_562eba.png)

![Imagem Slide 51](assets/Treinamento_HTML_-_Suporte_slide51_181ba1.png)

FERRAMENTAS

F12 - Developer Tools - Network:

Detalhes Requisição

Network

Apresenta as Requisições

## Slide 52

![Imagem Slide 52](assets/Treinamento_HTML_-_Suporte_slide52_503223.png)

![Imagem Slide 52](assets/Treinamento_HTML_-_Suporte_slide52_175d35.png)

FERRAMENTAS

F12 - Developer Tools - Network:

Network

Apresenta as Requisições

Limpa o Log

Resposta da Requisição

![Imagem Slide 52](assets/Treinamento_HTML_-_Suporte_slide52_cbcbd8.png)

## Slide 53

![Imagem Slide 53](assets/Treinamento_HTML_-_Suporte_slide53_f41912.png)

![Imagem Slide 53](assets/Treinamento_HTML_-_Suporte_slide53_999ccd.png)

FERRAMENTAS

HAR ANALYZER:

Exportação das Requisições

## Slide 54

![Imagem Slide 54](assets/Treinamento_HTML_-_Suporte_slide54_67dcbd.png)

FERRAMENTAS

HAR ANALYZER:

![Imagem Slide 54](assets/Treinamento_HTML_-_Suporte_slide54_656d90.png)

Requisições

Visualização

Filtro

Retorno

Erro

Filtro por Código de Resposta

Acesso: https://toolbox.googleapps.com/apps/har_analyzer/

![Imagem Slide 54](assets/Treinamento_HTML_-_Suporte_slide54_42cd60.png)

## Slide 55

![Imagem Slide 55](assets/Treinamento_HTML_-_Suporte_slide55_14a4f1.png)

FERRAMENTAS

DTS-REST-UI:

fin/api/v1/customer.p

Principais Características: 
Simula Requisição;
Mesma execução realizada pelo FrameWork;
Full Progress;
Execução na máquina local;
Controle de Transação;
Não é necessário alterar nada na API-REST;
Utilizado para Desenv, Manuteção e Suporte.

![Imagem Slide 55](assets/Treinamento_HTML_-_Suporte_slide55_af91df.png)

Disponível em: \\enseada\desems5\Atalhos\dts-rest-ui\dts-rest-ui.p

![Imagem Slide 55](assets/Treinamento_HTML_-_Suporte_slide55_6be40b.png)

## Slide 56

05

Dicas

![Imagem Slide 56](assets/Treinamento_HTML_-_Suporte_slide56_ee47b8.png)

## Slide 57

![Imagem Slide 57](assets/Treinamento_HTML_-_Suporte_slide57_f7c6df.png)

![Imagem Slide 57](assets/Treinamento_HTML_-_Suporte_slide57_2003d4.png)

![Imagem Slide 57](assets/Treinamento_HTML_-_Suporte_slide57_25fbfa.png)

DICAS

Diferenciando THF1 x PO-UI

Como saber se a tela é THF1 ou PO-UI ?


THF1: dts + módulo + programa (menu)

PO-UI: totvs-menu + program-html + programa (menu)

## Slide 58

DICAS

![Imagem Slide 58](assets/Treinamento_HTML_-_Suporte_slide58_feb9ff.png)

![Imagem Slide 58](assets/Treinamento_HTML_-_Suporte_slide58_61b23d.png)

Diferenciando THF1 x PO-UI

Como saber a requisição é THF1 ou PO-UI ?


THF1: api + fch + módulo + programa

PO-UI: prg + área + versão + programa

![Imagem Slide 58](assets/Treinamento_HTML_-_Suporte_slide58_3624ed.png)

## Slide 59

![Imagem Slide 59](assets/Treinamento_HTML_-_Suporte_slide59_044978.png)

DICAS

Versão do Projeto HTML

![Imagem Slide 59](assets/Treinamento_HTML_-_Suporte_slide59_b7b1ae.png)


É apresentado no carregamento do Projeto;
Restrição: 
Somente para Projetos que estão no novo modelo Devops;
Veremos a possibilidade de incluir no modelo atual.
Lembrete:
De forma geral, a versão do projeto é a “versão da release do produto”;
Levar em considerações os Paths de Liberação;
Mas, pode ter uma liberação “pontual” pela equipe responsável.

Projeto

Versão

![Imagem Slide 59](assets/Treinamento_HTML_-_Suporte_slide59_07048e.png)

## Slide 60

![Imagem Slide 60](assets/Treinamento_HTML_-_Suporte_slide60_d2ac61.png)

DICAS

Versão da API-REST

![Imagem Slide 60](assets/Treinamento_HTML_-_Suporte_slide60_29d847.png)

Versão


Restrição: 
Implementação específica, realizada pelo Backoffice;
Foi implementado somente no EMS5.
Alternativa: 
As API-REST do EMS2 executam a include padrão de versionamento;
Portanto é possível consultar o “.r”


![Imagem Slide 60](assets/Treinamento_HTML_-_Suporte_slide60_ca152b.png)

![Imagem Slide 60](assets/Treinamento_HTML_-_Suporte_slide60_def1e1.png)

## Slide 61

![Imagem Slide 61](assets/Treinamento_HTML_-_Suporte_slide61_c2bba5.png)

DICAS

Diretório Temporários para Simulação - Ambientes Internos

Para alguns ambientes, o GCAD disponibiliza um diretório temporário que está no Propath do AppServer;
Estes diretórios ficam no propath na frente do diretório oficial de expedição;
Desta forma, é possível realizar alterações nas API-REST’s, que são executadas a partir das telas HTML;
O conteúdo deles é eliminado todos dias a noite;
Como está no servidor, todos os usuários "enxergam" o programa;
Estes diretórios não afetam execuções locais (na máquina do próprio usuário).

## Slide 62

![Imagem Slide 62](assets/Treinamento_HTML_-_Suporte_slide62_bf6e3d.png)

DICAS

Diretório Temporários para Simulação - Ambientes Internos

Exemplos:

gales:8180 (Teste Integrado - Progress)
     \\arpoador\tst-prgs-psc115x-nfrw\

vigia:8480 (Teste Integrado - SQL)
     \\arpoador\tst-prgs-sql-115x\

Os diretórios estão documentados na página de Ambientes:
     https://tdn.totvs.com/pages/viewpage.action?pageId=183730513

## Slide 63

![Imagem Slide 63](assets/Treinamento_HTML_-_Suporte_slide63_ead7af.png)

DICAS

Lembretes

O progress roda no Servidor (não tem propath local);
Não tem extrato de versão;
Não tem Client Log;
Log do AppServer (configuração do nível do Log).


## Slide 64

![Imagem Slide 64](assets/Treinamento_HTML_-_Suporte_slide64_ea9a41.png)

06

Análise de Erros

## Slide 65

![Imagem Slide 65](assets/Treinamento_HTML_-_Suporte_slide65_3790cd.png)

ANÁLISE DE ERROS

Navegadores Homologados:

![Imagem Slide 65](assets/Treinamento_HTML_-_Suporte_slide65_e68719.png)

Cloud TOTVS

Mais Estável

## Slide 66

![Imagem Slide 66](assets/Treinamento_HTML_-_Suporte_slide66_aac93f.png)

ANÁLISE DE ERROS

200
404
400
500

Requisição - Principais Códigos de Resposta:

OK
Not Found (Não encontrado) = Informação não Encontrada
Bad Request (Solicitação Inválida) = Erro Interno “Tratado” ou de Negócio
Internal Server Error (Erro Interno do Servidor) = Erro Interno Desconhecido 


## Slide 67

![Imagem Slide 67](assets/Treinamento_HTML_-_Suporte_slide67_27965b.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 200 (OK)

![Imagem Slide 67](assets/Treinamento_HTML_-_Suporte_slide67_a3d1a1.png)

Informado o cliente 1 (Existente)

Status Code: 200

Serviço: customer
Código: 1

![Imagem Slide 67](assets/Treinamento_HTML_-_Suporte_slide67_cdb6b4.png)

## Slide 68

![Imagem Slide 68](assets/Treinamento_HTML_-_Suporte_slide68_d9b998.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 404 (Not Found)

![Imagem Slide 68](assets/Treinamento_HTML_-_Suporte_slide68_6d15d2.png)

Informado o cliente 55 (Inexistente)

Status Code: 404

Serviço: customer
Código: 55

![Imagem Slide 68](assets/Treinamento_HTML_-_Suporte_slide68_2ad2cc.png)

## Slide 69

![Imagem Slide 69](assets/Treinamento_HTML_-_Suporte_slide69_01cf93.png)

![Imagem Slide 69](assets/Treinamento_HTML_-_Suporte_slide69_930f4f.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 400 (Bad Request)

Status Code: 400

Serviço: financialCash

Mensagem para o Usuário

## Slide 70

![Imagem Slide 70](assets/Treinamento_HTML_-_Suporte_slide70_7e6f34.png)

![Imagem Slide 70](assets/Treinamento_HTML_-_Suporte_slide70_8f0743.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 400 (Bad Request)

Requisição

Retorno da Requisição

![Imagem Slide 70](assets/Treinamento_HTML_-_Suporte_slide70_c8fbdd.png)

## Slide 71

![Imagem Slide 71](assets/Treinamento_HTML_-_Suporte_slide71_001e67.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Com Descrição

![Imagem Slide 71](assets/Treinamento_HTML_-_Suporte_slide71_66ebbe.png)

Status Code: 500

Mensagem para o Usuário

Serviço: cashPendingPayment

## Slide 72

![Imagem Slide 72](assets/Treinamento_HTML_-_Suporte_slide72_57ebc5.png)

![Imagem Slide 72](assets/Treinamento_HTML_-_Suporte_slide72_3f989e.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Com Descrição

Mas detalhes
Retorno Requisição

## Slide 73

![Imagem Slide 73](assets/Treinamento_HTML_-_Suporte_slide73_2b81ab.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Com Descrição

![Imagem Slide 73](assets/Treinamento_HTML_-_Suporte_slide73_782ad0.png)

Procurar pelo Serviço

Não está tão claro o erro

Geração do Status 500

![Imagem Slide 73](assets/Treinamento_HTML_-_Suporte_slide73_609586.png)

Mas sei o local

## Slide 74

![Imagem Slide 74](assets/Treinamento_HTML_-_Suporte_slide74_e4ce49.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Sem Descrição

![Imagem Slide 74](assets/Treinamento_HTML_-_Suporte_slide74_621421.png)

Status Code: 500

Mensagem Genérica

## Slide 75

![Imagem Slide 75](assets/Treinamento_HTML_-_Suporte_slide75_24fb4f.png)

![Imagem Slide 75](assets/Treinamento_HTML_-_Suporte_slide75_825548.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Sem Descrição

Detalhe: 4GL STOP condition

## Slide 76

![Imagem Slide 76](assets/Treinamento_HTML_-_Suporte_slide76_10752d.png)

![Imagem Slide 76](assets/Treinamento_HTML_-_Suporte_slide76_6d2507.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Sem Descrição

O Erro está mais claro

![Imagem Slide 76](assets/Treinamento_HTML_-_Suporte_slide76_5adbdd.png)

## Slide 77

![Imagem Slide 77](assets/Treinamento_HTML_-_Suporte_slide77_27314d.png)

![Imagem Slide 77](assets/Treinamento_HTML_-_Suporte_slide77_b2beea.png)

ANÁLISE DE ERROS

Requisição - Código de Resposta: 500 (Internal Error) - Controle de Error - API-REST

Erro “tratado”

![Imagem Slide 77](assets/Treinamento_HTML_-_Suporte_slide77_7711a0.png)

Status Code: 400

## Slide 78

![Imagem Slide 78](assets/Treinamento_HTML_-_Suporte_slide78_aabb42.png)

ANÁLISE DE ERROS

Erro no HTML (Camada de Controle)

![Imagem Slide 78](assets/Treinamento_HTML_-_Suporte_slide78_a6ccdf.png)

Erro

Arquivo de Controle

## Slide 79

![Imagem Slide 79](assets/Treinamento_HTML_-_Suporte_slide79_27fc6c.png)

ANÁLISE DE ERROS

Erro de conversão UTF-8

![Imagem Slide 79](assets/Treinamento_HTML_-_Suporte_slide79_0a9aaa.jpg)

Erro retornado do BackEnd


Causa: 
O usuário copiou o texto de algum lugar;
Este texto possuir um caracter não reconhecido pelo progress;
Por exemplo o caracter “...” do Word.
Ação:
Transferir o Ticket para o Framework;
Antes de chamar o progress é feito uma tratativa para retirar estes caracteres;
Ela é por demanda, conforme aparecem os caracteres inválidos.

## Slide 80

OBRIGADO

adriano.avila@totvs.com.br

ADRIANO DE AVILA

