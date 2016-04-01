from time import time
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname + str(time())) #add time for different name contact
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.adress)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        self.change_field_value("byear", contact.birthday_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").click()
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.adress2)
        self.change_field_value("phone2", contact.home_phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len (wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contacts_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit edition
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        self.select_first_contact()
        #submit delition
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delition pop-up
        wd.switch_to_alert().accept()


    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len (wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        # checkboxes = wd.find_elements_by_xpath('//td/input')
        # checkboxes_id = []
        # for x in checkboxes:
        #     checkboxes_id.append(x.get_attribute('id'))
        #
        # firstname = wd.find_elements_by_xpath('//tr/td[3]')
        # firstname_text = []
        # for y in firstname:
        #     firstname_text.append(y.text)
        #
        # lastname = wd.find_elements_by_xpath('//tr/td[2]')
        # lastname_text = []
        # for z in lastname:
        #     lastname_text.append(z.text)
        #
        # zipped = zip(checkboxes_id, firstname_text, lastname_text)
        # contact = list(zipped)
        # return contact


        #     xz = []
        #     for td in wd.find_elements_by_css_selector("td"):
        #         y = td.text
        #         xz.append(y)
        #
        #     first = xz[1]
        #     last = xz[0]
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
        #     contact.append(Contact(firstname=first, lastname=last, id=id))
        #     return contact

        contact = []
        for element in wd.find_elements_by_css_selector("tr"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            last = element.find_elements_by_css_selector("td")[1]
            first = element.find_elements_by_css_selector("td")[2]
            contact.append(Contact(firstname=first, lastname=last, id=id))
        return contact
