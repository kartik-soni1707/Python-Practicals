try:#try something
    a = int(input('Enter Val1:'))
    b = int(input('Enter Val2:'))
    print(a/b)
except ZeroDivisionError:
    print('No div by 0!!')
except ValueError:
    print('Enter numbers!!')

except Exception as err:#handle errors here
    print('Something wicked happend!!:',err)

finally:#this executes anyways
    print('You finally made it here!!')