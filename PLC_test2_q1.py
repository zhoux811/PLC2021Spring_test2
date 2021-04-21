import re, string

f_name = 'sample2.txt'


def t2q1(input_string):
    if input_string == '\n':
        print('### empty line')
        return 0

    char_ptr = 0
    while char_ptr < len(input_string):
        result = re.match(r'[@$%][a-zA-Z_][A-Za-z0-9_]*', input_string[char_ptr:])
        if result:
            # print('### perl identifier')
            if result.group(0)[0] == '$':
                print('\tperl id private scalar:\t ' + result.group(0)) if result.group(0)[1] == '_' \
                    else print('\tperl id public scalar:\t ' + result.group(0))
            elif result.group(0)[0] == '@':
                print('\tperl id private array:\t ' + result.group(0)) if result.group(0)[1] == '_' \
                    else print('\tperl id public array:\t ' + result.group(0))
            elif result.group(0)[0] == '%':
                print('\tperl id private hash:\t ' + result.group(0)) if result.group(0)[1] == '_' \
                    else print('\tperl id public hash:\t ' + result.group(0))
            char_ptr += len(result.group(0))
        else:
            # print('didnt find perl stuff')
            result = re.match(r' ', input_string[char_ptr:])
            if result:
                # print('\t### a whitespace')
                char_ptr += 1
            else:
                result = re.match(r'(^str\s|^int\s|^void\s|^char\s|^float\s)', input_string[char_ptr:])
                if result:
                    print('\ttype declaration:\t\t ' + result.group(0))
                    char_ptr += len(result.group(0)) - 1
                else:
                    result = re.match(r'(&&|\|\||!=|==)', input_string[char_ptr:])
                    if result:
                        r = result.group(0)
                        if r == '||':
                            print('\tlen 2 logical operator\t ' + r + '\t\t\tOR')
                        elif r == '&&':
                            print('\tlen 2 logical operator\t ' + r + '\t\t\tAND')
                        elif r == '!=':
                            print('\tlen 2 logical operator\t ' + r + '\t\t\tNOT EQUAL')
                        elif r == '==':
                            print('\tlen 2 logical operator\t ' + r + '\t\t\tNOT EQUAL')
                        char_ptr += 2
                    else:
                        result = re.match(r'[!=\+\-\*\/\%\(\)\{\}\[\]]', input_string[char_ptr:])
                        if result:
                            r = result.group(0)
                            if r == '+':
                                print('\tlen 1 Special character\t ' + r + '\t\t\taddition')
                            elif r == '-':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tsubstraction')
                            elif r == '*':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tmultiplication')
                            elif r == '/':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tdivision')
                            elif r == '=':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tassign')
                            elif r == '!':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tNOT')
                            elif r == '%':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tmodulo operation')
                            elif r == '[':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tclose array index parameter')
                            elif r == ']':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tclose array index parameter')
                            elif r == '{':
                                print('\tlen 1 Special character\t ' + r + '\t\t\topen code block')
                            elif r == '}':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tclose code block')
                            elif r == '(':
                                print('\tlen 1 Special character\t ' + r + '\t\t\topen function parameter')
                            elif r == ')':
                                print('\tlen 1 Special character\t ' + r + '\t\t\tclose function parameter')
                            char_ptr += 1
                        else:
                            result = re.match(r'(\'.\')|'
                                              r'(u8\'.\')|'
                                              r'(\'\\[A-Za-z]\')|'
                                              r'(u\'.\')|'
                                              r'(U\'.\')|'
                                              r'(L\'.\')',
                                              input_string[char_ptr:])
                            if result:
                                print('\tc-char literal\t\t\t ' + result.group(0))
                                char_ptr += 3
                            else:
                                result = re.match(r'(\".*?\")', input_string[char_ptr:])
                                if result:
                                    print('\tjava string literal\t\t ' + result.group(0))
                                    char_ptr += len(result.group(0))
                                else:
                                    result = re.match(r'\d?\.\d?', input_string[char_ptr:])
                                    if result:
                                        print('\tC-Style float literal:   ' + result.group(0))
                                        char_ptr += len(result.group(0))
                                    else:
                                        result = re.match(r'\d+', input_string[char_ptr:])
                                        if result:
                                            print('\tC-Style integer literal: ' + result.group(0))
                                            char_ptr += len(result.group(0))
                                        else:
                                            result = re.match(r'[A-Za-z][A-Za-z_0-9]*', input_string[char_ptr:])
                                            if result:
                                                print('\ttypical identifier: \t' + result.group(0))
                                                char_ptr += len(result.group(0))
                                            else:
                                                print('\teverything else(special char): \t' + input_string[char_ptr])
                                                char_ptr += 1


f = open(f_name)

line_n = 1
for l in f:
    print('\nline ' + str(line_n) + ' : ' + l[:-1])
    t2q1(l)
    line_n += 1
