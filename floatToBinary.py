import sys, getopt

def floatToBinary(number):
    space = ""
    num1 = int(number)
    while num1 > 0:
        if num1 % 2 == 0:
            space = space + "0"
        else:
            space = space + "1"
        num1 = int(num1 / 2)
    else:
        space = space[::-1]
    return space
def main(argv):
    input = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print ('floatToBinary -i <input>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('floatToBinary.py -i <input>')
            sys.exit()
        elif opt in ("-i"):
            input = arg
            nums = input.split('.')
            if len(nums)>2:
                print ('invalid float entered')
                sys.exit()
    binary = ""
    for x in nums:
        binary = binary+floatToBinary(x)
    print ('Input is ''', input)
    print ('Binary is ''', binary)
if __name__ == "__main__":
    main(sys.argv[1:])
