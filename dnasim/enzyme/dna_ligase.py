from dnasim.enzyme.enzyme import Enzyme


class DNALigase(Enzyme):
    def __init__(self):
        """
        Объект фермента ДНК-лизы
        https://en.wikipedia.org/wiki/DNA_ligase
        """
        ec_number = None  # TODO: Указать Шифр КФ для метилтрансферазы
        super().__init__(ec_number)


