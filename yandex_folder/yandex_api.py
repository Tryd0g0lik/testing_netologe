import requests

import json
import urllib.parse as parse
from yand_token import token_key


path = 'disk:/foo' # путь к корневой папке
token = "%s" % (token_key())  # response_type =
header = {
  'Authorization': 'OAuth %s' %(token_key()),
  'Content-Type': 'application/json'
}
folder = "подпись_в_цифре"

def webcoding(folder): #web-encofing
  web_coding_folder = parse.urlencode({'web-folder' : folder}, encoding="utf-8")
  return web_coding_folder

def yandex_requet_get_disk(folder, token, header): # check the yandex-disk on the response code-200
  url = 'https://cloud-api.yandex.net/v1/disk/resources'

  param = {'path' : '/%s' %(folder)}

  response = requests.get(url, params=param, headers=header)
  return response

# f = yandex_requet_get_disk(folder, token, header)
# print(f)

path_in_root = "подпись_в_цифре"
folder_of_putting = "xxx2"
def yandex_request_put_foldr(path_in_root, folder_of_putting, header):

  url = "https://cloud-api.yandex.net/v1/disk/resources"
  parametres = {'path' : "%s/%s" % (path_in_root, folder_of_putting)}
  response = requests.put(url, params=parametres, headers=header)
  return response

t = yandex_request_put_foldr(path_in_root, folder_of_putting, header)
print(t)