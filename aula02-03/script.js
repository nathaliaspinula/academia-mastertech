// let filmes = ['Harry Potter', 'Titanic', 'Laranja Mecânica', 'Wall-e'];
// let i;

// // for tradicional
// for (i=0; i<filmes.length; i++) {
//     console.log(i + ". " + filmes[i]);
// }

// // for of = percorre os elementos da lista
// for (let item of filmes) {
//     console.log(item);
// }

// // for in = percorre indices
// for (let item in filmes) {
//     console.log(filmes[item]);
// }

// // calculadora
// function calculadora(a,b) {

// }
// let continuar = true;
// while (cons)
// console.log(calculaMedia(lista));
// // media
// function calculaMedia(lista) {
//     let soma = 0, cont = 0, media = 0;
//     for (let item in lista) {
//         soma += lista[item];
//         cont = cont + 1;
//     }
//     media = soma/cont;
//     return media;
// }

// // arrow function 
// calcMedia = (n1,n2,n3) => {
//     return ((n1+n2+n3)/3).toFixed(1);
// }
var idade = prompt("Digite sua idade: ");
indicaFilme(idade);
function indicaFilme(idade) {
    let filmes = [
        {titulo:"Star Wars", classificacao: 14},
        {titulo:"Shrek", classificacao: 0},
        {titulo:"Ninja Assassino", classificacao: 18},
    ];
    let text = "";
    for (let item of filmes) {
        if (item.classificacao <= idade) {
            text += "\n" + item.titulo;
        }
    }
    alert("Filmes Indicados: " + text);
}
