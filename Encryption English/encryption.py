from math import *

def encrypted_word( actual_message ):
    filtered_message=""
    for X in actual_message:
        if ord(X)!=32:
            filtered_message+=X
            
    filtered_m_length=len(filtered_message)
##    print("string length",filtered_m_length)
    
    floor_value = floor(sqrt(filtered_m_length))    
    ceil_value  = floor(sqrt(filtered_m_length))

##    print("floor before",floor_value)
##    print("ceil before",ceil_value)

    row_len = floor_value
    column_len = floor_value
##    print("row * column ",row_len*column_len)
    if row_len*column_len < filtered_m_length:
##        print("andar aaya pehale if ke")
        column_len+=1     
##    print("row * column ",row_len*column_len)

    if row_len*column_len < filtered_m_length:
##        print("andar aaya pehale dusre ke")
        row_len+=1

##    print("after floor",row_len)
##    print("after ceil", column_len)

    end_s=""

    if row_len == column_len:
        for X in range(0, row_len):

            current = X+column_len
            end_s = end_s + filtered_message[X]


            while(True):
                if( current <= filtered_m_length-1 ):
                    end_s = end_s + filtered_message[current]
                    current+= column_len
                else:
                    break

            
            end_s = end_s +" "


    else:
         for X in range(0, row_len+1):

            current = X+column_len
            end_s = end_s + filtered_message[X]


            while(True):
                if( current <= filtered_m_length-1 ):
                    end_s = end_s + filtered_message[current]
                    current+= column_len
                else:
                    break

            
            end_s = end_s +" "

            
    return end_s
    
print(encrypted_word("chillout"))
print("\nchillout")


########        Done
