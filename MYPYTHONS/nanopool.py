import requests
address = 't1UtZktQLxzxyonziphEsrXzD6xdLheevQH'
content = requests.get('https://api.nanopool.org/v1/eth/balance/0x3ec503237e873a6221dc01d9cd49c8ce46c2ac12')
averageHash = requests.get('https://api.nanopool.org/v1/eth/avghashrate/0x3ec503237e873a6221dc01d9cd49c8ce46c2ac12')
data = content.json()
hashw = averageHash.json()
print(data, hashw)
