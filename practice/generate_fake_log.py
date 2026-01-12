# Generate employee data 
import faker
import pandas as pd

fake = faker.Faker('en_IN')

def generate_employee():
    '''Generate fake data of 100 employees'''
    phone_number = fake.numerify(text="##########")
    return {
        "Employee_ID": f"EMP{fake.random.randint(1, 9999):04d}",
        "Name": fake.name(),
        "Gender": fake.random.choice(["Male", "Female"]),
        "Age": fake.random.randint(22, 60),
        "Department": fake.random.choice([
            "IT", "HR", "Finance", "Operations", "Marketing"
        ]),
        "Salary": fake.random.randint(300000, 1500000),
        "Phone": phone_number,
        "Email": fake.email(),
        "Address": fake.address().replace('\n', ' ').replace(',', '')
    }
    
    with open('employee_data.csv', "w", encoding="UTF-8") as file:
        # Heading
        file.write("Employee_ID,Name,Gender,Age,Department,Salary,Phone,Email,Address\n")
        for i in range(1, 100):
            emp = generate_employee()
            
            file.write(f"{emp['Employee_ID']},{emp['Name']},{emp['Gender']},{emp['Age']},{emp['Department']},"
                        f"{emp['Salary']},{emp['Phone']},{emp['Email']},{emp['Address']}\n")
            
if __name__ == '__main__':
    generate_employee()