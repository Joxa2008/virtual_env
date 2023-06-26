"""
#######################################################################################################################
Importing moduls/Importing moduls/Importing moduls/Importing moduls/Importing moduls/Importing moduls/Importing moduls/
#######################################################################################################################
"""
import requests
import os

def NBU_bank():

########################################################################################################################
#Getting data from NBU/Getting data from NBU/Getting data from NBU/Getting data from NBU/Getting data from NBU/Getting #
########################################################################################################################

    data = requests.get('https://nbu.uz/uz/exchange-rates/json/').json()

########################################################################################################################
#Creating function for often using parts of code/Creating function for often using parts of code/Creating function for #
########################################################################################################################

    def Buy():
        print('Buy')
        buy_price = data[que1-1]['nbu_cell_price']
        while True:
            try:
                buy_num = float(input(f'Write how many {currency_name} do you want to buy: '))
                break
            except ValueError:
                print('Incorrect!')
                os.system('clear')

        print(f'\n\n    Please pay: {float(buy_price) * int(buy_num)}UZS')
        print('    Thank you for using this app!')
    
    def Sell():
        print('Sell')
        sell_price = data[que1-1]['nbu_buy_price']
        while True:
            try:
                sell_num = float(input(f'Write how many {currency_name} do you want to buy: '))
                break
            except ValueError:
                print('Incorrect!')
                os.system('clear')

        print(f'\n\n {sell_num} {currency_name} equal to: {sell_num * float(sell_price)} UZS')
        print('    Thank you for using this app!')
        return None



    x = [i['code'] for i in data]

########################################################################################################################
#Showing all options of choosing currency / Showing all options of choosing currency / Showing all options of choosing #
########################################################################################################################


    num = 0
    os.system('clear')    
    for i in range(len(x)):
        if i == 0:
            print('-'*((len(x[i])+7)*4), end='')
        if i % 4 == 0:
            print()
        if 0 <= i < 9:
            print(' ' + str(i+1)+'.', x[i], end=' | ')
        else:
            print(str(i+1)+'.', x[i], end=' | ')

    print('\n' + '-'*((len(x[i])+7)*4))

    que1 = input('\nChoose the currency (write the number or name): ').strip().upper()

    while True:
        try:
            if 1 <= int(que1) <= len(x):
                    que1 = int(que1)
                    break
            else:
                int('lnml')
        except:
            if que1 in x:
                for i in x:
                    if i == que1:
                        que1 = x.index(i)+1
                        break
            else:
                print('Ther is no such currency!')
                que1 = input('\nChoose the currency (write the number or name): ').strip().upper()

    os.system('clear') 

    currency_name = data[que1-1]['title']

########################################################################################################################
#Checking are there any emty parts in data / Checking are there any emty parts in data / Checking are there any emty p #
########################################################################################################################

    if (data[que1-1]['nbu_buy_price'] == '' or data[que1-1]['nbu_buy_price'] == '--') and (data[que1-1]['nbu_cell_price'] == '' or data[que1-1]['nbu_cell_price'] == '--'):
        print('\nNow there is no such data in our server please try later')
        return ':('
    
    elif (data[que1-1]['nbu_buy_price'] == '' or data[que1-1]['nbu_buy_price'] == '--') and (data[que1-1]['nbu_cell_price'] != '' or data[que1-1]['nbu_cell_price'] != '--'):
        Buy()
        return None

    elif (data[que1-1]['nbu_buy_price'] != '' or data[que1-1]['nbu_buy_price'] != '--') and (data[que1-1]['nbu_cell_price'] == '' or data[que1-1]['nbu_cell_price'] == '--'):
        Sell()
        return None


    os.system('clear') 
    print('\n\n1. Buy', x[que1-1])
    print('2. Sell', x[que1-1])



########################################################################################################################
#Fixing Errors and Counting part /  Fixing Errors and Counting part / Fixing Errors and Counting part / Fixing Errors a#
########################################################################################################################

    while True:
        que2 = input('Choose option: ').strip().title()
        os.system('clear') 
        try:
            if 1 == int(que2):
                Buy()
                break    
            elif 2 == int(que2):
                Sell()
                break
            else:
                print('Incorrect option!')
                print('\n\n1. Buy', x[que1-1])
                print('2. Sell', x[que1-1])

        except ValueError:
            if que2 == 'Buy':
                Buy()
                break

            elif que2 == 'Sell':
                Sell()
                break
            else:
                print('Incorrect option!')
                print('\n\n1. Buy', x[que1-1])
                print('2. Sell', x[que1-1])
                
    print('\nNBU.uz')

"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//End of main function # End of main function # End of main function # End of main function # End of main function # End of m//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
            
NBU_bank()