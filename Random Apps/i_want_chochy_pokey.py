def stall_for_time():
    input("")

def its_chochy_pokey():
    print("""
THERE HE IS!

ilu <3
BFFs 4ever

When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state
And trouble deaf heaven with my bootless cries
And look upon myself and curse my fate,
Wishing me like to one more rich in hope,
Featured like him, like him with friends possess'd,
Desiring this man's art and that man's scope,
With what I most enjoy contented least;
Yet in these thoughts myself almost despising,
Haply I think on thee, and then my state,
Like to the lark at break of day arising
From sullen earth, sings hymns at heaven's gate;
For thy sweet love remember'd such wealth brings
That then I scorn to change my state with kings.
""")

def not_chochy_pokey():
    chochy_pokey_again = input("\nLet's try this again ... Who are you? \n").lower()
    if chochy_pokey_again == ("chochy-pokey" or "chochy pokey" or "chochypokey"):
        its_chochy_pokey()
    else:
        print("Go away! I want Chochy-Pokey!")
        not_chochy_pokey()

def i_want_chochy_pokey():
    chochy_pokey = input("Who are you? \n").lower()
    if chochy_pokey == ("chochy-pokey" or "chochy pokey" or "chochypokey"):
        its_chochy_pokey()
    else:
        print("Go away! I want Chochy-Pokey!")
        not_chochy_pokey()

i_want_chochy_pokey()

stall_for_time()
