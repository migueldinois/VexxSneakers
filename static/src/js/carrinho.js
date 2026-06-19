const cart = document.getElementById("cart");
const openBtn = document.getElementById("cart-button");
const butButton = document.querySelector('.btn-buy-now')
const closeBtn = document.getElementById("close-cart");
const euQueroBotao = document.querySelector('.button--small')

let total = 0;

openBtn.addEventListener("click", () => {
  cart.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  cart.classList.remove("active");
});

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
          `
          // Atualizando total (tofixed para arredonda para dois numeros dps da virgula))
          document.querySelector("#cart-total").innerText = total.toFixed(2);

      carrinho.innerHTML += linha;

    }
  }
}

async function adicionarItemCarrinho(cod_produto, quantidade=1){
  const resposta = await fetch('/api/post/carrinho', 
                        {
                          method: "POST",
                          headers:{
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

  if(!resposta.ok){
    alert("Erro ao adicionar item no carrinho")
  } else {

      
  }
}

async function deletarItemCarrinho(cod_item_carrinho){
  const resposta = await fetch('/api/delete/carrinho', 
                        {
                          method: "DELETE",
                          headers:{
                                      "Content-Type": "application/json"
                          },
                          body: JSON.stringify(
                                                {
                                                  "cod_carrinho": cod_item_carrinho
                                                }
                          )
                        }

  )
  if(!resposta.ok){
    alert("Erro ao deletar item do carrinho")
  } else {
    mostrar_carrinho();
  }
}




mostrar_carrinho();
