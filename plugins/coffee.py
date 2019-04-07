from disco.bot import Bot, Plugin
import rolldice
from enum import Enum

class Drinks(Enum):
    espresso = (1, "Эспрессо")
    americano = (2, "Американо")
    cappuccino = (3, "Капучино")
    latte = (4, "Латте")
    raf = (5, "Раф-кофе")
    flat_white = (6, "Флэт Уайт")
    mocachino = (7, "Мокаччино")
    frappuchino = (8, "Фраппучино")
    hot_chocolate = (9, "Горячий шоколад")
    cacao = (10, "Какао")
    milk_coctail = (11, "Молочный коктейль")
    tea = (12, "Чай")

    enjoy1 = (13, "Латте бельгийская вафля")
    enjoy2 = (14, "Арахисовый капучино")
    enjoy3 = (15, "Капучино кокосовый бисквит")
    enjoy4 = (16, "Лавандовый раф")
    enjoy5 = (17, "Грушевый раф с солёной карамелью")
    enjoy6 = (18, "Чай с вишней и пряностями")

    latte_tea = (19, "Латте чай")

    # feel_winter1 = (20, "Хвойный раф")
    # feel_winter2 = (21, "Раф грецкий орех в клиновом сиропе")
    # feel_winter3 = (22, "Чай шиповник-липа")
    # feel_winter4 = (23, "Чай японский лимон Юзу")

    feel_spring1 = (20, "Раф малина-ваниль")
    feel_spring2 = (21, "Яблочно-вишнёвый грог")
    feel_spring3 = (22, "Капучино черника-банан")
    feel_spring4 = (23, "Латте ягодное печенье")

    def __init__(self, id, title):
        self.id = id
        self.title = title

class Syrops(Enum):
    syroup1 = (1, "Карамель")
    syroup2 = (2, "Солёная карамель")
    syroup3 = (3, "Банан")
    syroup4 = (4, "Ваниль")
    syroup5 = (5, "Миндаль")
    syroup6 = (6, "Кокос")
    syroup7 = (7, "Кленовый")
    syroup8 = (8, "Клубника")
    syroup9 = (9, "Имбирный пряник")
    syroup10 = (10, "Шоколад")
    syroup11 = (11, "Амаретто")
    syroup12 = (12, "Ирландский крем")
    syroup13 = (13, "Мята")
    syroup14 = (14, "Лесной орех")
    syroup15 = (15, "Шоколадное печенье")
    syroup16 = (16, "Цветочный мёд")
    syroup17 = (17, "Малина")
    sugar = (18, "Ванильный сахар")
    combo1 = (19, "Солёная карамель и имбирный пряник")

    def __init__(self, id, title):
        self.id = id
        self.title = title


class Teas(Enum):
    green = (1, "Зелёный")
    black = (2, "Чёрный")
    fruit = (3, "Фруктовый")

    def __init__(self, id, title):
        self.id = id
        self.title = title


class CoffeePlugin(Plugin):
    @Plugin.command('coffee', '[param:str]')
    def on_coffee(self, event, param=''):
        try:
            result = ""
            if param.lower() == 'classic':
                result1, expl1 = rolldice.roll_dice('1d12')
            elif param.lower() == 'raf':
                result1, expl1 = (5, 'User')
            else:
                result1, expl1 = rolldice.roll_dice('1d23')
            result += list(Drinks)[result1-1].title
            if result1 == 5:
                result2, expl2 = rolldice.roll_dice('1d18')
                if result2 > 16:
                    result2, expl2 = rolldice.roll_dice('1d15')
                    result21, expl21 = rolldice.roll_dice('1d15')
                    result += "\n**Сиропы**: {} и {}".format(list(Syrops)[result2 - 1].title, list(Syrops)[result21 - 1].title)
                else:
                    result += "\n**Сироп**: {}".format(list(Syrops)[result2 - 1].title)
            elif result1 == 9:
                result2, expl2 = rolldice.roll_dice('1d2')
                if result2 == 1:
                    result += "\nТёмный"
                else:
                    result += "\nМолочный"
            elif result1 == 12 or result1 == 19:
                result2, expl2 = rolldice.roll_dice('1d3')
                result += " {}".format(list(Teas)[result2 - 1].title)
        except Exception as e:
            event.msg.reply(str(e))
        else:
            event.msg.reply(result)
