def f(x, y):
    # Kanei to y lista. px l1 = [5,6,3,6,6]
    l1 = [int(i) for i in str(y)]
    # Lista tis opoias kathe stoixeio einai to antistoixo stoixeio tis l1 ypsomeno sto tetragwno.
    # px l2 = [25, 36, 9, 36, 36]
    l2 = [i * i for i in l1]
    s = 0
    for i in range(len(l2)):  # For apo to 0 mexri to mikos this l2. px 5
        # Gia na orizetai to x[i], to x prepei na einai lista (list int opws tha doume sti sinexeia).
        # Gia na epistrepsei 2 o algorithmos prepei na epileksoume ena x, tou opoiou ta stoixeia na diairoun teleia
        # ola ta stoixeia to AM, ektws apo duo.
        # Gia auta ta duo to upoloipo tis dairesis prepei na einai 1.
        # Arkei loipon na broume dyo stoixeia to AM pou na einai monoi arithmoi kai na tous diaresoume me to 2.
        # Px: x = [2,6,2,6,6] kai y = 56366
        s += l2[i] % x[i]
    return s


print(f([2, 6, 2, 6, 6], 56366))

# Notes:
#   % -> mod (ypoloipo treleias diairesis)
#   += -> s += 7 === s = s + 7
