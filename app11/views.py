import csv
import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def findfactorial(request):
    number=int(request.POST.get('number'))
    factorial = 1
    for i in range(1,number+1):
        factorial= factorial*i
    return Response(factorial)

@api_view(['GET'])
def getdata(request):
    file=open('app11/M2project.csv')
    csvreader=csv.reader(file, delimiter=",")
    header=[]
    header = next(csvreader)
    print("\n")
    print("CSV file header is as below:")
    print(header)
    print("\n")
    
    csv_data=[]
    for x in csvreader:
        csv_data.append(x)
    print("CSV file data is as below:")
    print(csv_data) 
    print("\n")
    
    json_data=json.dumps(csv_data)
    print("Data in json format is as below:")
    file.close
    return Response(json_data)


@api_view(['POST'])
def checkpasswordformat(request):
    string=request.POST.get('string')
    status='Invalid string'
    l,u,p,d=0,0,0,0
    if(len(string)>= 8):
        for letter in string:
            if(letter.islower()):
                l+=1
            if(letter.isupper()):
                u+=1
            if(letter.isdigit()):
                d+=1
            if(letter=="@" or letter=="$" or letter=="_"):
                p+=1
            print(l,u,p,d)
            if(l>=1 and u>=1 and p>=1 and d>=1 and l+u+p+d==len(string)):
                print("valid string")
                status="valid string"
            else:
                print("Invalid string")
                status="Invalid string"
    return Response(status)



@api_view(['GET'])
def checkstring(request):
    input_string=request.GET.get('input_string')
    myfile=open('app11/M2file.txt','a+')
    status="String does not exist "
    with open('app11/M2file.txt') as myfile:
        if input_string in myfile.read():
            status="the string exists in the file"
        myfile.close()
    return Response(status)
                        
       
    
@api_view(['POST'])
def factors(request):
    number=int(request.POST.get('number'))
    factors=1
    factor_list=[]
    output_string=''
    for x in range(1,number+1):
        y=number%x
        if y == 0:
            factor_list.append(x)
        else:
            continue
    output_string =', '.join(str(x) for x in factor_list)
    return Response(output_string)       


@api_view(['GET'])
def vowels(request):
    input_string=request.GET.get('input_string')
    output_string=''
    vowels=["a", "e", "i", "o", "u"]
    temp_list=[]
    
    for i in input_string:
        if(i in vowels):
            temp_list.append(i)
        else:
            temp_list.append("_")
            
@api_view(['POST'])
def Vowels(request):
    input_string = request.POST.get('input_string')
    output_string =''
    vowels = ["a", "e", "i", "o", "u", " "]
    temp_list = []
    
    for x in input_string:
        if(x in vowels):
            temp_list.append(x)
        else:
            temp_list.append("_")
    output_string = ' '.join(str(x) for x in temp_list)
    output_string = output_string.upper()
    return Response(output_string)

@api_view(['POST'])
def Repeatedchar(request):
    input_string = request.POST.get('input_string')
    output_list = []
    x = 0
    len = 0
    for char in input_string:
        output_list.append(char)
        len = len + 1
        
    while x <(len-1):
        if output_list[x] == output_list [x+1]:
            output_list[x] = ""
        x=x+1 
    output_string = ''.join(str(i) for i in output_list)
    return Response(output_string) 

@api_view(['POST'])
def Decimaltobinary(request):
    Number = int(request.POST.get('Number'))
    quotient = Number//2
    firstbit = Number%2
    binarylist = [firstbit,]
    binarystring = ''
    
    while quotient >=1:
        bit =quotient%2
        binarylist.append(bit)
        quotient = quotient//2
                  

    binarylistReverse = binarylist[::-1]
    binarystring = ' '.join(str(x) for x in binarylistReverse)
    return Response(binarystring)    


@api_view(['POST'])
def Decimaltoocta(request):
    number = int(request.POST.get('number'))
    quotient = number//8
    firstbit = number%8
    octallist = [firstbit,]
    octastring = ' '
    while quotient >=1:
        oct  = quotient%8
        octallist.append(oct)
        quotient = quotient//8
    octallistReverse=octallist[::-1]
    octalstring =' '.join(str(x) for x in octallistReverse)
    return Response(octalstring)


@api_view(['POST'])
def Decimaltohexa(request):
    number = int(request.POST.get('number'))
    quotient = number//16
    firstbit = number%16
    hexalist = [firstbit,]
    hexastring = ' '
    while quotient >=1:
        hex  = quotient%16
        hexalist.append(hex)
        quotient = quotient//16
    hexalistReverse=hexalist[::-1]
    hexastring =' '.join(str(x) for x in hexalistReverse)
    return Response(hexastring)


    
                  
                         
            
