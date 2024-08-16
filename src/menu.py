#TODO: Add fail safe for inputs outside of choices
def make_menu(header: str, menu_options: list, back=False, back_label='Back', horizontal=False) -> int:
    #Returns list index
    number = 1
    if horizontal == True:
        end = '\t'
    else:
        end = '\n'
    print(header)
    for item in menu_options:
        print(f'{number}. {item.capitalize()}', end=end)
        number += 1
    if back == True:
        print(f'0. {back_label}')
    menu_choice = int(input())
    #clear_terminal()
    return menu_choice - 1


if __name__ == '__main__':
    options = ['Option1', 'Option2', 'Option3', 'Option4']
    a = make_menu('What do you choose?', options, back=True, back_label='Back', horizontal=True)
    print(f'You chose {options[a]}')

