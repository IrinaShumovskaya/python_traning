# -*- coding: utf-8 -*-

from group import Group
from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixrure = Application()
    request.addfinalizer(fixrure.destroy)
    return fixrure


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
