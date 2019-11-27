 REMOVE_LIST = ["a", "an", "as", "at", ...]

 remove = '|'.join(REMOVE_LIST)
 regex = re.compile(r'('+remove+')', flags=re.IGNORECASE)
 out = regex.sub("", text)