from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import requests
import urllib.request
import io
import pandas
import json
import sys
import os

#csv
csv = pandas.read_csv("userdata.csv")
df = pandas.DataFrame(csv)
# Save DataFrame to a CSV file
df.to_csv('userdata.csv', index=False)

signupname=""
signuppassword=""
arrayOfPokemon = []
arrayOfPokemonnames = []
arrayOfPokemontypes = []
arrayOfPokemontypenames = []
arrayOfPokemon2 = []

#page draw/destroy

def drawPage1():
    widgetArraypack1 = [labellogo,entry1,entry2]    
    for i in widgetArraypack1:
        i.pack()
    
    combo_box.pack()
    sign_up_button.place(x=225,y=200)
    login_button.place(x=425,y=200)
        
    destroyPage2()

def destroyPage1():
    widgetArrayforget1 = [labellogo, sign_up_box, login_box,create_button,login_check_button, entry1,entry2,entry3,entry4]
    for i in widgetArrayforget1:
        i.pack_forget()
        
    placeforget = [sign_up_button,login_button]
    for i in placeforget:
        i.place_forget()
        
def drawPage2():
    widgetArrayforget2 = [labelball,Select_box,entry5,combo_box,pokedex_button,pokemon_selection_box,entry1,entry2]
    for i in widgetArrayforget2:
        i.pack()
    destroyPage1()
    
def destroyPage2():
    widgetArrayforget2 = [labelball,Select_box,entry5,pokedex_button,combo_box,pokemon_selection_box,entry1,entry2]
    for i in widgetArrayforget2:
        i.pack_forget()

#pokedexapi

def retryselection():
    entry5.delete(0, END)
    entry6.delete(0, END)
    for i in arrayOfPokemon:
        i.place_forget()
    for i in arrayOfPokemonnames:
        i.place_forget()
    combo_box.pack_forget()
    exit.place_forget()
    roster.place_forget()
    apibutton1.place_forget()
    pokemon_box.place_forget()
    Select_box2.place_forget()
    entry6.place_forget()
    apibutton1.place_forget()
    apibutton2.place_forget()
    label.place_forget()
    drawPage2()
    
def typedelete():
    for i in arrayOfPokemontypenames:
        i.place_forget()
    for i in arrayOfPokemontypes:
        i.place_forget()
        Select_box.place_forget()
        entry5.place_forget()
        pokedex_button2.place_forget()
        combo_box.set("single pokemon")
        pokedexapi()

def pokedexapi():
    if combo_box.get() != "" and combo_box.get() != "single pokemon":
        selected_type = entry5.get()
        entry5.delete(0, END)
        response = requests.get(f"https://pokeapi.co/api/v2/type/{selected_type}")

        if response.status_code == 200:
            type_data = response.json()
            pokemon_urls = [pokemon['pokemon']['url'] for pokemon in type_data['pokemon'][:10]]  # Get URLs of first 10 Pokémon of the selected type
            pokemontypeselection(pokemon_urls)                        
    else:
        global apibutton1,apibutton2,label
        user=(entry5.get())
        response=requests.get("https://pokeapi.co/api/v2/pokemon/" + user)

        if response.status_code == 200:
            apidict=response.json()
            image_url=apidict["sprites"]["other"]["official-artwork"]["front_default"]

            
            if image_url:
                image_response=requests.get(image_url)
                if image_response.status_code == 200:
                    image_data=io.BytesIO(image_response.content)
                    img=Image.open(image_data)
                    tk_image=ImageTk.PhotoImage(img)
                    label = tkinter.Label(image=tk_image)   
                    label.image = tk_image
                    arrayOfPokemon2.append(label)
                    drawpokedex()

                    
            else:
                pass
        else:
            pass

