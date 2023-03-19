import pandas as pd
def oper_greater(c1,break_query,table,store1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] > int(break_query[i])]
        print(df1)

def oper_equal(c1,break_query,table,store1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] == int(break_query[i])]
        print(df1)

                    
                    
def oper_less(c1,break_query,table,stor1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] < int(break_query[i])]
        print(df1)
                    
                    
def oper_greatereq(c1,break_query,table,store1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] >= int(break_query[i])]
        print(df1)

def oper_lesseq(c1,break_query,table,store1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] <= int(break_query[i])]
        print(df1)

def oper_noteq(c1,break_query,table,store1):
    for i in range(c1,(len(break_query)-1)):
        df1 = table[table[store1] != int(break_query[i])]
        print(df1)

def where(c,break_query,table,li):
    colname=0
    c_col = 0
    for i in range(2,len(li)):
        if(li[i]=='<end_table>'):
            break
        else:
            required_col = table[colname]
            store1 = colname
            col = li[i]
            if(break_query[c]==col):
                print(" ",col)
                c_col=c_col+1
                c=c+1
                c1 = c
                break
        colname = colname+1
    for i in range(c1,len(break_query)):
        if(c_col==1 and (break_query[i] == '=' or break_query[i] == '>' or break_query[i] == '<' or break_query[i] == '<=' or break_query[i] == '>=' or break_query[i] == '!=')):
            c1=c1+1
            store_operator=break_query[i]
            #print(required_col)
            if(store_operator=='>'):
                oper_greater(c1,break_query,table,store1)
            if(store_operator=='='):
                oper_equal(c1,break_query,table,store1)
            if(store_operator=='<'):
                oper_less(c1,break_query,table,store1)
            if(store_operator=='>='):
                oper_greatereq(c1,break_query,table,store1)
            if(store_operator=='<='):
                oper_lesseq(c1,break_query,table,store1)
            if(store_operator=='!='):
                oper_noteq(c1,break_query,table,store1)
            break 
            
def colrev(lst,li,table):
    columns1 = []
    k = 0
    for j in range(2,len(li)):
        if(li[j]=='<end_table>' or li[j]=='<end_table'):
            break
        else:
            columns1.append(li[j])
    #print(columns1)
    table.columns = columns1
    #print(table)
    for i in range(0,len(lst)):
        k=0
        for l in range(2,len(li)):
            if(lst[i] == li[l]):
                col = lst[i]
                required_col = table[col]
                print(required_col)
                
            k=k+1
    

def colwhere(c,lst,break_query,table,li):
    print(c)
    
    
def mainaggremin(storeagge,table,li):
    colname = 0
    for j in range(2,len(li)):
        if(li[j]=='<end_table>'):
                break
        else:
            required_col = table[colname]
            if(storeagge == li[j]):
                #print(required_col)
                break
        colname = colname+1
    agg = table[colname].min()
    print(agg)
    
def mainaggremax(storeagge,table,li):
    colname = 0
    for j in range(2,len(li)):
        if(li[j]=='<end_table>'):
                break
        else:
            required_col = table[colname]
            if(storeagge == li[j]):
                #print(required_col)
                break
        colname = colname+1
    agg = table[colname].max()
    print(agg)
        
def mainaggreavg(storeagge,table,li):
    colname = 0
    for j in range(2,len(li)):
        if(li[j]=='<end_table>'):
                break
        else:
            required_col = table[colname]
            if(storeagge == li[j]):
                #print(required_col)
                break
        colname = colname+1
    agg = table[colname].mean()
    print(agg)
    
def mainaggresum(storeagge,table,li):
    colname = 0
    for j in range(2,len(li)):
        if(li[j]=='<end_table>'):
                break
        else:
            required_col = table[colname]
            if(storeagge == li[j]):
                #print(required_col)
                break
        colname = colname+1
    agg = table[colname].sum()
    print(agg)
    
def mainaggrecount(storeagge,table,li):
    colname = 0
    for j in range(2,len(li)):
        print(li[j])
        if(li[j]!='<end_table>'):
            required_col = table[colname]
            if(storeagge == li[j]):
                #print(required_col)
                break
        colname = colname+1
    agg = table[colname].count()
    print(agg)
    
def aggregate(c,break_query,tablename,table,li,count):
    storebreak = break_query[c]
    c1 = 0
    c_from2 = 0
    c_table2 = 0
    c_semi2 = 0
    storeagge = ""
    if(count==5):
        for j in range(6,len(storebreak)):
            #print(storebreak[j])
            if(storebreak[j]==')' or storebreak[j]==','):
                break
            else:
                storeagge = storeagge + storebreak[j]
    else:
        for j in range(4,len(storebreak)):
            if(storebreak[j]==')' or storebreak[j]==','):
                break
            else:
                storeagge = storeagge + storebreak[j]
    #print(storeagge)
    c1 = c+1
    for i in range(c1,len(break_query)):
        if(break_query[i]=='from'):
            c_from2 = c_from2+1
        elif(c_from2==1 and break_query[i]==tablename):
            c_table2 = c_table2+1
        elif(c_table2==1 and break_query[i]==';'):
            c_semi2 = c_semi2 + 1
    if(c_semi2 == 1 and count==1):
        mainaggremin(storeagge,table,li)
    if(c_semi2 == 1 and count==2):
        mainaggremax(storeagge,table,li)
    if(c_semi2 == 1 and count==3):
        mainaggreavg(storeagge,table,li)
    if(c_semi2 == 1 and count==4):
        mainaggresum(storeagge,table,li)
    if(c_semi2 == 1 and count==5):
        mainaggrecount(storeagge,table,li)
    
    
