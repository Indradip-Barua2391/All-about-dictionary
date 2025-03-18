country_code = {
    
    "North Korea" : "00850",
    "Australia" : "0025",
    "Bangladesh" : "00880"
} 

print("Country code for Bangladesh - ")
print(country_code.get("Bangladesh", "Not found"))

print("Country code for Japan -")
print(country_code.get("Japan", "Not found"))