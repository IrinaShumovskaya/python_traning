from model.group import Group
from random import randrange

import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]

@pytest.mark.parametrize("editgroup", testdata, ids=[repr(x) for x in testdata])


def test_modify_group(app, editgroup):
    if app.group.count() == 0:
        app.group.create(editgroup)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = editgroup
    app.group.modify_group_by_index(index, group)
    group.id = old_groups[index].id
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
