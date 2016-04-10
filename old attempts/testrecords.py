#!/usr/badgeIn/python
from random import choice,randrange
import string
import linecache
from datetime import date


def alphanum(length):
    'returns random alphanumeric string with length $length'
    anout = ''
    for x in range(1,length):
        anout = anout + choice(string.digits + string.ascii_uppercase)
    return anout

def phone():
    'returns random phone number'
    phone = choice([ '(' + str(randrange(200,999)) + ')' + str(randrange(2000000,9999999)), str(randrange(200,999)) + '-' + str(randrange(200,999)) + '-' \
                    + str(randrange(2000,9999)), str(randrange(200,999)) + str(randrange(2000000,9999999))  ])
    return phone

def rdate(start,end):
    'returns random date'
    return date(randrange(int(start),int(end)), randrange(2,12), randrange(21,28)).strftime('%m/%d/%Y')

def rline(filename):
    'returns a random line from the given file'
    return linecache.getline(filename + '.txt', randrange(2,int(linecache.getline(filename + '.txt', 1).rstrip()))).rstrip()


def generate_person():
    'create a random person record'

    # Identifying Details
    sex = choice([ 'M','F','U' ])
    race = choice([ 'A','B','I','U','W' ])
    ssn = str(randrange(200101000, 665000000))
    hairColor = choice([ 'BLK','BLN','BLU','BRO','GRN','BRY','ONG','PLE','PNK','RED','SDY','WHI','XXX' ])
    eyeColor = choice([ 'BLK','BLU','BRO','GRN','HAZ','MAR','MUL','PNK','XXX' ])
    height = str(randrange(23,107))   # Pauline Musters to Robert Wadlow
    weight = str(randrange(25,1400))  # Average adult skeleton to Jon Minnoch
    
    # Name
    if sex == 'F':
        firstName = rline('ffnames')
        middleName = choice([ rline('ffnames'),'' ])
    else:
        firstName = rline('mfnames')
        middleName = choice([ rline('mfnames'),'' ])
    lastName = rline('lnames')
    suffix = choice([ '',choice([ 'JR','SR','I','II','III','IV','V','VI','VII','VIII','IX' ]) ])

    # Alias
    if sex == 'F':
        aliasFirstName = rline('ffnames')
        aliasMiddleName = choice([ rline('ffnames'),'' ])
    else:
        aliasFirstName = rline('mfnames')
        aliasMiddleName = choice([ rline('mfnames'),'' ])
    aliasLastName = rline('lnames')
    aliasSuffix = choice([ '',choice([ 'JR','SR','I','II','III','IV','V','VI','VII','VIII','IX' ]) ])
    
    # Date and place of birth
    dob = rdate(1900,2005)
    pobCountry = choice([ rline('iso3166'),'USA','USA','USA' ])
    if pobCountry == 'USA':
        pobState = choice([ 'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',\
                           'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY' ])
        pobCity = rline('cities')
        pobCounty = choice([ rline('cities') + ' county','','' ])
    else:
        pobState = ''; pobCity = ''; pobCounty = ''

    # Contact Information
    street1 = str(randrange(2,9999)) + ' ' + rline('streets') +\
                    choice([ '','','','','',' ST',' STREET',' BOULEVARD',' BLVD',' RD',' ROAD',' HWY',' HIGHWAY',' PL',' PLACE',' WAY' ])
    street2 = choice([ '',choice([ 'APT ','APARTMENT ','SUITE ','ROOM ','OFFICE ' ]) + choice([ '','# ' ]) + str(randrange(2,500)) ])
    city = rline('cities')
    state = choice([ 'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',\
                    'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY' ])
    postalCode = str(randrange(20001,99999)).rjust(5, '0')  + choice([ '','-' + str(randrange(2001,9999)).rjust(4, '0') ])
    country = rline('iso3166')
    email = firstName + '.' + lastName + choice([ '', dob[-4:] ]) + '@' + choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + choice(['.COM','.ORG','.EDU','.GOV','.NET','.CO.UK' ])
    homeTelephone = phone()
    businessTelephone = phone()
    mobileTelephone = phone()
    pagerTelephone = phone()
    faxTelephone = phone()

    # Citizenship
    citizenship = choice([ rline('iso3166'),'USA','USA','USA' ])
    if citizenship == 'USA':
        naturalizationDate = choice([ rdate(dob[ -4: ],2012),'','','' ])
        alienNumber = ''
        i94ArrivalDepartureFormNumber = ''
    else:
        naturalizationDate = ''
        alienNumber = 'A' + str(randrange(200,999)) + str(randrange(200,999)) + str(randrange(200,999))
        i94ArrivalDepartureFormNumber = str(randrange(20000000000,99999999999))
    if choice([ 'TRUE','FALSE' ]) == 'FALSE':  # Is this person a boring, no-document-needing American?
        passportCountry = choice([ rline('iso3166'),citizenship ])
        passportNumber = str(randrange(2000000001,9999999999)).rjust(10, '0')
        passportType = choice([ 'P','M','D' ])
        visaNumber = alphanum(7)
        visaType = rline('visatypes')
        visaClassOfAdmissionClassificationCode = alphanum(10)
        birthAbroadCertificationId = alphanum(10)
        certificateOfCitizenshipNumber = alphanum(8)
        certificateOfNaturalizationNumber = alphanum(9)
        ds1350CertificationOfBirthAbroad = alphanum(6)
        citizenshipCertificateId = alphanum(10)
        admissionId = alphanum(8)
    else:
        passportCountry = 'USA'
        passportNumber = str(randrange(2000000001,9999999999)).rjust(10, '0')
        passportType = choice([ 'P','M','D' ])
        visaNumber = ''
        visaType = ''
        visaClassOfAdmissionClassificationCode = alphanum(10)
        birthAbroadCertificationId = ''
        certificateOfCitizenshipNumber = ''
        certificateOfNaturalizationNumber = ''
        ds1350CertificationOfBirthAbroad = ''
        citizenshipCertificateId = ''
        admissionId = ''
        
    # employer info
    employerName = rline('employers')
    employerPOC = rline('mfnames') + ' ' + rline('lnames')
    employerTelephone = phone()
    employerEmail = employerPOC + '@' + employerName + '.' + choice([ 'COM','ORG','EDU','GOV','NET','CO.UK' ])
    employerStreet1 = str(randrange(2,9999)) + ' ' + rline('streets') + \
                      choice([ '','','','','',' ST',' STREET',' BOULEVARD',' BLVD',' RD',' ROAD',' HWY',' HIGHWAY',' PL',' PLACE',' WAY' ])
    employerStreet2 = choice([ '',choice([ 'APT ','APARTMENT ','SUITE ','ROOM ','OFFICE ' ]) + choice([ '','# ' ]) + str(randrange(2,500)) ])
    employerCity = rline('cities')
    employerState = choice([ 'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO',\
                            'MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY' ])
    employerPostalCode = str(randrange(20001,99999)).rjust(5, '0')  + choice([ '','-' + str(randrange(2001,9999)).rjust(4, '0') ])
    employerCountry = rline('iso3166')

    # Fingerprints
    caseProgram = choice([ 'AW','GA','ACP' ])
    if caseProgram == 'AW':
        caseSubprogram = choice([ 'FP','FPO','NFP','PFP' ])
    if caseProgram == 'GA':
        caseSubprogram = choice([ 'DCM-FP','DCM-PFP','MDW-PFP','MDW-FP','PCS-FP','PCS-PFP','TFS-FP','TFS-PFP' ])
    else:
        caseSubprogram = 'FPO'
    airportCode = rline('airportcodes')
    if caseSubprogram[ -2: ] == '-FP' or caseSubprogram[ -3: ] == 'FPO' or (caseProgram == 'AW' and caseSubprogram == 'FP'):
        fingerprintFileName = firstName + '_' + lastName + '_' + alphanum(6) + '.eft'
    else:
        fingerprintFileName = ''
    if caseSubprogram[ -3: ] == 'PFP':
        fingerprintCaseNumber = 'FAKE' + str(randrange(200000,999999))
    else:
        fingerprintCaseNumber = ''
                                                    
    # badge (maybe) ONLY FOR PROGRAM == AW,ACP
    if caseProgram == 'AW' or caseProgram == 'ACP':
        if randrange(1,10) >= 3:
            badgeId = choice(string.ascii_uppercase + string.digits) + choice(string.ascii_uppercase + string.digits) + choice(string.ascii_uppercase + string.digits) \
                        + choice(string.ascii_uppercase + string.digits) + choice(string.ascii_uppercase + string.digits)
            badgeIssueDate = rdate(2000,2011)
            badgeExpirationDate = str(badgeIssueDate)[ :6 ] + str(int(badgeIssueDate[ -4: ])+1)
            badgeAccessSecured = choice([ 'True','False' ])
            badgeAccessSterileArea = choice([ 'True','False' ])
            badgeAccessAOA = choice([ 'True','False' ])
            badgeAccessPublicArea= choice([ 'True','False' ])
            badgeAccessRT = choice([ 'True','False' ])
            badgeAccessSIDA = choice([ 'True','False' ])
            badgeLocalType = choice([ 'Blue','Red','Yellow','Black','Contractor','Security' ])
            badgeAirportCode = choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + choice(string.ascii_uppercase)        
            badgeArea = choice([ 'Food Court','Concourse A','Concourse B','Terminal 1','Terminal 2','Ticketting','Tarmac','Baggage Handling' ])
            badgeStatus = choice([ 'A','I','NI','P','R','S' ])
            if badgeStatus == 'I':
                badgeChangeReason = 'Leave of Absence'
            elif badgeStatus == 'NI':
                badgeChangeReason = 'Hiring Decision'
            elif badgeStatus == 'R':
                badgeChangeReason = choice([ 'Returned','Termination','Resignation','Deceased','TSA Direction','Lost','Expired' ])
            elif badgeStatus == 'S':
                badgeChangeReason = 'Employer Direction'
            else:
                badgeChangeReason = ''          
        else:
            badgeId = '';badgeIssueDate = '';badgeExpirationDate = '';badgeAccessSecured = '';badgeAccessSterileArea = '';badgeAccessAOA = '';badgeAccessPublicArea = ''
            badgeAccessRT = '';badgeAccessSIDA = '';badgeLocalType = '';badgeAirportCode = '';badgeStatus = '';badgeArea = '';badgeChangeReason = '';badgeStatus = ''
    else:
        badgeId = '';badgeIssueDate = '';badgeExpirationDate = '';badgeAccessSecured = '';badgeAccessSterileArea = '';badgeAccessAOA = '';badgeAccessPublicArea = ''
        badgeAccessRT = '';badgeAccessSIDA = '';badgeLocalType = '';badgeAirportCode = '';badgeStatus = '';badgeArea = '';badgeChangeReason = '';badgeStatus = ''
    
    # Return the field values to Main
    return firstName + seperator + middleName + seperator + lastName + seperator + suffix + seperator + aliasFirstName + seperator + aliasMiddleName + seperator + aliasLastName + seperator + aliasSuffix + seperator + dob + seperator + pobCountry + seperator + pobState + seperator + pobCity + seperator + pobCounty + seperator + sex + seperator + race + seperator + ssn + seperator + hairColor + seperator + eyeColor + seperator + height + seperator + weight + seperator + street1 + seperator + street2 + seperator + city + seperator + state + seperator + postalCode + seperator + country + seperator + homeTelephone + seperator + businessTelephone + seperator + mobileTelephone + seperator + pagerTelephone + seperator + faxTelephone + seperator + email + seperator + citizenship + seperator + naturalizationDate + seperator + passportCountry + seperator + passportNumber + seperator + passportType + seperator + visaNumber + seperator + visaType + seperator + visaClassOfAdmissionClassificationCode + seperator + birthAbroadCertificationId + seperator + certificateOfCitizenshipNumber + seperator + alienNumber + seperator + i94ArrivalDepartureFormNumber + seperator + certificateOfNaturalizationNumber + seperator + ds1350CertificationOfBirthAbroad + seperator + citizenshipCertificateId + seperator + admissionId + seperator + employerName + seperator + employerStreet1 + seperator + employerStreet2 + seperator + employerCity + seperator + employerState + seperator + employerPostalCode + seperator + employerCountry + seperator + employerEmail + seperator + employerTelephone + seperator + employerPOC + seperator + caseProgram + seperator + caseSubprogram + seperator + airportCode + seperator + fingerprintFileName + seperator + fingerprintCaseNumber + seperator + badgeId + seperator + badgeIssueDate + seperator + badgeExpirationDate + seperator + badgeAirportCode + seperator + badgeLocalType + seperator + badgeArea + seperator + badgeAccessSIDA + seperator + badgeAccessSterileArea + seperator + badgeAccessAOA + seperator + badgeAccessSecured + seperator + badgeAccessPublicArea + seperator + badgeAccessRT + seperator + badgeStatus + seperator + badgeChangeReason + '\n' 
    


