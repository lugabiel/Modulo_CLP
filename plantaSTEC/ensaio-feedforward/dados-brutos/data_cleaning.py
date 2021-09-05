data = ""
with open('saidas1-setpoint-fixo.txt', 'r') as file:
    data = file.read().replace(',', '.')
with open("setpoint-fixo.txt", "w") as out_file:
    out_file.write(data)
with open('saidas2-setpoint-degrau.txt', 'r') as file:
    data = file.read().replace(',', '.')
with open("setpoint-degrau.txt", "w") as out_file:
    out_file.write(data)