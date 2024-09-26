from bs4 import BeautifulSoup as bs
import requests



def GetHtml(userID):
    url = f'https://www.acmicpc.net/user/{userID}'
    res = requests.get(url,headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}) #User-Agent 바꿔서 요청거절못하게
    html = res.text

    soup = bs(html,'html.parser')

    elements = soup.find_all('rect')
    print(elements)


GetHtml('lpchaze')