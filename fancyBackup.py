import os

def fancyBackup(fileName, pathName):
    # Parse expected inputs as combined string paths
    if pathName.endswith('/'):
        origPath='%s%s' %(pathName, fileName)
    ## If path doesn't end with / then add it before file name
    else:
        origPath = '%s/%s' %(pathName, fileName)
        
    ## Put backup file in a folder and append *.orig to filename
    localBackup = './backup/%s.orig' %(fileName)



    # Error handlers for missing files or directory
    ## Missing source
    if not os.path.exists(origPath):
        print('Source \'%s\' does not exist!' %(origPath))
        return '\n\nCheck path/filename and try again.'
    ## Missing backup directory
    if not os.path.exists('./backup/'):
        print('You removed ./backup/?\n\nYOU HEATHEN!\n\nLet me just make that for you...', end='')
        os.mkdir('./backup/')
        print('... Done!')


    # Check for existing *.orig backup
    if not os.path.exists(localBackup):
        ## If it backup.orig doesn't exist, write as that name
        b=open(localBackup, 'w')
    else:
        ## Otherwise, look for backup.orig[#], counting up from 0, until a free slot is found
        i=0
        while os.path.exists('%s[%d]' %(localBackup, i)):
            i += 1
        ## Append backup filename with free number then open file for use
        localBackup = '%s[%d]' %(localBackup, i)
        b=open(localBackup, 'w')

    # Write to backup file
    print('\n\nCopying source file to ./backup...\n\n###')
    with open(origPath, 'r') as f:
        for l in f:
            b.write(l)
##            # Print each line as it's written
##            print('%s' %(l))
    b.close()
    f.close()
    print('###\n\nSuccess!')
    return 'Wrote %s from %s\n' %(localBackup, origPath)
