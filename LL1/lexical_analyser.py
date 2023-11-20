import re

def lex(filename):
    print('---------------------------------------------------------------------------------\nLexical Analysis\n---------------------------------------------------------------------------------')
    f = open(filename, 'r')

    operators = {'=': 'Assignment Operator', '+': 'Additon Operator', '-': 'Substraction Operator', '>': 'comparision operator',
                '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'increment Operator', '--': 'Decrement Operator'}
    optr_keys = operators.keys()

    comments = {r'//': 'Single Line Comment', r'/*': 'Multiline Comment Start',
                r'*/': 'Multiline Comment End', '/**/': 'Empty Multiline comment'}
    comment_keys = comments.keys()

    header = {'.h': 'header file'}
    header_keys = header.keys()

    sp_header_files = {'<stdio.h>': 'Standard Input Output Header',
                    '<string.h>': 'String Manipulation Library'}

    macros = {r'#\w+': 'macro'}
    macros_keys = macros.keys()

    datatype = {'int': 'Integer', 'float': 'Floating Point',
                'char': 'Character', 'long': 'long int'}
    datatype_keys = datatype.keys()

    keyword = {'return': 'Return Value From Block'}
    keyword_keys = keyword.keys()

    delimiter = {';': 'Delimeter Line Ends(;)'}
    delimiter_keys = delimiter.keys()

    while_block = {'while': 'Enter While Loop',
                'end while': 'Exit While Loop'}
    while_block_keys = while_block.keys()

    blocks = {'begin': 'Enter Block',
            'end': 'Exit Block\nTokens generated successfully'}
    block_keys = blocks.keys()

    builtin_functions = {'printf': 'Prints Lines'}

    non_identifiers = ['_', '-', '+', '/', '*', '`', '~', '!', '@', '#', '$', '%', '^',
                    '&', '*', '(', ')', '=', '|', '"', ':', ';', '{', '}', '[', ']', '<', '>', '?', '/']

    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    dataFlag = False


    i = f.read()

    count = 0
    program = i.split('\n')

    for line in program:
        count = count+1
        print('\033[1m' + "Line #", count, line + '\033[0m'+'\n')

        tokens = line.split(' ')
        if 'end' in tokens and 'while' in tokens:
            tokens = ['end while']
        while '' in tokens:
            tokens.remove('')
        print("Tokens are", tokens)
        print('properties:')
        for token in tokens:

            if '\r' in token:
                position = token.find('\r')
                token = token[:position]
            if token in while_block_keys:
                print(while_block[token])
            if token in block_keys:
                print(blocks[token])
            if token in optr_keys:
                print("Operator is: ", operators[token])
            if token in comment_keys:
                print("Comment Type: ", comments[token])
            if token in macros_keys:
                print("Macro is: ", macros[token])
            if '.h' in token:
                print("Header File is: ", token, sp_header_files[token])
            if '()' in token:
                print("Function named", token)

            if dataFlag == True and (token not in non_identifiers) and ('()' not in token) and (token not in numerals):
                print("Identifier: ", token)
            if token in numerals:
                print("Numeral: ", token)
            if token in datatype_keys:
                print("type is: ", datatype[token])
                dataFlag = True

            if token in keyword_keys:
                print(keyword[token])

            if token in delimiter:
                print("Delimiter", delimiter[token])
            if '#' in token:
                match = re.search(r'#\w+', token)
                print("Header", match.group())
            if token in numerals:
                print(token, type(int(token)))
        

        dataFlag = False

        print('------------------------------------------------------')
    f.close()
