import math
import logging

COINS = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]


def round_down(x):
    return int(math.floor(x / 100.0)) * 100


def handler(total, pay):
    if total > pay:
        return False
    return pay - total


def convert_change(total):
    results = []
    obj_change = {}
    try:
        change = []
        for i in COINS:
            while total > i:
                change.append(i)
                total = total - i

        for i in change:
            if i not in obj_change:
                obj_change[i] = 1
            else:
                obj_change[i] += 1
        for key, value in sorted(obj_change.iteritems(), reverse=True):
            results.append("{} lembar {}".format(value, key))

    except Exception as e:
        logging.error(e)

    return results


def format_currency(number, delimiter='.'):
    y = str(number)
    if len(y) <= 3:
        return y
    else:
        p = y[-3:]
        q = y[:-3]
        return format_currency(q) + '{}'.format(delimiter) + p


def process(total, pay):
    if type(total) == int and type(pay) == int:
        print 'Input'
        try:
            print 'Total belanja seorang customer: Rp {}'.format(format_currency(total))
            print 'Pembeli membayar: Rp {}'.format(format_currency(pay))

            print '\nOutput'
            ans = handler(total, pay)
            if ans:
                print 'Kembalian yang harus diberikan kasir: {},'.format(format_currency(ans))
                print 'dibulatkan menjadi: {}'.format(format_currency(round_down(ans)))
                print '\nPecahan Uang:'
                for i in convert_change(ans):
                    print i
            else:
                print 'False, Kurang Bayar'
            return
        except Exception as e:
            logging.error(e)
    print '\nOutput: Something Wrong, Please check your input!'


def test_1():
    print '\n-------'
    total = 700649
    pay = 800000
    process(total, pay)
    print '------------------------'


def test_2():
    print '\n-------'
    total = 700649
    pay = 700000
    process(total, pay)
    print '------------------------'


if __name__ == '__main__':
    test_1()
    test_2()