def Columnfun(c,break_query,tablename,table,li):
    lst=[]
    c_from1=0
    c_table1 = 0
    c_semi = 0
    c_where = 0
    for i in range(c,len(break_query)):
        store3 = break_query[i]
        if(store3[0]=='m' and store3[1]=='i' and store3[2]=='n' and store3[3]=='('):
            count=1
            aggregate(c,break_query,tablename,table,li,count)
            break
        if(store3[0]=='m' and store3[1]=='a' and store3[2]=='x' and store3[3]=='('):
            count=2
            aggregate(c,break_query,tablename,table,li,count)
            break
        if(store3[0]=='a' and store3[1]=='v' and store3[2]=='g' and store3[3]=='('):
            count=3
            aggregate(c,break_query,tablename,table,li,count)
            break
        if(store3[0]=='s' and store3[1]=='u' and store3[2]=='m' and store3[3]=='('):
            count=4
            aggregate(c,break_query,tablename,table,li,count)
            break
        if(store3[0]=='c' and store3[1]=='o' and store3[2]=='u' and store3[3]=='n' and store3[4]=='t' and store3[5]=='('):
            count=5
            aggregate(c,break_query,tablename,table,li,count)
            break
        if(break_query[i]!='from' and break_query[i]!=tablename and break_query[i]!=',' and break_query[i]!=';' and break_query[i]!='where'):
            c=c+1
            lst.append(break_query[i])
            c=c+1
        elif(break_query[i]=='from'):
            c_from1 = c_from1+1
            c=c+1
        elif(c_from1==1 and break_query[i]==tablename):
            c_table1 = c_table1+1
            c=c+1
        elif(c_table1==1 and break_query[i] == 'where'):
            c_where = c_where+1;
            colwhere(c,lst,break_query,table,li)
            break
        elif(c_table1==1 and break_query[i]==';'):
            c_semi = c_semi+1
    #print(lst)
    if(c_where==0 and c_semi==1):
        colrev(lst,li,table)
        
def alfun(list1,table,count4):
    if(count4==1):
        df = table.sort_values([list1[0]],ascending=False)
        print(df)
    else:
        df = table.sort_values([list1[0]])
        print(df)
        
    
    
def orderfun(c,break_query,tablename,table,li):
    list1=[]
    c_semi=0
    count4 = 0
    c_desc = 0
    for i in range(c,len(break_query)):
        column1=0
        if(break_query[i] == 'desc' or break_query[i] == 'DESC'):
            c_desc=c_desc+1
            count4 = count4+1
        if(break_query[i] ==';'):
            c_semi=c_semi+1
            break
        else:
            for j in range(2,len(li)):
                if(li[j]=='<end_table>'):
                    break
                elif(break_query[i]==li[j]):
                    list1.append(column1)
                    break
                column1=column1+1
    if(c_semi==1):
        alfun(list1,table,count4)
    
                
def query1(break_query,tablename,table,li):
    c_select=0
    c_star=0
    c_from=0
    c_table=0
    c=0
    c_order=0
    
    if(break_query[0]=='select' and break_query[1]!='*'):
        c=c+1
        Columnfun(c,break_query,tablename,table,li)
    else:
        
        for i in range(0,len(break_query)):
            if(break_query[-1]!=';'):
                print("Invalid statement...please check your tablename or sql syntax")
                break
            if(break_query[i]=='select' or break_query[i]=='SELECT' or break_query[i]=='Select'):
                c_select=c_select+1
                c=c+1
            elif(c_select==1 and break_query[i]=='*'):
                c_star=c_star+1
                c=c+1
            elif(c_star==1 and (break_query[i]=='from' or break_query[i]=='FROM' or break_query[i]=='From')):
                c_from=c_from+1
                c=c+1
            elif(c_from==1 and break_query[i]==tablename):
                c_table=c_table+1
                c=c+1
            elif(c_table==1 and (break_query[i]=='WHERE' or break_query[i]=='Where' or break_query[i]=='where')):
                c=c+1
                where(c,break_query,table,li)
                break
            elif(c_table==1 and break_query[i]==';'):
                print(table)
            elif(c_table==1 and break_query[i]=='order'):
                c_order=c_order+1
                c=c+1
            elif(c_order==1 and break_query[i]=='by'):
                c=c+1
                orderfun(c,break_query,tablename,table,li)
                break;
            else:
                print("Invalid statement")
                

one = pd.read_csv('Book2.csv',header=None)
val1 = "Book2"
#print(one)
print("\n")
#print(two)
#print("\n")
query = input()
break_query = query.split()
#print(break_query)
count=0
checke = open("metadata1.txt",'r');
l = checke.readlines()
#print(l)
li = []
for line in l:
    li.append(line[:len(line)-1])
#print(li)
for i in range(0,len(li)):
    #print(li[i])
    if li[i] in break_query:
        count += 1
        tablename = li[i]
        if(tablename == val1):
            #print("table found")
            query1(break_query,tablename,one,li)
        break
if(count==0):
    print("Invalid statement...please check your tablename or sql syntax")
    

