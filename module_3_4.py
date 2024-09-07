def single_root_words(root_word,*other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.upper() in str(other_words[i]).upper() or str(other_words[i]).upper() in root_word.upper():
            same_words.append(other_words[i])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('дом' , 'Домашний' , 'Домовой', 'дым','Дама' ,'демон' ,
                            'ДУРАК' ,'доголом' ,'дуб' ,'ДАрр' ,'дурдом' ,)
print(result1)
print(result2)
print(result3)