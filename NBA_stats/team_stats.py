class Team_stats (object):


    def __init__(self, stat) -> None:
        
        self.games = stat["games"]
        self.fastBreakPoints = float(stat["fastBreakPoints"])
        self.pointsInPaint = float(stat["pointsInPaint"])
        self.biggestLead = float(stat["biggestLead"])
        self.secondChancePoints = float(stat["secondChancePoints"])
        self.pointsOffTurnovers = float(stat["pointsOffTurnovers"])
        self.longestRun = float(stat["longestRun"])
        self.points = stat["points"]
        self.fgm = int(stat["fgm"])
        self.fga = int(stat["fga"])
        self.fgp = float(stat["fgp"])
        self.ftm = int(stat["ftm"])
        self.fta = int(stat["fta"])
        self.ftp = float(stat["ftp"])
        self.tpm = int(stat["tpm"])
        self.tpa = int(stat["tpa"])
        self.tpp = float(stat["tpp"])
        self.offReb = float(stat["offReb"])
        self.defReb = float(stat["defReb"])
        self.totReb = float(stat["totReb"])
        self.assists = int(stat["assists"])
        self.pFouls = float(stat["pFouls"])
        self.steals = int(stat["steals"])
        self.turnovers = float(stat["turnovers"])
        self.blocks = stat["blocks"]
        self.plusMinus = float(stat["plusMinus"])