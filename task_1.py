class Solution():
    def __init__(self, param):
        self.author = 'Hasim Imahdudin'
        self.param = param

    def process(self):
        found_same = {}
        list_input_string = self.param["list_input_string"]
        print '\nInput: {}'.format(list_input_string)

        for i in range(len(list_input_string)):
            if list_input_string[i] not in found_same:
                found_same[list_input_string[i]] = 1
            else:
                found_same[list_input_string[i]] += 1

        found_first = ''
        found_list = []
        for i in range(len(list_input_string)):
            char = list_input_string[i]
            if found_first != '' and found_first != char:
                continue

            if found_same[char] > 1:
                found_first = char
                found_list.append(i + 1)

        return found_list


def test_1():
    # n = input("Input N: ")
    # list_input_string = []
    # for i in range(n):
    #     s = raw_input("String {}: ".format(i + 1))
    #     list_input_string.append(s)

    n = 4
    list_input_string = ['abcd', 'acbd', 'aaab', 'acbd']
    params = {
        "n": n,
        "list_input_string": list_input_string
    }
    handler = Solution(params)
    rsp = handler.process()
    if rsp:
        print 'Output: {}'.format(rsp)
    else:
        print 'Output: False'


def test_2():
    # n = input("Input N: ")
    # list_input_string = []
    # for i in range(n):
    #     s = raw_input("String {}: ".format(i + 1))
    #     list_input_string.append(s)

    n = 5
    list_input_string = ['pisang', 'goreng', 'enak', 'sekali', 'rasanya']
    params = {
        "n": n,
        "list_input_string": list_input_string
    }
    handler = Solution(params)
    rsp = handler.process()
    if rsp:
        print 'Output: {}'.format(rsp)
    else:
        print 'Output: False'


def test_3():
    # n = input("Input N: ")
    # list_input_string = []
    # for i in range(n):
    #     s = raw_input("String {}: ".format(i + 1))
    #     list_input_string.append(s)

    n = 11
    list_input_string = ['Satu', 'Sate', 'Tujuh', 'Tusuk', 'Tujuh', 'Sate', 'Bonus', 'Tiga', 'Puluh', 'Tujuh', 'Tusuk']
    params = {
        "n": n,
        "list_input_string": list_input_string
    }
    handler = Solution(params)
    rsp = handler.process()
    if rsp:
        print 'Output: {}'.format(rsp)
    else:
        print 'Output: False'


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
