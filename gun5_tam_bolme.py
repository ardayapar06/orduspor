def tam_bolme(a, b):
    if b == 0:
        return "Hata: 0'a bölünemez"
    
    sonuc = a // b
    return sonuc


def main():
    sayi1 = 17
    sayi2 = 3

    print("Tam bölme işlemi sonucu:")
    print(tam_bolme(sayi1, sayi2))


if __name__ == "__main__":
    main()