print("***KBC BY Pushpendra Patil***\n \n" )

questions = [
    ["Which language was used to create Facebook?","Python","French","Javascript","PHP","None",4],
    ["Who Created Python?","Dennis Ritchie","Guido Van Rossum","Bjarne Stroustrup","None",2],
    ["What does HTML stands?","Hyper Text Markup Language","High tech modern language","None",1],
    ["Who won WorldCup of 2026?","England","Brazil","South Africa","India","None",4],
    ["What is the Powerhouse of cell?","Ribosome","Mitochondria","DNA","Cell Membrane",2],
    ["Which animal is known as the King of the Jungle?","Tiger","Dog","Monky","Lion","None",4],
    ["Who was the PM of India?","Pushpendra Patil","Rahul Gandhi","Narendra Modi","Sukha Patil","None",3],
    ["What does BMW stands?","Bayerische Motorn Werke","Big Money Wasted","British Motor Ways","Best Motor Wheels","None",1]
]

levels = [1000,2000,3000,4000,5000,10000,20000,30000]

money = 0

for i in range(0,len(questions)):
    question = questions[i]

    print(f"\n Question for Rs.{levels[i]}\n")
    print(question[0])
    print(f"1. {question[1]}      2. {question[2]}")
    print(f"3. {question[3]}      4. {question[4]}")

    reply = int(input("Enter your answer with the option numbers only:"))

    if reply == question[-1]:
        print(f"Correct Answer, You have Won Rs. {levels[i]}")

        money = levels[i]

        if i==2:
            money = 3000

        elif i == 4:
            money = 10000

        elif i == 6:
            money = 30000

    else:
        print("Wrong Answer..!!")
        break

print(f"Your Balance: Rs.{money}")