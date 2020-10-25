from typing import List
from dnasim.nucleic_acid import NucleicAcid
from dnasim.enzyme.methyltransferase import Methyltransferase
from dnasim.enzyme.restrictase import Restrictase
from dnasim.protein import Protein


def replicate(dna: NucleicAcid) -> NucleicAcid:
    """
    Репликация - синтез ДНК по матрице ДНК
    :return: копия ДНК
    """
    return None


def transcription(dna: NucleicAcid) -> NucleicAcid:
    """
    Транскрипция - синтез РНК по матрице ДНК
    :return: РНК
    """
    return None


def translation(rna: NucleicAcid) -> Protein:
    """
    Трансляция - синтез белка по матрице РНК
    :return: белок
    """
    return None


def restriction(dna: NucleicAcid, restrictase: Restrictase, sites) -> List[NucleicAcid]:
    """
    Рестрикция - разрезание ДНК на ферменты
    :param dna: разрезаемая ДНК
    :param restrictase: применяемая для этого рестриктаза
    :param restriction_sites: сайты рестрикции - участки ДНК, по которым осуществляется разрезание
    :return:
    """
    return None


def methylation(dna: NucleicAcid, methyltransferase: Methyltransferase) -> NucleicAcid:
    """
    Метилироваие - добавление метильных групп к азотистым основаниям нуклеотидов
    :return:
    """
    return None