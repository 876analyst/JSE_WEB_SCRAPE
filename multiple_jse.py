import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


stocklist = []

def getstocks(tag):
	url = f'https://www.jamstockex.com/market-data/instruments/?symbol={tag}'
	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')

	containers = soup.findAll("div",{"class":"col-xs-12 text-center"})

	for container in containers:
		stocks = {
		'tag': tag,
		'instrument': soup.h3.text.strip('\n'),
		'last_traded': containers[0].text.replace("Last Traded Price","").strip('\n'),
		'close_price': containers[1].text.replace("Close Price","").strip('\n'),
		'change': containers[2].text.replace("Change ($)","").strip('\n'),
		'percent_change': containers[3].text.replace("Change (%)","").strip('\n'),
		}
		
		stocklist.append(stocks)
	return


getstocks('138SL')
getstocks('1834')
getstocks('AFS')
getstocks('AMG')
getstocks('BIL')
getstocks('BPOW')
getstocks('BRG')
getstocks('CABROKERS')
getstocks('CAC')
getstocks('CAR')
getstocks('CBNY')
getstocks('CCC')
getstocks('CFF')
getstocks('CPJ')
getstocks('CWJDEFERREDA')
getstocks('DCOVE')
getstocks('DTL')
getstocks('ECL')
getstocks('EFRESH')
getstocks('ELITE')
getstocks('EPLY')
getstocks('EPLY8.25')
getstocks('EPLY8.75')
getstocks('FESCO')
getstocks('FIRSTROCKJMD')
getstocks('FIRSTROCKUSD')
getstocks('FOSRICH')
getstocks('FTNA')
getstocks('GENAC')
getstocks('GHL')
getstocks('GK')
getstocks('GWEST')
getstocks('HONBUN')
getstocks('ICREATE')
getstocks('INDIES')
getstocks('JAMT')
getstocks('JBG')
getstocks('JETCON')
getstocks('JMMBGL')
getstocks('JMMBGL7.00NC')
getstocks('JMMBGL7.25C')
getstocks('JMMBGL7.35')
getstocks('JMMBGL7.50')
getstocks('JP')
getstocks('JSE')
getstocks('KEX')
getstocks('KEY')
getstocks('KLE')
getstocks('KPREIT')
getstocks('KREMI')
getstocks('KW')
getstocks('LAB')
getstocks('LASD')
getstocks('LASF')
getstocks('LASM')
getstocks('LUMBER')
getstocks('MAILPAC')
getstocks('MDS')
getstocks('MEEG')
getstocks('MIL')
getstocks('MJE')
getstocks('MTLJA')
getstocks('MTL')
getstocks('NCBFG')
getstocks('PAL')
getstocks('PJAM')
getstocks('PROVENJA')
getstocks('PROVEN')
getstocks('PTL')
getstocks('PULS')
getstocks('PURITY')
getstocks('QWI')
getstocks('RJR')
getstocks('SALF')
getstocks('SCIJMD')
getstocks('SCIUSD')
getstocks('SELECTF')
getstocks('SELECTMD')
getstocks('SEP')
getstocks('SGJ')
getstocks('SJ')
getstocks('SOS')
getstocks('SSLVC')
getstocks('SVL')
getstocks('TJH')
getstocks('TJHUSD')
getstocks('TROPICAL')
getstocks('VMIL')
getstocks('WIG')
getstocks('WISYNCO')
getstocks('XFUND')



df = pd.DataFrame(stocklist)
df.to_csv('jse_stocks.csv')
print('List_of_Stocks.')




