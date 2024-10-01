skaitlis = int(input("ievadi skaitli no 1-100 "))
dalitajs = 1
while dalitajs != 101:
    if skaitlis % dalitajs == 0:
        print(skaitlis, "dalas ar", dalitajs)
        dalitajs += 1
    else:
        dalitajs += 1
