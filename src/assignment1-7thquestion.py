'''
bu fonksiyon verilen bir index kümesinin (setinin)
tüm permütasyonlarını recursive bir şekilde bulur.

bu kodda blok içi indexlerin tüm
permütasyonlarını bulmak için kullanılmıştır.
'''
def perms_of_set(_set):
    #eğer sadece 1 elemanımız varsa tek bir permütasyonumuz vardır. (base case)
    if (len(_set) == 1):
        last_element = _set.pop()
        _set.add(last_element)
        return [[last_element]]
    
    #eğer 1'den fazla elemanımız varsa tüm permütasyonları
    # [ set[0], perms_of_set(set - set[0]]) ] + [ set[1], perms_of_set(set - set[1]] + ... + [set[N], perms_of_set(set - set[N])]
    #şeklinde bulabiliriz.

    perm_list = []
    setList = [i for i in _set]
    for i in range(len(setList)):
        # önceden seçilmemiş bir eleman için [seçilen eleman + diğer elemanların permütasyonu] listeleri oluşturulur.
        ind = setList[i]
        _set.remove(ind) #setten bu seçilen eleman çıkarılır

        other_perms = perms_of_set(_set) #seçilmeyenlerin permütasyonları alınır
        for perm in other_perms:
            perm_list.append(perm + [ind]) #seçilen eleman ile birlikte seçilmeyenler sıralanır
        
        _set.add(ind) #seçilen eleman geri eklenir bir sonraki döngü için.
        
    return perm_list

'''
bu fonksiyon kapalı metin üzerine 
tüm olabilecek permütasyonları blok blok uygular ve
açık metin karşılıklarını liste olarak verir. 

fonksiyonun çıktısı incelenerek anlamlı olan açık metin
ve ona neden olan permütasyon anahtarı bulunabilir.
'''
def brute_force_decrypt(cipher, block_size):
    _set = set(range(block_size))  #blok içi indexleri bir kümeye yerleştirir
    perms = perms_of_set(_set)     #bu kümenin permütasyonları liste halinde alınır
    
    plain_text = ""   #elde edilen açık metinler bu string aracılığı ile kaydedilir                    
    decryptions = []  #elde eilden açık metin-anahtar ikilileri buraya eklenir  

    #alınan tüm permütasyonlar için: kapalı metnin her bloğu bu permütasyona göre açık metin haline getirilir.
    for perm in perms:
        for i in range(0, len(cipher), block_size):
            for j in range(block_size):
                #i = blok başlangıç indexi, j = karakterin blok içi indexinin yeni karşılığı
                plain_text += cipher[i + perm[j]] #bu satır kapalı metindeki her karakter için çalıştırılır.

        decryptions.append((plain_text, perm))
        plain_text = "" #bir sonraki açık metni alabilmek için boşaltılır.
    return decryptions

'''
tanımlanan fonksiyonlar aşağıdaki gibi kapalı metin ve blok uzunluğu
verilerek kullanılabilir. En sonda tüm olası açık metinleri
basıyoruz.
'''

cipher_text = "TKREUYASNIAOINTBDIGRIEGANSRENTEORPUEDNWAEETRSNISAA"
block_size = 5

all_decryptions = brute_force_decrypt(cipher_text, block_size)

print("All Decryptions: ")
for decryption in all_decryptions:
    print("Chosen Permutation Key:", decryption[1], "||" , "Decryption:", decryption[0])