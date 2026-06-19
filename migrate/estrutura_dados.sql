-- Criação das categorias
INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_infantil.png', 'Infantil');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_masculino.png', 'Masculino');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_feminino.png', 'Feminino');

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/banners_categorias/banner_esportes.png', 'Esportes');

-- PRODUTOS INFANTIS (Categoria 1)
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Kid Drip Colorful', 'Tênis infantil estilo chunky colorido super confortável para o dia a dia.', 249.90, '/static/src/img/produtos/kid_colorful_foto.png', '/static/src/img/produtos/kid_colorful_banner.png', 1);

INSERT INTO produto (nome, descricao, valor, foto, banner, categoria)
VALUES (
    'Vexx La Casa de Papel', 
    'Tênis de alto conforto e macio.', 
    789.90, 
    '/static/src/img/produtos/godo2_colorful_banner.png', 
    '/static/src/img/produtos/godo2_colorful_banner.png', 
    5
);

INSERT INTO categorias(imagem, nome) 
VALUES('/static/src/img/produtos/godo_colorful_banner.png', 'Para Ratos');

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Kid Track Pastel', 'Modelo streetwear mini em tons pastel com amortecimento premium.', 269.90, '/static/src/img/produtos/kid_pastel_foto.png', '/static/src/img/produtos/kid_pastel_banner.png', 1);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Kid Bolt Light', 'Tênis leve e flexível com luzes embutidas na sola futurista.', 199.90, '/static/src/img/produtos/kid_bolt_foto.png', '/static/src/img/produtos/kid_bolt_banner.png', 1);

-- PRODUTOS MASCULINOS (Categoria 2)
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Men Track Triple Black', 'O legítimo drip inglês todo preto, robusto e resistente.', 599.90, '/static/src/img/produtos/men_black_foto.png', '/static/src/img/produtos/men_black_banner.png', 2);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Men Street Stealth', 'Silhueta discreta com mesh respirável e detalhes refletivos.', 489.90, '/static/src/img/produtos/men_stealth_foto.png', '/static/src/img/produtos/men_stealth_banner.png', 2);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Men Cyber Drip', 'Cores neon e grafismos cibernéticos para destacar qualquer outfit.', 649.90, '/static/src/img/produtos/men_cyber_foto.png', '/static/src/img/produtos/men_cyber_banner.png', 2);

-- PRODUTOS FEMININOS (Categoria 3)
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Women Track Rose Gold', 'Chunky sneaker feminino com acabamento luxuoso em detalhes metálicos.', 589.90, '/static/src/img/produtos/women_rose_foto.png', '/static/src/img/produtos/women_rose_banner.png', 3);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Women Street Orchid', 'Em tons lilás e violeta, leve e perfeito para caminhadas com estilo.', 459.90, '/static/src/img/produtos/women_orchid_foto.png', '/static/src/img/produtos/women_orchid_banner.png', 3);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Women Ivory Platform', 'Solado plataforma off-white muito confortável e moderno.', 499.90, '/static/src/img/produtos/women_ivory_foto.png', '/static/src/img/produtos/women_ivory_banner.png', 3);

-- PRODUTOS ESPORTES (Categoria 4)
INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Sport Speed Neon', 'Tênis de alta performance para corrida com placa de carbono.', 699.90, '/static/src/img/produtos/sport_speed_foto.png', '/static/src/img/produtos/sport_speed_banner.png', 4);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Sport Trail Matrix', 'Solado tratorado com alta aderência para trilhas e treinos externos.', 549.90, '/static/src/img/produtos/sport_trail_foto.png', '/static/src/img/produtos/sport_trail_banner.png', 4);

INSERT INTO produto(nome, descricao, valor, foto, banner, categoria)
VALUES('Vexx Sport Volt Hyper', 'Super leve, ideal para treinos de alta intensidade na academia.', 379.90, '/static/src/img/produtos/sport_volt_foto.png', '/static/src/img/produtos/sport_volt_banner.png', 4);
