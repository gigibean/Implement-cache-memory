class Memory:
    hit = 0 #hit를 0으로 초기화함
    total_hit = 0 #total_hit를 0으로 초기화함
    total_time = 0 #total_time 최종 접근시간

    def __init__(self, name, size, time, lower_memory=None): #초기화를 통해 name,size,time,lower_memory를 생성해줌
        self.name = name
        self.MEMORY_SIZE = size
        self.ACCESS_TIME = time
        self.memory = []
        self.lower_memory = lower_memory

    def get(self, data):
        if data in self.memory: #데이터가 캐시, 램, 디스크에 있는지의 유무를 확인하여 줌
            Memory.total_hit += 1
            Memory.total_time += self.ACCESS_TIME
            if self.name == 'L1' or self.name == "L2" or self.name == 'L3': #데이터가 캐시 L1,L2,L3에 있는지의 유무를 확인하여줌
                Memory.hit += 1 #데이터가 캐시 안에 있으면 1을 더하여 줌
            return data, self.ACCESS_TIME #데이터 값과 접근시간을 리턴해 줌
        else:
            if self.lower_memory is None: #메모리에 데이터가 있는지의 유무를 확인하여 줌 
                raise ValueError('There is not {} in {}.'.format(data, self.name)) #데이터가 메모리에 없는 경우 예외처리를 해줌
            data, time = self.lower_memory.get(data) #메모리에 데이터가 없기 때문에 하드디스크에서 데이터를 가지고 옴
            if len(self.memory) == self.MEMORY_SIZE: #가지고 온 데이터를 캐시 L3, L2, L1 순으로 메모리 사이즈를 확인한 후 넣어줌
                self.memory.pop(0) #사이즈를 확인하고 차있는 경우 pop을 통해 삭제함 
            self.memory.append(data) #그렇지 않다면 데이터를 넣어줌 
            return data, time + self.ACCESS_TIME #데이터 값과 접근시간을 리턴해 줌

    def data_init(self):
        self.memory = list(range(self.MEMORY_SIZE)) #메모리 사이즈의 크기만큼 리스트를 생성해줌
