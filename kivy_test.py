# coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

class calc(BoxLayout):
    def __init__(self, **kwargs):
        super(calc, self).__init__(**kwargs)
        self.value = ""
    def addition(self,array):
        if "+" in array:
            sil = []
            index_multi = array.index('+')
            sil.append(index_multi)
            num_1 = ""
            counter = index_multi -1
            array_2 = []
            while counter > -1 :
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        array_2.append(array[counter])
                        counter -= 1
                    else:
                        if (str(type(float(array[counter]))) == "<class 'float'>"):
                            sil.append(counter)
                            array_2.append(array[counter])
                            counter -= 1
                        else:
                            counter = -1
                except:
                    counter = -1
            for i in range(len(array_2) -1 , -1,-1):
                num_1 =   num_1 + str(array_2[i])
            counter = index_multi + 1
            num_2 = ""

            while counter != -1:
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        num_2 = num_2 + str(array[counter])
                        array_2.append(array[counter])
                        counter += 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            num_2 = num_2 + str(array[counter])
                            counter += 1
                        else:
                            counter = -1
                except:
                    counter = -1
            enK = min(sil)
            sil =  sorted(sil, reverse=True)
            for i in sil:
                del array[i]
            ans = str(float(num_1) + float(num_2))
            array.insert(enK,ans)
            return array
    def subtraction(self,array):
        if "-" in array:
            sil = []
            index_multi = array.index('-')
            sil.append(index_multi)
            num_1 = ""
            counter = index_multi -1
            array_2 = []
            while counter > -1 :
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        array_2.append(array[counter])
                        counter -= 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            array_2.append(array[counter])
                            counter -= 1
                        else:
                            counter = -1
                except:
                    counter = -1
            for i in range(len(array_2) -1 , -1,-1):
                num_1 =  num_1 + str(array_2[i])
            counter = index_multi + 1
            num_2 = ""
            while counter != -1:
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        num_2 = num_2 + str(array[counter])
                        array_2.append(array[counter])
                        counter += 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            num_2 = num_2 + str(array[counter])
                            counter += 1
                        else:
                            counter = -1
                except:
                    counter = -1
            enK = min(sil)
            sil =  sorted(sil, reverse=True)
            for i in sil:
                del array[i]
            ans = str(float(num_1) - float(num_2))
            array.insert(enK,ans)
            return array
    def multiplication(self,array):
        if "x" in array:
            sil = []
            index_multi = array.index('x')
            sil.append(index_multi)
            num_1 = ""
            counter = index_multi -1
            array_2 = []
            while counter > -1 :
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        array_2.append(array[counter])
                        counter -= 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            array_2.append(array[counter])
                            counter -= 1
                        else:
                            counter = -1
                except:
                    counter = -1
            for i in range(len(array_2) -1 , -1,-1):
                num_1 =  num_1 + str(array_2[i])
            counter = index_multi + 1

            num_2 = ""
            while counter != -1:
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        num_2 = num_2 + str(array[counter])
                        array_2.append(array[counter])
                        counter += 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            num_2 = num_2 + str(array[counter])
                            counter += 1
                        else:
                            counter = -1
                except:
                    counter = -1
            enK = min(sil)
            sil =  sorted(sil, reverse=True)
            for i in sil:
                del array[i]
            ans = str(float(num_1) * float(num_2))
            array.insert(enK,ans)
            return array
    def division(self,array):
        if "/" in array:
            sil = []
            index_multi = array.index('/')
            sil.append(index_multi)
            num_1 = ""
            counter = index_multi -1
            array_2 = []
            while counter > -1 :
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        array_2.append(array[counter])
                        counter -= 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            array_2.append(array[counter])
                            counter -= 1
                        else:
                            counter = -1
                except:
                    counter = -1
            for i in range(len(array_2) -1 , -1,-1):
                num_1 = num_1 + str(array_2[i])
            counter = index_multi + 1
            num_2 = ""
            while counter != -1:
                try:
                    if array[counter] == ".":
                        sil.append(counter)
                        num_2 = num_2 + str(array[counter])

                        array_2.append(array[counter])
                        counter += 1
                    else:
                        if str(type(float(array[counter]))) == "<class 'float'>":
                            sil.append(counter)
                            num_2 = num_2 + str(array[counter])
                            counter += 1
                        else:
                            counter = -1
                except:
                    counter = -1
            try:
                enK = min(sil)
                sil =  sorted(sil, reverse=True)
                for i in sil:
                    del array[i]
                ans = str(float(num_1) / float(num_2))
                array.insert(enK,ans)
                return array
            except :
                return ["division by zero"]
    def process(self,value):
        array = []
        for i in self.value:
            array.append(i)
        reco_array = array
        syc = 0
        empty = []
        process_mul_div = []
        process_add_sub = []
        for i in reco_array:
            if i == "x" or i == "/":
                empty.append(syc)
                process_mul_div.append(i)
            if i == "+" or i == "-":
                process_add_sub.append(i)
            syc += 1

        for i in process_mul_div:
            if i == "x":
                array = self.multiplication(array)
            if i == "/":
                x = self.division(array)
        for i in process_add_sub:
            if i == "+":
                array = self.addition(array)
            if i == "-":
                array = self.subtraction(array)


        ans = array[0]
        reco = self.value
        self.value = ""
        self.ids['screen'].text = reco + "=" + str(ans)
    def enter_button(self,value):
        if value.isnumeric() or value == ".":
            self.value = str(self.value) + (value)
            self.ids['screen'].text = self.value
        elif value == "about":
            self.value = ""
            self.ids['screen'].text =  "author by Ercan Sezdi"
        elif value == "C":
            self.value = ""
            self.ids['screen'].text = self.value
        elif value == "/":
            self.value = str(self.value) + str(value)
            self.ids['screen'].text = self.value
        elif value == "x":
            self.value = str(self.value) + str(value)
            self.ids['screen'].text = self.value
        elif value == "-":
            self.value = str(self.value) + str(value)
            self.ids['screen'].text = self.value
        elif value == "+":
            self.value = str(self.value) + str(value)
            self.ids['screen'].text = self.value
        elif value == "<":
            array = []
            for i in self.value:
                if i != " ":
                    array.append(i)
            self.value = ""
            for i in range(0,len(array)-1):
                if array[i] == "/" or array[i] == "X" or array[i] == "+" or array[i] == "-":
                    self.value = self.value + str(array[i])
                else:
                    self.value = self.value  + str(array[i])
            self.ids['screen'].text = self.value
        else:
            pass


class calcstart(App):
    def build(self):
        return calc()


if __name__ == "__main__":
    calcstart().run()
