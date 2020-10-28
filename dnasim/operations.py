from typing import List, Union
from dnasim.nucleic_acid import NucleicAcid
from dnasim.enzyme.enzyme import Enzyme
from dnasim.enzyme.dna_ligase import DNALigase
from dnasim.enzyme.dna_methyltransferase import DNAMethyltransferase
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


def restriction(dna: NucleicAcid, restrictase: Union[Enzyme, Restrictase], sites) -> List[NucleicAcid]:
    """
    Рестрикция - разрезание ДНК на ферменты
    :param dna: разрезаемая ДНК
    :param restrictase: применяемая для этого рестриктаза
    :param restriction_sites: сайты рестрикции - участки ДНК, по которым осуществляется разрезание
    :return:
    """
    return []


def methylation(dna: NucleicAcid, methyltransferase: Union[Enzyme, DNAMethyltransferase]) -> None:
    """
    Метилироваие - добавление метильных групп к азотистым основаниям нуклеотидов.
    Является защитным механизмом от рестрикции молекулы ДНК
    :return:
    """
    return None


def ligation(dna: NucleicAcid, dna_ligase: Union[Enzyme, DNALigase]) -> None:
    """
    Лигирование - восстановление сахаро-фосфатного остова в молекуле ДНК
    https://en.wikipedia.org/wiki/Ligation_(molecular_biology)
    :return:
    """
    return None
