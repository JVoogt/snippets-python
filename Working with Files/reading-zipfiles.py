def readDataFromZip(fqdn):
    record = []
    with gzip.open(fqdn, "rb") as text:
        for lines in text:
            record.append(line.decode("latin_1"))

    return record

if __name__ == '__main__':
    fqdn = input('Please enter file name: ')
    file_obj = readDataFromZip(fqdn)
    