class Widget():
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y
    
    def print_info(self):
        print("інформація про віджет")
        print(self.text,self.x,self.y)
class Button(Widget):
    def __init__(self, text, x, y, is_cklick):
        super().__init__(text, x, y)
        self.is_click = is_click
    
    def click(self):
        print("Молодець")
        self.is_click = True
adolf = Button("Я Адольф", 56,14,False)
adolf.print_info()
a=input("???????????").lower()
if a == "так":
    adolf.click()
else:
    print("Ов ноуууууу")

    