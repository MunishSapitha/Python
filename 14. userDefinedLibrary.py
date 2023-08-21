class multipleFns():
    
    def age_category():  
        age=int(input("Enter your age :"))
        if age<18:
            print("Children")
            cate="Children"
        elif age<35:
            print("Adult")
            cate="Adult"
        elif age<59:
            print("Citizen")
            cate="Citizen"
        else:
            print("Senior Citizen")
            cate="Senior Citizen"      
        return cate
            


    def odd_Even():
        num=int(input("Enter the number :"))
        if num%2==0:
            print("Even Number")
            msg="Even Number"
        else:
            print("Odd Number")
            msg="Odd Number"     
        return msg
    
    
    
    def bmi_index():
        bmi=int(input("Enter the BMI Index :"))
        if bmi<18:
            print("Underweight")
            msg="Underweight"
        elif bmi<25:
            print("Normal")
            msg="Normal"
        elif bmi<30:
            print("Overweight")
            msg="Overweight"
        else:
            print("Obese")
            msg="Obese"
        return msg