# Написать игру крестики-нолики

my_field = {
  "1" : " 1 ",
  "2" : " 2 ",
  "3" : " 3 ",
  "4" : " 4 ",
  "5" : " 5 ",
  "6" : " 6 ",
  "7" : " 7 ",
  "8" : " 8 ",
  "9" : " 9 "
}

def print_field(fld):
    print(fld.get("1") + fld.get("2") + fld.get("3"))
    print(fld.get("4") + fld.get("5") + fld.get("6"))
    print(fld.get("7") + fld.get("8") + fld.get("9"))
        
def check_winner(fld):
    if fld["1"] == fld["2"] == fld["3"]:
        return True
    elif fld["4"] == fld["5"] == fld["6"]:
         return True
    elif fld["7"] == fld["8"] == fld["9"]:
        return True
    elif fld["1"] == fld["4"] == fld["7"]:
        return True
    elif fld["2"] == fld["5"] == fld["8"]:
        return True
    elif fld["3"] == fld["6"] == fld["9"]:
        return True
    elif fld["1"] == fld["5"] == fld["9"]:
        return True
    elif fld["3"] == fld["5"] == fld["7"]:
        return True
    else:
        return False


print_field(my_field)
move = 4

# my_field.update({f"{move}" : " X "})
# print_field(my_field)

for i in range(1,10):
    if i%2 != 0:
        if check_winner(my_field):
            print ("Победил нолик!")
            break
        else:
            move = int(input("Крестик, ваш ход. Введите номер свободной ячейки от 1 до 9: "))
            my_field[move] = "X"
            my_field.update({f"{move}" : " X "})
            print_field(my_field)
    if i%2 == 0:
        if check_winner(my_field):
            print ("Победил крестик!")
            break
        else:
            move = int(input("Нолик, ваш ход. Введите номер свободной ячейки от 1 до 9: "))
            my_field[move] = "0"
            my_field.update({f"{move}" : " 0 "})
            print_field(my_field)
    if i == 9:
        print("Вничью сыграли)")













