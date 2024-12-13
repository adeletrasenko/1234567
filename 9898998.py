def all_variants(text):
    if not text:
        yield ""
    else:
        for var in all_variants(text[1:]):
            
            yield var
            yield text[0] + var


a = all_variants("abc")
for i in a:
    print(i)
