# Deoxyribonucleic acid, DNA is the primary information storage molecule
# in biological systems. It is composed of four nucleic acid bases
# Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells.
# RNA differs slightly from DNA its chemical structure and contains no Thymine.
# In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# Дезоксирибонуклеиновая кислота, ДНК, является основной молекулой
# для хранения информации в биологических системах. Она состоит
# из четырех оснований нуклеиновых кислот
# Гуанин ("G"), цитозин ("C"), аденин ("A") и тимин ("T").

# Рибонуклеиновая кислота, РНК, является основной молекулой-посредником в клетках.
# РНК немного отличается от ДНК по своей химической структуре и не содержит тимина.
# В РНК тимин заменен другой нуклеиновой кислотой - урацилом ("U").

# Создайте функцию, которая преобразует данную цепочку ДНК в РНК.
# ""GCAT" => "GCA"
# Входная строка может быть произвольной длины - в частности,
# она может быть пустой. Все входные данные гарантированно будут корректными,
# т.е. каждая входная строка всегда будет состоять только из 'G', 'C', 'A' и/или 'T'.

def dna_to_rna(dna):
    elem_new = ""
    for elem in dna:
        if elem == "T":
            elem_new = elem_new + "U"
        else:
            elem_new = elem_new + elem
    return elem_new

    # return dna.replace('T', 'U')

print(dna_to_rna("TTTT"), "UUUU")
print(dna_to_rna("GCAT"), "GCAU")
print(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")

