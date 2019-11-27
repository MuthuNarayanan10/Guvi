def rreplace(s, old, new):
    li = s.rsplit(old, 1) #Split only once
    return new.join(li)
 rreplace('Helloworld, hello world, hello world', 'hello', 'hi')