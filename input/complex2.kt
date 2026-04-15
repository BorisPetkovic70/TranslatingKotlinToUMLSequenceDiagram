fun main() {
    val pump = WaterPump()
    val controller = PumpController(pump)
    val gardener = AutomaticGardener(controller)

    var day = 1
    while (day <= 3) {
        println("--- Dan $day ---")
        val report = gardener.monitorSoil(day)
        println("Izveštaj: $report")
        day = day + 1
    }
}

class AutomaticGardener(val controller: PumpController) {
    fun monitorSoil(currentDay: Int): String {
        var status = "Zemlja je vlažna"
        
        if (currentDay == 2) {
            val flow = controller.startIrrigation(50)
            status = "Navodnjavanje aktivno: $flow L/min"
        } else {
            val flow = controller.stopIrrigation()
            status = "Sistem u mirovanju"
        }
        
        return status
    }
}

class PumpController(val pump: WaterPump) {
    fun startIrrigation(power: Int): Int {
        return pump.powerOn(power)
    }

    fun stopIrrigation(): Int {
        return pump.powerOff()
    }
}

class WaterPump {
    fun powerOn(level: Int): Int {
        return level * 2
    }

    fun powerOff(): Int {
        return 0
    }
}