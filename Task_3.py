#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

dictionary_eng = dict()
dictionary_eng['1'] = 'AEIOULNSTR'
dictionary_eng['2'] = 'DG'
dictionary_eng['3'] = 'BCMP'
dictionary_eng['4'] = 'FHVWY'
dictionary_eng['5'] = 'K'
dictionary_eng['8'] = 'JX'
dictionary_eng['10'] = 'QZ'

dictionary_ru = dict()
dictionary_ru['1'] = 'АВEИНОРСТ'
dictionary_ru['2'] = 'ДКЛМПУ'
dictionary_ru['3'] = 'БГЁЬЯ'
dictionary_ru['4'] = 'ЙЫ'
dictionary_ru['5'] = 'ЖЗХЦЧ'
dictionary_ru['8'] = 'ШЭЮ'
dictionary_ru['10'] = 'ФЩЪ'

scores = 0
print('Выберите язык: ru or eng')
lang = input()
word = input('Введите слово: ')

if lang == 'eng':
    for letter in word:
         for key in dictionary_eng:
             for letter_key in dictionary_eng.get(key):
                 if letter in letter_key:
                     scores += int(key)
else:
    for letter in word:
         for key in dictionary_ru:
             for letter_key in dictionary_ru.get(key):
                 if letter in letter_key:
                     scores += int(key)

print(scores)