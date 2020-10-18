class SystemRestrictionModification:
    def __init__(self, enzymes, restriction_sites):
        """
        Объект системы Рестрикции-Модификации
        :param enzymes: список ферментов рестриктазы и/или метилтрансферазы
        """
        self.enzymes = enzymes
        self.restriction_sites = restriction_sites
