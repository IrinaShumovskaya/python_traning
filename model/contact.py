from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, adress=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, email2=None, email3=None, homepage=None, birthday_year=None, anniversary_year=None,
                 adress2=None, secondaryphone=None, notes=None, id=None, all_phones_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.adress = adress
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_year = birthday_year
        self.anniversary_year = anniversary_year
        self.adress2 = adress2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize