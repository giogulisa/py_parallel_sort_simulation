my_list = [] 
# shemyavs my_list shi monacemebi xelit
arr_size = int(input("sheiyvanet arr zoma: "))
core_number = int(input("sheiyvanet core-ebis raodenoba: "))
#aq vigeb tu ramdeni cipris dasortva mouwevs tvitoeul Core-s
check_number=arr_size//core_number
if (arr_size)==(check_number*core_number):
    n =  (arr_size//core_number)
else:
    n =  (arr_size//core_number)+1
#aq my_list shi sheyvanil monacemebs vyop tanabrad Core-ebis shesaabamisad
for i in range(arr_size):
    my_list.append(int(input("sheiyvanet ciprebi arrayshi: ")))
#aq vinaxav ukve dasortirebul mtlian masivs rata gamotanisas tavshi davabewdino
my_list_sorted=sorted(my_list)
#aq iyopa tanabrad core ebis shesabamisad
def paralel(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n]     
def paralell():
    x = list(paralel(my_list, n)) 
    #print(x)
    new_x=[]
    for i in x:
        new_x.append(sorted(i))    
    #aq mtlianad davsorte rac gamovida dawris shemdeg
    new_array1=[]
    print("ra sheviyvanet")
    print(my_list)
    print("rogori iqneba bolos :")
    print(my_list_sorted)
    print("pirveli sapexuri :")
    print(new_x)
    #aq vadareb sort punqciit mtlianad dasortirebuls bolos migebul shedegtan da sanam toli ar iqneba cikli itrialebs
    while [my_list_sorted]!=new_x:
        #aq ubralod vitvaliswineb tu kenti iyo da xelit vxdi array-d
        if len(new_x)%2==1 and len(new_x)>0:
            last_pop=new_x.pop()
            #gaxdeba luwi
            while len(new_x)>0:
                new_array1.append(sorted(new_x.pop(0)+new_x.pop(0)))
            new_array1=new_array1+[last_pop]
            new_x=new_array1.copy()
            del new_array1[:]
            #rodesac gadaewereba zed mtavar amsivs dzveli masivi ishleba
            print("shemdegi sapexuri")
            print(new_x)         
        if len(new_x)%2==0 and len(new_x)>0:
            while len(new_x)>0:
                new_array1.append(sorted(new_x.pop(0)+new_x.pop(0)))
            new_x=new_array1.copy()
            del new_array1[:]
            print("shemdegi sapexuri") 
            print(new_x)        
        else:   
            break        
paralell()