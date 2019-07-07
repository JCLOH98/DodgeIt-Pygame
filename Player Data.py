
def main():
    File = open('Data.dat','a')
    print("Enter Name:")
    Name = input()
    print("Time:")
    Time = input()
    print("Level:")
    Level = input()
    File.write(Name)
    File.write(",")
    File.write(Time)
    File.write(",")
    File.write(Level)
    File.write('\n')
    File.close()

main()
