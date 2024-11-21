create database biblioteca;
use biblioteca;

create table usuario(
    id_usuario int auto_increment primary key,
    nome varchar(100),
    cpf varchar(13),
    telefone varchar(20),
    senha varchar(100)
);


create table livro(
    id_livro int auto_increment primary key,
    titulo varchar(50),
    autor varchar(50),
    genero varchar(50),
    status varchar(50),
    isbn int
);

create table emprestimo(
    id_emprestimo int auto_increment primary key,
    id_livro int,
    id_usuario int,
    data_emprestimo date NOT NULL,
    data_devolucao date,
    foreign key (id_livro) references livro(id_livro),
    foreign key (id_usuario) references usuario(id_usuario)
);