class Enzyme:
    def __init__(self, ec_number):
        """
        Объект фермента.
        https://ru.wikipedia.org/wiki/Ферменты
        https://en.wikipedia.org/wiki/Enzyme
        :param ec_number: шифр КФ (код фермента) - https://ru.wikipedia.org/wiki/Шифр_КФ
        """
        self.ec_number = ec_number
