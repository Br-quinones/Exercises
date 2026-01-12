# first exercise of decorations 

def adult_only(func):
    def checking(old_years):
        if old_years < 18:
            print("No, you cannot pass.")
        else:
            func()
    return checking

@adult_only
def enter_club():
    print("Welcome to the VIP section!")

enter_club(18)

# 31 minute