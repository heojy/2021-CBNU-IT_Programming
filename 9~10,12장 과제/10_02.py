try:
    infile = open("C:/Users/82107/Desktop/input.txt","r", encoding = "UTF8")
    
    lines = infile.readlines()
    best = []
    for line in lines:
        line = line.rstrip()
        word_list = line.split()
        
        for word in word_list:
            word = word.rstrip(".,?!")
            
        longest = 0
        
        for index in range(len(word_list)):
            if len(word_list[index]) > len(word_list[longest]):
                longest = index
        best.append(word_list[longest])
        
    
    longst = 0
        
    for index in range(len(best)):
        if len(best[index]) > len(best[longst]):
            longst = index
        best.append(word_list[longst])
    
    print(f"가장 긴 단어는 {best[longst]}입니다.")
    
finally:
    infile.close()