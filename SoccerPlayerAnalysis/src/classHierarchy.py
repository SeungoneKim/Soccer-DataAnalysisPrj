class Player:

    def __init__(self, name, position, EstimatedValue, currentClub, Nationality, age):
        self.name = name
        self.position = position
        self.EstimatedValue = EstimatedValue
        self.currentClub = currentClub
        self.Nationality = Nationality
        self.age = age

        self.data = []
        self.avgdata = []


    # getter methods
    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getEstimatedValue(self):
        return self.EstimatedValue

    def getCurrentClub(self):
        return self.currentClub

    def getNationality(self):
        return self.Nationality

    def getAge(self):
        return self.age
        
    def getdata(self,season,info):
        return self.data[season][info]
        
    def addSeason(self,seasoninfo):
        self.data.append(seasoninfo)
    
    def makeAvgData(self):
        for idx in range(0,4):
            self.avgdata.append(self.data[0][idx])
        for idx in range(4,len(self.data[0])):
            tmpsum=0.0
            num=0
            flg = False
            for addidx in range(len(self.data)):
                if self.data[addidx][idx]!='-' and self.data[addidx][idx]!='':
                    if self.data[addidx][idx][-1]!='%':
                        tmpsum = tmpsum+ float(self.data[addidx][idx])
                    else:
                        tmpsum = tmpsum+ float(self.data[addidx][idx][:-1])
                        flg=True
                    num = num+1
            if num!=0:
                if flg is False:
                    self.avgdata.append(str(tmpsum/num))
                else:
                    self.avgdata.append(str(tmpsum/num)+'%')
            else:
                self.avgdata.append('-')
  
            
    def getInfoFromAvgData(self,idx):
        return self.avgdata[idx]
