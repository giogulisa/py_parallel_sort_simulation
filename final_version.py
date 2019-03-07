my_list = [] 
# shemyavs my_list shi monacemebi xelit
arr_size = int(input("sheiyvanet arr zoma: "))
core_number = int(input("sheiyvanet core-ebis raodenoba: "))
#aq my_listshi vwer monacemebs
if arr_size<core_number:
    core_number==arr_size
for i in range(arr_size):
    my_list.append(int(input("sheiyvanet ciprebi arrayshi: ")))
#aq vinaxav ukve dasortirebul mtlian masivs rata gamotanisas tavshi davabewdino
my_list_sorted=sorted(my_list)
#aq iyopa tanabrad core ebis shesabamisad
def paralel(my_list, core_number):
    k, m = divmod(len(my_list), core_number)
    return (my_list[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(core_number))  
def paralell():
    x=list(paralel(my_list,core_number))
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