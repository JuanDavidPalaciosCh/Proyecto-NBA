class Team_stats (object):


    def __init__(self, stat) -> None:
        
        self.games = stat["games"]
        self.fastBreakPoints = stat["fastBreakPoints"]
        self.pointsInPaint = stat["pointsInPaint"] #inutil
        self.biggestLead = stat["biggestLead"] 
        self.secondChancePoints = stat["secondChancePoints"]
        self.pointsOffTurnovers = stat["pointsOffTurnovers"]
        self.longestRun = stat["longestRun"]
        self.points = stat["points"]
        self.fgm =stat["fgm"]
        self.fga = stat["fga"]
        self.fgp = stat["fgp"]
        self.ftm = stat["ftm"]
        self.fta = stat["fta"]
        self.ftp = stat["ftp"]
        self.tpm = stat["tpm"]
        self.tpa = stat["tpa"]
        self.tpp = stat["tpp"]
        self.offReb = stat["offReb"]
        self.defReb = stat["defReb"]
        self.totReb = stat["totReb"]
        self.assists = stat["assists"]
        self.pFouls = stat["pFouls"]
        self.steals = stat["steals"]
        self.turnovers =stat["turnovers"]
        self.blocks = stat["blocks"]
        self.plusMinus = stat["plusMinus"]