import requests

proxy = ['proxy', 'vmess', 'ss', 'trojan', 'clash']
for i in proxy:
    try:
        with open('{}.txt'.format(i), 'w', encoding='utf-8') as f:
            if i != 'clash':
                r = requests.get("https://bitbucket.org/huwo1/proxy_nodes/raw/f31ca9ec67b84071515729ff45b011b6b09c10f2/{}.md".format(i))
            else:
                r = requests.get("https://bitbucket.org/huwo1/proxy_nodes/raw/f31ca9ec67b84071515729ff45b011b6b09c10f2/{}.yaml".format(i))
                r.encoding = r.apparent_encoding
            data = r.text
            f.write(data)
            f.close()
    except Exception as e:
        print(e)

