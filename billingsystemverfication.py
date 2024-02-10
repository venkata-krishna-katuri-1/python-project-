def search_bill_by_id(customer_id):
    with open('customer_data.txt', 'r') as file:
        lines = file.readlines()

    found = False
    bill_details = []

    for line in lines:
        if customer_id in line:
            found = True
        if found:
            bill_details.append(line.strip())
        if found and "customer" in line.lower():
            break  # Stop reading when the keyword "customer" is found

    if found:
        return bill_details
    else:
        return ["Bill not found."]

# Example usage:
search_id = input("Enter the customer ID to search for: ")
result = search_bill_by_id(search_id)

if "Bill not found." in result:
    print("Bill not found.")
else:
    print("\n\nBILL DETAILS\n" + "-" * 60)
    for line in result:
        print(line)
    if result and "customer" in result[-1].lower():
        file_path = 'customer_data.txt'  
        try:
            with open(file_path, 'r') as file:
                line_count = 0
                max_lines = 20  # Change this to the number of lines you want to read

                for line in file:
                    print(line.strip())
                    line_count += 1

                    if line_count >= max_lines:
                        break

            print("-" * 60 + "\n")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", str(e))
