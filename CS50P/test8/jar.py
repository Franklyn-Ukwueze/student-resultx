class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity 
        self.cookie_jar = [] 

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        for _ in range(n):
            self.cookie_jar.append("🍪")
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        for _ in range(n):
            self.cookie_jar.pop()
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return len(self.cookie_jar)

jar = Jar()

jar.deposit(5)
print(jar)
jar.withdraw(2)
print(jar)