#lovely_loveseat
lovely_loveseat_description = "Lovely loveseat. Tifted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep/ Red or white." 
lovely_loveseat_price = 254.00 

#stylish_settee
stylish_sette_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black." 
stylish_sette_price = 180.50 

#luxurious_lamp 
Luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15 

#tax
sale_tax = 0.088 

#customer1
customer_one_total = 0 
customer_one_itemization = ""

customer_one_total += 254.00
customer_one_itemization += "One Lovely Loveseat, "

customer_one_total += 52.15
customer_one_itemization += "One Luxurious Lamp"
#final checkout calculation
customer_one_tax = (customer_one_total * sale_tax)
customer_one_total += customer_one_tax

#recipt 
print("Customer One Items:")
print (customer_one_itemization) 
print("Customer One Total:")
print ("$", customer_one_total)             
