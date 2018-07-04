import textwrap
#test

pp = int(200000)

class wtf_is_a_class:

#def textwrap(words):
    #print(textwrap.fill(words))

    def mathing(salary):
        if (salary < pp) == True:
            pp_difference = round(float(pp - salary))
            pp_fraction = round(float(pp / salary),1)
        if (salary >= pp) == True:
            pp_difference = round(float(salary - pp))
            pp_fraction = round(float(salary / pp),1)

    #def pp_numbers_wtextwrap(words):
        #print(textwrap.fill(words.format(pp, pp_difference, pp_fraction)))

def what_you_must_generate():
    salary = round(float(input("Roughly how much money do you make a year?\n$")))
    if (salary < pp) == True:
        pp_difference = round(float(pp - salary))
        pp_fraction = round(float(pp / salary),1)
        print("""
Did you know that to be considered valuable enough to keep your job, you have to make the company ${} a year?

That's ${}, or {} times more than what the company pays you.
""".format(pp, pp_difference, pp_fraction))
    if (salary >= pp) == True:
        pp_difference = round(float(salary - pp))
        pp_fraction = round(float(salary / pp),1)
        print("""
You'll be glad to know you make ${}, or {} times
more than what is needed to be considered valuable enough to keep your job.
Lucky you!
""".format(pp_difference, pp_fraction))

what_you_must_generate()


input("")
