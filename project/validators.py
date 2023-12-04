class Validator:

    @staticmethod
    def check_for_empty_strings(value: str, message):
        if value.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_for_negative_rating(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def check_route_length(value, message):
        if value < 1:
            raise ValueError(message)
