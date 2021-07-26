def process():
    closing = "}>]"
    opening = "}<["

    # TRUE
    # string = "{{[<>[{{}}]]}}"
    # string = "{<{[[{{[]<{{[{[]<>}]}}<>>}}]]}>}"


    # FALSE
    # string = "]"
    # string = "]["
    string = "[>]"
    # string = "[>"
    # string = "{{[<>[{{}}]]}}"
    # string = "[{}<[>]"
    # string = "{<{[[{{[]<{[{[]<>}]}}<>>}}]]}>}"
    # string = "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}"
    # string = "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<>>[]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]"

    pair = {
        "<": ">",
        "{": "}",
        "[": "]",
    }

    opening_pair = {
        ">": "<",
        "}": "{",
        "]": "[",
    }

    string_list = list(string)

    for i in range(0, len(string_list)):
        if string_list[0] in closing:
            print 'In Closing'
            return False

        if string_list[i] in closing:
            # opening = opening_pair[string_list[i]]
            # if opening not in string_list[0:i]:
            #     print string
            #     print string_list
            #     print string_list[0:i]
            #     print 'No Opening', "'{}'".format(string_list[i])
            #     return False
            # else:
            #     for m in string_list[0:i]:
            #         if m in opening:
            #             return False
            continue

        if string_list[i] == 'X':
            continue

        pairing = pair[string_list[i]]

        new_string_list = string_list

        k = 0
        empty_pair = True
        for j in range(0, len(new_string_list)):
            if new_string_list[j] == pairing:
                print string_list[i], new_string_list[j], i, j
                empty_pair = False
                k = j

        if empty_pair:
            print 'empty'
            return False
        print string
        print ''.join([str(elem) for elem in string_list])
        string_list[k] = 'X'
        string_list[i] = 'X'
        print ''.join([str(elem) for elem in string_list])
        print i, k
        print '--------------'
    return True


if __name__ == '__main__':
    rsp = process()
    print rsp
