fun main() {
    val ac = AirConditioner()
    val term = Thermostat(ac)
    val owner = HomeOwner(term)
    owner.comeHome()
    
}

class HomeOwner(val term: Thermostat) {
    fun comeHome() {
        println("Stigao sam kući")
        term.setDesiredTemp(22)
    }
    
}

class Thermostat(val ac: AirConditioner) {
    fun setDesiredTemp(temp: Int) {
        println("Podešavam temperaturu na $temp°C")
        ac.startCooling(temp)
    }
    
}

class AirConditioner {
    fun startCooling(targetTemp: Int) {
        println("Klima radi, hladi na $targetTemp°C")
    }
    
}