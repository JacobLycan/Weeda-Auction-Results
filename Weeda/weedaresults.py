#Initalize variables
masterlistbidders = [];
masterbidders = {};
realtotal = 0;
totallots =0;
#Loop through each year
for i in ["weeda2005", "weeda2006",  "weeda2007", "weeda2008", "weeda2009", "weeda2010", "weeda2011", "weeda2012", "weeda2013", "weeda2014", "weeda2015", "weeda2016", "weeda2017", "weeda2018", "weeda2019", "weeda2020", "weeda2021", "weeda2022","weeda2023","weeda2024"]:
    # Open file for the selected year
    with open("auctionresults/"+ i + ".txt",  errors='ignore' ) as f:
        total = 0;
        bidders = {};
        newbidders =0;
        lots = 0;
        prevLot = 0;
        maxLot = 0;
        maxLotnum =0;
        maxLotbuyer = 0;
        listbidders = [];

        #Loop through each line of the file
        for line in f:
            a =line.split("$");
            a[0]= a[0].replace("\n","");
            # Make sure line actually contains auction results
            if (len(a) >= 2):
                lots += 1;
                totallots += 1;
                ans = a[len(a)-1].replace("\n","");
                ans = a[len(a)-1].replace(",","");
          
                prevLot = float(ans);
                # Check if current lot is actually the most expensive so far
                if prevLot > maxLot:
                    maxLot = prevLot;
                    maxLotnum = lots;
                total += float(ans);
                realtotal += float(ans);
            # Check if line contains bidder information
            elif (a[0].isnumeric() ):
                if lots == maxLotnum:
                    maxLotbuyer = int(a[0]);
                listbidders.append(int(a[0]));
                masterlistbidders.append(int(a[0]));
                # Update bidder info for the selected year
                if int(a[0]) in bidders:
               
                    bidders[int(a[0])] = bidders[int(a[0])] + prevLot;
                else:
                    bidders[int(a[0])] = prevLot;
                # Update bidder info for all years
                if int(a[0]) in masterbidders:
                    
                    masterbidders[int(a[0])] = masterbidders[int(a[0])] + prevLot;
                else:
                    masterbidders[int(a[0])] = prevLot;
                    newbidders = newbidders + 1 ;
    # Print stats for selected year
    print(i);         
    print ("# of lots: " + str(lots));
    print ("Average lot price was: " + str(round(float(total)/float(lots),2)));
    print ("Most expensive lot was # " + str(maxLotnum) + " and it went for " + str(maxLot) + " and was purchased by " + str(maxLotbuyer));
    print("Total sales were " + str(total));
    print("Number of new bidders for the year was " + str(newbidders))
    set_list = set(listbidders);

    #Calculate and print number of unique bidders for the year
    uniquebidders = list(set_list);
    printlist = []
    for i in uniquebidders:
        printlist.append([i,listbidders.count(i),bidders[i]]);
    def myFunc(e):
        return e[1];
    printlist.sort(key=myFunc, reverse=True  );
    print ("Number of unique winners was " + str(len(printlist)));
    print (" ");

# Print stats for combined period 2005 to 2024
print ("For 2005 to 2024")
print("Total sales were " + str(realtotal));
print (" Number of lots was " + str(totallots));
set_list = set(masterlistbidders);
uniquebidders = list(set_list);
printlist = [];
for i in uniquebidders:
    printlist.append([i,masterlistbidders.count(i),masterbidders[i]]);
def myFunc(e):
    return e[1];
printlist.sort(key=myFunc, reverse=True  );
print ("Number of unique winners was " + str(len(printlist)));
print (" ");

#Find and print top ten bidders by most purchased lots
print ("Ten bidders who bought most lots")
wonlots =0;
for n in range(10):
    i = printlist[n];
    wonlots += i[1];
    print("#" + str(n+1) + " Bidder " + str(i[0]) + " Won " + str(i[1]) + " lots for $" + str(i[2]));
print ("The top ten bidders won " + str(wonlots) + " lots which is " + str( round((float(wonlots)/float(totallots))*100,2)) + "% of the total")
def sortMoney(e):
    return e[2];
#Sort bidder list by how much money they have spent
printlist.sort(key=sortMoney, reverse = True);
print (" ");

#Print the top ten bidders by money spent
print ("Top ten biggest spenders: ");
bigspend = 0;
for i in range(10):
    l = printlist[i];
    bigspend += l[2];
    print("#" + str(i+1) + ": Bidder " + str(l[0]) + " Won " + str(l[1]) + " lots for $" + str(l[2]));
print("The top ten spenders spent a total of " + str(bigspend) + " which is "  + str(round (float(bigspend)/float(realtotal)*100, 2)) + "% of the total");



  
