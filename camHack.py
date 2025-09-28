import requests, re, colorama, random
from requests.structures import CaseInsensitiveDict
import os


colorama.init()





# Colors
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'




# Clen the terminal, cmd
def clean():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    else:
       _ =  os.system('clear')






url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers[
    "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']







def banner():
    camhack =  f"""{Re}
    
{Cy}   ______    ______   __       __          __    __   ______    ______   __    __ 
{Cy} /      \  /      \ /  \     /  |        /  |  /  | /      \  /      \ /  |  /  |
{Re}/$$$$$$  |/$$$$$$  |$$  \   /$$ |        $$ |  $$ |/$$$$$$  |/$$$$$$  |$$ | /$$/ 
{Re}$$ |  $$/ $$ |__$$ |$$$  \ /$$$ | ______ $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/  
{Re}$$ |      $$    $$ |$$$$  /$$$$ |/      |$$    $$ |$$    $$ |$$ |      $$  $$<   
{Re}$$ |   __ $$$$$$$$ |$$ $$ $$/$$ |$$$$$$/ $$$$$$$$ |$$$$$$$$ |$$ |   __ $$$$$  \  
{Gr}$$ \__/  |$$ |  $$ |$$ |$$$/ $$ |        $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \ 
{Gr}$$    $$/ $$ |  $$ |$$ | $/  $$ |        $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |
{Gr} $$$$$$/  $$/   $$/ $$/      $$/         $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ 
 
 
           {Wh}|----------------------------------------|
           {Wh}| {Gr}CAM-HACK                               {Wh}|
           {Wh}| {Gr}@CODE BY GHERIS                        {Wh}|
           {Wh}|----------------------------------------| 
                                                    
    """

    print(camhack)


def banner2():
    camhack1 = f"""{Wh}

{Cy}     .'``'.      ...           {Wh}|----------------------------------------|
{Cy}     :o  o `....'`  ;          {Wh}| {Gr}CAM-HACK                               {Wh}|
{Cy}     `. O         :'           {Wh}|       {Gr}@CODE BY GHERIS                  {Wh}|
{Mage}       `':          `.         {Wh}|----------------------------------------|
{Mage}         `:.          `.
{Mage}          : `.         `.
{Gr}         `..'`...       `.
{Gr}                 `...     `.
{Gr}                   ``...  `.
{Gr}                          `````.                        
                         
        """

    print(camhack1)



def camapp():
    clean()
    banner()


    columns = 3  # numero di colonne
    count = 0  # contatore per andare a capo

    for key, value in countries.items():
        # stampa senza andare a capo, aggiungendo tabulazione
        print(f'{Gr}({key}) {value["country"]} ({value["count"]})'.ljust(30), end=' ')
        count += 1
        # ogni "columns" elementi vai a capo
        if count % columns == 0:
            print()  # va a capo


    # per stampare eventuali elementi rimanenti
    if count % columns != 0:
        print()



    try:



        country = input(f"""\n{Re}┌─[{Cy}CAM-HACK{Blu}~{Wh}@HOME{Re}]
└──╼{Wh}$ """).lower()
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)

        clean()
        banner2()
        for ip in find_ip:
            print("")
            print(f"""{Re}{ip}""")

        input(f"\n{Blu}Press Enter to continue...")
        clean()
        camapp()




    except Exception as e:
        print(f"Errore: {e}")







if __name__ == '__main__':
    try:
        camapp()
    except KeyboardInterrupt:
        clean()
        exit()

