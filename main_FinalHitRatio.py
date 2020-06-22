from memory import Memory
from cpu import Cpu
import random
import matplotlib.pyplot as plt

hdd = Memory('HDD', 5000, 3.)
hdd.data_init()
# 캐시 메모리가 l1만 있을 때 -> l1의 lower_memory = ram
ram = Memory('RAM', 1000, 1., hdd)
# l3 = Memory('L3', 200, 0.1, ram)
# l2 = Memory('L2', 20, 0.1, l3)
# l1= Memory('L1', 5, 0.1, l2)
l1 = Memory('L1', 5, 0.1, ram)

cpu = Cpu(l1)
for i in range(1000):
    v1 = random.randint(1, 1000)
    v2 = random.randint(1, 1000)
    print("(register 1)", v1, "(register 2)", v2, " = ", cpu.plus(v1, v2))
    print("cache L1 : ", l1.memory)
print("Hit =", Memory.hit)

print('Memory access time of L1, ram, hdd =', round(Memory.total_time,2))
hitRatio1 = Memory.hit / Memory.total_hit
totalTime1 = Memory.total_time

# 캐시 메모리가 l1, l2, l3 3개일 때 -> 각각의 lower_memory는 순차적으로 내려감
# 메모리의 상황이 달라졌기 때문에 다시 초기화한다.
ram = Memory('RAM', 1000, 1., hdd)
l3 = Memory('L3', 200, 0.1, ram)
l2 = Memory('L2', 20, 0.1, l3)
l1 = Memory('L1', 5, 0.1, l2)

cpu = Cpu(l1)

for i in range(1000):
    v1 = random.randint(1, 1000)
    v2 = random.randint(1, 1000)
    print("(register 1)", v1, "(register 2)", v2, " = ", cpu.plus(v1, v2))
    print("cache L1 : ", l1.memory)
    print("cache L2 : ", l2.memory)
    print("cache L3 : ", l3.memory)
print("Hit =", Memory.hit)
print('Memory access time of L1, L2, L3, ram, hdd =', round(Memory.total_time,2))
hitRatio2 = Memory.hit / Memory.total_hit
totalTime2 = Memory.total_time

missRatio1 = 1 - hitRatio1
missRatio2 = 1 - hitRatio2
print("HitRatio L1 : ", hitRatio1, "HitRatio L1, L2, L3 : ", hitRatio2, "MissRatio L1 : ", missRatio1, "MissRatio L1, L2, L3 : ", missRatio2)
plt.bar(["HitRatio L1", "HitRatio L1, L2, L3"], [hitRatio1, hitRatio2])
plt.show()
plt.bar(["MissRatio L1", "MissRatio L1, L2, L3"], [missRatio1, missRatio2])
plt.show()
plt.bar(["Access Time L1", "Access Time L1, L2, L3"], [totalTime1, totalTime2])
plt.show()
