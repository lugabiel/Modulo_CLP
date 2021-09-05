from matplotlib import colors
import matplotlib.pyplot as plt
plt.show()
while True:
    #abrindo arquivo
    data = open("saidas.txt", "r")
    temp1 = []
    temp2 = []
    temp3 = []
    for line in data:
        splitted = line[15:-1].split(' ')
        var1 = splitted[0]
        var2 = splitted[0]
        var3 = splitted[0]
        try: 
            var1 = splitted[0].replace(',','.')
        except:
            var1 = temp1[-1]
        try:
            var2 = splitted[1].replace(',','.')
        except:
            var2 = temp2[-1]
        try:    
            var3 = splitted[2].replace(',','.')
        except:
            var3 = temp3[-1]
        temp1.append(float(var1 if len(str(var1)) else 0))
        temp2.append(float(var2 if len(str(var2)) else 0))
        temp3.append(float(var3 if len(str(var3)) else 0))
    plt.plot(temp1,color='#ff362b')
    plt.plot(temp2,color='#111111')
    plt.plot(temp3,color='#666666')
    #plt.pause(0.05)          
    plt.pause(0.20)          
    data.close()


