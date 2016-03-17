# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="edit-name", middlename="edit-mname", lastname="edit-lname", nickname="edit-nname",
                               title="edit-title", company="edit-com.pany", adress="edit-adress", home_phone="11111111",
                               mobile_phone="22222222", work_phone="33333333", fax="44444444", email2="email@com.tu",
                               email3="email@con.ui", homepage="www.tqre.yu", birthday_year="1989", anniversary_year="1999",
                               adress2="edit-adress", home_phone2="77777777", notes="edit-notes"))
    app.session.logout()