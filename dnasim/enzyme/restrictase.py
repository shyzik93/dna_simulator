from dnasim.enzyme.enzyme import Enzyme


class Restrictase(Enzyme):
    def __init__(self, can_restrict=True, can_methylate=False):
        """
        Объект фермента Рестриктаз (эндонуклеаза рестрикции)
        """
        ec_number = None  # TODO: Указать Шифр КФ для рестриктазы
        super().__init__(ec_number)


