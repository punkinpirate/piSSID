'''
You made this?

I made this.
'''

def forceOpen(fileName):
    try:
        f = open(fileName, 'r')
        f.close()
    # Create file if it doesn't exist
    except IOError as e:
        print(e, '\n\nCreating file, %s...' %(fileName))
        try:
            f = open(fileName, 'w')
            print('Success!\n')
            f.close()
        except Exception as e:
            print('ERROR ', e)
