def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
#--------------2------------#
'''
The keywords 'try', 'except' and 'finally' are 
exception handling keywords in python 
whereas the word 'accept' is not a keyword at all.
'''
#--------------3------------#
import copy
a=[10,23,56,[78]]
b=copy.deepcopy(a)
a[3][0]=95
a[1]=34
print(b)
#-------------4-------------#
a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)
#-------------5-------------#
'''
host        : a computer that enables resource sharing by other computers on the same network
throughput  : the amount of material or items passing through a system or process.
RG-58/U     : is a type of coaxial cable often used for low-power signal and RF connections.
'''
#-------------6-------------#
'''The Microsoft Remote Desktop Protocol (RDP) provides remote display and 
input capabilities over network connections for Windows-based applications running on a server.
'''
#-------------7-------------#
'''
full-duplex :	A type of transmission in which signals may travel in both directions over 
a medium simultaneously. May also be called, simply, “duplex.”
half-duplex :	A type of transmission in which signals may travel in both directions over 
a medium, but in only one direction at a time.
'''
#-------------8-------------#
'''
Stands for "Gigabits per second." 1Gbps is equal to 1,000 Megabits per second (Mbps), or 1,000,000,000 bits per second.
'''
#-------------9-------------#
'''
Which IPv4 address format was created for ease of use by people and is expressed as 201.192. 1.14? Explanation
: For ease of use by people, binary patterns are represented as dotted decimal.
'''
