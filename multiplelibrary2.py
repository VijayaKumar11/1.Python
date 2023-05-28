class multiplefun():
    def Subfields():
        print("Sub-fields in AI are:")
        i="Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"
        for num in i:
            print(num)
            message=num
            
    def OddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print(num,"is Even Number")
            message="Even Number"
        else:
            print(num,"is Odd Number")
            message="Odd Number"  
         
    def Elegibility():
        gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gen,"male"):
            if(age<21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(gen,"female"):
            if(age<18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
                    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        percentage=Total/5
        print("Total",Total)
        print("Percentage",percentage")
              
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area=(height*breadth)/2
        print("Area of Triangle",Area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=h1+h2+b
        print("Perimeter of Triangle: ",perimeter)