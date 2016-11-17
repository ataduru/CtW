import os
import copy
from threading import Thread
import time
from random import *
import sys
import objects
import pickle
#import cl


secenekler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]

secenekler2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]

renkler = {'216': 'k', '217': 'X', '214': 'i', '215': '-', '212': 'u', '213': 'O', '210': '>', '211': 'W', '165': 'S', '218': 'g', '219': 'P', '133': '/', '132': 'S', '131': 'i', '130': 'o', '137': 'Y', '136': 'W', '135': 'Y', '134': 'i', '139': 'P', '138': 'I', '166': '`', '24': 'z', '25': '4', '26': '|', '27': 'C', '20': 'j', '21': 'n', '22': '_', '23': 'O', '160': 'q', '28': '+', '29': ' ', '161': '=', '4': 'w', '8': 'i', '163': '[', '119': ' ', '120': '.', '121': '=', '122': 'X', '123': 'r', '124': '5', '125': '&', '126': 'c', '127': 'L', '128': '(', '129': '.', '167': 'e', '118': 'G', '59': 'h', '58': 'y', '55': 'n', '54': 'F', '57': 'Y', '56': 'd', '51': 'H', '50': 'w', '53': 'u', '52': '>', '164': 'R', '201': '7', '199': 'm', '179': 's', '200': 'k', '195': 'j', '194': 'G', '197': '<', '178': '.', '191': 'I', '190': '2', '193': '9', '192': 'G', '115': '[', '114': 's', '88': ':', '89': '(', '111': '@', '110': 'U', '113': 'U', '112': 'Y', '82': '_', '83': 'Z', '80': ',', '81': '(', '86': 'f', '87': ':', '84': '`', '85': '*', '251': 'n', '198': 'j', '256': 'O', '206': '*', '226': 's', '3': '-', '177': 'P', '254': '_', '7': 'y', '247': '6', '255': 'W', '225': 'L', '245': '&', '244': '4', '108': ')', '109': 'g', '241': 'u', '240': 'W', '243': '`', '242': 'I', '102': ';', '103': '3', '100': '?', '101': 'n', '106': '9', '107': '?', '104': '^', '105': 'O', '39': '"', '38': 'j', '33': '2', '32': '(', '31': 'R', '30': 'K', '37': '{', '36': 'n', '35': 'Z', '34': 'B', '246': '=', '252': 'F', '205': '@', '223': 'x', '176': 'l', '60': 'C', '61': '.', '62': 'B', '63': 'T', '64': '(', '65': 'p', '66': 'K', '67': 'C', '68': 'h', '69': '^', '175': 'E', '174': 'q', '173': '4', '172': '6', '171': 'A', '170': 'a', '203': 'n', '222': 'q', '181': 'G', '253': 'X', '248': 'U', '182': ')', '183': ']', '180': '6', '2': '%', '162': 'B', '187': '.', '184': 'Q', '6': 'A', '220': 'F', '186': 'O', '188': 'z', '189': '"', '202': 'g', '196': '`', '221': 'F', '185': '6', '99': ':', '98': 'W', '168': '/', '169': 't', '229': '$', '228': 'H', '91': 'J', '90': '/', '93': 'A', '92': ' ', '95': 'p', '94': 'O', '97': 'C', '96': '|', '11': '.', '10': 'R', '13': 'g', '12': '!', '15': 'c', '14': '^', '17': '/', '16': '-', '19': '+', '18': 'G', '117': '*', '250': '6', '116': 'm', '204': '?', '151': '0', '150': 'c', '153': ']', '152': 'M', '155': 'L', '154': 'I', '157': '[', '156': '4', '159': 'u', '158': 'H', '234': '^', '238': '9', '239': 'A', '207': '"', '235': 'Z', '236': '}', '237': 'K', '230': "'", '231': 'O', '232': '1', '233': 'i', '224': 'J', '48': '4', '49': 'h', '46': 'g', '47': 'c', '44': 'u', '45': 'A', '42': '5', '43': '{', '40': ' ', '41': 'j', '1': 'j', '5': 'I', '9': '?', '146': 'n', '147': '5', '144': 'V', '145': 'q', '142': 'U', '143': 'O', '140': 'E', '141': 'R', '209': 'B', '208': 'H', '148': '?', '149': 'p', '77': '?', '76': '#', '75': 'K', '74': '5', '73': '?', '72': '~', '71': '|', '70': 'R', '79': 'w', '78': 'j', '249': 'j', '227': 'k'}

oyunTipi = 0

