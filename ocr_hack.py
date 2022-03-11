import pytesseract
from PIL import Image
from requests.structures import CaseInsensitiveDict
import urllib3

headers = CaseInsensitiveDict()
headers = {"Cookie":"WC=16370875-43237-VjV82DrCvlC5JKhS"}
url = 'https://www.wechall.net/challenge/can_you_readme/gimme.php'

http = urllib3.PoolManager()
response = http.request('GET', url, headers=headers)
soup = response.data

with open('1.png', 'wb') as f:
    f.write(soup)

text = pytesseract.image_to_string(Image.open("1.png"))
svar = 'https://www.wechall.net/challenge/can_you_readme/index.php?solution='+text

response = http.request('GET', svar, headers=headers)
print(svar)
print(response)