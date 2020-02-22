import requests

url = 'https://swift.dkrz.de/v1/dkrz_ffd3ca9004324ad28243244b834f92b1/notebooks/data/AFR-22.nc?temp_url_sig=0f1416dc9891ca4cf97a076aa0b0629b8ad8945c&temp_url_expires=2020-02-29T13:49:21Z'

myfile = requests.get(url)
open('AFR-22.nc', 'wb').write(myfile.content)
