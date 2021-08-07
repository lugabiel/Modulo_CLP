from matplotlib import colors
import matplotlib.pyplot as plt
plt.show()
while True:
    data = open("saida2.txt", "r")
    temp = []
    for line in data:
        splitted = line[13:-1].split(' ')
        number = line[20:25]
        try: 
            number = splitted[4].replace(',','.')
        except:
            number = temp[-1]
        temp.append(float(number if len(number) else 0))
    plt.plot(temp,color='#ff362b')
    plt.pause(0.05)          
    data.close()


