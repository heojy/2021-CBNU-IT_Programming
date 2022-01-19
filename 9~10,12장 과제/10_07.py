while True:
        try:
            filename = input("입력 파일 이름: ")
            infile = open(filename, "r") 
            
            print("파일이 성공적으로 열렸습니다.")
            break
            
        except IOError:
                print("파일 " + filename + " 이 없습니다. 다시 입력하시오.")

infile.close()