class User:
	empire_no = 0
	noktalar = []
	def bilgiler(self, empire_id):
		return objects.dicts[`empire_id`].coin

	#def asker_uretim_hizini_arttir(self):
	#	if(objects.dicts[`self.empire_no`].coin > 5000):
	#		objects.dicts[`self.empire_no`].askeri_okul.hiz += 1
	#		oobjects.dicts[`self.empire_no`].coin -= 5000

	def saldiri_asker_gucu_arttir(self):
		if(objects.dicts[`self.empire_no`].coin > 10000):
			objects.dicts[`self.empire_no`].saldiri_askerleri.saldiri_gucu += 1
			objects.dicts[`self.empire_no`].coin -= 10000

	def savunma_asker_gucu_arttir(self):
		if(objects.dicts[`self.empire_no`].coin > 10000):
			objects.dicts[`self.empire_no`].savunma_askerleri.saldiri_gucu += 1
			objects.dicts[`self.empire_no`].coin -= 10000

	def isci_sayisi_arttir(self):
		if(objects.dicts[`self.empire_no`].coin > 1000):
			objects.dicts[`i`].tahta_ureten_isciler +=  int((objects.dicts[`i`].tahta_ureten_isciler/2)*objects.dicts[`self.empire_no`].isci_okulu.saglamlik_durumu)
			objects.dicts[`i`].metal_ureten_isciler +=  int((objects.dicts[`i`].metal_ureten_isciler/2)*objects.dicts[`self.empire_no`].isci_okulu.saglamlik_durumu)
			objects.dicts[`self.empire_no`].coin -= 1000

	def bankayi_gelistir(self):
		if(objects.dicts[`self.empire_no`].coin > 6000):
			objects.dicts[`self.empire_no`].banka.uretilen_coin += int(25*objects.dicts[`self.empire_no`].banka.saglamlik_durumu)
			objects.dicts[`self.empire_no`].coin -= 6000

	def savunmayi_arttir(self):
		if(objects.dicts[`self.empire_no`].coin > 10000):
			if(objects.dicts[`self.empire_no`].sinir_savunmasi + objects.dicts[`self.empire_no`].sinir_savunmasi/2 < 50):
				objects.dicts[`self.empire_no`].sinir_savunmasi = 50
				objects.dicts[`self.empire_no`].coin -= 10000
			else:
				objects.dicts[`self.empire_no`].sinir_savunmasi += objects.dicts[`self.empire_no`].sinir_savunmasi/2 
				objects.dicts[`self.empire_no`].coin -= 10000

	def savunma_askeri_sayisi_arttir(self, sayi):
		if(objects.dicts[`self.empire_no`].coin > (50*sayi)):
			objects.dicts[`self.empire_no`].savunma_askerleri.sayi += int(sayi*objects.dicts[`self.empire_no`].askeri_okul.saglamlik_durumu)
			objects.dicts[`self.empire_no`].coin -= (50*sayi)

	def saldiri_askeri_sayisi_arttir(self, sayi):
		if(objects.dicts[`self.empire_no`].coin > (50*sayi)):
			objects.dicts[`self.empire_no`].saldiri_askerleri.sayi += int(sayi*objects.dicts[`self.empire_no`].askeri_okul.saglamlik_durumu)
			objects.dicts[`self.empire_no`].coin -= (50*sayi)

	def hastaneyi_gelistir(self, tedavi_iyilestirme_hizi):
		self.tedavi_iyilestirme_hizi = tedavi_iyilestirme_hizi+1

	def hava_saldirisi(self):
		if(objects.dicts[`self.empire_no`].coin > 10000 and objects.dicts[`self.empire_no`].tahta_miktari > 1000 and objects.dicts[`self.empire_no`].metal_miktari > 750):
			objects.dicts[`self.empire_no`].hava_saldirisi += 1
			objects.dicts[`self.empire_no`].tahta_miktari -= 1000
			objects.dicts[`self.empire_no`].tahta_miktari -= 750
			objects.dicts[`self.empire_no`].coin -= 10000

	def deniz_saldirisi(self):
		if(objects.dicts[`self.empire_no`].coin > 10000):
			objects.dicts[`self.empire_no`].deniz_saldirisi += 1
			objects.dicts[`self.empire_no`].coin -= 10000

	def yapiyi_onar(self, yapi_turu):
		if(objects.dicts[`self.empire_no`].coin > 3000 and objects.dicts[`self.empire_no`].tahta_miktari > 1000 and objects.dicts[`self.empire_no`].metal_miktari > 700):
			if(yapi_turu == 1):
				if(objects.dicts[`self.empire_no`].askeri_okul.saglamlik_durumu < 1):
					objects.dicts[`self.empire_no`].askeri_okul.saglamlik_durumu += 0.1
			if(yapi_turu == 2):
				if(objects.dicts[`self.empire_no`].isci_okulu.saglamlik_durumu < 1):
					objects.dicts[`self.empire_no`].isci_okulu.saglamlik_durumu += 0.1
			if(yapi_turu == 3):
				if(objects.dicts[`self.empire_no`].banka.saglamlik_durumu < 1):
					objects.dicts[`self.empire_no`].banka.saglamlik_durumu += 0.1

			objects.dicts[`self.empire_no`].coin -= 3000
			objects.dicts[`self.empire_no`].tahta_miktari -= 1000
			objects.dicts[`self.empire_no`].metal_miktari -= 700
	

	def hava_saldirisi_yap(self, savunan):
		if(objects.dicts[`self.empire_no`].hava_saldirisi == 1):
			objects.dicts[`savunan`].sinir_savunmasi -= 40
			objects.dicts[`savunan`].savunma_askerleri.sayi -= 60
			objects.dicts[`savunan`].tahta_ureten_isciler -= 20
			objects.dicts[`savunan`].metal_ureten_isciler -= 15
			objects.dicts[`self.empire_no`].hava_saldirisi -= 1

	def saldir(self, empire_id):

		saldiranrandom=[]
		savunanrandom=[]
		
		kalsin=0
		tersecevir=0			
		savunansolda=0
		savunansagda=0
		kalsinflag = 0
		tersecevirflag=0
		savunansagdaflag=0
		savunansoldaflag=0		

		if len(objects.dicts[`self.empire_no`].yuz_olcumu[2]) > 0:
			for i in range(80):
				x=choice(objects.dicts[`self.empire_no`].yuz_olcumu[2]) 
				saldiranrandom.append(x)		

		if len(objects.dicts[`empire_id`].yuz_olcumu[2]) > 0:
			for i in range(80):
				x=choice(objects.dicts[`empire_id`].yuz_olcumu[2]) 
				savunanrandom.append(x)		
		
		for i in saldiranrandom:
			for j in savunanrandom:
				if(i[0]<j[0]):
					kalsin+=1
				if(i[0]>j[0]):
					tersecevir+=1
				if(i[1]>j[1]):
					savunansolda+=1						
				if(i[1]<j[1]):
					savunansagda+=1
				

		if(kalsin==max(kalsin,tersecevir,savunansolda,savunansagda)):
			objects.dicts[`self.empire_no`].yuz_olcumu[2].sort()
			kalsinflag = 1
			objects.dicts[`self.empire_no`].yuz_olcumu[2].reverse()

		if(tersecevir==max(kalsin,tersecevir,savunansolda,savunansagda)):
			tersecevirflag=1
			objects.dicts[`empire_id`].yuz_olcumu[2].reverse()

		if(savunansagda==max(kalsin,tersecevir,savunansolda,savunansagda)):
			savunansagdaflag=1
			for i in range(len(objects.dicts[`empire_id`].yuz_olcumu[2])):
				objects.dicts[`empire_id`].yuz_olcumu[2][i][0],objects.dicts[`empire_id`].yuz_olcumu[2][i][1]=objects.dicts[`empire_id`].yuz_olcumu[2][i][1],objects.dicts[`empire_id`].yuz_olcumu[2][i][0]
				

			objects.dicts[`empire_id`].yuz_olcumu[2].sort()


			for i in range(len(objects.dicts[`empire_id`].yuz_olcumu[2])):
				objects.dicts[`empire_id`].yuz_olcumu[2][i][0],objects.dicts[`empire_id`].yuz_olcumu[2][i][1]=objects.dicts[`empire_id`].yuz_olcumu[2][i][1],objects.dicts[`empire_id`].yuz_olcumu[2][i][0]

		if(savunansolda==max(kalsin,tersecevir,savunansolda,savunansagda)):
			savunansoldaflag=1
			for i in range(len(objects.dicts[`empire_id`].yuz_olcumu[2])):
				objects.dicts[`empire_id`].yuz_olcumu[2][i][0],objects.dicts[`empire_id`].yuz_olcumu[2][i][1]=objects.dicts[`empire_id`].yuz_olcumu[2][i][1],objects.dicts[`empire_id`].yuz_olcumu[2][i][0]
				

			objects.dicts[`empire_id`].yuz_olcumu[2].sort()


			for i in range(len(objects.dicts[`empire_id`].yuz_olcumu[2])):
				objects.dicts[`empire_id`].yuz_olcumu[2][i][0],objects.dicts[`empire_id`].yuz_olcumu[2][i][1]=objects.dicts[`empire_id`].yuz_olcumu[2][i][1],objects.dicts[`empire_id`].yuz_olcumu[2][i][0]

			objects.dicts[`empire_id`].yuz_olcumu[2].reverse()
				
		ekstra_atak = 0
		diger_ulke = 0

		
		for i in objects.dicts[`empire_id`].yuz_olcumu[2]:
			if i[0] == 99 or i[0] == 899 or i[1] == 99 or i[1] == 899:
				diger_ulke = 1
				break

		if(objects.dicts[`self.empire_no`].deniz_saldirisi != 0 and diger_ulke==1):		
			for i in objects.dicts[`self.empire_no`].yuz_olcumu[2]:
				if i[0] == 99 or i[0] == 899 or i[1] == 99 or i[1] == 899:
					ekstra_atak = objects.dicts[`self.empire_no`].deniz_saldirisi
					break

		saldiran = objects.dicts[`self.empire_no`].saldiri_askerleri		
		savunan = objects.dicts[`empire_id`].savunma_askerleri


		if(((saldiran.sayi * (saldiran.saldiri_gucu + ekstra_atak))*2 + ((savunan.sayi * savunan.savunma_gucu) + objects.dicts[`empire_id`].sinir_savunmasi)*3) > 0):
			
			savunma = (savunan.sayi * savunan.savunma_gucu)
			saldirma = (saldiran.sayi * (saldiran.saldiri_gucu+ekstra_atak))

			toprakMiktari = (int(saldirma / (savunma + objects.dicts[`empire_id`].sinir_savunmasi)))*10
			asd=len(objects.dicts[`empire_id`].yuz_olcumu[2])
			

			if(toprakMiktari>=asd):
				toprakMiktari=asd
			toprak=toprakMiktari
			

			turSayisi = 0

			#lost = randint(0,100)
			#if(lost in range(20,35)):
			#	toprakMiktari = 0

			if (toprakMiktari % 50 == 0):
				turSayisi = toprakMiktari/50

			elif (toprakMiktari % 50 > 0):
				turSayisi = toprakMiktari/50
			
			turSayisi = turSayisi+1
			control = toprakMiktari

			while(turSayisi):
				
				if turSayisi == 1:
					toprakMiktari = control % 50
				else:
				    toprakMiktari = 50

				sonA = control

				for i in objects.dicts[`empire_id`].yuz_olcumu[2]:
					for j in objects.dicts[`self.empire_no`].yuz_olcumu[2]:
						if(toprakMiktari == 0):
							break
						else:
							if(i[0]==j[0]):
								if(i[1]+1==j[1] or i[1]==j[1]+1):
									if(i not in self.noktalar):
										self.noktalar.append(i)	
										toprakMiktari -= 1						
										control -= 1			

							elif(i[1]==j[1]):
								if(i[0]+1==j[0] or i[0]==j[0]+1):
									if(i not in self.noktalar):
										self.noktalar.append(i)	
										toprakMiktari -= 1	
										control -= 1			

				if toprakMiktari == 0:				
					turSayisi -= 1
				
				if(control==toprak):
					break	

				
				objects.dicts[`self.empire_no`].yuz_olcumu[2].extend(self.noktalar)
				for i in self.noktalar:
					if(i in objects.dicts[`empire_id`].yuz_olcumu[2]): 				
						objects.dicts[`empire_id`].yuz_olcumu[2].remove(i)	

				del self.noktalar [:]	
		
				if(sonA == control):
					break

			if(toprak != toprakMiktari):
				if objects.dicts[`empire_id`].savunma_askerleri.sayi - int((float(saldirma)/(saldirma+savunma))*(objects.dicts[`empire_id`].savunma_askerleri.sayi)/5) > 0:
					objects.dicts[`empire_id`].savunma_askerleri.sayi -= int((float(saldirma)/(saldirma+savunma))*(objects.dicts[`empire_id`].savunma_askerleri.sayi)/5)
				if objects.dicts[`self.empire_no`].saldiri_askerleri.sayi - int((float(savunma)/(saldirma+savunma))*(objects.dicts[`self.empire_no`].saldiri_askerleri.sayi)/5) > 0:
					objects.dicts[`self.empire_no`].saldiri_askerleri.sayi -= int((float(savunma)/(saldirma+savunma))*(objects.dicts[`self.empire_no`].saldiri_askerleri.sayi)/5)
				if(objects.dicts[`empire_id`].sinir_savunmasi - (objects.dicts[`empire_id`].sinir_savunmasi/5) * 2 > 0):
					objects.dicts[`empire_id`].sinir_savunmasi -= (objects.dicts[`empire_id`].sinir_savunmasi/5) * 2
				#objects.dicts[`empire_id`].yuz_olcumu[2].sort()
				#objects.dicts[`self.empire_no`].yuz_olcumu[2].sort()
				harita.GridUpdate(self.empire_no, empire_id)

				hasarMiktari = int(toprakMiktari/10)
				if( 2 < hasarMiktari or hasarMiktari < 4):
					if(objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu > 0.1):
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu -= 0.1
					else:
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu = 0
				elif( 4 <= hasarMiktari or hasarMiktari < 6):
					if(objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu > 0.2):
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu -= 0.2
					else:
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu = 0

					if(objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu > 0.1):
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu -= 0.1
					else:
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu = 0

				elif( 6 <= hasarMiktari or hasarMiktari < 8):
					if(objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu > 0.3):
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu -= 0.3
					else:
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu = 0

					if(objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu > 0.2):
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu -= 0.2
					else:
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu = 0

					if(objects.dicts[`empire_id`].banka.saglamlik_durumu > 0.1):
						objects.dicts[`empire_id`].banka.saglamlik_durumu -= 0.1
					else:
						objects.dicts[`empire_id`].banka.saglamlik_durumu = 0

				elif(8 <= hasarMiktari):
					if(objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu > 0.3):
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu -= 0.3
					else:
						objects.dicts[`empire_id`].isci_okulu.saglamlik_durumu = 0

					if(objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu > 0.3):
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu -= 0.3
					else:
						objects.dicts[`empire_id`].askeri_okul.saglamlik_durumu = 0

					if(objects.dicts[`empire_id`].banka.saglamlik_durumu > 0.3):
						objects.dicts[`empire_id`].banka.saglamlik_durumu -= 0.2
					else:
						objects.dicts[`empire_id`].banka.saglamlik_durumu = 0

			if kalsinflag == 1:
				objects.dicts[`self.empire_no`].yuz_olcumu[2].reverse()

			if tersecevirflag == 1:
				objects.dicts[`empire_id`].yuz_olcumu[2].reverse()

			if savunansagdaflag==1:
				objects.dicts[`empire_id`].yuz_olcumu[2].sort()

			if savunansoldaflag==1:
				objects.dicts[`empire_id`].yuz_olcumu[2].sort()

			
 


