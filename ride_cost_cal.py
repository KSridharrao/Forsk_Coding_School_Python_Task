"""Python program to find the travelling charges of an employee """
name=input("Enter your name:")
distance_travelled=int(input("Enter the distance travelled from your home to office (in kms):"))
cost=int(input("Enter the cost of the diesel per litre:"))
avg_fuel=int(input("Enter the mileage of your vehicle per litre of diesel:"))
fuel_consumption=(distance_travelled*2)/avg_fuel
cost_per_day=(cost*fuel_consumption)
print(name , " , the total travelling charge for you per one day is ",cost_per_day, " INR (Indian Rupees) ")
