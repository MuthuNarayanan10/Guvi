def areplace(s, old, new):
    li = s.split(old, 1) #Split only once
    return new.join(li)
 rreplace('Helloworld, hello world, hello world', 'hello', 'hi')