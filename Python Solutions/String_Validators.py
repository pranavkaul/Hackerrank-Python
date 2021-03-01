from pip._vendor.distlib.compat import raw_input

s = raw_input()
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print (any(method(s) for c in s))



