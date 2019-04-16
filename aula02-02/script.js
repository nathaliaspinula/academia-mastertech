
// Senha
    let nome = prompt("Digite seu nome: ")
    let senhaCadastrada = "aviao123";
    let senhaDigitada = prompt("Digite sua senha");
    
    if (senhaCadastrada === senhaDigitada) {
        // Saque 
        let saldo = 300;
        let vlrSaque = prompt("Olá, " + nome + "!\nSeu saldo é R$"+ saldo +",00.\nDigite o valor do saque: ");
        if (vlrSaque <= saldo) {
            let novoSaldo = saldo - vlrSaque;
            alert("Saque aprovado. Seu novo saldo é: R$" + novoSaldo);
        }
        else {
            alert("Saldo insuficiente.");
        }
    }
    else {
        alert("Senha Incorreta.")
    }
