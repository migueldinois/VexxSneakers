CREATE DATABASE IF NOT EXISTS VexxSneakers;

USE VexxSneakers;

CREATE TABLE usuarios(
	nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL PRIMARY KEY,
    telefone VARCHAR(32) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    senha varchar(40) NOT NULL
);

CREATE TABLE categorias (
	codigo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    imagem VARCHAR(350) NOT NULL,
    nome VARCHAR(30) NOT NULL
);

CREATE TABLE produto (
	codigo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(350) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    valor FLOAT,
    foto VARCHAR(350) NOT NULL,
    banner VARCHAR(350) NOT NULL,
    categoria INT NOT NULL,
    FOREIGN KEY (categoria) REFERENCES categorias(codigo)
);

CREATE TABLE comentarios (
	id_mensagem INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_produto INT NOT NULL,
	usuario VARCHAR(50) NOT NULL,
    mensagem VARCHAR(200) NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto(codigo)
);

CREATE TABLE IF NOT EXISTS carrinhos (
	cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(32),
    data datetime default current_timestamp,
    finalizado bool,
    constraint fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(email)
);
    
CREATE TABLE IF NOT EXISTS itens_carrinho (
	cod_itens_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    constraint fk_carrinho_carrinhos foreign key (cod_carrinho) references carrinhos(cod_carrinho),
    constraint fk_itens_carrinho_itens foreign key (cod_produto) references produto (codigo)
);