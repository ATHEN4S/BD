# BD
Este repositório contém o código-fonte e os recursos necessários para implementar um sistema de Banco de Dados para uma simulação de loja de roupas. O projeto é desenvolvido utilizando as linguagens Python e SQLite3 como Sistema de Gerenciamento de Banco de Dados (SGBD), com o auxílio do software DBeaver para a administração do banco de dados.

## Visão Geral do Projeto
O objetivo deste projeto é criar um sistema que permita o gerenciamento de dados relacionados a uma loja de roupas, incluindo informações sobre produtos, estoque, clientes e vendas. Para atingir esse objetivo, implementamos as operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados SQLite.

## Tecnologias Utilizadas
Python: A linguagem de programação utilizada para desenvolver a aplicação.
SQLite3: O Sistema de Gerenciamento de Banco de Dados escolhido para armazenar e manipular os dados.
DBeaver: Uma ferramenta de administração de banco de dados que simplifica a criação e a gestão do banco de dados SQLite.

## Configuração e Uso
Antes de executar a aplicação, certifique-se de que as seguintes dependências estão instaladas em seu ambiente:

* Python
* SQLite3
* DBeaver (opcional, mas altamente recomendado para administração do banco de dados)

## Estrutura do Projeto
interface.py: O ponto de entrada da aplicação. Contém a lógica principal para interagir com o banco de dados. Define as operações de banco de dados, como criar tabelas, inserir registros, atualizar registros e realizar consultas.
bdinit.py: Script para criar o banco de dados e inserir dados iniciais, contém as definições das funções utilizadas para mexer nas tabelas do banco de dados. 
clientes.db: O Banco de Dados fictício.
