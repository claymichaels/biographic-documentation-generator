import libfullname

def create( p ):
    details = [[],[]]
    details[0] = details[0] + [ '<HR><H3>BIOGRAPHIC INFORMATION</H3>','Full Name:','First Name:','Middle Name:','Last Name:','Suffix:','Sex:','Alias Full Name:','Alias First Name:','Alias Middle Name:','Alias Last Name:','Alias Suffix:','Date of Birth:','Eye Color:','Hair Color:','Height:','Weight:','Place of Birth Country:' ]
    details[1] = details[1] + [ '',p.fullname,p.fname,p.mname,p.lname,p.suffix,p.sex,p.fullalias,p.falias,p.malias,p.lalias,p.salias,p.dob,p.eyecolor,p.haircolor,p.height,p.weight,p.pobcountry ]
    
    if p.pobcountry.lower(  ) == 'usa':
        details[0] = details[0] + [ 'Place of Birth State:','Place of Birth City:' ]
        details[1] = details[1] + [ p.pobstate, p.pobcity ]
    details[0] = details[0] + [ '<HR><H3>CITIZENSHIP INFORMATION</H3>','Citizenship Status:','Citizenship Country:' ]
    details[1] = details[1] + [ '',p.status,p.citizenship ]
    if p.pobcountry.lower(  ) != 'usa' and p.citizenship.lower(  ) == 'usa':
        details[0] = details[0] + [ 'Naturalization Number:' ]
        details[1] = details[1] + [ p.naturalizationno ]
    details[0] = details[0] + [ '<HR><H3>DOCUMENT INFORMATION</H3>','Driver\'s License Number:','Social Security Number:','Passport Country:','Passport Number:','Passport Type:' ]
    details[1] = details[1] + [ '',p.dl,p.ssnformatted,p.citizenship,p.passportno,p.passporttype ]
    if p.status.lower(  ) != 'citizen':
        details[0] = details[0] + [ 'Visa Type:','Visa Number:','Visa Class:','Alien Number:' ]
        details[1] = details[1] + [ p.visatype,p.visano,p.visaclass,p.anumber ]
    if p.pobcountry != 'USA':
        details[0] = details[0] + [ 'DS1350 Birth Abroad Form Number:','Birth Abroad Certificate Number:' ]
        details[1] = details[1] + [ p.ds1350birthabroadno,p.birthabroadno ]
    details[0] = details[0] + [ '<HR><H3>CONTACT INFORMATION</H3>','Phone Number:','Address1:','Address2:','City:','State:','County:','Zipcode:','Country:' ]
    details[1] = details[1] + [ '',p.phone,p.address[0],p.address[1],p.city,p.state,p.county,p.zipcode,p.country ]
    details[0] = details[0] + [ '<HR><H3>EMPLOYER INFORMATION</H3>','Name:','POC:','Phone Number:','Email:','Address1:','Address2:','City:','State:','Zipcode:' ]
    details[1] = details[1] + [ '',p.emp,libfullname.joinname(p.empPOC),p.empphone,p.empemail,p.empadd[0],p.empadd[1],p.empcity,p.empstate,p.empzip ]
    return details
