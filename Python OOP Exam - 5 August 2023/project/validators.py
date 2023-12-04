class Validator:
    @staticmethod
    def check_for_empty_string(value, message):
        if value.strip() == '':
            raise ValueError(message)
