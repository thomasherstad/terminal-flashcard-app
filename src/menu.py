#TODO: Add fail safe for inputs outside of choices
def make_menu(header: str, menu_options: list, back=False, back_label='Back') -> int:
    #Returns list index
    number = 1
    print(header)
    for item in menu_options:
        print(f'{number}. {item.capitalize()}')
        number += 1
    if back == True:
        print(f'0. {back_label}')
    menu_choice = int(input())
    #clear_terminal()
    return menu_choice - 1