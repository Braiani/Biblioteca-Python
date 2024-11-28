create database biblioteca;
use biblioteca;

create table usuario(
    id_usuario int auto_increment primary key,
    nome varchar(100),
    usuario varchar(100) NOT NULL,
    cpf varchar(13),
    telefone varchar(20),
    senha varchar(100) NOT NULL,
    is_admin tinyint default 0
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

INSERT INTO usuario(nome,usuario,cpf,telefone,senha,is_admin) VALUES ('Admin','admin','123456789','9999-9999','1234',1);