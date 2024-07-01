# Frozensets are like sets , but  they are immutable
# You can modify `set` elements anytime , but `frozensets`cannot be changed once created

data={"Name":"Roger", "Pin": 3056, "ActNo":989}
fset= frozenset(data)
print(fset)
