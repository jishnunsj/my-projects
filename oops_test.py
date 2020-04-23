class my_details:
    def __init__(self):
        self.name = "blah"
        self.age = "14"

p1 = my_details()
p2 = my_details()

p1.name = "blah_2"

print(p1.name)