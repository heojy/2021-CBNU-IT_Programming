ph=float(input("pH 농도를 입력하시오 :"))

if ph > 7:
    print("이 용액은 알칼리성 입니다.")
elif ph == 7:
    print("이 용액은 중성 입니다.")
else:
    print("이 용액은 산성 입니다.")