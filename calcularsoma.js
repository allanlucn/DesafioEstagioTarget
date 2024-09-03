// calcularsoma.js
function calcularSoma(indice) {
    let soma = 0;
    let k = 1;

    while (k < indice) {
        k += 1;
        soma += k;
    }
    return soma;
}

document.getElementById('calcularBtn').addEventListener('click', function () {
    const indice = 12;
    const resultadosoma = calcularSoma(indice);
    document.getElementById('resultadosoma').innerText = `A soma dos números de 1 até ${indice} é: ${resultadosoma}`;
});
