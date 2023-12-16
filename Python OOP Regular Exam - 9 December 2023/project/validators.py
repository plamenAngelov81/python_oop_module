class Validator:

    @staticmethod
    def check_for_empty_string(value: str, message):
        if value.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_points(value: int, message):
        if not 1 <= value <= 10:
            raise ValueError(message)

    @staticmethod
    def check_oxygen_level(value, message):
        if value < 0:
            raise ValueError(message)
