fun main() {
    val heater = Heater()
    val thermostat = Thermostat(heater)
    val room = Room(thermostat, 18)
    
    // Simulacija temperature tokom dana
    val temperatures = listOf(18, 22, 26, 19, 24)
    
    for (temp in temperatures) {
        println("\n=== Provjera za temperaturu: $temp°C ===")
        room.currentTemp = temp
        room.checkTemperature()
    }
}

class Room(val thermostat: Thermostat, var currentTemp: Int) {
    fun checkTemperature() {
        println("Trenutna temperatura je $currentTemp°C")
        if (currentTemp < 20) {
            println("Hladno je, palim grijanje")
            thermostat.setHeating(true)
        } else {
                println("Prevruće je, palim hlađenje")
                thermostat.setCooling(true)
            
        }
    }
}

class Thermostat(val heater: Heater) {
    fun setHeating(enable: Boolean) {
        if (enable) {
            println("Termostat: uključujem grijanje")
            heater.turnOn()
        } else {
            println("Termostat: isključujem grijanje")
            heater.turnOff()
        }
    }
    
    fun setCooling(enable: Boolean) {
        if (enable) {
            println("Termostat: uključujem hlađenje")
            heater.startCooling()
        } else {
            println("Termostat: isključujem hlađenje")
            heater.stopCooling()
        }
    }
}

class Heater {
    fun turnOn() {
        println("Grijalica radi, grije prostoriju")
    }
    
    fun turnOff() {
        println("Grijalica je ugašena")
    }
    
    fun startCooling() {
        println("Klima radi, hladi prostoriju")
    }
    
    fun stopCooling() {
        println("Klima je ugašena")
    }
}