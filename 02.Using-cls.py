class Counter:
    count = 0  

    def __init__(self):
      
        Counter.count += 1

    @classmethod
    def get_count(cls):
       
        print(f"Number of Counter instances created: {cls.count}")

a = Counter()
b = Counter()
c = Counter()


Counter.get_count()  
