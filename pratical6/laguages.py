from pratical6.programming_laguage import ProgramingLanguage

def main():

    ruby= ProgramingLanguage("Ruby", "Dynamic",True,1995)
    python= ProgramingLanguage ("Python", "Dynamic", True, 1991)
    visual_basic = ProgramingLanguage ("Visual basic", "Static", False , 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    Programing_List=[]
    Programing_List.append(ruby)
    Programing_List.append(python)
    Programing_List.append(visual_basic)
    print("The Dynamic Type are")

    for i in range(len(Programing_List)):
        test =  Programing_List[i].is_dynamic()
        if test==True:
            print(Programing_List[i].field)

main()