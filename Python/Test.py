def gobplayer_move(goblin1, player1, changeoutput, turncount, listdatanew):

    player_class = changeoutput[2]
    
    if len(turncount) == 1: #first turn will always have all the moves available

        if player_class == "WAR":
                
            coollist = {"Basic Atk":1, "Serrate":2, "Pommel Strike":3, "Whirlwind Spin":4 }
            ablelist = ["Basic Atk", "Serrate", "Pommel Strike", "Whirlwind Spin"]

            funclist = {1:player1.basic_atk,
                        2:player1.warriors_serrate,
                        3:player1.pommel_strike,
                        4:player1.whirlwind_spin
                            
                            }

        if player_class == "WIZ":
            coollist = {"Basic Atk":1, "Magic Rain":2, "Magic Crackers":3, "Arcanus Pinnus":4}
            ablelist = ["Basic Atk", "Magic Rain", "Magic Crackers", "Arcanus Pinnus"]

            funclist = {1:player1.basic_atk,
                        2:player1.magic_rain,
                        3:player1.magic_crackers,
                        4:player1.arcanus_pinnus

                            }
        
        if player_class == "ROG":
            coollist = {"Basic Atk":1, "Ankle Cutter":2, "Dropkick Slash":3, '"Thousand" Flashstep':4}
            ablelist = ["Basic Atk", "Ankle Cutter", "Dropkick Slash", '"Thousand" Flashstep']


            funclist = {1:player1.basic_atk,
                        2:player1.ankle_cutter,
                        3:player1.dropkick_slash,
                        4:player1.thousand_flashstep

                            }

        print(f"\n    {ablelist[0]} - 1\n\n    {ablelist[1]} - 2\n\n    {ablelist[2]} - 3\n\n    {ablelist[3]} - 4\n")
        moveinput = int(input("> "))


        if moveinput == 1:
            funclist[1]()
            removed = ablelist[moveinput - 1]
            ablelist.pop(0)
            turncount.append(1)
            time.sleep(5)
            return ablelist, turncount, coollist, removed

        if moveinput == 2:
            funclist[2]()
            removed = ablelist[moveinput - 1]
            ablelist.pop(1)
            turncount.append(1)
            time.sleep(5)
            return ablelist, turncount, coollist, removed                   #return data ---> [['Move 2', 'Move3', 'move4'], [1, 1], {"Basic Atk":1, "Ankle Cutter":2, "Dropkick Slash":3, '"Thousand" Flashstep':4}, "removedmove" ]
            
        if moveinput == 3:
            funclist[3]()
            removed = ablelist[moveinput - 1]
            ablelist.pop(2)
            turncount.append(1)
            time.sleep(5)
            return ablelist, turncount, coollist, removed
               
        if moveinput == 4:
            funclist[4]()
            removed = ablelist[moveinput - 1]
            ablelist.pop(3)
            turncount.append(1)
            time.sleep(5)
            return ablelist, turncount, coollist, removed
            


    elif len(turncount) > 1: #for second turn onwards, must calc cooldowns listdata[3] = removed move

        if len(listdatanew[0]) < 4:
            listdataold = []               #had to create a list since cannot change tuple
            listdataold.append(listdatanew) 
            removed = []
            removed.append(listdatanew[3])

            cooldown = listdatanew[2][listdatanew[3]] #finally figured out how to index into a nested list


                
            if removed.count(listdatanew[2][2]) == True:
                listdataold.insert(, 1)
                

            if removed.count(listdatanew[3][3]) == True:
                listdataold.insert(, 2)
                

            if removed.count(listdatanew[4][4]) == True:
                listdataold.insert(, 3)
            

            listvariants = [""]

                


            time.sleep(5)
            #print(f"\n    {...} - 1\n\n    {listdatanold[0]} - 2\n\n    {listdatanold[1]} - 3\n\n    {listdatanold[0][2]} - 4\n")
    
        turncount.append(1)