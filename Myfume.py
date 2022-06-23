#from curses import window
from ast import Lambda
from turtle import window_width
from unicodedata import name
import mysql.connector
import tkinter
import tkinter.messagebox
import customtkinter
from tabulate import tabulate
from tkinter import *


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Changingseasons1!",
    database="Myfume"
)

mycursor = db.cursor()
#perfume
#mycursor.execute("CREATE TABLE perfume(perfume_id int UNIQUE NOT NULL AUTO_INCREMENT, perfume_name varchar(100), price int, rating_score int(10), brand_in_id int, type_in_id int, user_in_id int, PRIMARY KEY(perfume_id), FOREIGN KEY(brand_in_id) REFERENCES brand(brand_id), FOREIGN KEY(type_in_id) REFERENCES type(type_id), FOREIGN KEY(user_in_id) REFERENCES user(user_id))")

# mycursor.execute("INSERT INTO type (type_name, type_rating) VALUES (%s,%s)", ("Digity Brand", 11))
# db.commit()
#https://us04web.zoom.us/j/73102936828?pwd=x3LPj7xLY0aodGcOeDyc4dT46S3nE.1 Failed Grandma Stream
# to get in to mongodb ./mongo
#db.restaurants.find({ $or:[{no_franchises:{$gt: 10000}}, {no_franchises:{$lt: 100}}]}).pretty() restaurants greater than 10000, less than 100
# db.restaurants.find({no_franchises:{$gt:500}}).pretty() restaurants greater than 500
# db.restaurants.find({dishes:{$regex:"Burrito"}}).pretty() restaurants that serve burritos
# db.restaurants.updateOne({name: "McDonald's"}, {$push:{dishes: "Egg McMuffin"}})
# db.restaurants.updateOne({name: "Panda Express"}, {$push:{dishes: "Teriyaki Chicken"}})

#def addATypeTest(mycursor):
#    mycursor.execute("INSERT INTO type (type_name, type_rating) VALUES (%s,%s)", ("Other Button Brand", 1))
#    db.commit()

#def addABrandTest(mycursor):
#    mycursor.execute("INSERT INTO brand (brand_name, brand_rating) VALUES (%s,%s)", ("Raisin Brand", 8))
#    db.commit()

#def addAUserTest(mycursor):
#    mycursor.execute("INSERT INTO user (username, password) VALUES (%s,%s)", ("Ted Sheckler", "password"))
#    db.commit()

def testOfAllTests(mycursor, testyGuy):  # outdated, to be removed
            x = [testyGuy.get()]
            mycursor.execute("INSERT INTO type (type_name) VALUE (%s)", (x))
            db.commit()

def addATypeTest(mycursor, testyGuy):
    x = [testyGuy.get()]
    mycursor.execute("INSERT INTO type (type_name) VALUE (%s)", (x))
    db.commit()

def addABrandTest(mycursor, testyGuy):
    x = [testyGuy.get()]
    mycursor.execute("INSERT INTO brand (brand_name) VALUE (%s)", (x))
    db.commit()

def addAPerfumeTest(mycursor, nameCondition):
    x = [nameCondition.get()]
    mycursor.execute("INSERT INTO perfume (perfume_name) VALUE (%s)", (x))
    db.commit()

def updater(mycursor, testyGuy, nameCondition):
    mycursor.execute("UPDATE perfume SET perfume_name = (%s) WHERE perfume_name = (%s)", (testyGuy.get(),nameCondition.get()))
    db.commit()
    
def deletePerfume(mycursor, testyGuy):
    x = [testyGuy.get()]
    mycursor.execute("DELETE FROM perfume WHERE perfume_name = (%s)", (x))
    db.commit()
    
def deleteBrand(mycursor, testyGuy):
    x = [testyGuy.get()]
    mycursor.execute("DELETE FROM brand WHERE brand_name = (%s)", (x))
    db.commit()

def deleteType(mycursor, testyGuy):
    x = [testyGuy.get()]
    mycursor.execute("DELETE FROM type WHERE type_name = (%s)", (x))
    db.commit()

def FkAdderBrandIn(mycursor, testyGuy, nameCondition):
    #x = [testyGuy.get()]
    #y = [nameCondition.get()]
    mycursor.execute("UPDATE perfume SET brand_in_id  = (%s) WHERE perfume_name = (%s)", (testyGuy.get(),nameCondition.get()))
    db.commit()

