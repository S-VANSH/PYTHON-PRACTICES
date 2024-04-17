# def new_group(group_name, members):
    group_name = "eagles"
    members = "sahil", "vansh", "harshdeep"
    
new_group= ("harsh", "sahil")
print(new_group)
new_group()


# def generate_band_name():
    print("welcome top the band name generate.")
    city = input("which city did you grow up in? \n")
    pet = input("what is the name if you have a pet? \n")
    return f"your band name could be(city.capitalize())(pet.captilaize())"

band_name = generate_band_name()
print(band_name)

#list
shopping_cart = ["kiwi", "banana", "apple", "orange"]
shopping_cart.append("chilli")
print(shopping_cart)
shopping_cart.remove("banana")
print(shopping_cart)
