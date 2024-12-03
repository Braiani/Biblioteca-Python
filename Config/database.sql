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

INSERT INTO livro (titulo, autor, genero, status, isbn) VALUES
('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 'Disponível', 123456789),
('Dom Casmurro', 'Machado de Assis', 'Romance', 'Disponível', 987654321),
('A Culpa é das Estrelas', 'John Green', 'Romance', 'Disponível', 112233445),
('1984', 'George Orwell', 'Distopia', 'Disponível', 223344556),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil', 'Disponível', 334455667),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia', 'Disponível', 445566778),
('O Código Da Vinci', 'Dan Brown', 'Mistério', 'Disponível', 556677889),
('O Hobbit', 'J.R.R. Tolkien', 'Fantasia', 'Disponível', 667788990),
('O Morro dos Ventos Uivantes', 'Emily Brontë', 'Romance', 'Disponível', 778899001),
('O Diário de Anne Frank', 'Anne Frank', 'Biografia', 'Disponível', 889900112),
('A Guerra dos Tronos', 'George R.R. Martin', 'Fantasia', 'Disponível', 990011223),
('O Alquimista', 'Paulo Coelho', 'Filosofia', 'Disponível', 101112233),
('Cem Anos de Solidão', 'Gabriel García Márquez', 'Realismo Mágico', 'Disponível', 121314244),
('Orgulho e Preconceito', 'Jane Austen', 'Romance', 'Disponível', 131415355),
('A Menina que Roubava Livros', 'Markus Zusak', 'Drama', 'Disponível', 141516466),
('A Arte da Guerra', 'Sun Tzu', 'Estratégia', 'Disponível', 151617577),
('Moby Dick', 'Herman Melville', 'Aventura', 'Disponível', 161718688),
('O Grande Gatsby', 'F. Scott Fitzgerald', 'Romance', 'Disponível', 171819799),
('Fahrenheit 451', 'Ray Bradbury', 'Ficção Científica', 'Disponível', 181920800),
('O Senhor das Moscas', 'William Golding', 'Aventura', 'Disponível', 192021911),
('O Lobo da Estepe', 'Hermann Hesse', 'Filosofia', 'Disponível', 202122922),
('A Revolução dos Bichos', 'George Orwell', 'Política', 'Disponível', 212223033),
('Os Miseráveis', 'Victor Hugo', 'Romance Histórico', 'Disponível', 222324044),
('O Filho Eterno', 'Cristovão Tezza', 'Drama', 'Disponível', 232425155),
('Sapiens: Uma Breve História da Humanidade', 'Yuval Noah Harari', 'História', 'Disponível', 242526266),
('O Mundo de Sofia', 'Jostein Gaarder', 'Filosofia', 'Disponível', 252627377),
('O Poder do Hábito', 'Charles Duhigg', 'Autoajuda', 'Disponível', 262728488),
('A Ciência de Ficar Rico', 'Wallace D. Wattles', 'Autoajuda', 'Disponível', 272829599),
('A Cabana', 'William P. Young', 'Religião', 'Disponível', 282930600),
('O Último Desejo', 'Andrzej Sapkowski', 'Fantasia', 'Disponível', 292931711),
('O Vendedor de Sonhos', 'Augusto Cury', 'Psicologia', 'Disponível', 303132822),
('O Caçador de Pipas', 'Khaled Hosseini', 'Drama', 'Disponível', 313233933),
('O Escaravelho do Diabo', 'Lúcia Machado de Almeida', 'Mistério', 'Disponível', 323334044),
('A Casa dos Espíritos', 'Isabel Allende', 'Realismo Mágico', 'Disponível', 333435155),
('Vingança', 'Joaquim de Almeida', 'Ficção', 'Disponível', 343536266),
('A Sombria Jornada de Fawkes', 'Douglas Adams', 'Fantasia', 'Disponível', 353637377),
('O Último Samurai', 'Helen Dewitt', 'Aventura', 'Disponível', 363738488),
('O Cemitério de Praga', 'Umberto Eco', 'Mistério', 'Disponível', 373839599),
('Os Homens que Não Amavam as Mulheres', 'Stieg Larsson', 'Mistério', 'Disponível', 383940600),
('As Aventuras de Sherlock Holmes', 'Arthur Conan Doyle', 'Mistério', 'Disponível', 393941711),
('O Menino do Pijama Listrado', 'John Boyne', 'Drama', 'Disponível', 404142822),
('A Vida Secreta das Abelhas', 'Sue Monk Kidd', 'Drama', 'Disponível', 414243933),
('O Mundo Perdido', 'Arthur Conan Doyle', 'Aventura', 'Disponível', 424344044),
('O Pássaro', 'Yoko Ogawa', 'Ficção', 'Disponível', 434345155),
('A Cabana', 'William P. Young', 'Religião', 'Disponível', 444346266),
('O Livro das Sombras', 'Cecilia Samartin', 'Drama', 'Disponível', 454347377),
('Noites Brancas', 'Fiódor Dostoiévski', 'Romance', 'Disponível', 464348488),
('O Príncipe', 'Nicolau Maquiavel', 'Filosofia', 'Disponível', 474349599),
('A Trilogia da Escuridão', 'Carlos Ruiz Zafón', 'Fantasia', 'Disponível', 484350600),
('O Inferno de Dante', 'Dante Alighieri', 'Poesia', 'Disponível', 494351711);
