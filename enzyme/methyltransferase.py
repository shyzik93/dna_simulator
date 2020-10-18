from enzyme.enzyme import Enzyme

class Methyltransferase(Enzyme):
    """
    Объект фермента Метилтрансфераза
    """
    def __init__(self, ):
        ec_number = None  # TODO: Указать Шифр КФ для метилтрансферазы
        super().__init__(ec_number)

    def Methylation(self):
        """
        Метилироваие - добавление метильных групп к азотистым основаниям нуклеотидов
        :return:
        """
        return None
