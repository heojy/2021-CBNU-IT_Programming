filename = input("파일 이름을 입력하시오 :")
infile = open(filename, "r")

freqs = {}
tab = 0
for line in infile:
    tab +=1
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
            
print(f"스페이스 수 = {freqs[' ']}, 탭의 수 = {tab}")
infile.close()