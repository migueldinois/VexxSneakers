-- Criação da categoria
INSERT INTO categorias(imagem, nome) 
VALUES('https://picsum.photos/500/500', 'Infantil');


-- Criação de itens para a categoria
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 1', 'Esse produto é um produto teste da Vexx Sneakers', 22.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 1)


