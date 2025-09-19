# Pytest – mini-kursus (A–C)

See projekt on mõeldud õpilastele, et harjutada **testide kirjutamist** `pytest` abil.
Fookus: kirjuta teste, et leida vigane kood. Funktsioonid on juba valmis (mõned on tahtlikult vigased).

## Kuidas käivitada testid
1) Ava terminal projektikaustas `pytest-kursus`
2) Käivita kõik testid:
   pytest -q
3) Käivita ainult A-osa testid:
   pytest -q tests/test_a_basics.py
4) Käivita üksik testinimi (näiteks test_add_basic):
   pytest -q -k test_add_basic

## Ülesanne
1) Vaata `src/` failides olevaid funktsioone
2) Kirjuta teste `tests/` failides, et kontrollida funktsioonide õigsust
3) Mõned funktsioonid on tahtlikult vigased - sinu testid peaksid need leidma!
4) Kui testid kukuvad, siis oled leidnud vea. Kui testid lähevad läbi, siis funktsioon on õige.

## Ülesannete ülevaade
- A (a_basics.py): algtaseme puhtad funktsioonid (aritmeetika, sõned)
- B (b_collections_io.py): kogud ja failisüsteem (listid, sõnastikud, failid)  
- C (c_module.py): väike moodul klassi ja keerukamate servajuhtudega

Kõik on eesti keeles ja minimalistlik. Edu!
