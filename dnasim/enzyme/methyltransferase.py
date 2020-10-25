from dnasim.enzyme.enzyme import Enzyme


class Methyltransferase(Enzyme):
    def __init__(self, can_restrict=False, can_methylate=True):
        """
        Объект фермента Метилтрансфераза
        """
        ec_number = None  # TODO: Указать Шифр КФ для метилтрансферазы
        super().__init__(ec_number)


