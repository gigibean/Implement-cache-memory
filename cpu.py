from memory import Memory #memory를 import함

class Cpu: #연산수행
    def __init__(self,L1): #초기화를 통해 레지스터 2개를 설치함
        self.R1=0
        self.R2=0
        self.L1 = L1
    def plus(self, operand1, operand2): #덧셈연산을 수행하는 함수
        self.R1, time1 = self.L1.get(operand1) #R1(근원지겸 목적지 레지스터)에 값을 추가
        self.R2, time2 = self.L1.get(operand2) #R2에(근원지 레지스터)에 값을 추가
        print("(access time) ", round(time1, 2), " , (access time) ", round(time2, 2)) #각 데이터 접근시간을 구함(round()함수를 통해 반올림)
        self.R1 += self.R2 #R1 = R1 + R2
        #print("(register 1) ", self.R1, " + (register 2) ", self.R2, " = (result) ", self.R1 + self.R2)
        return self.R1
