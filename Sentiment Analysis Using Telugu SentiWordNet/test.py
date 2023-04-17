

positive_list = []
negative_list = []
neutral_list = []

pos = 0
neg = 0
neu = 0

with open("Telugu_SentiWordNet/TE_NEG.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
    for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        negative_list.append(arr[1])

      
with open("Telugu_SentiWordNet/TE_NEU.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
    for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        neutral_list.append(arr[1])

with open("Telugu_SentiWordNet/TE_POS.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
    for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split("\t")
        positive_list.append(arr[1])

count = 1
with open("Book_Reviews_Dataset/book_neg.txt", "r",encoding="utf-8") as file:  #reading LIWC dictinary
    for line in file:
        line = line.strip('\n')
        line = line.strip()
        arr = line.split()
        pos = 0
        neg = 0
        neu = 0
        if len(arr) > 0 and (line.startswith('__________________________') == False):
            for word in arr:
                if word in neutral_list:
                    neu = neu + 1
                if word in negative_list:
                    neg = neg + 1
                if word in positive_list:
                    pos = pos + 1

            pos = pos + neu
            if pos == 0 and neg == 0:
                print(str(count)+" neutral")
            elif pos > 0 and neg > 0:
                pos = pos/len(arr)
                neg = neg/len(arr)
                if pos > neg :
                    print(str(count)+" positive "+str(pos))
                else:
                    print(str(count)+" negative "+str(neg))
            elif pos > 0 and neg == 0:
                pos = pos/len(arr)
                print(str(count)+" positive "+str(pos))
            elif pos == 0 and neg > 0:
                neg = neg/len(arr)
                print(str(count)+" negative "+str(neg))
                
            count = count + 1




            
                    
                    
        
