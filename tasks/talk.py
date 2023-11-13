class Talking:
    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.answer = True

    def to_answer(self):
        if self.answer:
            self.yes_count += 1
            self.answer = False
            return 'moore-moore'
        else:
            self.no_count += 1
            self.answer = True
            return 'meow-meow'

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count






tk = Talking('Pussy')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no“ {tk1.number_no()} times')