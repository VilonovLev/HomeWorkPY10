
class Person:
    def __init__(self, name, sname, lname, dict_ph):
        self.name = name
        self.lname = sname
        self.sname = lname
        self.dict_ph = dict_ph

    def get_phone(self):
        return dict(self.dict_ph).get("private")

    def get_name(self):
        return f"{self.sname} {self.name} {self.lname}"

    def get_work_phone(self):
        return dict(self.dict_ph).get('work')

    def get_sms_text(self):
        return (f"Уважаемый {self.name} {self.lname}! Примите участие " +
                "в нашей беспройгрышном конкурсе для физических лиц!")


class Company:
    def __init__(self, name_c, type_c, dict_cont,*person):
        self.name_c = name_c
        self.type_c = type_c
        self.dict_cont = dict(dict_cont)
        self.person_list = list(person)

    def get_phone(self):
        if 'contact' in self.dict_cont.keys():
            return self.dict_cont.get('contact')
        else:
            for person in self.person_list:
                tel = person.get_work_phone()
                if tel == None:
                    return tel
            return 

    def get_name(self):
        return self.name_c

    def get_sms_text(self):
        return (f"Для компании {self.name_c} есть супер предложение!" +
        f"Примите участие в нашем беспройгрышном конкурсе для {self.type_c}.")

def send_sms(*args):
    for contact in args:
        if contact.get_phone() == None:
            if isinstance(contact, Company):
                for person in contact.person_list:
                    if person.get_work_phone() != None:
                        work_phone = person.get_work_phone()
                        print(f"Отправлено СМС на номер {work_phone} с текстом {contact.get_sms_text()}")
                        break
                else:
                    continue
            print(f"Не удалось отправить сообщение абоненту {contact.get_name()}")
        else:       
            print(f"Отправлено СМС на номер {contact.get_phone()} с текстом {contact.get_sms_text()}")

# Первый пример

# person1 = Person("Ivan", "Ivanovich", "Ivanov", {'private': 123, 'work': 456})
# person2 = Person("Ivan", "Petrovich", "Petrov", {'private': 789})
# person3 = Person("Ivan", "Petrovich", "Sidorov", {'work': 789})
# person4 = Person("Jhon", "Unknown", "Doe", {})
# company1 = Company("Bell","OOO",{"contact":111},person3,person4)
# company2 = Company("Cell","AO",{"non_contact":222},person2,person3)
# company3 = Company("Dell","Ltd",{"non_contact":333},person2,person4)
# send_sms(person1,person2,person3,person4,company1,company2,company3)

# Второй пример

person1 = Person("Степан", "Петрович", "Джобсов", {'private': 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {'private': 777,'work': 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {'work': 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат","OOO",{"contact":111},person1,person4)
company2 = Company("ПластОкно","AO",{"non_contact":222},person2)
company3 = Company("Пингвинья ферма","Ltd",{"non_contact":333},person4)
send_sms(person1,person2,person3,person4,company1,company2,company3)