fun main() {
    val calc = Calculator()
    val math = MathOperations(calc)
    val result = math.calculateSum(10, 20)
    println("Rezultat je: $result")
}

class MathOperations(val calc: Calculator) {
    fun calculateSum(a: Int, b: Int): Int {
        println("Računam zbir $a i $b")
        return calc.add(a, b)
    }
}

class Calculator {
    fun add(x: Int, y: Int): Int {
        println("Sabiranje: $x + $y")
        val sum = x + y
        return sum
    }
}