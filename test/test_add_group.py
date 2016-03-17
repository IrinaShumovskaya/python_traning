# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixrure = Application()
    request.addfinalizer(fixrure.destroy)
    return fixrure


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
