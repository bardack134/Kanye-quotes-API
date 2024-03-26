from tkinter import *


import requests


def get_quote():
    pass
    #Write your code here.


def get_quote():
    
    #hacemos una get request a la API kanye Rest API
    api="https://api.kanye.rest/"


    response=requests.get(api)


    response.raise_for_status()
           
            
    #obtenemos la respuesta en formato 'json'
    response_json=response.json()


    #usamos diccionario, clave, valor para hacer al text
    new_quote=response_json["quote"]


    #ingresamos el texto en el canvas
    canvas.itemconfigure(quote_text, text=new_quote)
    
   

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


    
window.mainloop()