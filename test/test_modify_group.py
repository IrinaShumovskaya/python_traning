from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="edit-name", header="edit-header", footer="edit-footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

def test_modify_group_empty_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="sdsdd", footer="sdsdsd"))
    else:
        if not app.group.first_empty_name() == 0:
           app.group.modify_first_group(Group(name=""))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New1 group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

