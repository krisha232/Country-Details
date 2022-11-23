from tkinter import *
import requests
import json
root=Tk()
root.title("Countries")
root.geometry("350x300")

root.configure(background="white")
#Setting labels
city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

country_info_label = Label(root,text="Country: ", bg="white", font=("bold", 10))
country_info_label.place(relx=0.23,rely=0.5,anchor=CENTER) 

region_info_label = Label(root,text="Region: ", bg="white", font=( "bold",10)) 
region_info_label.place(relx=0.23,rely=0.6,anchor=CENTER) 

language_info_label = Label(root,text="Language: ", bg="white", font=( "bold",10)) 
language_info_label.place(relx=0.23,rely=0.7,anchor=CENTER) 

population_info_label = Label(root,text="Population: ", bg="white", font=( "bold",10)) 
population_info_label.place(relx=0.22,rely=0.8,anchor=CENTER) 

area_info_label = Label(root,text="Area: ", bg="white", font=( "bold",10)) 
area_info_label.place(relx=0.22,rely=0.9,anchor=CENTER) 

def city_name():
    api_request=requests.get("https://restcountries.com/v2/capital/"+city_entry.get())
    api_output_json=json.loads(api_request.content)
   
    country_info=api_output_json[0]['name']
    region_info=api_output_json[0]['region']
    language_info=api_output_json[0]['languages'][0]['name']
    population_info=api_output_json[0]['population']
    area_info=api_output_json[0]['area']
    
    
    country_info_label["text"]="Country : "+str(country_info)
    region_info_label["text"]="Region : "+str(region_info)
    language_info_label["text"]="Language : "+str(language_info)
    population_info_label["text"]="Population : "+str(population_info)
    area_info_label["text"]="Areay : "+str(area_info)
    
    
    city_name_label["text"]=city_entry.get()
    city_entry.destroy()
    search_btn.destroy()
    
search_btn=Button(root,text="City Details",command=city_name,relief=FLAT)
search_btn.place(relx=0.6,rely=0.35,anchor=CENTER)
    
    
root.mainloop()