def pokemontypeselection(pokemon_urls):
    destroyPage2()
    place = 0
    place2 = 40
    for pokemon_url in pokemon_urls:
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_name = pokemon_data['forms'][0]['name']
            sprite_url = pokemon_data['sprites']['front_default']
            if sprite_url:
                image_response = requests.get(sprite_url)
                if image_response.status_code == 200:
                    image_data = io.BytesIO(image_response.content)
                    img = Image.open(image_data)
                    img = img.resize((80, 80))
                    tk_image = ImageTk.PhotoImage(img)
                    pokemon_image_label = tkinter.Label(image=tk_image)
                    pokemon_image_label.image = tk_image
                    pokemon_name_label = Label(root, text=pokemon_name)
                    pokemon_name_label.config(font=("lato", 14))
                    pokemon_image_label.place(x=225, y=place)
                    pokemon_name_label.place(x=435, y=place2)  
                    place += 75 #image size
                    place2 += 75
                    Select_box.place(x=225, y=800)
                    entry5.place(x=225, y=850)
                    pokedex_button2.place(x=225, y=900)
                    arrayOfPokemontypes.append(pokemon_image_label)
                    arrayOfPokemontypenames.append(pokemon_name_label)
    
def drawpokedex(): #deletes all boxes and places new ones
    pokedex_button.pack_forget()
    entry5.pack_forget()
    Select_box.pack_forget()
    labelball.pack_forget()
    label.place(x=125,y=-20)
    entry6.place(x=200,y=500)
    apibutton1.place(x=200,y=550)
    apibutton2.place(x=400,y=550)
    Select_box2.place(x=225,y=470) 
    
def savepokemondata():
    for i in arrayOfPokemon2:
        i.place_forget()
    entry5.pack_forget()
    pokemon_number=(entry6.get())
    try:
        pokemon_number = float(pokemon_number)
        #prevents number from being anything from 1 to 6
        if pokemon_number > 6:
            raise Exception

        pokemon_box.place_forget()
        drawpokedex()
        label.place_forget()
        entry6.place_forget()
        apibutton1.place_forget()
        apibutton2.place_forget()
        Select_box2.place_forget()
        combo_box.pack_forget()
        Select_box3.place(x=225,y=200)
        pokemon_saved=(entry5.get())
        pokemon_saved_slot=(entry6.get())
        pokemon_saved_slot = "Pokemon" + pokemon_saved_slot
        roster_no.place(x=300,y=240)
        roster_yes.place(x=400,y=240)
        
        for i,j in csv.iterrows():
            if j[0] == entry3.get(): # get currently active user
                # entry bug sort it out later
                csv.at[i, pokemon_saved_slot] = pokemon_saved
                csv.to_csv("userdata.csv", encoding="utf-8", index=False)

    except:
        pokemon_box.place(x=195,y=595)


def yes(): #shows the roster
    global pokemon_name_box,pokemon_images,arrayOfPokemon,arrayOfPokemonnames
    Select_box3.place_forget()
    roster_no.place_forget()
    roster_yes.place_forget()
    roster.place(x=175,y=50)
    exit.place(x=200,y=700)
    apibutton1.place(x=380,y=700)
    place=(0)
    place2=(40)
    for i,j in csv.iterrows():
        if j[0] == loginname:
            for k in range(2,8): # draw multiple pokemon 
                user = j[k]
                place=place+100
                place2=place2+100
                if isinstance(user, float):
                    user = int(user)
                response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(user))
                pokemon_name_box = Label(root, text=(user))
                if response.status_code == 200:
                    apidict=response.json()
                    image_url=apidict["sprites"]["front_default"]
                    pokemon_name_box = apidict["forms"][0]["name"]

                    if image_url:
                        image_response=requests.get(image_url)
                        if image_response.status_code == 200:
                            image_data=io.BytesIO(image_response.content)
                            img=Image.open(image_data)
                            tk_image=ImageTk.PhotoImage(img)
                            pokemon_images = tkinter.Label(image=tk_image)
                            pokemon_images.image = tk_image
                            pokemon_images.place(x=225,y=place)
                            pokemon_name_box = Label(root, text=pokemon_name_box)
                            pokemon_name_box.config(font=("lato", 14))
                            pokemon_name_box.place(x=435,y=place2)
                            
                            arrayOfPokemon.append(pokemon_images)
                            arrayOfPokemonnames.append(pokemon_name_box)
                            
#signup 

def signup():
        signuppack = [sign_up_box,entry1,entry2,create_button]
        for i in signuppack:
            i.pack()
            sign_up_button.place_forget()
            login_button.place_forget()


