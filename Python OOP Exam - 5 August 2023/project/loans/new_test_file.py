from project.bank_app import BankApp

obj = BankApp(5)
obj.add_client('Student', ' ', 'PL67891555', 98.36)
# obj.add_client('Student', 'Atanas', 'PL67891555', 55.3)
# obj.add_client('Student', 'Atanas', 'PL67891555', 85.1)
# obj.add_client('Student', 'Atanas', 'PL67891555', 23.5)
# obj.add_client('Student', 'Atanas', 'PL67891555', 68.4)
# income_list = [x.income for x in obj.clients]
# print(sorted(income_list, key=lambda x: x))
print(obj.clients[0].name)