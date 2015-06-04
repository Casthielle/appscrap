# encodign: ascii
import httplib, urllib, json, pg, time
from BeautifulSoup import BeautifulSoup

# BBVA Provincial
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

class bbva(object):
	def __init__(self, card, passwd):
		super(bbva, self).__init__()
		self.pgconnect=pg.connect(dbname='scrapy',user='Casthielle',passwd='xd15cw666sc',host='localhost')
		self.card = card
		self.passwd = passwd
		self.codeid="001085413-9"
		codecard = {
			"A1":"106", "A2":"745", "A3":"078", "A4":"584", "A5":"396", "A6":"818", "A7":"537", "A8":"577", "A9":"184", "A10":"380",
			"B1":"555", "B2":"103", "B3":"740", "B4":"924", "B5":"131", "B6":"482", "B7":"028", "B8":"116", "B9":"040", "B10":"282",
			"C1":"434", "C2":"608", "C3":"027", "C4":"452", "C5":"194", "C6":"085", "C7":"633", "C8":"058", "C9":"427", "C10":"897",
			"D1":"126", "D2":"477", "D3":"292", "D4":"583", "D5":"052", "D6":"275", "D7":"951", "D8":"162", "D9":"162", "D10":"709",
			"E1":"917", "E2":"549", "E3":"889", "E4":"154", "E5":"316", "E6":"903", "E7":"874", "E8":"892", "E9":"136", "E10":"587",
			"F1":"997", "F2":"146", "F3":"524", "F4":"056", "F5":"402", "F6":"290", "F7":"848", "F8":"690", "F9":"133", "F10":"522",
			"G1":"149", "G2":"089", "G3":"109", "G4":"390", "G5":"546", "G6":"016", "G7":"669", "G8":"509", "G9":"812", "G10":"419",
			"H1":"974", "H2":"639", "H3":"670", "H4":"119", "H5":"646", "H6":"272", "H7":"565", "H8":"489", "H9":"207", "H10":"049"
		}

		self.headers = {"Cookie":"COOKIE-BANCA_MOVIL=R420047659; path=/","Content-type":"application/x-www-form-urlencoded","Host":"bancamovil.provincial.com","Connection":"Keep-Alive","User-Agent":"Apache-HttpClient/UNAVAILABLE (java 1.4)"}
		self.connect = httplib.HTTPSConnection("bancamovil.provincial.com")
		params = urllib.urlencode({'a':'iniciarSesion','rq':self.card+';'+self.passwd+';Android/ ZTE V815W/ 4.4.2','v':'0121','nc':'09627087'})
		self.connect.request("POST", "/logeo", params, self.headers)
		response = self.connect.getresponse()
		status = str(response.status)

		if status=="200":
			source	= response.read()
			divider = source.split("\n")
			code	= divider[7]
			self.hashstr = divider[5]
			self.hashnum = divider[4]
			value	= codecard[code]
			params = urllib.urlencode({'a':'validarCoordenada','rq':self.card+';'+self.codeid+';'+code+';'+value+';'+self.hashstr+';Android/ ZTE V815W/ 4.4.2','v':'0121','nc':'09627087'})
			self.connect.request("POST", "/logeo", params, self.headers)
			response = self.connect.getresponse()
			status = str(response.status)
			if status=="200":
				source = response.read()
				divider = source.split("\n")
				result = divider[1]


	def balance(self):
		params = urllib.urlencode({'a':'consultarDetallada','rq':self.hashnum+';'+self.card+';09627087;Android/ ZTE V815W/ 4.4.2','v':'0121','nc':'09627087'})
		self.connect.request("POST", "/PosicionGlobal", params, self.headers)
		response = self.connect.getresponse()
		status = str(response.status)
		if status=="200":
			source = response.read()
			divider = source.split("\n")
			self.user = divider[3].split(" ")
			self.user = self.user[0]+" "+self.user[1]+" "+self.user[2]+" "+self.user[3]
			self.date = divider[4]
			self.money = divider[5]
			self.money = self.money.split(" ")[1]
			self.money = self.money.replace(".", "").replace(",", ".")
		print "\033[34m "+"Usuario:".ljust(10," ")+self.user.title()+"\033[0m"
		print "\033[92m "+"Saldo:".ljust(10," ")+"Bs. "+self.money+"\033[0m\n"
		code="UPDATE account SET balance='"+self.money+"' WHERE owner='"+self.user.title()+"';"
		execute=self.pgconnect.query(code)


	def transactions(self):
		params = urllib.urlencode({'a':'obtenerCuentas','rq':self.hashnum+';'+self.card+';09627087;Android/ ZTE V815W/ 4.4.2','v':'0121','nc':'09627087'})
		self.connect.request("POST", "/consultaGlobal", params, self.headers)
		response = self.connect.getresponse()
		status = str(response.status)
		if status=="200":
			source = response.read()
			divider = source.split("\n")
			divider = divider[2].split(";")
			self.account=divider[4]
			params = urllib.urlencode({'a':'consultarMovimientos','rq':self.hashnum+';'+self.card+';'+self.account+';Android/ ZTE V815W/ 4.4.2','v':'0121','nc':'09627087'})
			self.connect.request("POST", "/Cuentas", params, self.headers)
			response = self.connect.getresponse()
			status = str(response.status)
			if status=="200":
				source = response.read()
				divider = source.split(self.account)
				divider = divider[1].split("\n")
				print "\033[90m------+------------+------------------------------------------+------------+--------------\033[0m"
				print "\033[37m  ID  \033[90m|\033[37m "+"FECHA".ljust(10," ")+" \033[90m|\033[37m "+"CONCEPTO".ljust(40," ")+" \033[90m|\033[37m "+"MONTO".rjust(10," ")+" \033[90m|\033[37m      SALDO\033[0m"
				print "\033[90m------+------------+------------------------------------------+------------+--------------\033[0m"
				for i in divider:
					if i!="":
						x=i.split(";")
						rid=x[5]
						concept=x[0]
						date=x[1]
						date=date.split("-")
						date=date[0]+"/"+date[1]+"/"+date[2]
						amount=x[3]
						amount=amount.replace(".","")
						amount=amount.replace(",",".")
						aamount=x[2]
						if amount[0]=="-":
							print "\033[90m  "+rid+" \033[30m|\033[90m "+date+" \033[30m|\033[90m "+concept.title().ljust(40," ")+" \033[30m|\033[31m "+amount.rjust(10," ")+" \033[30m|\033[32m "+aamount.rjust(10," ")+"\033[0m"
							statuswhat="true"
						else:
							print "\033[90m  "+rid+" \033[30m|\033[90m "+date+" \033[30m|\033[90m "+concept.title().ljust(40," ")+" \033[30m|\033[92m "+amount.rjust(10," ")+" \033[30m|\033[32m "+aamount.rjust(10," ")+"\033[0m"
							if concept.split(" ")[0]=="TPBW" or concept.split(" ")[0]=="TR/OB" or concept.split(" ")[0]=="TR/REC":
								statuswhat="false"
							else:
								statuswhat="true"
						execute=self.pgconnect.query("SELECT *FROM transactions WHERE id='"+rid+"'")
						rows=execute.ntuples()
						if rows==0:
							code="INSERT INTO transactions(id,account_id,date,concept,amount,statuswhat) VALUES('"+rid+"',(SELECT id FROM account WHERE owner='"+self.user.title()+"'), '"+date+"','"+concept.title()+"','"+str(amount)+"','"+statuswhat+"')"
							execute=self.pgconnect.query(code)
				print "\033[90m------+------------+------------------------------------------+------------+--------------\033[0m\n"


	def close(self):
		self.connect.close()


