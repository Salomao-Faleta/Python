//Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

// let numero = Number(promptp("Digite um número:"))
// console.log(`O antecessor de ${numero} é ${numero - 1}`);
// console.log(`O sucessor de ${numero} é ${numero + 1}`);


// Exercício Python 06: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

// let numero = Number(prompt("Digite um número"))
// console.log(`O dobro de ${numero} é ${numero * 2}`)
// console.log(`O triplo de ${numero} é ${numero * 3}`)
// console.log(`A raiz quadrada de ${numero} é ${numero ** (1/2).toFixed(2)}`)


// Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

// let nota1 = Number(prompt("Digte a nota 1"))
// let nota2 = Number(prompt("Digte a nota 2"))
// console.log(`A média od aluno foi: ${(nota1 + nota2) / 2}`)




/*
    Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
    O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
    mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
*/

// let num_digitado = soma = 0;
// let numero = Number(prompt('Digite um número [999 PARA PARAR]'));

// while(numero != 999){
    
//     soma+=numero;
//     num_digitado++;
    
//     numero = Number(prompt('Digite um número [999 PARA PARAR]'));
// }

// console.log(`Números digitados: ${num_digitado}`)
// console.log(`A soma dos números deu ${soma}`)




/*
    Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
*/

//todas as variaveis terão o valor 0 (zero)

// let media = quant = soma = maiorNum = menorNum = 0;

// while(true){
//     let numero = Number(prompt('Digite um número'));

//     soma += numero;
//     quant++;
//     media = soma / quant;

//     if(quant == 1){
//         maiorNum = menorNum = numero;
//     }else{
//         if(numero > maiorNum){
//             maiorNum = numero
//         }

//         if(numero < menorNum){
//             menorNum = numero
//         }
//     }
    
//     let pergunta = prompt('Deseja continuar? [S/N]').charAt(0).toUpperCase();
//     if(pergunta == 'N'){
//         break;
//     }

// }

// console.log(`a soma dos numeros foi: ${soma}`)
// console.log(`vezes: ${quant}`)
// console.log(`a media foi ${media.toFixed(2)}`)
// console.log(`O maior núemro foi: ${maiorNum}`)
// console.log(`O menor núemro foi: ${menorNum}`)




// Exercício JS 66: Crie um programa que leia números inteiros pelo teclado.
// O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
// No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


// let numero = Number(prompt('Digite um núemro (999 para parar): '))
// let soma = 0;
// let num_digitado = 0;

// while(numero != 999) {
//     soma += numero;
//     num_digitado += 1

//     numero = Number(prompt('Digite um núemro (999 para parar): '))
// }

// console.log(`A soma dos números foi ${soma} e vc digitou ${num_digitado}`);





// Exercício JS 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
// para cada valor digitado pelo usuário.
// O programa será interrompido quando o número solicitado for negativo.


// while (true) {
//     let numero = Number(prompt('Quer ver que tabuada? '));

//     if (numero > 0) {
//         for (let i = 1; i < 11; i++) {
//             console.log(`${numero} x ${i} = ${numero * i}`);
//         }
//     }

//     else{
//         console.log('NÃO ACEITAMOS NÚMEROS INVÁLIDOS');
//         break;
//     }

// }



// Exercício JS 68: Faça um programa que jogue par ou ímpar com o computador.
// O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
// conquistou no final do jogo.

// let vitoria = 0;

// while(true){
//     let jogador = Number(prompt('Digite um número '));
//     let compuatdor = Math.floor(Math.random() * 10);
//     let total = jogador + compuatdor;
//     let tipo = prompt('PAR OU ÍMPAR? ').toUpperCase().charAt(0);

//     if(tipo == 'P'){
//         if(total % 2 == 0){
//             alert('VOCÊ GANHOU');
//             alert(`vc jogou ${jogador} computador ${compuatdor} = ${total}`)
//             vitoria+=1;
//         }else{
//             alert('VOCÊ PEDEU')
//             alert(`vc jogou ${jogador} computador ${compuatdor} = ${total}`)
//             break;
//         }
//     }else if(tipo == 'I'){
//         if(total % 2 == 1){
//             alert('VOCÊ VENCEU');
//             alert(`vc jogou ${jogador} computador ${compuatdor} = ${total}`)
//             vitoria+=1;
//         }else{
//             alert('VOCÊ PERDEU');
//             alert(`vc jogou ${jogador} computador ${compuatdor} = ${total}`)
//             break;
//         }
//     }
// }

// console.log(`você jogou ${vitoria} vezes`)



// Exercício JS 69: Crie um programa que leia a idade e o sexo de várias pessoas.
// A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

// A) quantas pessoas tem mais de 18 anos.

// B) quantos homens foram cadastrados.

// C) quantas mulheres tem menos de 20 anos.

// let maioresDeIdade = 0;
// let homensCadastrados = 0;
// let mulhereMenos20 = 0;

// while (true) {
//     let idade = +prompt('Digite sua idade: ');
//     let sexo = prompt('Digite seu sexo: ').toLocaleUpperCase().charAt(0);

//     if (idade > 18) {
//         maioresDeIdade++;
//     }

//     if (sexo == 'M') {
//         homensCadastrados++;
//     }

//     if (idade < 20 && sexo == 'F') {
//         mulhereMenos20++;
//     }

//     pergunta = prompt('Deseja continuar cadastrando? [S/N]').toUpperCase().charAt(0);
//     if (pergunta == 'N') {
//         break;
//     }
// }

// console.log(`Total de pessoas com mais de 18 anos: ${maioresDeIdade}`);
// console.log(`Total de homens cadastrados: ${homensCadastrados}`);

// if (mulhereMenos20 > 1) {
//     console.log(`E temos ${mulhereMenos20} mulheres com menos de 20 anos`);
// }else{
//     console.log(`E temos ${mulhereMenos20} mulher com menos de 20 anos`);

// }




// Exercício JS 70: Crie um programa que leia o nome e o preço de vários produtos.
// O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

// A) qual é o total gasto na compra.

// B) quantos produtos custam mais de R$1000.

// C) qual é o nome do produto mais barato.


// let totCompra = 0;
// let produtoMaisMil = 0;
// let produtoMaisBarato = 0;
// let menor = 0;
// let cont = 0;


// while (true) {
//     let nomeProduto = prompt('Qual o nome do produto? ');
//     let precoProduto = Number(prompt('Qual o preço? R$ '));
//     cont++;

//     totCompra += precoProduto;

//     if (precoProduto > 1000) {
//         produtoMaisMil++;
//     }

//     if (cont == 1) {
//         menor = precoProduto;
//         produtoMaisBarato = nomeProduto;
//     } else if (precoProduto < menor) {
//         menor = precoProduto
//         produtoMaisBarato = nomeProduto

//     }

//     let pergunta = prompt('Deseja continuar? [S/N]').toUpperCase().charAt(0);
//     if (pergunta == 'N') {
//         break;
//     }


// }

// console.log('---------FINALIZANDO COMPRA---------')
// console.log(`O total da compra foi: ${totCompra.toFixed(2)}`);
// console.log(`Temos ${produtoMaisMil} produtos que custam mais de R$1000 reais`);
// console.log(`E o produto mais barato custa ${menor.toFixed(2)}`);
