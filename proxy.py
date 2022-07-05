import requests
from lxml import html


proxy = ['proxy', 'vmess', 'ss', 'trojan']
for i in proxy:
    try:
        with open('{}.txt'.format(i), 'w', encoding='utf-8') as f:
            r = requests.get("https://github.com/colatiger/v2ray-nodes/blob/master/{}.md".format(i))
            tree = html.fromstring(r.text)
            data = tree.xpath("//*[@id='readme']/article/p/text()")[0]
            f.write(data)
            f.close()
    except Exception as e:
        print(e)
