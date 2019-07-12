import random
import time
# Define class of game
class Loto:
    def __init__(self):
        self.count_barrels = 90
        self.ticket_user = list()
        self.ticket_PC = list()
        self.value_barrel = list()
        self.dict_users = {"ticket_user": "Ваша карточка", "ticket_PC": "Карточка копьютера"}
        self.user_lost = 0
        self.user_win = 0

    def generation_ticket(self):
        create = list()
        while len(create) != 15:
            num = random.randint(1, 90)
            if num not in create:
                create.append(num)
        create.sort()
        return create

    def print_ticket(self, ticket , name):
        print(f"{name}".center(21, "-"))
        if len(ticket) > 11:
            print(ticket[:5])
            print(ticket[5:10])
            print(ticket[10:])
            print()
        elif 5 < len(ticket) <= 11:
            print(ticket[:5])
            print(ticket[5:])
            print()
        else:
            print(ticket)
            print()
        # print(f"{ticket[0]} {ticket[1]}  {ticket[2]} {ticket[3]} {ticket[4]}".center(15, " "))
        # print(f"  {ticket[5]} {ticket[6]} {ticket[7]}  {ticket[8]} {ticket[9]}".center(15, " "))
        # print(f"{ticket[10]} {ticket[11]}  {ticket[12]}  {ticket[13]}  {ticket[14]}".center(15, " "))

    def generator_random_barrel(self):
        property = 0
        while property == 0:
            random_barel = random.randint(1, 90)
            if random_barel not in self.value_barrel:
                self.value_barrel.append(random_barel)
                return random_barel

    def is_lost(self):
        if self.user_lost == 1:
            return True
        elif self.user_lost == 0:
            return False
        else:
            raise Exception("Error check function is_lost ")

    def is_win(self):
        if self.user_win == 1:
            return True
        elif self.user_win == 0:
            return False
        else:
            raise Exception("Error check function is_win ")

    # Проверяем завершилась ли игра?
    # Проверить сумму эллементов Массива или сравнить с Max и проверка функции проигрыша или выигрыша
    def end_game(self):
        # предусмотреть ,что бочонки кончаться ,а тикет остался
        if sum(self.ticket_user) <= 0:
            self.user_win = 1
            return True
        elif sum(self.ticket_PC) <= 0:
            self.user_lost = 1
            return True
        elif self.is_win() == 1 or self.is_lost() == 1:
            return True
        elif self.count_barrels == 0:
            if len(self.ticket_user) < len(self.ticket_PC):
                self.self.user_win = 1
                return True
            elif len(self.ticket_user) > len(self.ticket_PC):
                self.user_lost = 1
                return True
            elif len(self.ticket_user) == len(self.ticket_PC):
                self.user_lost = 1
                return True
        else:
            return False

    def start_game(self):
        print("Welcome to the Game. You will see ticket...".center(20, "-"))
        self.ticket_user = self.generation_ticket()
        self.ticket_PC = self.generation_ticket()
        while self.end_game() != True:
            barel = self.generator_random_barrel()
            self.count_barrels -= 1
            self.value_barrel.append(barel)
            print(f"Новый бочонок: {barel} (осталось {self.count_barrels})".center(20, "-"))
            self.print_ticket(self.ticket_user, "Ваша карточка")
            self.print_ticket(self.ticket_PC, "Карточка компьютера")
            choise = None
            # Спросить у пользователя зачеркнуть или нет
            while choise != "Y" or choise != 'y':
                print()
                choise = input("Зачеркнуть цифру? (y/n)".center(15, "-"))
                # Проверить условия
                # Если зачеркнуть и число есть, то Заменить в массиве число в массиве на "-"
                # Зачеркиваем барель в билете компьютера
                if barel in self.ticket_PC:
                    self.ticket_PC.pop(self.ticket_PC.index(barel))
                        # del self.ticket_PC[self.ticket_PC.index(barel)]
                if choise == "y" or choise == "Y":
                    if barel in self.ticket_user:
                        self.ticket_user.pop(self.ticket_user.index(barel))
                            # del self.ticket_user[self.ticket_user.index(barel)]
                        break
                    else:
                        self.user_lost = 1
                        print("Игрок выбрал зачеркнуть цифру, которой нет".center(20, "-"))
                        break
                elif choise == "n" or choise == "N":
                    break
                else:
                    print("Error choise. Repeat".center(20, "-"))
        if self.is_lost() == True:
            print()
            print("You loose".center(20, "-"))
            time.sleep(10)

        elif self.is_win() == True:
            print()
            print("You Win".center(20, "-"))
            time.sleep(10)

# To call the main function
a = Loto()
a.start_game()