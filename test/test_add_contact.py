# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact= (Contact(firstname="name", middlename="mname", lastname="lname", nickname="nname",
                      title="title", company="com.pany", adress="adress", homephone="11111111",
                      mobilephone="22222222", workphone="33333333", fax="44444444", email2="email@com.tu",
                      email3="email@con.ui", homepage="www.tqre.yu", birthday_year="1989", anniversary_year="1999",
                      adress2="adress", secondaryphone="77777777", notes="notes"))
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






