import json

# new_text = input("New text here: ")

# dictionary = {
#     "ishchi_nomi": "Jhon Doe",
#     "ish_joyi": "Hokimiyat",
#     "ish_vaqti": "9:00/18:00",
#     "daromadi": 2000000
# } 

data = [
    {
    "ishchi_nomi": "Jhon Doe",
    "ish_joyi": "Hokimiyat",
    "ish_vaqti": "9:00/18:00",
    "daromadi": 2000000
    },
     {
    "ishchi_nomi": "Kimsanboy",
    "ish_joyi": "Vazirlik",
    "ish_vaqti": "9:00/18:00",
    "daromadi": 12000000
    }
]


i = 1
while(i <= 1):
    ishchi_nomi = input("ishchi_nomi: ")
    ish_joyi = input("ish_joyi: ")
    ish_vaqti = input("ish_vaqti: ")
    daromadi = input("daromadi: ")
    
    new_data = {
    "ishchi_nomi": ishchi_nomi,
    "ish_joyi": ish_joyi,
    "ish_vaqti": ish_vaqti,
    "daromadi": daromadi
    }

    data.append(new_data)

    i+=1


with open('data.json', 'w') as f:
    json.dump(data, f, indent = 4)


