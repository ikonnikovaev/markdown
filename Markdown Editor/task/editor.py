# write your code here
formatters_string = 'plain bold italic header link inline-code ordered-list unordered-list new-line'

#'plain bold italic header link inline-code new-line'

special_commands_string = '!help !done'
formatters = formatters_string.split()
special_commands = special_commands_string.split()
prompt_string = 'Choose a formatter: '
help_string = f'Available formatters: {formatters_string}\n' \
              f'Special commands: {special_commands_string}'
error_string = 'Unknown formatting type or command'

def set_header_parameters():
    level = int(input('Level: '))
    while level not in range(1, 7):
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    text = ask_for_text()
    return text, level

def apply_header_format(text, level):
    return f'{"#" * level} {text}\n'

def apply_font_format(text, font):
    if font == 'plain':
        return text
    if font == 'bold':
        return f'**{text}**'
    if font == 'italic':
        return  f'*{text}*'
    if font == 'inline-code':
        return f'`{text}`'

def set_list_parameters():
    n_rows = int(input('Number of rows: '))
    while n_rows <= 0:
        print('The number of rows should be greater than zero')
        n_rows = int(input('Number of rows: '))
    elements = []
    for i in range(n_rows):
        elements.append(input(f'Row #{i + 1}').strip())
    return elements

def apply_list_format(elements, order):
    result = f''
    n = len(elements)
    for i in range(n):
        if order:
            result += f'{i + 1}. {elements[i]}\n'
        else:
            result += f'* {elements[i]}\n'
    return result



def set_link_parameters():
    label = input('Label: ')
    url = input('URL: ')
    return label, url

def apply_link_format(label, url):
    return f'[{label}]({url})'


def format_text(formatter):
    if formatter == 'header':
        text, level = set_header_parameters()
        return apply_header_format(text, level)
    if formatter in ['plain', 'bold', 'italic', 'inline-code']:
        text = ask_for_text()
        return apply_font_format(text, formatter)
    if formatter in ['ordered-list', 'unordered-list']:
        elements = set_list_parameters()
        order = False
        if formatter == 'ordered-list':
            order = True
        return apply_list_format(elements, order)

    if formatter == 'link':
        label, url = set_link_parameters()
        return apply_link_format(label, url)
    if formatter == 'new-line':
        return '\n'


def ask_for_text():
    text = input('Text: ').strip()
    return text


def act():
    full_text = ''
    while True:
        user_input = input(prompt_string)
        while user_input not in formatters + special_commands:
            print(error_string)
            print(prompt_string)
            user_input = input()
        if user_input == '!done':
            break
        elif user_input == '!help':
            print(help_string)
        elif user_input in formatters:
            text = format_text(user_input)
            full_text += text
            print(full_text)







text = '''
# John Lennon
or ***John Winston Ono Lennon***  was one of *The Beatles*.
Here are the songs he wrote I like the most:

- Imagine
- Norwegian Wood
- Come Together
- In My Life
- ~~Hey Jude~~ (that was *McCartney*)
'''
# print(text)
act()


