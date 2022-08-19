from modules.app import get_doc_owner_name
from modules.app import delete_doc

from modules.app import get_doc_shelf
from modules.app import add_new_doc
import pytest

number = [
  ('2207 876234', 'Code: 200'),
  ('22O7 876234', None),
  ('2207 87r234', None),
  ('11-2', 'Code: 200'),
  ('112', None),
  ('11 2', None),
  ('2207  876234', None),
  ( ' 2207 876234', None),
  ('2207876234', None),
  ('2207-876234', None),
  ('2207 87623', None),
  ('220787623', None),
  ('', None)
]

@pytest.mark.parametrize("number, result", number)
def test_get_doc_owner_name(number, result):
  assert get_doc_owner_name(number) == result

#new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number
document = [
    ("2207 876235", "passpor", "Дмитрий Гупкин", "1", 'Code: 200'),
    ("2207 876236", "passport", "Дмитрий Гупкин", "2", 'None'),
    ("2207 876237", "invoice", "Дмитрий Гупкин", "2", 'None'),
    ("2207 876238", "insurance", "Дмитрий Гупкин", "3", 'None'),
    ("2207 876233", "passport", "Дмитрий", "1", 'None'),
    ("2207 876240", "passport", "Василий Гупкин", "2", 'None'),
    ("2207 876241", "passport", "Василий Гупкин", "3", 'None'),
    ("2207 876242", "passport", "Василий Гупкин", "1", 'None'),
    ("2207876243", "passport", "Василий Гупкин", "1", 'None'),
    ("2207 876244", "passpor", "Василий Гупкин", "1", 'None'),
    ("11-1", "invoice", "Илья Покемонов", "2", 'Code: 200'),
    ("11-2", "invoice", "Ilia Pokemonov", "2", 'None'),
    ("11-3", "invoice", "ИЛЬЯ ПОКЕМОНОВ", "2", 'None'),
    ("11--4", "invoice", "Илья Покемонов", "2", 'None'),
    ("11--5", "Invoice", "Илья Покемонов", "2", 'None'),
    ("11-6", "invoice", "Илья Покемонов", "2", 'None'),
    ("11-7", "invoice", "Илья Покемонов", "", 'None'),
    ("11-8", "invoice", "", "2", 'None'),
    ("11-9", "", "Илья Покемонов", "2", 'None'),
    ("", "invoice", "Илья Покемонов", "2", 'None'),
    ("10-1", "invoice", "ИльяПокемонов", "2", 'None'),
    ("12-2", "invoice", " Илья Покемонов", "2", 'None'),
    ("13-2", "invoice", "илья Покемонов", "2", 'None'),
    ("14-2", "invoice", "Илья покемонов", "2", 'None'),
    ("15-2", "invoice", "Илья Покемонов", "3", 'None'),
    ("16-22", "invoice", "Илья Покемонов", "2", 'None'),
    ("17-22 ", "invoice", "Илья Покемонов", "2", 'None'),
    (" 18-22", "invoice", "Илья Покемонов", "2", 'None'),
    ("112", "invoice", "Илья Покемонов", "2", 'None'),
    ("19-2", "passport", "Илья Покемонов", "2", 'None'),
    ("20-2", "invoice", "Илья Покемонов", "1", 'None'),
    ("10006", "insurance", "Дмитрий Павлов", "3", 'Code: 200'),
    ("100 06", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 07", "insurance", "Дмитрий павлов", "3", 'None'),
    ("100 08", "insurance", "дмитрий Павлов", "3", 'None'),
    ("100 09", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 10", "insurance", "ДмитрийПавлов", "3", 'None'),
    ("100 11", "insurance", "Дмитрий Павлов", "", 'None'),
    ("10 12", "insurance", "", "3", 'None'),
    ("100 13", "", "Дмитрий Павлов", "3", 'None'),
    ("", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("1 0006", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("10 006", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 06", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 14", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 15", "insurance", " Дмитрий Павлов", "3", 'None'),
    ("100 15", "insurance", "Дмитрий Павлов", "03", 'None'),
    ("100 16", "insurance", "Дмитрий Павлов", " 3", 'None'),
    ("100 17", "insurance", " Дмитрий Павлов", "3", 'None'),
    ("100 18", " insurance", "Дмитрий Павлов", "3", 'None'),
    (" 10006", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 19", "insurance", "Дмитрий Павлов", "3", 'None'),
    ("100 20", "insurance", "Дмитрий Павлов", "2", 'None'),
    ("100 21", "insurance", "Дмитрий Павлов", "1", 'None'),
    ("100 22", "insurance", "Dmitrii Pavlov", "3", 'None'),
]

@pytest.mark.parametrize("new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result", document)
def test_add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result):
  assert add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number) == result



number = [
("2207 876234", "Code: 200"),
("2207-876234", "None"),
(" 2207 876234", "None"),
("2207 87623", "None"),
("220 876234", "None"),
("22 876234", "None"),
("2207876234", "None"),
("11-2", "Code: 200"),
("11-2 ", "None"),
("1-12", "None"),
(" 11-2", "None"),
("11", "None"),
("112", "None"),
("10006", "Code: 200"),
("10007", "None"),
("1006", "None"),
("10006 ", "None"),
("1000-6", "None"),
("100-06", "None"),
("10-006", "None"),
("1-0006", "None"),
(" 10006", "None"),
("", "None")
]
@pytest.mark.parametrize("user_doc_number, result", number)
def test_get_doc_shelf_(user_doc_number, result):


  assert get_doc_shelf(user_doc_number) == result

number = [
("2207 876234", ("2207 876234", True)),
("2207-876234", ("None",)),
(" 2207 876234", ("None",)),
("2207 87623", ("None",)),
("220 876234", ("None",)),
("22 876234", ("None",)),
("2207876234", ("None",)),
("11-2", ("11-2", True)),
("11-2 ", ("None",)),
("1-12", ("None",)),
(" 11-2", ("None",)),
("11", ("None",)),
("112", ("None",)),
("10006", ("10006", True)),
("10007", ("None",)),
("1006", ("None",)),
("10006 ", ("None",)),
("1000-6", ("None",)),
("100-06", ("None",)),
("10-006", ("None",)),
("1-0006", ("None",)),
(" 10006", ("None",)),
("", ("None",))
]

@pytest.mark.parametrize("user_doc_number, result", number)
def test_delete_doc(user_doc_number, result):
  assert delete_doc(user_doc_number) == result