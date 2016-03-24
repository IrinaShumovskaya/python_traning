from model.group import Group


#def test_modify_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
#    app.group.modify_first_group(Group(name="edit-name", header="edit-header", footer="edit-footer"))


def test_modify_group_empty_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="sdsdd", footer="sdsdsd"))
    else:
        if app.group.first_empty_name():
         app.group.modify_first_group(Group(name=""))
    app.group.modify_first_group(Group(name="New1 group"))


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="gfgsdfgf", header="sdsdd", footer="sdsdsd"))
#    app.group.modify_first_group(Group(header="New header"))
