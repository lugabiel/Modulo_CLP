import matplotlib.pyplot as plt

while True:
    data = open("saida.txt", "r")

    temp = []

    for line in data:
        splitted = line[13:-1].split(' ')
        number = line[20:25]
        try: 
            number = splitted[4].replace(',','.')
        except:
            number = temp[-1]
        temp.append(float(number if len(number) else 0))
    #plt.clf()
    plt.plot(temp)
    plt.show()
            
    data.close()


