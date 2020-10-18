from enzyme.enzyme import Enzyme

class Restrictase(Enzyme):
    """
    Объект фермента Рестриктаз (эндонуклеаза рестрикции)
    """
    def __init__(self):
        ec_number = None  # TODO: Указать Шифр КФ для рестриктазы
        super().__init__(ec_number)

    def restriction(self):
        """
        Рестрикция - разрезание ДНК на ферменты
        :return:
        """
        return None
