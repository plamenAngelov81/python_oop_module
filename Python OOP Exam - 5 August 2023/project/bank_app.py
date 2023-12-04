from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }

    CLIENT_TYPES = {
        'Student': Student,
        'Adult': Adult
    }

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def find_client_by_id(self, client_id):
        clients = [cl for cl in self.clients if cl.client_id == client_id]
        if clients:
            return clients[0]
        return None

    def find_loan_by_type(self, loan_type):
        loans = [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]
        return loans

    def find_clients_by_interest_rate(self, min_rate):
        return [client for client in self.clients if client.interest < min_rate]

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f'{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        loan = self.find_loan_by_type(loan_type)[0]

        if not client.POSSIBLE_LOAN_TYPE == loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)

        if client is None:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loans = [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]
        [loan.increase_interest_rate() for loan in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        filtered_clients = self.find_clients_by_interest_rate(min_rate)
        [client.increase_clients_interest() for client in filtered_clients]
        return f"Number of clients affected: {len(filtered_clients)}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        # # return f'Active Clients: {len(self.clients)}\n'\
        # #        f'Total Income: {total_income:.2f}\n'\
        # #        f'Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}\n'\
        # #        f'Available Loans: {len(self.loans)}, Total SumL {not_granted_sum:.2f}\n'\
        # #        f'Average Client Interest Rate: {avg_client_rate:.2f}'
        #
        # result = ''
        # result += f'Active Clients: {len(self.clients)}\n'
        # result += f'Total Income: {total_income:.2f}\n'
        # result += f'Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}\n'
        # result += f'Available Loans: {len(self.loans)}, Total Sum {not_granted_sum:.2f}\n'
        # result += f'Average Client Interest Rate: {avg_client_rate:.2f}'

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_rate:.2f}"""
