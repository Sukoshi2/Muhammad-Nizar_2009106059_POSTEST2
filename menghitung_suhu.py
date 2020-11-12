print("----------Konversi Suhu----------")
#pertama kita masukan nilai suhu celcius
suhu = int(input("Masukan nilai suhu dalam satuan Celcius : "))
#kedua kita membuat fungsi untuk menghitung konversi suhu dan masukan rumus-rumus konversi suhu(celcius) ke Kelvin,Fahrenheit,dan reamur
kelvin = 273 + suhu
fahrenheit = (suhu * 9/5)+32
reamur = 4/5 * suhu
#ketiga kita outputkan hasil dari operasi konversi suhu di setiap macam suhu
print("Konversi Suhu dari celcius ke kelvin yaitu : ", kelvin , "K")
print("Konversi Suhu dari celcius ke fahrenheit yaitu : ", fahrenheit , "F")
print("Konversi Suhu dari celcius ke reamur yaitu : ", reamur , "R")
print("----------Terima Kasih----------")
