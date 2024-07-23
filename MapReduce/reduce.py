import sys
from collections import defaultdict

class WordCountReducer:
    def __init__(self):
        # 用于存储中间的键值对
        self.intermediate = defaultdict(list)
    
    def reduce(self, key, values):
        # 将接收到的值累加到对应的键
        self.intermediate[key].extend(values)
    
    def finalize(self):
        # 计算每个键的总和并打印结果
        for key, counts in self.intermediate.items():
            total_count = sum(counts)
            print(f"{key}\t{total_count}")

if __name__ == "__main__":
    reducer = WordCountReducer()
    
    for line in sys.stdin:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            key, value = parts
            count = int(value)  # 将字符串转换为整数
            reducer.reduce(key, [count])  # 将键和值列表传递给reduce方法
    
    reducer.finalize()  # 完成所有reduce操作后，调用finalize来打印最终结果