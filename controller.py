"""Controller."""


# main.py: Controller
# Autor(s): Pierre Abraham Mulamba
# Date of creation (modification): 20180525 (20180525)

# import os
import datetime
import random
from employee import Employee, employee_sort
from subscriber import Subscriber
from operator import attrgetter


def main():
    """Controller of the Library Management Inventory System."""
    message = 'Library Management Inventory System'

    # DATA STRUCTURE
    numbers = [1, 1, 2, 1, 3, 4, 7, 8, 7, 9, 9]
    li = [1, -3, 2, -6, 3, -4, -5]  # list
    tup = (9, 8, 1, 2, 7, 3, 6, 4, 5)  # tuple
    names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
    heros = ['Batman', 'Superman', 'Spiderman', 'Wolveringe', 'Deadpool']

    first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'John']
    last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart']
    street_names = ['Antonio', 'Allard', 'Shevchenko', 'conde', 'Tomba']
    cities_names = ['Laval', 'Montreal', 'Saskatoon', 'Ottawa', 'Toronto']
    provinces_names = ['QC', 'ON', 'BC', 'AB', 'NB', 'PE', 'NS', 'MB', 'SK']
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    try:

        fin = open('test.txt')
        fout = open('test_out.txt', 'w')

        tmp = random.choices(names, k=10)
        st = {name for name in tmp}  # set comprehension

        dic = {hero: name for hero, name in zip(heros, names) if name != 'Peter'}
        dic_qa = dict(sorted((answer, question)
                             for question, answer in dict(zip(questions, answers)).items()))
        # print("I am {Batman}. I am {Superman}. I am {Wolveringe}. I am {Blackpanther}".format(**dic))

        s_dic = sorted((name, hero) for hero, name in dic.items())
        final_dic = dict(s_dic)

        s = {number for number in numbers}  # create a set
        # Generator expression
        gen = (number*number for number in numbers)

        # SORTING
        li.sort()
        s_tup = sorted(tup)

        e1 = Employee('Carl', 37, 70000)
        e2 = Employee('Sarah', 29, 8000)
        e3 = Employee('John', 43, 9000)
        employees = [e1, e2, e3]
        s_employees = sorted(employees, key=attrgetter('age_'))

        sub1 = Subscriber('1839456', 'John', 'Doe', 23)
        # sub1.print()

    except AttributeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except IOError as e:
        print(e)
    except KeyError as e:
        print("Missing {} key".format(e))
    except NameError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception:
        print('Unknown Exception Thrown')
    else:
        print(datetime.datetime.now())
        print(f'{message.upper()}')
        print(tmp)
        print(st)
        print(final_dic)
        print(s)

        with fin:
            with fout:
                for line in fin:
                    fout.write(line)

        for num in gen:
            print(num)

        print(li)
        print(s_tup)

        print(sub1.__repr__())
        print(sub1.__str__())

        for i in range(Employee.nEmployees):
            print(employees[i])

        print(employees)

        print('SORTING WITH attrgetter')
        print(s_employees)

        print('SORTING WITH employee_sort')
        s_employees = sorted(employees, key=employee_sort)
        print(s_employees)

        print(dic_qa)

        with open('fake_data.txt', 'w') as fout_data:
            for num in range(100):
                first = random.choices(first_names)
                last = random.choices(last_names)
                phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'
                street_num = random.randint(100, 999)
                street = random.choices(street_names)
                city = random.choices(cities_names)
                province = random.choices(provinces_names)
                zip_code = random.randint(10000, 99999)
                address = f'{street_num} {street[0]} Av., {city[0]} {province[0]} {zip_code}'
                email = first[0].lower() + '.' + last[0].lower() + '@bogusemail.com'

                fout_data.write(f'{first[0]} {last[0]} \n{phone}\n{address}\n{email}\n\n')

    finally:
        fout.close()
        fin.close()
        print('Program Ended Successfully!')


if __name__ == '__main__':
    main()
