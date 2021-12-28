#Basic calculator for finding approximate post-tax income

import locale
locale.setlocale(locale.LC_ALL, '' )

def main():
        #Explains function of app, and then determines whether to calculate annual income from hourly wage or just calculate tax
        print('This is a basic income calculator. \nChoose to calculate an hourly rate or annual salary and this program will estimate your gross and post-tax annual income.\n \n')
        hourly_income_type = input('Calculate annual income from an hourly rate? Type yes/no: ')
        hourly_income_type = hourly_income_type.casefold()
        if hourly_income_type == 'yes':
                #Calculates income from hourly wage
                dollar_per_hour = input('Enter the dollar amount per hour you earn here: ')
                gross_dollar_year = float(dollar_per_hour) * 40 * 52
                gross_dollar_year = round(dollar_per_hour, 2)
                print(f'\nGross annual income: {locale.currency(gross_dollar_year, grouping=True)}' )
        elif hourly_income_type == 'no':
                #Only calculates taxes from annual salary
                gross_dollar_year = input('Enter your annual salary here: ')
                gross_dollar_year = float(gross_dollar_year)
                gross_dollar_year = round(gross_dollar_year, 2)
        else:
                input('Sorry, that input was not valid. Press ENTER to try again.')
                main()

        #if/elif statements to determine tax rate based on gross_dollar_year calculated income
        if gross_dollar_year in range(0, 9951):
                tax_rate = 0.10
        elif gross_dollar_year in range(9951, 40526):
                tax_rate = 0.12
        elif gross_dollar_year in range(40526, 86376):
                tax_rate = 0.22
        elif gross_dollar_year in range(86376, 164926):
                tax_rate = 0.24
        elif gross_dollar_year in range(164926, 209426):
                tax_rate = 0.32
        elif gross_dollar_year in range(209426, 523601):
                tax_rate = 0.35
        else:
                tax_rate = 0.37

        #Actually performs the tax calculations based on gross_dollar_year and tax_rate values
        tax_per_year = gross_dollar_year * tax_rate
        tax_per_year = round(tax_per_year, 2)
        print(f'\nAnnual amount of taxes deducted: {locale.currency(tax_per_year, grouping=True)}')
        income_after_tax = locale.currency(gross_dollar_year - tax_per_year, grouping=True)
        print(f'\nAnnual income (after taxes): {income_after_tax}')
        restart()

#Allows the program to be restarted
def restart():
        restart = input('\nCalculate a new income? Please type yes/no: ')
        restart = restart.casefold()
        if restart == 'yes':
                print('\n')
                main()
        elif restart == 'no':
                input('Press ENTER to exit the program.')
        else:
                input('Sorry, that input was not valid. Press ENTER to try again.')
                restart()

if __name__ == '__main__':
        main()