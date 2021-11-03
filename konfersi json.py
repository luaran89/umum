import os

berat = input("masukkan data berat : ")
tarif = input("masukkan data tarif : ")
kelipatan = input("masukkan kelipatan : ")
layanan = input("masukkan kodelayanan ; ")
berat2 = berat.split('|')
tarif2 = tarif.split('|')


panjang = int((len(berat2)))
panjang2 = int((len(tarif2)))
"""
print("Banyak Data Berat : ", panjang)
print("Banyak Data Tarif : ", panjang2)
print(berat2)
print(tarif2)
"""
jumlah1 = 1
i = 0
berat3 = []
tarif3 = []

for i in range(len(tarif2)):
    if not berat2[i]:
      #  print("base_tariff_", jumlah1, ":", tarif2[i])
        tarif3.append('"base_tariff_'+str(jumlah1)+'":'+str(tarif2[i])+",")
    else:
        #print("actual_weight_", jumlah1, ":", berat2[i], "base_tariff_", jumlah1, ":", tarif2[i])
        berat3.append('"actual_weight_'+str(jumlah1)+'":'+str(berat2[i])+",")
        tarif3.append('"base_tariff_'+str(jumlah1)+'":'+str(tarif2[i])+",")
    jumlah1 = jumlah1+1
hasil = ('{'+''.join(berat3)+''.join(tarif3)+'"kelipatan":' +
         str(kelipatan)+',"kdlayanan_pelanggan":'+str(layanan)+'}')
#to_json = json.dump(hasil)
# print(to_json)

print(hasil)
os.system("pause")
