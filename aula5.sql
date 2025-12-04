CREATE DATABASE biblioteca;
use biblioteca;

create table livros(
id int primary key auto_increment,
titulo varchar(50)
);

insert into livros (titulo) values ('hp');
select * from livros;

alter table livros add column numero_paginas int;

insert into livros (titulo, numero_paginas) values ('livrao', '2000000');
alter table livros add column autor varchar(50);
alter table livros add column preco double;
alter table livros add column isbn float;
alter table livros add column descricao text;