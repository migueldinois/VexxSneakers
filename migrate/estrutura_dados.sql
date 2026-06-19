-- Criação das categorias
INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_infantil.png', 'Infantil');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_masculino.png', 'Masculino');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_feminino.png', 'Feminino');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_esportes.png', 'Esportes');

-- Criação de itens para cada categoria
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 1', 'Esse produto é um produto teste da Vexx Sneakers', 290.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 1);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 2', 'Esse produto é um produto teste da Vexx Sneakers', 220.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 2);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 3', 'Esse produto é um produto teste da Vexx Sneakers', 120.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 3);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 3', 'Esse produto é um produto teste da Vexx Sneakers', 430.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 4);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Produto teste 3', 'Esse produto é um produto teste da Vexx Sneakers', 430.00, 'https://picsum.photos/500/500', 'https://picsum.photos/200/300', 4);
