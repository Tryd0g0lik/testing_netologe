import requests
import pytest
# from yandex_api import yandex_request_put_foldr
from yandex_folder.yand_token import token_key
from yandex_folder.yandex_api import yandex_request_put_foldr
from yandex_folder.decorate import parametrized_decoder

token = token_key()

header = {
  'Authorization': 'OAuth %s' %(token),
  'Content-Type': 'application/json'
}

# path_in_root = "подпись_в_цифре"
# folder_of_putting = "xxx2"

parametre = [
  ("подпись_в_цифре", "xxx7", header, f"{(201,)}"),
  ("подпись_в_цифре", "xxx2", header, f"{(409,)}"),
  ("подпись_в_цифрЕ", "xxx4", header, f"{(409,)}"),
  ("Подпись_в_цифре", "xxx5", header, f"{(409,)}"),
  ("подписьв_цифре", "xxx6", header, f"{(409,)}")
]

@pytest.mark.parametrize("path_in_root, folder_of_putting, header, result", parametre)
def test_yandex_request_put_foldr(path_in_root, folder_of_putting, header, result):
  assert yandex_request_put_foldr(path_in_root, folder_of_putting, header) == result