def random_saldir(c, b):	
	saldiranrandom=[]
	savunanrandom=[]
	noktalar = []
	
	kalsin=0
	tersecevir=0			
	savunansolda=0
	savunansagda=0
	kalsinflag = 0
	tersecevirflag=0
	savunansagdaflag=0
	savunansoldaflag=0		

	if len(objects.dicts[`c`].yuz_olcumu[2]) > 0:
		for i in range(80):
			x=choice(objects.dicts[`c`].yuz_olcumu[2]) 
			saldiranrandom.append(x)		

	if len(objects.dicts[`b`].yuz_olcumu[2]) > 0:
		for i in range(80):
			x=choice(objects.dicts[`b`].yuz_olcumu[2]) 
			savunanrandom.append(x)		
	
	for i in saldiranrandom:
		for j in savunanrandom:
			if(i[0]<j[0]):
				kalsin+=1
			if(i[0]>j[0]):
				tersecevir+=1
			if(i[1]>j[1]):
				savunansolda+=1						
			if(i[1]<j[1]):
				savunansagda+=1

	if(kalsin==max(kalsin,tersecevir,savunansolda,savunansagda)):
		#objects.dicts[`c`].yuz_olcumu[2].sort()
		kalsinflag = 1
		objects.dicts[`c`].yuz_olcumu[2].reverse()

	if(tersecevir==max(kalsin,tersecevir,savunansolda,savunansagda)):
		tersecevirflag=1
		objects.dicts[`b`].yuz_olcumu[2].reverse()

	if(savunansagda==max(kalsin,tersecevir,savunansolda,savunansagda)):
		savunansagdaflag=1
		for i in range(len(objects.dicts[`b`].yuz_olcumu[2])):
			objects.dicts[`b`].yuz_olcumu[2][i][0],objects.dicts[`b`].yuz_olcumu[2][i][1]=objects.dicts[`b`].yuz_olcumu[2][i][1],objects.dicts[`b`].yuz_olcumu[2][i][0]
			

		objects.dicts[`b`].yuz_olcumu[2].sort()


		for i in range(len(objects.dicts[`b`].yuz_olcumu[2])):
			objects.dicts[`b`].yuz_olcumu[2][i][0],objects.dicts[`b`].yuz_olcumu[2][i][1]=objects.dicts[`b`].yuz_olcumu[2][i][1],objects.dicts[`b`].yuz_olcumu[2][i][0]

	if(savunansolda==max(kalsin,tersecevir,savunansolda,savunansagda)):
		savunansoldaflag=1
		for i in range(len(objects.dicts[`b`].yuz_olcumu[2])):
			objects.dicts[`b`].yuz_olcumu[2][i][0],objects.dicts[`b`].yuz_olcumu[2][i][1]=objects.dicts[`b`].yuz_olcumu[2][i][1],objects.dicts[`b`].yuz_olcumu[2][i][0]
			

		objects.dicts[`b`].yuz_olcumu[2].sort()


		for i in range(len(objects.dicts[`b`].yuz_olcumu[2])):
			objects.dicts[`b`].yuz_olcumu[2][i][0],objects.dicts[`b`].yuz_olcumu[2][i][1]=objects.dicts[`b`].yuz_olcumu[2][i][1],objects.dicts[`b`].yuz_olcumu[2][i][0]

		objects.dicts[`b`].yuz_olcumu[2].reverse()
						

	saldiran = objects.dicts[`c`].saldiri_askerleri		
	savunan = objects.dicts[`b`].savunma_askerleri

	if(((saldiran.sayi * saldiran.saldiri_gucu)*2 + ((savunan.sayi * savunan.savunma_gucu) + objects.dicts[`b`].sinir_savunmasi)*3) > 0):
		
		savunma = (savunan.sayi * savunan.savunma_gucu)
		saldirma = (saldiran.sayi * saldiran.saldiri_gucu)

		toprakMiktari = (int(saldirma / (savunma + objects.dicts[`b`].sinir_savunmasi)))*10
		asd=len(objects.dicts[`b`].yuz_olcumu[2])
		

		if(toprakMiktari>=asd):
			toprakMiktari=asd
		toprak=toprakMiktari
		

		turSayisi = 0


		if (toprakMiktari % 50 > 0):
			turSayisi = toprakMiktari/50
		
		turSayisi = turSayisi+1
		control = toprakMiktari

		while(turSayisi):
			
			if turSayisi == 1:
				toprakMiktari = control % 50
				toprak = control % 50
			else:
			    toprakMiktari = 50
			    toprak = 50

			sonA = control

			for i in objects.dicts[`b`].yuz_olcumu[2]:
				for j in objects.dicts[`c`].yuz_olcumu[2]:
					if(toprakMiktari == 0):
						break
					else:
						if(i[0]==j[0]):
							if(i[1]+1==j[1] or i[1]==j[1]+1):
								if(i not in noktalar):
									noktalar.append(i)	
									toprakMiktari -= 1						
									control -= 1			

						elif(i[1]==j[1]):
							if(i[0]+1==j[0] or i[0]==j[0]+1):
								if(i not in noktalar):
									noktalar.append(i)	
									toprakMiktari -= 1	
									control -= 1			

			if toprakMiktari == 0:				
				turSayisi -= 1
			
			if(control==toprak):
				break	

			
			objects.dicts[`c`].yuz_olcumu[2].extend(noktalar)
			for i in noktalar:
				if(i in objects.dicts[`b`].yuz_olcumu[2]): 				
					objects.dicts[`b`].yuz_olcumu[2].remove(i)	

			del noktalar [:]	
	
			if(sonA == control):
				break

		if(toprak != toprakMiktari):
			if objects.dicts[`b`].savunma_askerleri.sayi - int((float(saldirma)/(saldirma+savunma))*(objects.dicts[`b`].savunma_askerleri.sayi)/5) > 0:
				objects.dicts[`b`].savunma_askerleri.sayi -= int((float(saldirma)/(saldirma+savunma))*(objects.dicts[`b`].savunma_askerleri.sayi)/5)
			if objects.dicts[`c`].saldiri_askerleri.sayi - int((float(savunma)/(saldirma+savunma))*(objects.dicts[`c`].saldiri_askerleri.sayi)/5) > 0:
				objects.dicts[`c`].saldiri_askerleri.sayi -= int((float(savunma)/(saldirma+savunma))*(objects.dicts[`c`].saldiri_askerleri.sayi)/5)
			if(objects.dicts[`b`].sinir_savunmasi - (objects.dicts[`b`].sinir_savunmasi/5) * 2 > 0):
				objects.dicts[`b`].sinir_savunmasi -= (objects.dicts[`b`].sinir_savunmasi/5) * 2
			#objects.dicts[`b`].yuz_olcumu[2].sort()
			#objects.dicts[`c`].yuz_olcumu[2].sort()
			harita.GridUpdate(c, b)

			hasarMiktari = int(toprakMiktari/10)
			if( 2 < hasarMiktari or hasarMiktari < 4):
				if(objects.dicts[`b`].isci_okulu.saglamlik_durumu > 0.1):
					objects.dicts[`b`].isci_okulu.saglamlik_durumu -= 0.1
				else:
					objects.dicts[`b`].isci_okulu.saglamlik_durumu = 0
			elif( 4 <= hasarMiktari or hasarMiktari < 6):
				if(objects.dicts[`b`].isci_okulu.saglamlik_durumu > 0.2):
					objects.dicts[`b`].isci_okulu.saglamlik_durumu -= 0.2
				else:
					objects.dicts[`b`].isci_okulu.saglamlik_durumu = 0

				if(objects.dicts[`b`].askeri_okul.saglamlik_durumu > 0.1):
					objects.dicts[`b`].askeri_okul.saglamlik_durumu -= 0.1
				else:
					objects.dicts[`b`].askeri_okul.saglamlik_durumu = 0

			elif( 6 <= hasarMiktari or hasarMiktari < 8):
				if(objects.dicts[`b`].isci_okulu.saglamlik_durumu > 0.3):
					objects.dicts[`b`].isci_okulu.saglamlik_durumu -= 0.3
				else:
					objects.dicts[`b`].isci_okulu.saglamlik_durumu = 0

				if(objects.dicts[`b`].askeri_okul.saglamlik_durumu > 0.2):
					objects.dicts[`b`].askeri_okul.saglamlik_durumu -= 0.2
				else:
					objects.dicts[`b`].askeri_okul.saglamlik_durumu = 0

				if(objects.dicts[`b`].banka.saglamlik_durumu > 0.1):
					objects.dicts[`b`].banka.saglamlik_durumu -= 0.1
				else:
					objects.dicts[`b`].banka.saglamlik_durumu = 0

			elif(8 <= hasarMiktari):
				if(objects.dicts[`b`].isci_okulu.saglamlik_durumu > 0.3):
					objects.dicts[`b`].isci_okulu.saglamlik_durumu -= 0.3
				else:
					objects.dicts[`b`].isci_okulu.saglamlik_durumu = 0

				if(objects.dicts[`b`].askeri_okul.saglamlik_durumu > 0.3):
					objects.dicts[`b`].askeri_okul.saglamlik_durumu -= 0.3
				else:
					objects.dicts[`b`].askeri_okul.saglamlik_durumu = 0

				if(objects.dicts[`b`].banka.saglamlik_durumu > 0.3):
					objects.dicts[`b`].banka.saglamlik_durumu -= 0.2
				else:
					objects.dicts[`b`].banka.saglamlik_durumu = 0



		if kalsinflag == 1:
			objects.dicts[`c`].yuz_olcumu[2].reverse()

		if tersecevirflag == 1:
			objects.dicts[`b`].yuz_olcumu[2].reverse()

		if savunansagdaflag==1:
			objects.dicts[`b`].yuz_olcumu[2].sort()

		if savunansoldaflag==1:
			objects.dicts[`b`].yuz_olcumu[2].sort()

		


