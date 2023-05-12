import requests
from bs4 import BeautifulSoup as bs

        #����� �������
def vivod(grid1,strokmax):
    print("N |       CNAME      | symbl |       PRICE     | 1hour | 24hrs | 1week | markcap | market cap precise  |")
    for j in range(strokmax):
        print("%2s|  %15s | %6s|  %15s| %6s| %6s| %6s| %8s| %20s|"%(grid1[j][0],grid1[j][1],grid1[j][2],grid1[j][3],grid1[j][4],grid1[j][6],grid1[j][8],grid1[j][10],grid1[j][11],))

def poisk(grid1,strokmax):
    print("choose key: 1 - number, 2 - name, 3 - shortname")
    x=input()
    print("input key:")
    ky=input()
    if(x=="1"):
        for j in range(strokmax):
         if(grid1[j][0]==ky):
            print("N |       CNAME      | symbl |       PRICE     | 1hour | 24hrs | 1week | markcap | market cap precise  |")
            print("%2s|  %15s | %6s|  %15s| %6s| %6s| %6s| %8s| %20s|"%(grid1[j][0],grid1[j][1],grid1[j][2],grid1[j][3],grid1[j][4],grid1[j][6],grid1[j][8],grid1[j][10],grid1[j][11],))
            break
    elif(x=="2"):
        for j in range(strokmax):
         if(grid1[j][1]==ky):
            print("N |       CNAME      | symbl |       PRICE     | 1hour | 24hrs | 1week | markcap | market cap precise  |")
            print("%2s|  %15s | %6s|  %15s| %6s| %6s| %6s| %8s| %20s|"%(grid1[j][0],grid1[j][1],grid1[j][2],grid1[j][3],grid1[j][4],grid1[j][6],grid1[j][8],grid1[j][10],grid1[j][11],))
            break
    elif(x=="3"):
        for j in range(strokmax):
         if(grid1[j][2]==ky):
            print("N |       CNAME      | symbl |       PRICE     | 1hour | 24hrs | 1week | markcap | market cap precise  |")
            print("%2s|  %15s | %6s|  %15s| %6s| %6s| %6s| %8s| %20s|"%(grid1[j][0],grid1[j][1],grid1[j][2],grid1[j][3],grid1[j][4],grid1[j][6],grid1[j][8],grid1[j][10],grid1[j][11],))
            break

        
r= requests.get("https://coinmarketcap.com/") #�������� ������ � ����� � ������ ���������
html = bs(r.content, "html.parser")           #��������� ���������� � ������� BeautifulSoup ��������� html.parser
print("Loading recources from https://coinmarketcap.com/ .....")
curname= html.find("tbody").findAll("p")      #�������� ��� ���������� �, ���������� ����������� �������� ������� �����
print("33% .....")
curprop= html.find("tbody").findAll("span")   #�������� ��� ���������� �������� ����, ���������� ��� �������� �������� ��������
print("67% .....")
stroklen=14   
strokmax=10
k=1
k1=0
grid1 = mas = [[0] * stroklen for i in range(strokmax)] #������� ��������� ������, ����������� ������
#print(curprop)

        #��������� �������:

for j in range(strokmax):
    grid1[j][0]=curname[k1].text
    k1=k1+1
    grid1[j][1]=curname[k1].text
    k1=k1+1
    grid1[j][2]=curname[k1].text   #������ 5,7,9,12,13 �������� ������ �����, � ������� ��� ����������� �� �� ���������, ��� �� ��)
    k1=k1+5
    for i in range(3,stroklen):
        grid1[j][i]=curprop[k].text
        k=k+1

        #������� ����
print("Done")
while(1):
    print('1: Show all currencies')
    print('2: find currency')
    x=input()
    if(x=="1"):
        vivod(grid1,strokmax)
    elif(x=="2"):
        poisk(grid1,strokmax)
    else:
        break