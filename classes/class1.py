class g:
    def ini(s):
        s.input_string = ""

    def gS(s1):
        s1.input_string = input()

    def p(s2):
        print("String in upper case:", s2.input_string.upper())

gans = g()
gans.gS()
gans.p()