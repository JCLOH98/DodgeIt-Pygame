
def main():
    File = open('Data.dat','r')
    Read = File.read()

    #All the datas in Datas
    Datas = Read.splitlines()
    #print(Datas)

    #Show the set of datas
    SetOfData = len(Read.splitlines())
    #print(SetOfData)

    NewData = []
    for i in range(SetOfData):
        #print(Datas[i].split(','))
        #They both different
        #NewData = NewData + (Datas[i].split(','))
        NewData.append((Datas[i].split(',')))

    #print(NewData)

    for i in range(SetOfData):
        for j in range(3):
            print(NewData[i][j],end = ' ')
        print('\n')

main()
