
def find_moves(checkers: dict, dice1: int, dice2: int):
    important_doors = [5, 6, 7, 8, 17, 18, 19, 20]
    res_list = []

    def get_point(_checkers, moved_list, key:int):
        """
            Taşların Son haline göre puan hesaplama
        """
        t = 0
        if _checkers.get(key, 0)<2 and moved_list[key] >= 2:
            t += 2 if key in important_doors else 1

        if _checkers.get(key, 0)>=2 and moved_list[key] < 2:
            t -= 2 if key in important_doors else 1

        if (_checkers.get(key, 0) == 0 or _checkers.get(key, 0) >= 2) and moved_list[key] == 1:
            t -= 1

        if _checkers.get(key, 0) == 1 and (moved_list[key] == 0 or moved_list[key] >= 2):
            t += 1

        return t

    for obj in checkers.keys():
        first_x = obj
        for dice in [dice1, dice2]:
            first_y = first_x + dice
            first_point = (first_x, first_y)
            first_list = checkers.copy()

            first_list[first_x] -= 1
            first_list[first_y] = first_list.get(first_y,0)+1

            first_p1 = get_point(checkers, first_list, first_x)
            first_p1 += get_point(checkers, first_list, first_y)

            # 2. hamle
            last_count = (dice2+dice1) - dice
            for last_x in first_list.keys():
                last_list = first_list.copy()
                last_y = last_x + last_count
                if last_y <= 24:
                    last_point = (last_x, last_y)
                    last_list[last_x] -= 1
                    last_list[last_y] = last_list.get(last_y, 0)+1

                    last_p1 = get_point(first_list, last_list, last_x)
                    last_p1 += get_point(first_list, last_list, last_y)

                    if first_p1+last_p1>0:
                        # print("first_point %s puan:%s, last_point %s, puan:%s toplam:%s" % (first_point, first_p1, last_point, last_p1, (first_p1+last_p2)))
                        res_list.append((first_point, last_point, (first_p1+last_p1)))

    return tuple(res_list)

checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1 }
print(find_moves(checkers, 6, 1))

