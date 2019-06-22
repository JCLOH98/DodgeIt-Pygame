
def main():
    File = open('Data.dat','r')
    Read = File.read()

    #All the datas in Datas
    Datas = Read.splitlines()
    print(Datas)

    #Show the set of datas
    SetOfData = len(Read.splitlines())
    print(SetOfData)

    for i in range(SetOfData):
        print(Datas[i].split(','))

main()
