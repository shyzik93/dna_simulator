'''
== Организмы с минимальным набором нуклеотидных пар ==

1. Mycoplasma genitalium (582 970 н. п.) - https://ru.m.wikipedia.org/wiki/Mycoplasma genitalium
2. Nanoarchaeum equitans (490 885 н. п.) - https://ru.m.wikipedia.org/wiki/Наноархеоты
3. Carsonella ruddii (159 662 н. п.) - https://en.m.wikipedia.org/wiki/Candidatus_Carsonella_ruddii
4. Tremblaya princeps (139 000 н. п.)
4. Nasuia_deltocephalinicola (112 091 н. п.) - https://en.m.wikipedia.org/wiki/Nasuia_deltocephalinicola

Человек разумный — 3.2 миллиарда н. п.

== Ссылки ==

+ Модельные организмы
https://ru.m.wikipedia.org/wiki/Модельные_организмы

https://ru.m.wikipedia.org/wiki/Хлорелла

База геномов вирусов (2408 штук)
https://www.ncbi.nlm.nih.gov/genome/viruses/
https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/

+ Biopython — модуль BioSQL
https://coderlessons.com/tutorials/python-technologies/izuchite-biopython/biopython-modul-biosql
+ Introduction to SeqIO
https://biopython.org/wiki/SeqIO

База данных белков:
https://ru.wikipedia.org/wiki/UniProt
http://www.uniprot.org/
'''

# Азотистые основания
# https://www.nature.com/articles/nature13314
nitrogenous_bases = '''
A Аденин
G Гуанин
C Цитозин
U Урацил
T Тимин
X d5SICSTP
Y dNaMTP
'''

Complementarity = 
A-T
G-C

# У некоторых прокариот стартовыми кодонами также являются GUG, AUU, CUG, UUG. У эукариот — AUG
# ru.wikipedia.org/wiki/Кодон
codons = '''
    AAA Lys/K Лизин
    AAG Lys/K Лизин
    AAC Asn/N Аспарагин
    AAU Asn/N Аспарагин

    AGA Arg/R Аргинин
    AGG Arg/R Аргинин
    AGC Ser/S Серин
    AGU Ser/S Серин

    ACA Thr/T Треонин
    ACG Thr/T Треонин
    ACC Thr/T Треонин
    ACU Thr/T Треонин

    AUA Ile/I Изолейцин
    AUG Met/M Метионин
    AUC Ile/I Изолейцин
    AUU Ile/I Изолейцин

    GAA Glu/E Глутаминовая кислота
    GAG Glu/E Глутаминовая кислота
    GAC Asp/D Аспарагиновая кислота
    GAU Asp/D Аспарагиновая кислота

    GGA Gly/G Глицин
    GGG Gly/G Глицин
    GGC Gly/G Глицин
    GGU Gly/G Глицин

    GCA Ala/A Аланин
    GCG Ala/A Аланин
    GCC Ala/A Аланин
    GCU Ala/A Аланин

    GUA Val/V Валин
    GUG Val/V Валин
    GUC Val/V Валин
    GUU Val/V Валин

    CAA Gln/Q Глутамин
    CAG Gln/Q Глутамин
    CAC His/H Гистидин
    CAU His/H Гистидин

    CGA Arg/R Аргинин
    CGG Arg/R Аргинин
    CGC Arg/R Аргинин
    CGU Arg/R Аргинин

    CCA Pro/P Пролин
    CCG Pro/P Пролин
    CCC Pro/P Пролин
    CCU Pro/P Пролин

    CUA Leu/L Лейцин
    CUG Leu/L Лейцин
    CUC Leu/L Лейцин
    CUU Leu/L Лейцин

    UAA stop Охра
    UAG stop Янтарь
    UAC Tyr/Y Тирозин
    UAU Tyr/Y Тирозин

    UGA stop Опал
    UGG Trp/W Триптофан
    UGC Cys/C Цистеин
    UGU Cys/C Цистеин

    UCA Ser/S Серин
    UCG Ser/S Серин
    UCC Ser/S Серин
    UCU Ser/S Серин

    UUA Leu/L Лейцин
    UUG Leu/L Лейцин
    UUC Phe/F Фенилаланин
    UUU Phe/F Фенилаланин
'''

class Gene:
    def __init__(self, codons=None, acids=None, name=None, type=None):
        pass