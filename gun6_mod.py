def mod(a, b):
    if b == 0:
        return "Hata: 0'a bölünemez"
    
    sonuc = a % b
    return sonuc


def main():
    sayi1 = 17
    sayi2 = 5

    print("Mod (kalan) işlemi sonucu:")
    print(mod(sayi1, sayi2))


if __name__ == "__main__":
    main()