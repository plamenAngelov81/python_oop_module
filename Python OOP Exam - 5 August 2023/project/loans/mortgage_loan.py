from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50_000.0
    RATE_INCREMENT = 0.5
    LOAN_TYPE = 'MortgageLoan'

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.RATE_INCREMENT
