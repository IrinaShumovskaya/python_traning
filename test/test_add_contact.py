# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact= (Contact(firstname="name", middlename="mname", lastname="lname", nickname="nname",
                               title="title", company="com.pany", adress="adress", home_phone="11111111",
                               mobile_phone="22222222", work_phone="33333333", fax="44444444", email2="email@com.tu",
                               email3="email@con.ui", homepage="www.tqre.yu", birthday_year="1989", anniversary_year="1999",
                               adress2="adress", home_phone2="77777777", notes="notes"))
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






