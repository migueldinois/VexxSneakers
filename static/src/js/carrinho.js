

let total = 0;

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
        alert("Erro ao obter o carrinho:");
    } else {
        const dadosCarrinho = await resposta.json()
        const carrinho = document.querySelector("#cart-items");

        carrinho.innerHTML = "";

        let total = 0;

        for (let item of dadosCarrinho) {
            console.log(item)
            total += item.valor;
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
                                    <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                                </svg>
                            </button>
                        </div>
                        
                    </div>
                </div>
            `;
            // Atualizando total (tofixed para arredonda para dois numeros dps da virgula))
            document.querySelector(".cart-total-price").innerText = "R$" +total.toFixed(2);

            carrinho.innerHTML += linha;

        }
    }
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
        alert("Erro ao adicionar item no carrinho")
    } else {


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



mostrar_carrinho();
