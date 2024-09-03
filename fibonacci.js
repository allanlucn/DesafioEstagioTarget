// fibonacci.js
const FibonacciUtils = {
    sequenciaFib(n) {
        let a = 0, b = 1;
        while (a < n) {
            [a, b] = [b, a + b];
        }
        return a === n;
    },

    pertenceASequencia(n) {
        return n >= 0 && this.sequenciaFib(n);
    },

    verificarNumero() {
        const numeroInput = document.getElementById("numeroInput");
        const resultado = document.getElementById("resultado");
        const numero = parseInt(numeroInput.value);

        if (!isNaN(numero)) {
            if (this.pertenceASequencia(numero)) {
                resultado.innerText = `${numero} pertence à sequência de Fibonacci.`;
            } else {
                resultado.innerText = `${numero} não pertence à sequência de Fibonacci.`;
            }
        } else {
            resultado.innerText = "O número informado não é válido.";
        }
    },

    init() {
        const botao = document.getElementById("verificarBtn");
        botao.addEventListener("click", this.verificarNumero.bind(this));
    }
};

// Inicializa após o carregamento do documento
document.addEventListener("DOMContentLoaded", () => {
    FibonacciUtils.init();
});