class Grid:	

	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	baslangic_x1 = 0
	baslangic_x2 = 0
	baslangic_y1 = 0
	baslangic_y2 = 0

	def __init__(self):
		self.harita = []
		self.boyut = 0
		self.boy = 1000
		self.boyut = self.boy		
		for i in range(self.boy):
			self.harita.append([])	
			for j in range(self.boy):
				self.harita[i].append('~')

		for i in range(1,257):
			for k in range(objects.dicts[`i`].yuz_olcumu[0][0], objects.dicts[`i`].yuz_olcumu[1][0]):
				for m in range(objects.dicts[`i`].yuz_olcumu[0][1], objects.dicts[`i`].yuz_olcumu[1][1]):
					self.harita[k][m] = renkler[`i`]
					objects.dicts[`i`].yuz_olcumu[2].append([k,m])   

	

	def GridUpdate(self,a,b):
		for k in objects.dicts[`b`].yuz_olcumu[2]:
			self.harita[k[0]][k[1]] = renkler[`b`]   
		
		for k in objects.dicts[`a`].yuz_olcumu[2]:
			self.harita[k[0]][k[1]] = renkler[`a`]   


	def GridUpdate2(self):
		for i in range(1,257):
			for k in objects.dicts[`i`].yuz_olcumu[2]:
				self.harita[k[0]][k[1]] = renkler[`i`]	


	def showMap(self):
		r = ""
		for k in range(self.y1,self.y2):
			for m in range(self.x1,self.x2):
				r = r + " " + self.harita[k][m]
			r = r + "\n"
		return r
		
	
	

