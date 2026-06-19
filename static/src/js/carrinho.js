

const botaoCarrinho = document.querySelector('.icon__cart')
let total = 0;

let alertaExibido = false;

function addToCart(nome, preco) {
    const cartItems = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");

    const item = document.createElement("div");
    item.innerHTML = `<p>${nome} - R$ ${preco}</p>`;

    cartItems.appendChild(item);

    total += preco;
    cartTotal.innerText = total.toFixed(2);

    cart.classList.add("active");
}


async function mostrar_carrinho() {
    const resposta = await fetch("/api/get/carrinho");

    if (!resposta.ok) {
        if (resposta.status === 401) {
            if (window.location.pathname.includes("/login")) {
                return;
            }
            mensagemNaTela(
                "Acesso Restrito",
                "Você precisa estar logado para ver o seu carrinho.",
                "warning",
                "Ir para o Login" 
            ).then((result) => {

                if (result.isConfirmed) {
                    window.location.href = "/login";
                }
            });
            
        } else {
        
            mensagemNaTela(
                "Erro no Servidor",
                "Não foi possível recuperar os dados do seu carrinho. Tente novamente mais tarde.",
                "error"
            );
        }
        return; 
    }


    const dadosCarrinho = await resposta.json();
    const carrinho = document.querySelector("#cart-items");

    carrinho.innerHTML = "";
    let totalCarrinho = 0;

    if (dadosCarrinho.length === 0) {
        document.querySelector(".cart-total-price").innerText = "R$ 0.00";
        carrinho.innerHTML = "<p class='text-center text-muted p-3'>Seu carrinho está vazio.</p>";
        return;
    }

    for (let item of dadosCarrinho) {
        totalCarrinho += item.valor;
        let linha = `
            <div class="card bg-light border-0 rounded-4 overflow-hidden mb-3 shadow-sm">
                <div class="row g-0 align-items-center">
                    <div class="col-3 bg-body-secondary">
                        <div class="ratio ratio-1x1">
                            <img src="${item.foto}" class="object-fit-cover w-100 h-100" alt="${item.nome}">
                        </div>
                    </div>
                    <div class="col-7 p-2 d-flex flex-column justify-content-center">
                        <p class="fw-bold text-dark mb-0 small text-uppercase text-truncate" title="${item.nome}">${item.nome}</p>
                        <p class="fw-semibold text-secondary small mb-2">R$ ${item.valor.toFixed(2)}</p>
                        <div class="d-inline-flex align-items-center bg-white rounded border p-1" style="width: fit-content;">
                            <span class="fw-bold small px-1 text-center" style="min-width: 20px;">${item.quantidade}</span>
                        </div>
                    </div>
                    <div class="col-2 text-center">
                        <button type="button" onclick="deletarItemCarrinho(${item.cod_carrinho})" class="btn btn-link text-dark p-0 border-0 link-danger" aria-label="Remover ${item.produto}">
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                                <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        `;
        carrinho.innerHTML += linha;
    }
    
    document.querySelector(".cart-total-price").innerText = "R$" + totalCarrinho.toFixed(2);
}

async function adicionarItemCarrinho(cod_produto, quantidade = 1) {
    const resposta = await fetch('/api/post/carrinho',
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(

                {
                    "cod_produto": cod_produto,
                    "quantidade": quantidade
                }
            )
        }
    )

    if (!resposta.ok) {
        // Se o usuário não estiver logado ao tentar adicionar
        if (resposta.status === 401) {
            mensagemNaTela("Acesso Restrito", "Você precisa fazer login para adicionar itens ao carrinho.", "warning", "Ir para o Login")
                .then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = "/login";
                    }
                });
        } else {
            mensagemNaTela("Erro", "Não foi possível adicionar o item ao carrinho.", "error");
        }
    } else {
        // Se a requisição deu certo, exibe o alerta de sucesso
        mensagemNaTela("Sucesso!", "O produto foi adicionado ao carrinho!", "success", "OK");
        mostrar_carrinho();
    }
}

async function deletarItemCarrinho(cod_item_carrinho) {
    const resposta = await fetch('/api/delete/carrinho', {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "cod_item_carrinho": cod_item_carrinho
        })
    });

    if (!resposta.ok) {
        alert("Erro ao deletar item do carrinho");
    } else {
        mostrar_carrinho();
    }
}


botaoCarrinho.addEventListener('click', () => {
    mostrar_carrinho();

})

