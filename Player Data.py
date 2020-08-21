
def main():
    File = open('Data.dat','a')
    print("Enter Name:")
    Name = input()
    
    print("Level:")
    Level = input()
    
    print("Time:")
    Time = input()
    
    File.write(Name)
    File.write(",")
    File.write(Level)
    File.write(",")
    File.write(Time)
    File.write('\n')
    File.close()

main()