def signupprint():
    global signupname, signuppassword, csv
    signupname = entry1.get()
    signuppassword = entry2.get()
    
    if signupname == "" or signuppassword == "":
        signup_box.pack()
    else:
        csv = pandas.read_csv("userdata.csv")
        if signupname in csv["Username"].values:
            usernametaken_box.pack()
        else:
            csv.loc[len(csv.index)] = [signupname, signuppassword, "", "", "", "", "", ""]
            csv.to_csv("userdata.csv", mode="w", index=False)
            python = sys.executable
            os.execl(python, python, *sys.argv)

#login

def login():
        loginpack = [ login_box,entry3,entry4,login_check_button]
        for i in loginpack:
            i.pack()
            
            sign_up_button.place_forget()
            login_button.place_forget()

def logincheck():
    global loginname, loginpassword
    loginname = entry3.get()
    loginpassword = entry4.get()
    
    for i,j in csv.iterrows():
        if j[0] == loginname:
            if j[1] == loginpassword:
                name_wrong.pack_forget()
                password_wrong.pack_forget()
                drawPage2()
                break
            else:
                password_wrong.pack()
                name_wrong.pack_forget()
                break
                #wrong password
        else:
            password_wrong.pack_forget()
            name_wrong.pack()
            pass # no username matches
    
    if loginname == "":
        name_wrong.pack_forget()

#page1
    
root = Tk()
root.title("pokedex project")
root.geometry("750x950")
root.resizable(False, False)
sign_up_button = Button(root, text="signup?", command=signup, width=10)
login_button = Button(root, text="login?", command=login, width=10)
sign_up_box = Label(root, text="-----------sign up page-----------")
login_box = Label(root, text="------------login page------------")
Select_box2 = Label(root, text=f"--select a slot for your pokemon --")
signup_box = Label(root, text=("please fill both text boxes"))
usernametaken_box = Label(root, text=("username is already taken"))
combo_box = ttk.Combobox(root, values=["single pokemon", "by type"])
combo_box.set("single pokemon")
pokemon_box = Label(root, text=("invalid input"))
name_wrong = Label(root, text=("incorrect user name"))
roster = Label(root, text=("--------your pokemon roster--------"))
password_wrong = Label(root, text=("incorrect password"))
create_button = Button(root, text="create account", command=signupprint, width=30)
login_check_button = Button(root, text="login", command=logincheck, width=30)
apibutton1 = Button(root, text="change pokemon", command=retryselection)
apibutton2 = Button(root, text="save selection", command=savepokemondata)
roster_no = Button(root, text="no ", command=root.destroy)
exit = Button(root, text="EXIT ", command=root.destroy)
roster_yes = Button(root, text="yes", command=yes)
logo = Image.open('pokemon small.png')
logo = ImageTk.PhotoImage(logo)
labellogo = Label(root, image=logo)

entry1 = Entry(root, borderwidth=5.0, width=30)
entry2 = Entry(root, borderwidth=5.0, width=30)
entry3 = Entry(root, borderwidth=5.0, width=30) 
entry4 = Entry(root, borderwidth=5.0, width=30) 
entry5 = Entry(root, borderwidth=5.0, width=30)
entry6 = Entry(root, borderwidth=5.0, width=30)

#page2

Select_box = Label(root, text="--please select a pokemon--")
Select_box3 = Label(root, text="would you like to view your roster?")
pokedex_button = Button(root, text="confirm", command=pokedexapi, width=30)
pokedex_button2 = Button(root, text="confirm", command=typedelete, width=30)
pokemon_selection_box = Label(root)
ball = Image.open('ball small.png')
ball = ImageTk.PhotoImage(ball)
labelball = Label(root, image=ball)

#customise

arrayforsize =[entry1,entry2,entry3,entry4,entry5,entry6,exit,roster_yes,roster_no,pokemon_box,Select_box2,pokedex_button2,Select_box3,sign_up_button,usernametaken_box,login_button,create_button,login_check_button,pokedex_button,password_wrong,name_wrong,signup_box,apibutton1,apibutton2]
for i in arrayforsize:
    i.config(font=("lato", 14))
    i.config(fg="black")
    combo_box.config(font=("lato", 14))
    combo_box.config(width=29)
      
boxes =[Select_box,sign_up_box,login_box,roster]
for i in boxes:
    i.config(font=("lato", 20))
    i.config(fg="black")
    
drawPage2()
drawPage1()
root.mainloop()