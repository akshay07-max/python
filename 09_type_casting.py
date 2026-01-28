# Interactive User Profile Program

print("=== User Profile Creator ===")
print()

# Taking inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
city = input("Enter your city: ")
is_student = input("Are you a student? (yes/no): ")

# Processing
birth_year = 2024 - age
height_cm = height * 30.48  # Convert feet to cm

# Display profile
print("\n" + "="*40)
print("YOUR PROFILE")
print("="*40)
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Birth Year: {birth_year}")
print(f"Height: {height} feet ({height_cm:.2f} cm)")
print(f"City: {city}")
print(f"Student Status: {is_student}")
print("="*40)
Example run:
=== User Profile Creator ===

Enter your name: Rahul
Enter your age: 22
Enter your height in feet: 5.9
Enter your city: Mumbai
Are you a student? (yes/no): yes

========================================
YOUR PROFILE
========================================
Name: Rahul
Age: 22 years old
Birth Year: 2002
Height: 5.9 feet (179.83 cm)
City: Mumbai
Student Status: yes
========================================