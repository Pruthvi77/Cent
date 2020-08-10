class area_triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5
        return self.area

a, b, c = input("a = "), input("b = "), input("c = ")

t = area_triangle(a, b, c)
print("area : {}".format(t.calculate_area()))


def filter_list(input_list, number):
    return (x for x in input_list if len(x) > number)

list1 = input("Enter some words here as input with comma(,) seperate: ")
number = input("Enter number to filter based on length of words: ")
n = int(number)
list_split = list1.split(",")

print(list(filter_list(list_split ,n)))



list_words = ['one','two','three','four','five','six','seven']
list_count = [len(i) for i in list_words]
print("Length of each word in a list -->",list_count)



def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels

print("Is 'c' is a vowel -->",is_vowel('c'))
print("Is 'e' is a vowel -->",is_vowel('e'))
