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

CREATE TABLE mangas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    volume INT,
    autor VARCHAR(80),
    data_lancamento DATE
);

INSERT INTO mangas (nome, volume, autor, data_lancamento)
VALUES ('Naruto', 52, 'Masashi Kishimoto', '2010-09-03');

INSERT INTO mangas (nome, volume, autor, data_lancamento)
VALUES ('Dragon Ball', 20, 'Akira Toriyama', '1987-05-15');

select * from mangas;