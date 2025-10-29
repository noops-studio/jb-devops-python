def main():
    year_inpute : int = int(input("Enter a year: "))
    if is_int(year_inpute):
        year = int(year_inpute)
        if is_leap_year(year):
            print(f"year {year} is a leap year")
        else:
            print(f"year {year} is not a leap year")
    else:
        print('please give only integer values as input')


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    main()
