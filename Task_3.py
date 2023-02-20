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
dictionary_eng['1'] = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
dictionary_eng['2'] = 'D', 'G'
dictionary_eng['3'] = 'B', 'C', 'M', 'P'
dictionary_eng['4'] = 'F', 'H', 'V', 'W', 'Y'
dictionary_eng['5'] = 'K'
dictionary_eng['8'] = 'J', 'X'
dictionary_eng['10'] = 'Q', 'Z'

dictionary_ru = dict()
dictionary_ru['1'] = 'А', 'В', 'E', 'И', 'Н', 'О', 'Р', 'С', 'Т'
dictionary_ru['2'] = 'Д', 'К', 'Л', 'М', 'П', 'У'
dictionary_ru['3'] = 'Б', 'Г', 'Ё', 'Ь', 'Я'
dictionary_ru['4'] = 'Й', 'Ы'
dictionary_ru['5'] = 'Ж', 'З', 'Х', 'Ц', 'Ч'
dictionary_ru['8'] = 'Ш', 'Э', 'Ю'
dictionary_ru['10'] = 'Ф', 'Щ', 'Ъ'

scores = 0
word = input('Введите слово: ')

for letter in word:
     # print('Буква слова: {} - {}'.format(letter, type(letter)))                   # Перебор букв в слове
     print(scores)
     for key in dictionary_eng:
         print('Ключ: {}'.format(key))                                              # Перебор ключей
         for letter_key in dictionary_eng.get(key):
             print('Буква слова: {} - {}'.format(letter, type(letter)))
             print('Буквы в ключе: {} - {}'.format(letter_key, type(letter_key)))   # Перебор букв в ключе
             if     letter  == letter_key:
                 scores += int(key)
                 print(scores)
             elif   letter  == letter_key:
                 scores += int(key)
                 print(scores)
             elif   letter  == letter_key:
                 scores += int(key)
                 print(scores)
             elif   letter  == letter_key:
                 scores += int(key)
                 print(scores)
             elif   letter  == letter_key:
                 scores += int(key)
                 print(scores)
             else:
                 scores += int(key)
                 print(scores)


print(scores)