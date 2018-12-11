#!/usr/bin/env python3
# Mixed lists (notice the string)
## Define a list
my_list = [ "192.168.0.5", 5060, "UP" ]

## Print the IP
print("The first item in the list (IP): " + my_list[0])

## Print the port - it is a string so we use the string function.
print("The second item in the list (port): " + str(my_list[1]) )

## Print the state
print("The last item in the list (state): " + my_list[2] )

## Define a list for advanced print
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

##Convert list items to strings
port1 = str(new_list[0])
port2 = new_list[1]
port3 = str(new_list[2])
ip1 = new_list[3]
ip2 = new_list[4]
method = new_list[5]

## Try to print everything - I failed on whitespace
print('When I',method,
'into IP addresses', ip1,
'or', ip2,
'I am unable to ping ports', port1,
',', port2,
', or', port3)
