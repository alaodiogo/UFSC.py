porcao_curupira = int(input())
porcao_boitata = int(input())
porcao_boto = int(input())
porcao_mapinguari = int(input())
porcao_iara = int(input())

curupira_come = 300
boitata_come = 1500
boto_come = 600
mapinguari_come = 1000
iara_come = 150
chica_come = 225

total_mandioca = ((curupira_come * porcao_curupira) + (boitata_come * porcao_boitata) + (boto_come * porcao_boto) \
                  + (mapinguari_come * porcao_mapinguari) + (iara_come * porcao_iara) + chica_come)

print (total_mandioca)
