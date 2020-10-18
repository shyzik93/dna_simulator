from enzyme.enzyme import Enzyme


class Methyltransferase(Enzyme):
    def __init__(self, can_restrict=False, can_methylate=True):
        """
        Объект фермента Метилтрансфераза
        """
        ec_number = None  # TODO: Указать Шифр КФ для метилтрансферазы
        super().__init__(ec_number)

    def Methylation(self):
        """
        Метилироваие - добавление метильных групп к азотистым основаниям нуклеотидов
        :return:
        """
        return None
