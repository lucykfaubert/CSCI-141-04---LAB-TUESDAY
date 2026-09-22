US_form = input("Enter the date in US format (MM/DD/YY): ")
extended_format = "20" +US_form[6:8] + "-" + US_form[0:2] + "-" + US_form[3:5]
print("The date in ISO 8601 extended format is:", extended_format)