print('TelosID TSA Random Record Generator')
print('-----------------------------------')
print('How many randomly-generated records would you like?')
numRecords = int(raw_input('?: '))
print('With which character would you like fields seperated within a record? ')
print('I suggest \",\" (default is \",\")')
seperator = str(raw_input('?: '))
if seperator == '':
    seperator = ','
outFile = open('output\\' + str(numRecords) + 'testrecords.txt', 'w') #a=append, w=write
outFile.write('firstName' + seperator + 'middleName' + seperator + 'lastName' + seperator + 'suffix' + seperator + 'aliasFirstName' + seperator + 'aliasMiddleName' +\
              seperator + 'aliasLastName' + seperator + 'aliasSuffix' + seperator + 'dob' + seperator + 'pobCountry' + seperator + 'pobState' + seperator + 'pobCity' +\
              seperator + 'pobCounty' + seperator + 'sex' + seperator + 'race' + seperator + 'ssn' + seperator + 'hairColor' + seperator + 'eyeColor' + seperator + 'height' +\
              seperator + 'weight' + seperator + 'street1' + seperator + 'street2' + seperator + 'city' + seperator + 'state' + seperator + 'postalCode' +\
              seperator + 'country' + seperator + 'homeTelephone' + seperator + 'businessTelephone' + seperator + 'mobileTelephone' + seperator + 'pagerTelephone' +\
              seperator + 'faxTelephone' + seperator + 'email' + seperator + 'citizenship' + seperator + 'naturalizationDate' + seperator + 'passportCountry' +\
              seperator + 'passportNumber' + seperator + 'passportType' + seperator + 'visaNumber' + seperator + 'visaType' +\
              seperator + 'visaClassOfAdmissionClassificationCode' + seperator + 'birthAbroadCertificationId' + seperator + 'certificateOfCitizenshipNumber' +\
              seperator + 'alienNumber' + seperator + 'i94ArrivalDepartureFormNumber' + seperator + 'certificateOfNaturalizationNumber' +\
              seperator + 'ds1350CertificationOfBirthAbroad' + seperator + 'citizenshipCertificateId' + seperator + 'admissionId' + seperator + 'employerName' +\
              seperator + 'employerStreet1' + seperator + 'employerStreet2' + seperator + 'employerCity' + seperator + 'employerState' + seperator + 'employerPostalCode' +\
              seperator + 'employerCountry' + seperator + 'employerEmail' + seperator + 'employerTelephone' + seperator + 'employerPOC' + seperator + 'caseProgram' +\
              seperator + 'caseSubprogram' + seperator + 'airportCode' + seperator + 'fingerprintFileName' + seperator + 'fingerprintCaseNumber' + seperator + 'badgeId' +\
              seperator + 'badgeIssueDate' + seperator + 'badgeExpirationDate' + seperator + 'badgeAirportCode' + seperator + 'badgeLocalType' + seperator + 'badgeArea' +\
              seperator + 'badgeAccessSIDA' + seperator + 'badgeAccessSterileArea' + seperator + 'badgeAccessAOA' + seperator + 'badgeAccessSecured' +\
              seperator + 'badgeAccessPublicArea' + seperator + 'badgeAccessRT' + seperator + 'badgeStatus' + seperator + 'badgeChangeReason' + ' \n')
index = 0
while (index < numRecords):
    outFile.write(generate_person())
    index = index + 1
outFile.close()
print 'SCRIPT COMPLETED'
print '  A file called \"' + str(numRecords) + 'testrecords.txt\" should have been created in the \\output directory.'