def default_seyler():
	for i in range(1,257):
		objects.dicts[`i`].coin += int(objects.dicts[`i`].banka.uretilen_coin * objects.dicts[`i`].banka.sayi * objects.dicts[`i`].banka.saglamlik_durumu)  
		objects.dicts[`i`].tahta_miktari += objects.dicts[`i`].tahta_ureten_isciler
		objects.dicts[`i`].metal_miktari += objects.dicts[`i`].metal_ureten_isciler/2
		if i != kul.empire_no:
			rand1 = choice([1,2])
			if rand1 == 1:
				if objects.dicts[`i`].coin > 50:
					objects.dicts[`i`].saldiri_askerleri.sayi += 1
					objects.dicts[`i`].coin -= 50
			else:
				if objects.dicts[`i`].coin > 50:
					objects.dicts[`i`].savunma_askerleri.sayi += 1
					objects.dicts[`i`].coin -= 50

			
			rand2 = choice([1,2,3,4])
			if rand2 == 1:
				if objects.dicts[`i`].coin > 10000:
					objects.dicts[`i`].saldiri_askerleri.saldiri_gucu += 1
					objects.dicts[`i`].coin -= 10000

			elif rand2 == 2:
				if objects.dicts[`i`].coin > 10000:
					objects.dicts[`i`].savunma_askerleri.savunma_gucu += 1
					objects.dicts[`i`].coin -= 10000

			if rand2 == 3:
				if objects.dicts[`i`].coin > 10000:
					objects.dicts[`i`].sinir_savunmasi += objects.dicts[`i`].sinir_savunmasi/2
					objects.dicts[`i`].coin -= 10000

			if rand2 == 4:
				if objects.dicts[`i`].coin > 6000:
					objects.dicts[`i`].banka.uretilen_coin += 25
					objects.dicts[`i`].coin -= 6000

def save():
	
	global kul
	if(oyunTipi == 1):
		f = open("db.txt", "r+")
	else:
		f = open("mpdb.txt", "r+")

	f.truncate()
	f.write(str(kul.empire_no) + "\n")
	#f.write(str(harita.x1) + "\n" + str(harita.x2) + "\n" + str(harita.y1) + "\n" + str(harita.y2) + "\n")
	f.write(str(harita.baslangic_x1) + "\n" + str(harita.baslangic_x2) + "\n" + str(harita.baslangic_y1) + "\n" + str(harita.baslangic_y2) + "\n")

	for k in secenekler:
		f.write(str(k) + " ")
	f.write("\n")

	for k in secenekler2:			
		f.write(str(k) + " ")
	f.write("\n")

	for i in range(1,257):
		f.write( str(objects.dicts[`i`].anaKuleSavunmasi)+ "\n" + str(objects.dicts[`i`].ad) + "\n") 

		for k in objects.dicts[`i`].yuz_olcumu[2]:
			f.write(str(k[0]) + " " + str(k[1]) + " ")
		f.write("\n")
		f.write(str(objects.dicts[`i`].sinir_savunmasi) + "\n")
		f.write(str(objects.dicts[`i`].coin) + "\n" + str(objects.dicts[`i`].tahta_miktari) + "\n" + str(objects.dicts[`i`].metal_miktari) + "\n" + str(objects.dicts[`i`].savunma_askerleri.sayi) + "\n") 
		f.write(str(objects.dicts[`i`].savunma_askerleri.saldiri_gucu) + "\n" + str(objects.dicts[`i`].savunma_askerleri.savunma_gucu) + "\n" + str(objects.dicts[`i`].saldiri_askerleri.sayi) + "\n")
		f.write(str(objects.dicts[`i`].saldiri_askerleri.saldiri_gucu) + "\n" + str(objects.dicts[`i`].savunma_askerleri.savunma_gucu) + "\n" + str(objects.dicts[`i`].askeri_okul.sayi) + "\n")
		f.write(str(objects.dicts[`i`].askeri_okul.hiz) + "\n" + str(objects.dicts[`i`].askeri_okul.saglamlik_durumu) + "\n" + str(objects.dicts[`i`].askeri_okul.uretilen_coin) + "\n")
		f.write(str(objects.dicts[`i`].askeri_okul.tedavi_iyilestirme_hizi) + "\n" + str(objects.dicts[`i`].askeri_okul.sinir_savunmasi) + "\n" + str(objects.dicts[`i`].isci_okulu.sayi) + "\n")
		f.write(str(objects.dicts[`i`].isci_okulu.hiz) + "\n" + str(objects.dicts[`i`].isci_okulu.saglamlik_durumu) + "\n" + str(objects.dicts[`i`].isci_okulu.uretilen_coin) + "\n" )
		f.write(str(objects.dicts[`i`].isci_okulu.tedavi_iyilestirme_hizi) + "\n" + str(objects.dicts[`i`].isci_okulu.sinir_savunmasi) + "\n" + str(objects.dicts[`i`].hastane.sayi) + "\n")
		f.write(str(objects.dicts[`i`].hastane.hiz) + "\n" + str(objects.dicts[`i`].hastane.saglamlik_durumu) + "\n" + str(objects.dicts[`i`].hastane.uretilen_coin) + "\n")  
		f.write(str(objects.dicts[`i`].hastane.tedavi_iyilestirme_hizi) + "\n" + str(objects.dicts[`i`].hastane.sinir_savunmasi) + "\n" + str(objects.dicts[`i`].banka.sayi) + "\n")
		f.write(str(objects.dicts[`i`].banka.hiz) + "\n" + str(objects.dicts[`i`].banka.saglamlik_durumu) + "\n" + str(objects.dicts[`i`].banka.uretilen_coin) + "\n" + str(objects.dicts[`i`].banka.tedavi_iyilestirme_hizi) + "\n")
		f.write(str(objects.dicts[`i`].banka.sinir_savunmasi) + "\n" + str(objects.dicts[`i`].tahta_ureten_isciler) + "\n" + str(objects.dicts[`i`].metal_ureten_isciler) + "\n")
		f.write(str(objects.dicts[`i`].hava_saldirisi) + "\n" + str(objects.dicts[`i`].deniz_saldirisi) + "\n")

	f.close()


def load():

	global kul
	if(oyunTipi == 1):
		f = open("db.txt", "r+")
	else:
		f = open("mpdb.txt", "r+")

	kul.empire_no = (int(f.readline()))

	harita.baslangic_x1 = (int(f.readline())) 
	harita.baslangic_x2 = (int(f.readline()))
	harita.baslangic_y1 = (int(f.readline()))
	harita.baslangic_y2 = (int(f.readline()))

	sec = f.readline().rstrip("\n").split(" ")
	del sec [-1]
	del secenekler [:]		
	for m in range(1, len(sec)):
		secenekler.append(int(sec[m]))
	

	sec2 = f.readline().rstrip("\n").split(" ")
	del sec2 [-1]
	del secenekler2 [:]		
	for m in range(1,len(sec2)):
		secenekler2.append(int(sec2[m]))

	for i in range(1,257):
		objects.dicts[`i`].anaKuleSavunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].ad = f.readline().rstrip("\n")
		yeniYuzOlcumu = f.readline().rstrip("\n").split(" ")
		k = 0

		del objects.dicts[`i`].yuz_olcumu[2] [:]

		for m in range(len(yeniYuzOlcumu)):
			objects.dicts[`i`].yuz_olcumu[2].append([])
			objects.dicts[`i`].yuz_olcumu[2][m].append(int(yeniYuzOlcumu[k]))
			k += 1
			objects.dicts[`i`].yuz_olcumu[2][m].append(int(yeniYuzOlcumu[k]))
			k +=1

			if(m == (len(yeniYuzOlcumu)/2 - 1)):
				break

		objects.dicts[`i`].sinir_savunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].coin = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].tahta_miktari = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].metal_miktari = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].savunma_askerleri.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].savunma_askerleri.saldiri_gucu = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].savunma_askerleri.savunma_gucu = int(f.readline().rstrip("\n"))	
		objects.dicts[`i`].saldiri_askerleri.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].saldiri_askerleri.saldiri_gucu = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].saldiri_askerleri.savunmasa_gucu = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.hiz = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.saglamlik_durumu = float(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.uretilen_coin = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.tedavi_iyilestirme_hizi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].askeri_okul.sinir_savunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.hiz = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.saglamlik_durumu = float(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.uretilen_coin = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.tedavi_iyilestirme_hizi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].isci_okulu.sinir_savunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.hiz = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.saglamlik_durumu = float(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.uretilen_coin = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.tedavi_iyilestirme_hizi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hastane.sinir_savunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].banka.sayi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].banka.hiz = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].banka.saglamlik_durumu = float(f.readline().rstrip("\n"))
		objects.dicts[`i`].banka.uretilen_coin = int(f.readline().rstrip("\n"))	
		objects.dicts[`i`].banka.tedavi_iyilestirme_hizi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].banka.sinir_savunmasi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].tahta_ureten_isciler = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].metal_ureten_isciler = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].hava_saldirisi = int(f.readline().rstrip("\n"))
		objects.dicts[`i`].deniz_saldirisi = int(f.readline().rstrip("\n"))		


class myClassA(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.start()
        def run(self):
        	while True:
        	    	a=raw_input()

			if(a=="Attack"):
				print "Enter the id of the empire that you want to attack:"
				b=input()
				if b in secenekler:
					kul.saldir(b)
				else:
					print "Invalid input"

			elif(a=="Improve Attack"):
				kul.saldiri_asker_gucu_arttir()

			elif(a=="Improve Defense"):
				kul.savunma_asker_gucu_arttir()

			elif(a=="Warcraft"):
				kul.hava_saldirisi()

			elif(a=="Air"):
				b = input("Enter enemy empire: ")
				if b in secenekler:
					kul.hava_saldirisi_yap(b)
				else:
					print "Invalid input"

			elif(a=="Sea"):
				kul.deniz_saldirisi()
				
			elif(a=="AS"):
				b = input("Enter soldier number: ")
				kul.saldiri_askeri_sayisi_arttir(b)

			elif(a=="DS"):
				b = input("Enter soldier number: ")
				kul.savunma_askeri_sayisi_arttir(b)

			elif(a=="Worker"):
				kul.isci_sayisi_arttir()

			elif(a=="Bank"):
				kul.bankayi_gelistir()

			elif(a=="Defense"):
				kul.savunmayi_arttir()

			elif(a=="Repair"):
				print "Military= ", objects.dicts[`kul.empire_no`].askeri_okul.saglamlik_durumu
				print "Worker= ", objects.dicts[`kul.empire_no`].isci_okulu.saglamlik_durumu
				print "Bank= ", objects.dicts[`kul.empire_no`].banka.saglamlik_durumu
				print("0-Exit\n1-Bank\n2-Military\n3-Worker")
				b=input("Choose number: ")
				if(b==0):
					pass
				elif(b==1):
					kul.yapiyi_onar(3)
				elif(b==2):
					kul.yapiyi_onar(1)
				elif(b==3):
					kul.yapiyi_onar(2)
				else:
					print "Invalid input"

			elif(a=="Save"):
				save()
		
			elif(a=="Save and exit"):
				save()
				sys.exit(0)

			elif(a=="Mu"):
				harita.y1 -= 20
				harita.y2 -= 20
		
			elif(a=="Ml"):
				harita.x1 -= 20
				harita.x2 -= 20  

			elif(a=="Mr"):
				harita.x1 += 20
				harita.x2 += 20

			elif(a=="Md"):
				harita.y1 += 20
				harita.y2 += 20
					
			elif(a=="C"):
				harita.x1 = harita.baslangic_x1			
				harita.x2 = harita.baslangic_x2
				harita.y1 = harita.baslangic_y1			
				harita.y2 = harita.baslangic_y2

			else:
				print("Invalid Input")

			os.system('clear')
			print (harita.showMap()) 
			print(objects.dicts[`kul.empire_no`].ad)
			print "Coin:",objects.dicts[`kul.empire_no`].coin
			print "Empire Defense:",objects.dicts[`kul.empire_no`].sinir_savunmasi
			print "Wood:",objects.dicts[`kul.empire_no`].tahta_miktari,"Iron:",objects.dicts[`kul.empire_no`].metal_miktari
			print "Attacking Soldier: ", objects.dicts[`kul.empire_no`].saldiri_askerleri.sayi,"(",objects.dicts[`kul.empire_no`].saldiri_askerleri.saldiri_gucu, ") - Defensive Soldier: ", objects.dicts[`kul.empire_no`].savunma_askerleri.sayi, "(", objects.dicts[`kul.empire_no`].savunma_askerleri.savunma_gucu, ")" 

class myClassB(Thread):

	def __init__(self):
	        Thread.__init__(self)
	        self.daemon = True
	        self.start()

	def run(self):
	        while True:
			default_seyler()
			time.sleep(2)

class myClassC(Thread):

	def __init__(self):
	        Thread.__init__(self)
	        self.daemon = True
	        self.start()

	def run(self):
	        while True:
			a=choice(secenekler)
			son = []
			yeni = [a-1,a+1,a-16,a+16]
			for i in yeni:
				if i in range(1,257):
					son.append(i)
			b=choice(son)

			if(a!=b):
				random_saldir(a,b)
			time.sleep(0.5)	
			
			for i in range(1,257):
				if len(objects.dicts[`i`].yuz_olcumu[2]) == 0:
					if i in secenekler:
						secenekler.remove(i) 
					if i in secenekler2:
						secenekler2.remove(i)

			if(len(objects.dicts[`kul.empire_no`].yuz_olcumu[2]) == 0):
				print "Game Over!"
			if(len(secenekler2) == 1):
				print "Congratz!"
			


kul = User()
harita = Grid()	

print("Menu")
print("\n")
print("1- Single Player")
print("2- Multiplayer")
print("About\n")

enter = input()

if(enter == 1): 		#SINGLEPLAYER OPTION
	
	oyunTipi = 1
	flag = 1

	while flag:
		print("Single Player: ")
		print("  1- New Game:")
		print("  2- Load Game:\n")
		
		secim = input()
		
		if(secim == 1):		#NEW GAME OPTION
			flag = 0

			secimFlag = 1

			while secimFlag:
				print('Welcome!')
				print('Choose Your Empire:')
				print('Pick a number between 1 and 256:\n')	

				empire_number = input()
				if(empire_number < 257):
					secimFlag = 0
					kul.empire_no = empire_number
					harita.y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
					harita.y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
					harita.x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
					harita.x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
					harita.baslangic_y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
					harita.baslangic_y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
					harita.baslangic_x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
					harita.baslangic_x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
					secenekler.remove(empire_number)
				else:
					print "Invalid input"

	
		elif(secim == 2):		#LOAD GAME OPTION

			if(os.stat("db.txt").st_size == 0):
				print "Not Found"
			else:
				flag = 0
				load()
				harita.y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
				harita.y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
				harita.x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
				harita.x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
				harita.baslangic_y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
				harita.baslangic_y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
				harita.baslangic_x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
				harita.baslangic_x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
				harita.GridUpdate2()

		else:
			print "Invalid input"

elif(enter==2):			#MULTIPLAYER OPTION
	
	oyunTipi = 2
	flag = 1


	while flag:
		print("Multiplayer: ")
		print("  1- Create Player:")
		print("  2- Join Game:\n")

		secim = input()
		
		if(secim == 1):		#CREATING NEW PLAYER
			flag = 0
			usernameFlag = 1

			while usernameFlag:
				print('Welcome!')
				print('Choose Your Username:\n')
				
				if(os.stat("usernames.txt").st_size != 0):
					f = open("usernames.txt", "r+")
					liste = ''.join(f.readlines())
					objects.usernames = pickle.loads(liste)
					f.close()

		
				username = raw_input()

				if username in objects.usernames:
					print "Unavailable"

				else:
					usernameFlag = 0
					objects.usernames.append(username)

					f = open("usernames.txt", "r+")
					f.truncate()
					f.write(pickle.dumps(objects.usernames))
					f.close()

					idFlag = 1
					while idFlag:
						if(os.stat("users.txt").st_size != 0):
							f = open("users.txt", "r+")
							geciciListe = ''.join(f.readlines())
							objects.users = pickle.loads(geciciListe)
							f.close()

						if(os.stat("id.txt").st_size != 0):
							f = open("id.txt", "r+")
							geciciListe = ''.join(f.readlines())
							objects.mp_empire_id = pickle.loads(geciciListe)
							f.close()

						mp_empire_id = input("Choose your empire:\nPick a number between 1 and 256:\n")

						if mp_empire_id not in objects.mp_empire_id:
							print "It is already taken"

						else:
							idFlag = 0
							objects.users[str(username)] = mp_empire_id
							
							f = open("users.txt", "r+")
							f.truncate()
							f.write(pickle.dumps(objects.users))
							f.close()

							objects.mp_empire_id.remove(mp_empire_id)
							f = open("id.txt", "r+")
							f.truncate()
							f.write(pickle.dumps(objects.mp_empire_id))
							f.close()

							secenekler.remove(mp_empire_id)
							kul.empire_no = mp_empire_id
							harita.y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
							harita.y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
							harita.x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
							harita.x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
							harita.baslangic_y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
							harita.baslangic_y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
							harita.baslangic_x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
							harita.baslangic_x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
				cl.client()

		elif(secim == 2):		#JOIN GAME
			if(os.stat("mpdb.txt").st_size == 0):
				print "Not Found"
			else:
				flag = 0
				usernameFlag = 1

				while usernameFlag:
					print('Welcome!')
					print('Enter Your Username:\n')
					
					if(os.stat("usernames.txt").st_size != 0):
						f = open("usernames.txt", "r+")
						liste = ''.join(f.readlines())
						objects.usernames = pickle.loads(liste)
						f.close()
			
					username = raw_input()

					if username not in objects.usernames:
						print "Wrong Username"

					else:
						usernameFlag = 0
						if(os.stat("users.txt").st_size != 0):
									f = open("users.txt", "r+")
									geciciListe = ''.join(f.readlines())
									objects.users = pickle.loads(geciciListe)
									f.close()

						load()
						kul.empire_no = objects.users[username]
						harita.y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
						harita.y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
						harita.x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
						harita.x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
						harita.baslangic_y1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][0] - 20
						harita.baslangic_y2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][0] + 20
						harita.baslangic_x1 = objects.dicts[`kul.empire_no`].yuz_olcumu[0][1] - 20
						harita.baslangic_x2 = objects.dicts[`kul.empire_no`].yuz_olcumu[1][1] + 20
						harita.showMap()
				cl.client()

		else:
			"Invalid Input"

else:
	print "Invalid input"
	sys.exit()

print(harita.showMap())	
print(objects.dicts[`kul.empire_no`].ad)
print "Coin:",objects.dicts[`kul.empire_no`].coin
print "Empire Defense:",objects.dicts[`kul.empire_no`].sinir_savunmasi
print "Wood:",objects.dicts[`kul.empire_no`].tahta_miktari,"Iron:",objects.dicts[`kul.empire_no`].metal_miktari
print "Attacking Soldier: ", objects.dicts[`kul.empire_no`].saldiri_askerleri.sayi,"(",objects.dicts[`kul.empire_no`].saldiri_askerleri.saldiri_gucu, ") - Defensive Soldier: ", objects.dicts[`kul.empire_no`].savunma_askerleri.sayi, "(", objects.dicts[`kul.empire_no`].savunma_askerleri.savunma_gucu, ")" 


myClassA()
myClassB()
myClassC()

while len(objects.dicts[`kul.empire_no`].yuz_olcumu[2]):
    pass

print "Game Over!"
	
	

