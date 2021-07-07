"""
Fonksiyonun akışı:
- Gönderilen list'in elemanlarını dolaş.
    - Eğer gönderilen listin elemanı list ise recursive olarak fonksiyona tekrar gönder.
        - Eğer dolaşılan list'in son elemanı ise dolaşılan list'i ters çevir.
    
    - Eğer gönderilen listin elemanı list değilse son eleman mı kontrol et.
        - Eğer son elemansa dolaşılan list'i ters çevir.
        - Eğer son eleman değilse list'i dolaşmaya devam et.
"""
def reversing(input_l):
    
    for i in input_l:           
        if type(i) == type([]):
            reversing(i)
            if i == input_l[-1]:
                input_l.reverse()
        else:
            if i == input_l[-1]:
                input_l.reverse()
            else:
                continue

    return input_l



input_l = [[1, [2, 5]], [3, 4], [5, 6, 7]]

print(reversing(input_l))
