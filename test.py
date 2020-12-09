import json


class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Lead:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


ctcList = []
leadList = []
# Add contacts to contact list
ctcList.append(Contact('Alice Brown', None, 1231112223))
ctcList.append(Contact('Bob Crown', 'bob@crowns.com', None))
ctcList.append(Contact('Carlos Drew', 'carl@drewess.com', 3453334445))
ctcList.append(Contact('Doug Emerty', None, 4564445556))
ctcList.append(Contact('Egan Fair', 'g@fairness.com', 5675556667))
# Add leads to lead list
leadList.append(Lead(None, 'kevin@keith.com', None))
leadList.append(Lead('Lucy', 'lucy@liu.com', 3210001112))
leadList.append(Lead('Mary Middle', 'mary@middle.com', 3331112223))
leadList.append(Lead(None, None, 4442223334))
leadList.append(Lead(None, 'ole@olson.com', None))
match = False
registrants = """{
   "registrant": [
      {
        "name":"Lucy Liu",
        "email":"lucy@liu.com",
        "phone":""
      },

      {
       "name":"Uma Thurman",
       "email":"doug@emmy.com",
       "phone":"4564445556"
      },
      {
       "name":"Doug",
       "email":"uma@thurs.com",
       "phone":""
      }
   ]
}
"""
# parse JSON data to python dictionary
python_registrants = json.loads(registrants)
# match registrants
for reg in python_registrants.get('registrant'):
    match = False
    if not match and reg.get('email'):
        for contact in ctcList:
            if reg.get('email') == contact.email:
                match = True
                if reg.get('phone') and not contact.phone:
                    contact.phone = reg.get('phone')
        if not match:
            for lead in leadList:
                if reg.get('email') == lead.email:
                    match = True
                    ctcList.append(Contact(lead.name, lead.email, lead.phone))
                    leadList.remove(lead)
    if not match and reg.get('phone'):
        for contact in ctcList:
            if reg.get('phone') == contact.phone:
                match = True
                if reg.get('email') and not contact.email:
                    contact.email = reg.get('email')
        if not match:
            for lead in leadList:
                if reg.get('phone') == lead.phone:
                    match = True
                    ctcList.append(Contact(lead.name, lead.email, lead.phone))
                    leadList.remove(lead)

    if not match and reg.get('name'):
        ctcList.append(Contact(reg.get('name'),
                               reg.get('email'),
                               reg.get('phone')))
