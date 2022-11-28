from random import randint


def gana_rebote_1(stat1, stat2):
    prob = 100 * stat1["offReb"] / (stat1["offReb"] + stat2["defReb"])
    r = randint(1, 100)
    if r < prob:
        return True
    else:
        return False


def gana_rebote_2(stat1, stat2):
    prob = 100 * stat2["offReb"] / (stat2["offReb"] + stat1["defReb"])
    r = randint(1, 100)
    if r < prob:
        return True
    else:
        return False


def simular_partido(stat1, stat2):
    points = [0, 0]
    posetion_1 = True
    for i in range(0, 200):
        if posetion_1 == True:
            r = randint(1, 100)
            if r < stat2["steals"]:
                posetion_1 = False
            else:
                r1 = randint(1, 100)
                r2 = randint(1, 100)
                if r1 < stat1["tpa"]:
                    if r2 < stat1["tpp"]:
                        points[0] = points[0] + 3
                        posetion_1 = False
                    else:
                        posetion_1 = gana_rebote_1(stat1, stat2)
                else:
                    r1 = randint(1, 100)
                    r2 = randint(1, 100)
                    r3 = randint(1, 100)
                    r4 = randint(1, 100)
                    r5 = randint(1, 100)
                    if r1 < stat2["pFouls"]:
                        posetion_1 = False
                        if r2 < stat1["ftp"]:
                            points[0] = points[0] + 1
                        if r3 < stat1["ftp"]:
                            points[0] = points[0] + 1
                    else:
                        if r4 < stat1["fga"]:
                            if r5 < stat1["fgp"]:
                                points[0] = points[0] + 2
                                posetion_1 = False
                            else:
                                posetion_1 = gana_rebote_1(stat1, stat2)
                        else:
                            posetion_1 = False

        else:
            r = randint(1, 100)
            if r < stat1["steals"]:
                posetion_1 = True
            else:
                r1 = randint(1, 100)
                r2 = randint(1, 100)
                if r1 < stat2["tpa"]:
                    if r2 < stat2["tpp"]:
                        points[1] = points[1] + 3
                        posetion_1 = True
                    else:
                        posetion_1 = not gana_rebote_2(stat1, stat2)
                else:
                    r1 = randint(1, 100)
                    r2 = randint(1, 100)
                    r3 = randint(1, 100)
                    r4 = randint(1, 100)
                    r5 = randint(1, 100)
                    if r1 < stat1["pFouls"]:
                        posetion_1 = True
                        if r2 < stat2["ftp"]:
                            points[1] = points[1] + 1
                        if r3 < stat2["ftp"]:
                            points[1] = points[1] + 1
                    else:
                        if r4 < stat2["fga"]:
                            if r5 < stat2["fgp"]:
                                points[1] = points[1] + 2
                                posetion_1 = True
                            else:
                                posetion_1 = not gana_rebote_2(stat1, stat2)
                        else:
                            posetion_1 = True
    points[0] += (points[0] * 0.01)
    return points


def eval_winner(stat_home, stat_visitor):
    home = {
        "fga": stat_home.fga / stat_home.games,
        "fgp": stat_home.fgp,
        "ftp": stat_home.ftp,
        "tpa": stat_home.tpa / stat_home.games,
        "tpp": stat_home.tpp,
        "offReb": stat_home.offReb / stat_home.games,
        "defReb": stat_home.defReb / stat_home.games,
        "pFouls": stat_home.pFouls / stat_home.games,
        "steals": stat_home.steals / stat_home.games,
    }

    visitor = {
        "fga": stat_visitor.fga / stat_visitor.games,
        "fgp": stat_visitor.fgp,
        "ftp": stat_visitor.ftp,
        "tpa": stat_visitor.tpa / stat_visitor.games,
        "tpp": stat_visitor.tpp,
        "offReb": stat_visitor.offReb / stat_visitor.games,
        "defReb": stat_visitor.defReb / stat_visitor.games,
        "pFouls": stat_visitor.pFouls / stat_visitor.games,
        "steals": stat_visitor.steals / stat_visitor.games,
    }

    winner, home_percentage, visitor_percentage = victoria(home, visitor)

    return winner, home_percentage, visitor_percentage


def victoria(stat1, stat2):
    victoria_local = 0
    empate = 0
    victoria_visitante = 0
    for i in range(0, 1000):
        if simular_partido(stat1, stat2)[0] > simular_partido(stat1, stat2)[1]:
            victoria_local += 1
        elif simular_partido(stat1, stat2)[0] == simular_partido(stat1, stat2)[1]:
            empate += 1
        else:
            victoria_visitante += 1

    if victoria_local == victoria_visitante:
        return None

    home_percentage = (victoria_local / (victoria_local + victoria_visitante)) * 100
    visitor_percentage = (
        victoria_visitante / (victoria_local + victoria_visitante)
    ) * 100

    return victoria_local > victoria_visitante, home_percentage, visitor_percentage
