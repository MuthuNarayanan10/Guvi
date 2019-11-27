def muthu_lstrip(input_str):
    leading = True
    for ch in input_str:
        if leading:
            if not ch.isspace():
              leading = False
              result = ch
        else:
            result += ch
    return result
input_str = "  Hello    "
result = muthu_lstrip(input_str)
print(repr(result))
