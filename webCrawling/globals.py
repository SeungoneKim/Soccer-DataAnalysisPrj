idxToLeague = ["PremierLeague", "LaLiga", "BundesLiga", "SerieA", "LigueOne"]
idxToSeason = ["17_18", "18_19", "19_20"]
idxToColumnTitle = {0: "Name", 1: "TeamName", 2: "Nationality", 5: "Age", 7: "PlayedTime", 8: "Goals", 9: "Assists",
               10: "YellowCards", 11: "RedCards", 14: "TacklesWon", 15: "AerialsWon", 16: "DuelsWon", 17: "ClearancesP90",
               22: "TouchesP90", 23: "InterceptP90", 26: "PassesP90", 27: "PassesCompleted",
               30: "AssistsP90", 31: "BigChances", 32: "DribblesP90", 33: "CrossesP90", 34: "PenaltyGoals", 35: "ShotsP90", 36: "TargetShotsP90",
               43: "CleanSheets", 44: "SavesMade", 47: "PenaltySaves", 48: "MOM", 49: "GoalsP90",
               50: "NonPenaltyGoalsP90", 51: "ShotsAccuracy", 56: "AvgRating"}
ColumnListforSoccerData = {0: "PlayedTime", 1: "Goals", 2: "Assists",
               3: "YellowCards", 4: "RedCards", 5: "TacklesWon", 6: "AerialsWon", 7: "DuelsWon", 8: "ClearancesP90",
               9: "TouchesP90", 10: "InterceptP90", 11: "PassesP90", 12: "PassesCompleted",
               13: "AssistsP90", 14: "BigChances", 15: "DribblesP90", 16: "CrossesP90", 17: "PenaltyGoals", 18: "ShotsP90", 19: "TargetShotsP90",
               20: "CleanSheets", 21: "SavesMade", 22: "PenaltySaves", 23: "MOM", 24: "GoalsP90",
               25: "NonPenaltyGoalsP90", 26: "ShotsAccuracy", 27: "AvgRating"}
playernum = [213,139,175,183,155]
firstkey = [0,215,356,533,718]

ColumnsforStriker = {0: "PlayedTime", 1: "Goals", 2: "Assists",
               3: "YellowCards", 4: "RedCards", 13: "AssistsP90", 14: "BigChances",17: "PenaltyGoals", 
               18: "ShotsP90", 19: "TargetShotsP90",23: "MOM", 24: "GoalsP90",25: "NonPenaltyGoalsP90", 
               26: "ShotsAccuracy", 27: "AvgRating"}

ColumnsforMidfielder = {0: "PlayedTime", 2: "Assists",
               3: "YellowCards", 4: "RedCards",9: "TouchesP90", 10: "InterceptP90", 11: "PassesP90", 12: "PassesCompleted",
               13: "AssistsP90", 14: "BigChances", 15: "DribblesP90", 16: "CrossesP90",23: "MOM", 24: "GoalsP90",27: "AvgRating"}

ColumnsforDefender = {0: "PlayedTime", 3: "YellowCards", 4: "RedCards", 5: "TacklesWon", 6: "AerialsWon", 7: "DuelsWon", 8: "ClearancesP90",
                    9: "TouchesP90", 10: "InterceptP90",23: "MOM",27: "AvgRating"}

ColumnsforGoalkeeper = {0: "PlayedTime", 3: "YellowCards", 4: "RedCards",
                    20: "CleanSheets", 21: "SavesMade", 22: "PenaltySaves", 23: "MOM",27: "AvgRating"}


StrikerPositions = {"SecondStriker","Centre-Forward","AttackingMidfield"}

MidfielderPositions = {"RightWinger","RightMidfield","Midfield","LeftWinger","LeftMidfield","CentralMidfield","Winger"}

DefenderPositions = {"Right-Back","Left-Back","DefensiveMidfield","Centre-Back"}

GoalkeeperPositions = {"Goalkeeper"}