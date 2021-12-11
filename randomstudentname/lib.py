def try_me():
    print('Welcome to batch 705! ¯\_(ツ)_/¯')
    print('This is a test of the try_me function, and as an example we will allow you to enter a string and know the length of it:')
    text = input('> ')
    if len(text) > 0:
        print(f'Your string is {len(text)} characters long.')
    else:
        print("Please, don't press just Enter! We will give you another chance.")
        try_me()
    print('Thanks for playing!')
