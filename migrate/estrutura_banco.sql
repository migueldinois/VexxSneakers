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
