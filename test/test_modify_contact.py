# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("middle", 10), lastname=random_string("last", 10), nickname=random_string("nickname", 10),
                      title=random_string("title", 10), company=random_string("company", 10), adress=random_string("adress", 20), homephone=random_string("+", 10),
                      mobilephone=random_string("+", 10), workphone=random_string("+", 10), fax=random_string("+", 10), email2=random_string("@", 5),
                      email3=random_string("@", 10), homepage=random_string("www.", 10), birthday_year=random_string("1", 3), anniversary_year=random_string("1", 3),
                      adress2=random_string("adress2", 20), secondaryphone=random_string("+", 10), notes=random_string("notes", 25))
    for i in range(5)
]

@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])


def test_modify_first_contact(app, contacts):
    if app.contact.count() == 0:
        app.contact.create(contacts)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact= (contacts)
    app.contact.modify_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



