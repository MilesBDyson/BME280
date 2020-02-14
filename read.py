import bme280_sensor

show = bme280_sensor.get_all()
temp1 = bme280_sensor.get_tempf()
temp2 = bme280_sensor.get_tempc()
humid = bme280_sensor.get_humidity()
pressure = bme280_sensor.get_pressure()

print show
print str(temp1) + " F"
print str(temp2) + " C"
print str(humid) + " %"
print str(pressure) + " hPa"