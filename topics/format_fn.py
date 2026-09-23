#format_function

pi=3.14
print("pi={:.2f}".format(pi))



a=10
b=20
c=30

print("a=",a,"b=",b,"c=",c)
print("a={} b={} c={}" .format(a,b,c))



string = input()

vowel = "aeiouAEIOU"

ch = string[0]

if ch in vowel:
    print("vowel")
else:
    print("not a vowel")


dg=int(input())
if dg>=0 and dg <=9:
    print("SiNGLE dIGIT")

elif dg>9 and dg<=9:
        print("double digit")

else:
     print("none")