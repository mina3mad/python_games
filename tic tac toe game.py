board=[0,1,2,
       3,4,5,
       6,7,8]
boardlog=[0,0,0,
          0,0,0,
          0,0,0]
a="tic tac toe"
print("*"*10+a.upper()+"*"*10)
print("----> player one should enter odd number & player two should enter even number ")
player=1                    #to initialize first plyer
total_moves=0               #to count moves
end_check=0
def check () :              #checcking the moves of player
    #check horizontal line
    if boardlog[0]+boardlog[3]+boardlog[6]==15 :
        print("you are won!!")
        return 1
    if boardlog[1]+boardlog[4]+boardlog[7]==15 :
        print("you are won!!")
        return 1
    if boardlog[2]+boardlog[5]+boardlog[8]==15 :
        print("you are won!!")
        return 1
    #check diagonal line
    if boardlog[0]+boardlog[4]+boardlog[8]==15:
        print("you are won!!")
        return 1
    if boardlog[2]+boardlog[4]+boardlog[6]==15:
        print("you are won!!")
        return 1
    #check vertical line
    if boardlog[0]+boardlog[1]+boardlog[2]==15 :
        print("you are won!!")
        return 1
    if boardlog[3]+boardlog[4]+boardlog[5]==15 :
        print("you are won!!")
        return 1
    if boardlog[6]+boardlog[7]+boardlog[8]==15 :
        print("you are won!!")
        return 1
    return 0


print("0|1|2")
print("-+-+-")
print("3|4|5")
print("-+-+-")
print("6|7|8")
print("_"*30)

while True:
    print(boardlog[0],'|',boardlog[1],'|',boardlog[2])
    print("--+--+---")
    print(boardlog[3],'|',boardlog[4],'|',boardlog[5])
    print("--+--+---")
    print(boardlog[6],'|',boardlog[7],'|',boardlog[8])
    print("_"*30)
    end_check=check()


    if total_moves ==9 or end_check==1:
        break

    while True:                        #input
        if player==1 :                 #choose player

            odd=int(input("player one enter odd number:"))
            pl1_input=int(input("player one enter replace space:"))
            if pl1_input in board:
                if odd %2==1:
                    boardlog[pl1_input]=int(odd)
                else:
                    odd2=int(input("please,enter only odd number:"))
                    boardlog[pl1_input]=int(odd2)
                player=2
                break
            else:                         #on wrong input
                print("invalid input please,try again ")
                continue
        else:                             #player two
            even=int(input("player two enter even number: "))
            pl2_input=int(input("player two enter replace space:"))
            if pl2_input in board :
                if even%2==0 :
                    boardlog[pl2_input]=int(even)
                else:
                    even2=input("please,enter even number:")
                    boardlog[pl2_input]=int(even2)
                player=1
                break
            else:                          #on wrong input
                print("invalid input please,try again")
                continue
    total_moves +=1
    print("_"*30)