def FkAdderTypeIn(mycursor, testyGuy, nameCondition):
    #x = [testyGuy.get()]
    #y = [nameCondition.get()]
    mycursor.execute("UPDATE perfume SET type_in_id  = (%s) WHERE perfume_name = (%s)", (testyGuy.get(),nameCondition.get()))
    db.commit()

#def showType(mycursor):
#    mycursor.execute("SELECT * FROM type")
#    myresult = mycursor.fetchall()
#    print(tabulate(myresult, headers=['ID','Name','Rating'], tablefmt='psql'))
#    win = tabulate(myresult, headers=['ID','Name','Rating'], tablefmt='psql')
#    return win
    

#def showBrand(mycursor):
#    mycursor.execute("SELECT * FROM brand")
#    myresult = mycursor.fetchall()
#    print(tabulate(myresult, headers=['ID','Name','Rating'], tablefmt='psql'))

#def showPerfume(mycursor):
#    mycursor.execute("SELECT * FROM perfume")
#    myresult = mycursor.fetchall()
#    print(tabulate(myresult, headers=['ID','Name','Price','Rating','Brand ID','Type ID','User ID'], tablefmt='psql'))
#mycursor.execute("SELECT * FROM perfume")
#myresult = mycursor.fetchall()
#my_text = tabulate(myresult, headers=['ID','Name','Price','Rating','Brand ID','Type ID','User ID'], tablefmt='psql')

my_text = ""

def showPerfume(mycursor, testFrame, self):
    mycursor.execute("SELECT * FROM perfume")
    myresult = mycursor.fetchall()
    global my_text 
    my_text = tabulate(myresult, headers=['ID','Name','Price','Rating','Brand ID','Type ID','User ID']) #rst,
    testFrame.label_info_1.config(text = my_text)
    #self.label_info_1.config(text= my_text)
    print(tabulate(myresult, headers=['ID','Name','Price','Rating','Brand ID','Type ID','User ID'], tablefmt='psql'))

def showBrand(mycursor, testFrame):
    mycursor.execute("SELECT * FROM brand")
    myresult = mycursor.fetchall()
    global my_text 
    my_text = tabulate(myresult, headers=['ID','Name','Rating'])
    testFrame.label_info_1.config(text = my_text)
    print(tabulate(myresult, headers=['ID','Name','Rating'], tablefmt='psql'))

def showType(mycursor, testFrame):
    mycursor.execute("SELECT * FROM type")
    myresult = mycursor.fetchall()
    global my_text 
    my_text = tabulate(myresult, headers=['ID','Name','Rating'])
    testFrame.label_info_1.config(text = my_text)
    print(tabulate(myresult, headers=['ID','Name','Rating'], tablefmt='psql'))



# Start of GUI


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

