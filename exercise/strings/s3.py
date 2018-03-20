#embedding value in string 

value = "500"
message = "i hav %s rupees"

print(message % value) 
#we can do without variable also 
print(message % 1000) 

#more example 

var1 = "sachin" 
var2 = "dentist"
message1 = "%s: is in love with %s"
message2 = "%s is so %s"
print(message1 % (var1,var2)) 
print(message2 % ('she','pretty'))

#multiplying string

print(5 * var1)
