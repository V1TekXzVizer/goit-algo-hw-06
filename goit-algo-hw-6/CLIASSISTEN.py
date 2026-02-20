from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be empty")
        super().__init__(name)
    

class Phone(Field):
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError("Phone cannot be empty")
        if len(value) != 10:
            raise ValueError("Phone must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone)) 
    
    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]
    
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break
            else:
                raise ValueError("Phone not found")
    
    def find_phone(self, phone: str) -> Phone:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    def find(self, name: str) -> Record:
        if name not in self.data:
            raise ValueError("Contact not found")
        return self.data[name]
    def delete(self, name: str) -> None:
        if name not in self.data:
            raise ValueError("Contact not found")
        del self.data[name] 
    def __str__(self):
        if not self.data:
            return "Address book is empty"
        result = "Address book:\n"
        for record in self.data.values():
            result += f"{record}\n"
        return result

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")