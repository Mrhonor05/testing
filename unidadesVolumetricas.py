def unidadesmVolumetricas():
    op1 = int(input("> "))
    if op1 == 1:
        print("(1) l->ml, (2) ml->l")
        op2 = int(input("> "))
        if op2 == 1:
            x = float(input("l = "))
            print(f"ml = {x*1000}")
        else:
            x = float(input("ml = "))
            print(f"l = {x/1000}")     