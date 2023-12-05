class Validator:
    @staticmethod
    def check_for_empty_strings(value: str, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def price_check(value: float, message):
        if value <= 0:
            raise ValueError(message)
