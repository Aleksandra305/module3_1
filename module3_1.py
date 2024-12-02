calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result
def is_constains(string, list_to_search):
    string = str(string)
    list_to_search = list(list_to_search)
    count_calls()
    result = False
    for str_in_list in list_to_search:
        if string.lower() == str_in_list.lower():
            result = True
            break

    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_constains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_constains('cycle', ['recycling', 'cyclinc']))
print(calls)
