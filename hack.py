import requests
from requests.structures import CaseInsensitiveDict


headers = CaseInsensitiveDict()
headers = {"Cookie":"WC=16369725-43237-27PkMDIRRBweCvy3"}
res = str(requests.get('http://www.wechall.net/challenge/training/programming1/index.php?action=request',
   headers=headers).text)
print(res)

svar = 'http://www.wechall.net/challenge/training/programming1/index.php?answer='+res
print(svar)
requests.post(svar)