# Banco Mercantil
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

class mercantil(object):
	def __init__(self, card, passwd):
		super(mercantil, self).__init__()
		self.card = card
		self.passwd = passwd
		self.pgconnect=pg.connect(dbname='scrapy',user='Casthielle',passwd='xd15cw666sc',host='localhost')
		self.headers = {"Content-type":"application/json","Host":"movilapi.bancomercantil.com","Connection":"Keep-Alive","Expect":"100-continue"}
		self.connect = httplib.HTTPSConnection("movilapi.bancomercantil.com")
		params = {
			"rsa_version":"20111102152226",
			"app":{
				"platform":"android-phone",
				"version":"20140908"
				},
			"mobile_stats":{
				"os":"Android",
				"brand":"ZTE",
				"lon":-63.25611833333334,
				"model":"ZTE V815W",
				"lat":10.645258333333334,
				"version":"4.4.2"
				},
			"usr_stats":{
				"phone_num":"04262022461",
				"email":"casthielle@gmail.com"
				},
			"maps_version":"0",
			"dcn":self.card,
			"pass":self.passwd
			}
		self.connect.request("POST", "/MercantilBancoRest/resources/login", json.dumps(params), self.headers)
		response = self.connect.getresponse()
		status = str(response.status)
		if status=="200":
			source	= response.read()
			data=json.loads(source)
			self.cid = response.getheader('cookieid')
			self.user = data['fname']
			self.money = data['acts'][0]['balance']
			self.id = data['acts'][0]['id_e']
			print "\033[31m "+"Usuario:".ljust(10," ")+self.user.title()+"\033[0m"
			print "\033[92m "+"Saldo:".ljust(10," ")+"Bs. "+self.money+"\033[0m\n"
			code="UPDATE account SET balance='"+self.money+"' WHERE owner='"+self.user.title()+"';";
			execute=self.pgconnect.query(code)


	def transactions(self):
		params = {"platform":"android-phone","cid":self.cid,"id_e":self.id}
		self.connect.request("POST", "/MercantilBancoRest/resources/details", json.dumps(params), self.headers)
		response = self.connect.getresponse()
		status = str(response.status)
		if status=="200":
			source = response.read()
			data=json.loads(source)
			movements=data['movements']
			print "\033[90m-------------+------------------------------------------+-------------\033[0m"
			print "\033[37m  "+"FECHA".ljust(10," ")+" \033[90m|\033[37m "+"CONCEPTO".ljust(40," ")+" \033[90m|\033[37m "+"MONTO".rjust(10," ")+"\033[0m"
			print "\033[90m-------------+------------------------------------------+-------------\033[0m"
			for i in movements:
				concept=i['desc']
				date=i['fullDate']
				amount=i['amount']
				if amount[0]=="-":
					print "\033[90m  "+date+" \033[30m|\033[90m "+concept.title().ljust(40," ")+" \033[30m|\033[31m "+amount.rjust(10," ")+" \033[0m"
					statuswhat="true"
				else:
					print "\033[90m  "+date+" \033[30m|\033[90m "+concept.title().ljust(40," ")+" \033[30m|\033[92m "+amount.rjust(10," ")+" \033[0m"
					statuswhat="false"
				code="INSERT INTO transactions(id,account_id,date,concept,amount,statuswhat) VALUES((SELECT COUNT(*)+1 FROM transactions),(SELECT id FROM account WHERE owner='"+self.user.title()+"'), '"+date+"','"+concept.title()+"','"+str(amount)+"','"+statuswhat+"')"
				execute=self.pgconnect.query(code)
			print "\033[90m-------------+------------------------------------------+-------------\033[0m\n"


	def close(self):
		params = {
			"cid":self.cid
			}
		self.connect.request("POST", "/MercantilBancoRest/resources/logout", json.dumps(params), self.headers)
		response = self.connect.getresponse()
		status = str(response.status)
		if status=="200":
			source	= response.read()
			data=json.loads(source)
			error=data['status']['code']


















