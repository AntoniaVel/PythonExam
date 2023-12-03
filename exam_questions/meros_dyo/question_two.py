def f(x):
    n = int(x * 3)  # x -> number
    if len(str(n)) != 6:  # 99999 > x * 3 > 999999 <=> 33333 > x > 333333
        return False
    j = 1
    while n >= 10:  # px n = 123456
        a = n % 10  # teleutaio psifio tou n. px a = 6
        n = n // 10  # px n = 12345
        b = n % 10  # telautaio psifio tou kainouriou n. px b = 5
        if a != b + j:  # px 6 != 5 + 1 -> False
            return False
        j = -j  # to j enallasetai metaksi 1 kai -1
        # ara o n prepei na einai enas 6psifios arithmos, tou opoiou ta psifia diaferoun, ana zeugi, kata 1
        # opws px to 121212. Ara x = 121212/3 = 40404
    return True


print(f(40404))
