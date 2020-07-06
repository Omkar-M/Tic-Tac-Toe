# the list "students" is already defined
students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]

print([x[0] for x in students if x[1] == 'A'])
