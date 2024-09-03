// contador.js
function contarA(frase) {
    const count = (frase.match(/a/gi) || []).length; // Conta 'a' e 'A'
    return count;
}

document.getElementById('contarBtn').addEventListener('click', function() {
    const frase = document.getElementById('fraseInput').value;
    const letraACount = contarA(frase);

    const resultadoElement = document.getElementById('resultadoContagem');
    if (letraACount > 0) {
        resultadoElement.innerText = `A letra 'a' aparece ${letraACount} vezes na string.`;
    } else {
        resultadoElement.innerText = "A letra 'a' não aparece nenhuma vez na string.";
    }
});
