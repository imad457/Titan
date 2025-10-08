import requests
from rich import print
def status_code ():
    url= input('ENTRE UR URL : ')
    try:
            response= requests.get(url)
            if response.status_code == 200 :
                print(f'[bold green]the website is up :[/] {url} | {response.status_code}')
            else:
                print(f"[bold red]the websits is not working :[/] {url}")
    except requests.exceptions.RequestException :
            print(f"[bold red] IS DOWN [/] {url}")


    