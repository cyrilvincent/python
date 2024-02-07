import requests
import numpy

print(numpy.__version__)
print(requests.__version__)

x = requests.get('https://www.cea.fr')
print(x.text)