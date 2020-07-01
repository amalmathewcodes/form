class Result:
    def mark(self,pysics,chemistry,maths):
        self.pysics = pysics
        self.chemistry = chemistry
        self.maths = maths

    def percent(self):
        percent = (self.pysics + self.maths + self.chemistry ) * 100 / 300
        return percent
        if( persent >= 90):
            print("student will be achived into distingtion")
        
    



x = Result()
x.mark(67, 96, 78)
print(x.percent())