#===============================================================================================================
#===================================== START PAGE ==============================================================
#===============================================================================================================
class StartPage(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    

    def __init__(self):
        super().__init__()

        StartPage = Tk()
        self.title("Myfume")
        self.geometry(f"1000x1000")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        


        # ============ variables ============

        testyGuy = StringVar()
        nameCondition = StringVar()

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Ryan's App of Excellence",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Show The Perfume Table",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:[self.button_event, showPerfume(mycursor, testFrame, self)])
                                                
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Show The Brand Table",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:[self.button_event, showBrand(mycursor, testFrame)])
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Show The Type Table",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:[self.button_event, showType(mycursor, testFrame)])
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add a Perfume Type Foreign Key",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:[self.button_event, FkAdderTypeIn(mycursor, testyGuy, nameCondition)])
        self.button_4.grid(row=6, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add a Perfume Brand Foreign Key",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:[self.button_event, FkAdderBrandIn(mycursor, testyGuy, nameCondition)])
        self.button_5.grid(row=7, column=0, pady=10, padx=20)


        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")



        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(13, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)            

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        testFrame = customtkinter.CTkFrame(master=StartPage, width=600, height=600, corner_radius=10)
        testFrame.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        #testFrame.entry = customtkinter.CTkEntry(master=testFrame,
        #                                         placeholder_text="Feed Me Words",
        #                                         width=120,
        #                                         height=25,
        #                                         border_width=2,
        #                                         corner_radius=10)
        #testFrame.entry.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
        testFrame.label_info_1 = customtkinter.CTkLabel(master=testFrame,
                                                   text= my_text,
                                                   height=300,
                                                   width=600,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        testFrame.label_info_1.grid(column=0, row=0, sticky="w", padx=15, pady=15)



        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   # text=my_text,
                                                   text="Welcome To Myfume!\n" +
                                                        "The Perfume Collecting Database,\n" +
                                                        "Where you can store all of your perfumes!" ,
                                                   height=100,
                                                   width=500,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        scroll_bar = tkinter.Scrollbar(self.frame_info)
        scroll_bar.pack
        #self.frame_info_1 = customtkinter.CTkEntry(master=self.frame_info,
        #                                           text=my_text,
        #                                           state='readonly',
        #                                           height=100,
        #                                           width=500,
        #                                           fg_color=("white", "gray38"),  # <- custom tuple-color
        #                                           justify=tkinter.LEFT)
        #self.frame_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    #    self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
    #    self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

 #       self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
   #                                                     text="What Coulmn Would You Like To Select:")
  #      self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

     #   self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
     #                                                      variable=self.radio_var,
     #                                                      text="Type",
     #                                                      value=0,
     #                                                      command=clicked)
     #   self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

     #   self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
     #                                                      variable=self.radio_var,
     #                                                      text="Brand",
     #                                                      value=1,
     #                                                      command=lambda: clicked(self.value.get()))
     #   self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

#        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
#                                                           variable=self.radio_var,
#                                                           text="Perfume",
#                                                           value=2,
#                                                           command=lambda: clicked(self.value.get()))
#        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

#        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
#                                                from_=0,
#                                                to=1,
#                                                number_of_steps=3,
#                                                command=self.progressbar.set)
 #       self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

  #      self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
   #                                             command=self.progressbar.set)
   #     self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

#        self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
 #                                                      height=25,
  #                                                     text="CTkButton",
   #                                                    command=self.button_event)
    #    self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

  #      self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
   #                                                    height=25,
    #                                                   text="CTkButton",
     #                                                  command=self.button_event)
#        self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Submit To Type",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, addATypeTest(mycursor, testyGuy)])
        self.checkbox_button_1.grid(row=3, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Submit To Brand",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, addABrandTest(mycursor, testyGuy)])
        self.checkbox_button_2.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Submit To Perfume",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, addAPerfumeTest(mycursor, testyGuy)])
        self.checkbox_button_3.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_4 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Submit A Perfume Name To Change",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, updater(mycursor, testyGuy, nameCondition)])
        self.checkbox_button_4.grid(row=7, column=2, columnspan=1, pady=100, padx=20, sticky="we")

        self.checkbox_button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Delete A Type",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, deleteType(mycursor, testyGuy)])
        self.checkbox_button_5.grid(row=10, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Delete A Brand",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, deleteBrand(mycursor, testyGuy)])
        self.checkbox_button_6.grid(row=11, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_7 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Delete A Perfume",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=lambda:[self.button_event, deletePerfume(mycursor, testyGuy)])
        self.checkbox_button_7.grid(row=12, column=2, columnspan=1, pady=10, padx=20, sticky="we")

     #   self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
    #                                                 text="CTkCheckBox")
   #     self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

       # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
      #                                              text="CTkCheckBox")
     #   self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry_type_name = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Please Enter A Name You Would Like To Add/ Foreign Key Value",
                                            textvariable=testyGuy)
        self.entry_type_name.grid(row=13, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.entry_type_name_two = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Please Enter A Type Name You Would Like To Change/ Foreign Key Name",
                                            textvariable=nameCondition)
        self.entry_type_name_two.grid(row=14, column=0, columnspan=2, pady=10, padx=20, sticky="we")

  #      self.button_submit = customtkinter.CTkButton(master=self.frame_right,
  #                                              text="Submit",
  #                                              command=lambda:[self.button_event, hearOfTheProg(case, mycursor, testyGuy)])
  #      self.button_submit.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")


        # set default values
       # self.radio_button_1.select()
        self.switch_2.select()
     #   self.slider_1.set(0.2)
     #   self.slider_2.set(0.7)
    #    self.progressbar.set(0.5)
        #self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        #self.radio_button_3.configure(state=tkinter.DISABLED)
        #self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
     #   self.check_box_2.select()
       
    
    
        

    def button_event(self):
        print("Button pressed")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    


if __name__ == "__main__":
    startPage = StartPage()
    startPage.mainloop()

#End of GUI