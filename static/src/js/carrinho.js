

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
            total += item.preco;
            let linha = `

                    <div class="cart-item-card d-flex align-items-center justify-content-between mb-3">
                    <div class="d-flex align-items-center flex-grow-1">
                        <div class="cart-item-img-container">
                            <img src="${item.foto}" class="img-fluid rounded object-fit-cover w-100"
                        </div>
                        <div class="cart-item-body">
                            <p class="cart-item-name">${item.nome}</p>
                            <p class="cart-item-price">R$ ${item.valor.toFixed(2)}</p>
                            
                            <div class="quantity-control">
                                <button type="button" class="quantity-btn" title="Diminuir">-</button>
                                <span class="quantity-value">${item.quantidade}</span>
                                <button type="button" class="quantity-btn" title="Aumentar">+</button>
                            </div>
                        </div>
                    </div>
                    
                    <button type="button" onclick="deletarItemCarrinho(${item.cod_carrinho})" class="cart-btn-delete" aria-label="Remover ${item.produto}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                            <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                        </svg>
                    </button>
                </div>
          `
            // Atualizando total (tofixed para arredonda para dois numeros dps da virgula))
            document.querySelector(".cart-total-label").innerText = total.toFixed(2);

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
    const resposta = await fetch('/api/delete/carrinho',
        {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(
                {
                    "cod_carrinho": cod_item_carrinho
                }
            )
        }

    )
    if (!resposta.ok) {
        alert("Erro ao deletar item do carrinho")
    } else {
        mostrar_carrinho();
    }
}




mostrar_carrinho();
