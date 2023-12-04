from project.clients.base_client import BaseClient


class Student(BaseClient):
    POSSIBLE_LOAN_TYPE = 'StudentLoan'

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=2)

    def increase_clients_interest(self):
        self.interest += 1
