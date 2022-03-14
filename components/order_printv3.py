#list to store ordered pizzas
order_list = ['Margherita', 'Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
#list to store pizza prices
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {'name':'Levi','phone':'0217612487', 'house':'78', 'street':'Joe', 'suburb':'Idk'}

#print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format( cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))

print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1