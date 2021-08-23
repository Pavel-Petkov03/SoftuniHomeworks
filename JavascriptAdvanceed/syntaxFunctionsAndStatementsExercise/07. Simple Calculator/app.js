function calculator() {
    function init(selector1, selector2 , resultSelector){
        this.selector1 = document.querySelector(selector1)
        this.selector2 = document.querySelector(selector2)
        this.resultSelector = document.querySelector(resultSelector)
    }

    function subtract(){
        this.resultSelector.value = Number(this.selector1.value) - Number(this.selector2.value)
    }

    function add(){
        this.resultSelector.value = Number(this.selector2.value) + Number(this.selector1.value)
    }

    return {
        init , subtract , add
    }
}


const calculate = calculator ();
calculate.init ('#num1', '#num2', '#result');


