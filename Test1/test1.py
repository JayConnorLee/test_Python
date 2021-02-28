import json
import requests as rq

from bs4 import BeautifulSoup


def P_Comment(x):
    print("==============================================================================")
    print(x)
    print("==============================================================================")

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


P_Comment("Json Repo Starts")

sJson = ['foo', {'bar': ('baz', None, 1.0, 2)}]
json.dumps(sJson)

c = {"c": 0, "b": 0, "a": 0}
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps(c, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
sResult = io.getvalue()
print(sResult)

P_Comment("Complex")

sResult = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
print(sResult)
#json.loads()




P_Comment("Beautiful Soup")


html_doc = 'http://www.naver.com'
page = rq.get(html_doc)


soup = BeautifulSoup(page.content, 'html.parser')

#sContent = soup.prettify(soup)
soup.prettify()


#For Item in list(soup.children):
#    type(item)

for it in soup.children:
    P_Comment(type(it))
    print(it)


print(soup)
print('end')

