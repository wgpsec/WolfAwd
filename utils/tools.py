from optparse import OptionParser
def parse_options():
    parser = OptionParser()
    parser.add_option("-m", "--module", \
                      dest="module", default="attack", \
                      help="Input the  func module here :)")
    parser.add_option("-p", "--poc", \
                      dest="vuln", default="chinaz",
                      help="The vuln you want to use")
    parser.add_option("-a", "--action", \
                      dest="action", default="get_flag",
                      help="The action you want to do")
    parser.add_option("-c", "--command", \
                      dest="command", default="",
                      help="The command you want to exec")
    parser.add_option("-t", "--targets", \
                      dest="targets", default="",
                      help="The target you want to attack")
    (options, args) = parser.parse_args()

    return options
