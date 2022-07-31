import requests
from lxml import html


proxy = ['proxy', 'vmess', 'ss', 'trojan']
for i in proxy:
    try:
        with open('{}.txt'.format(i), 'w', encoding='utf-8') as f:
            r = requests.get("https://bitbucket.org/huwo1/proxy_nodes/raw/f31ca9ec67b84071515729ff45b011b6b09c10f2/{}.md".format(i))
            data = r.text
            print(data)
            f.write(data)
            f.close()
    except Exception as e:
        print(e)
