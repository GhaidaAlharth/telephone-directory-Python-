#!/usr/bin/env python
# coding: utf-8

# In[1]:


phone_book = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}

def find_contact(phone_number):
    for name, number in phone_book.items():
        if number == phone_number:
            return name
    return None

def add_contact(name, phone_number):
    if len(phone_number) == 10 and phone_number.isdigit():
        phone_book[name] = phone_number
        print(f"تمت إضافة {name} إلى دليل الهاتف")
    else:
        print("رقم هاتف غير صالح")

def main():
    try:
        while True:
            print("\n1. البحث باسم الشخص")
            print("2. إضافة مستخدم جديد")
            print("3. الخروج")

            choice = input("اختر الخيار: ")

            if choice == '1':
                phone_number = input("أدخل رقم الهاتف: ")
                contact_name = find_contact(phone_number)
                if contact_name:
                    print(f"صاحب الرقم {phone_number} هو: {contact_name}")
                else:
                    print("Sorry, the number is not found")
                    
            elif choice == '2':
                new_name = input("أدخل اسم المستخدم الجديد: ")
                new_phone = input("أدخل رقم الهاتف: ")
                add_contact(new_name, new_phone)

            elif choice == '3':
                print("تم الخروج من البرنامج.")
                break

            else:
                print("خيار غير صالح، يرجى إعادة المحاولة.")

    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    main()


# In[ ]:




