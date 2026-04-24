# Python treats some values as False automatically.

# False
# 0
# 0.0
# None
# ''
# []
# {}
# set()

# Everything else usually True.

name = ""

if name:
    print("Entered")
else:
    print("Empty")