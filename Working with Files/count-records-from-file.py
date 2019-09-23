'''
    Count records in large files
'''
def countFile(fqdn):
    '''
        Count records in large files
    '''
    with open(fqdn,encoding="latin_1") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

if __name__ == '__main__':
    fqdn = input('File Name: ')
    countFile(fqdn)