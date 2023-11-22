
def get_text(filename):
    fin = open(filename,"r")
    lines = fin.readlines()
    fin.close()
    return lines

def write_text(lines,filename):
    fout = open("Track_time.txt","w")
    for line in lines:
        fout.write(line)
    fout.close()

def look_up(ques,name):
    if(ques == 1):
        lines = get_text("Track_time.txt")
        for i in lines:
            line = i.split(",")
            if(line[0]==name):
                convert = float(line[1])
                return convert
            
def no_identical(name):
    '''check if there is the identical name in the file'''
    lines = get_text("Track_time.txt")
    for i in lines:
        line = i.split(",")
        if(name == line[0]):
            return False
    return True

def add_new_ath(ques,name):
    if(ques == 2):
        lines = get_text("Track_time.txt")
        #fout = write_text(lines,"Track_time.txt")
        if(no_identical(name)==True):
            PR = input("Provide a PR")
            add = "{0},{1}"
            new_line = add.format(name,PR) + "\n"
            lines+=[new_line]
            print("Your information is added")
            
        else:
            print("This name is existed")
        fout = write_text(lines,"Track_time.txt")

def remove_graduated_senior(ques,name):
    if(ques == 3):
        new_lines = []
        lines = get_text("Track_time.txt")
        for i in lines:
            line = i.split(",")
            if(line[0]!=name):
                new_lines+=[i]
        fout = write_text(new_lines,"Track_time.txt")
        return new_lines

def old_PR(name):
    '''find a name with previous PR. Then, return PR'''
    lines = get_text("Track_time.txt")
    for i in lines:
        line = i.split(",")
        if(line[0]==name):
            convert = float(line[1])
            return convert

def check_PR(name,new_PR):
    if(float(new_PR) < old_PR(name)):
        return True
    return False
        
def update_PR(ques,name,new_PR):
    if(ques == 4):
        lines = get_text("Track_time.txt")
        for i in range(len(lines)):
            line = lines[i].split(",")
            if(line[0] == name):
                if(check_PR(name,new_PR) == True):
                    lines[i] = lines[i].replace(line[1],new_PR) + "\n"
                    print("Your information is updated")
                else:
                    print("You cannot add a worse PR")

        fout = write_text(lines,"Track_time.txt")

def main():
    menu = "These are options\n" + "1:Lookup an athlete's PR\n" + "2:Add new atheletes\n" + "3:Remove graduated seniors\n" + "4:Update stored PR\n"
    print(menu)
    ques = int(input("Choose one of those options by providing a number:"))
    name = input("Provide a name:")
    if(ques == 1):
        result = look_up(ques,name)
        print(result)

    elif(ques == 2):
        end = add_new_ath(ques,name)

    elif(ques == 3):
        final = remove_graduated_senior(ques,name)
        print("Your information is removed")
            
    elif(ques == 4):
        new_PR = input("Provide a new PR:")
        ans = update_PR(ques,name,new_PR)
main()

           
        
        
    
    
    
    
        
    
    



            
            
            
            
        
        
        
    


        
            
            
        
        
    
        
        
        
        
        

