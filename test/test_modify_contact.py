# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name", middlename="mname", lastname="lname", nickname="nname",
                                   title="title", company="com.pany", adress="adress", home_phone="11111111",
                                   mobile_phone="22222222", work_phone="33333333", fax="44444444", email2="email@com.tu",
                                   email3="email@con.ui", homepage="www.tqre.yu", birthday_year="1989", anniversary_year="1999",
                                   adress2="adress", home_phone2="77777777", notes="notes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact= (Contact(firstname="edit-name", middlename="edit-mname", lastname="edit-lname", nickname="edit-nname",
                                             title="edit-title", company="edit-com.pany", adress="edit-adress", home_phone="11111111",
                                             mobile_phone="22222222", work_phone="33333333", fax="44444444", email2="email@com.tu",
                                             email3="email@con.ui", homepage="www.tqre.yu", birthday_year="1989", anniversary_year="1999",
                                             adress2="edit-adress", home_phone2="77777777", notes="edit-notes"))
    app.contact.modify_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="New-name"))
    app.contact.modify_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

