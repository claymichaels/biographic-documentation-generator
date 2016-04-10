import librandbio, libordinal, libfullname, libdetailsarray
from libordinal import suffix
from libvalidatestate import toUSPS, fromUSPS
from libvalidatecountry import toFull, to2, to3
from random import choice
import Image, ImageDraw, ImageFont
from datetime import date, timedelta
import os

class Person:
    def __init__( self, pob = '', status = '' ):
        ''' blank pob will be random (Immigration) Status defaults to citizen. Options are citizen resident, foreigner. '''
        if status == '':
            self.status = choice( [ 'citizen', 'resident', 'foreigner' ] )
        else:
            self.status = status.lower(  )
        self.sex     = choice( [ 'M', 'F' ] )
        # name
        self.name     = librandbio.name( self.sex )
        self.fullname = libfullname.joinname( self.name )
        self.fname    = self.name[ 0 ]
        self.mname    = self.name[ 1 ]
        if self.mname == '':
            self.minitial = ''
        else:
            self.minitial = self.mname[0].upper(  )
        self.lname    = self.name[ 2 ]
        self.suffix   = self.name[ 3 ]
        # alias
        self.alias    = librandbio.name( self.sex )
        self.fullalias= libfullname.joinname( self.alias )
        self.falias   = self.alias[ 0 ]
        self.malias   = self.alias[ 1 ]
        self.lalias   = self.alias[ 2 ]
        self.salias   = self.alias[ 3 ]
        # dates for ages between 18 and 65, Date Of Birth will be chosen from between
        dob1 = date.today(  ) - timedelta( hours = 65 * 24 * 365 )
        dob2 = date.today(  ) - timedelta( hours = 18 * 24 * 365 )
        self.dob      = librandbio.datebetween( dob1, dob2 )
        # identifying details
        self.eyecolor = librandbio.eyecolor(  )
        self.haircolor= librandbio.haircolor(  )
        self.height   = librandbio.height(  )
        self.weight   = librandbio.weight(  )
        # contact info
        self.phone    = librandbio.phonenumber(  )
        self.address  = librandbio.address(  )
        self.city     = librandbio.city(  )
        self.state    = librandbio.state(  )
        self.county   = librandbio.county( self.state )
        self.zipcode  = librandbio.zipcode( self.state )
        self.country  = 'USA'
        self.dl       = librandbio.dlno(  )
        self.emp      = librandbio.employer(  )
        self.empPOC   = librandbio.employerPOC(  )
        self.empphone = librandbio.phonenumber(  )
        self.empemail = librandbio.employeremail( self.empPOC[0], self.empPOC[2], self.emp.replace("'","").replace(' ','') )
        self.empadd   = librandbio.address(  )
        self.empcity  = librandbio.city(  )
        self.empstate = librandbio.state(  )
        self.empzip   = librandbio.zipcode( self.empstate )
        if pob.lower(  ) == '':
            self.pobcountry = librandbio.country(  )
        else:
            self.pobcountry = pob
        if pob.lower(  ) == 'usa':
            self.pobstate = librandbio.state(  )
            self.pobcity = librandbio.city(  )
        if self.status.lower(  ) == 'citizen':
            self.citizenship = 'USA'
        elif self.status.lower(  ) == 'resident':
            self.citizenship = toFull( librandbio.country(  ) )
            self.visatype = librandbio.visatype(  )
            self.visano = librandbio.visano(  )
            self.visaclass = librandbio.visaadmissionclass(  )
            self.anumber = librandbio.anumber(  )
        elif self.status.lower(  ) == 'foreigner':
            self.citizenship = toFull( librandbio.country(  ) )
            self.visatype = librandbio.visatype(  )
            self.visano = librandbio.visano(  )
            self.visaclass = librandbio.visaadmissionclass(  )
            self.anumber = librandbio.anumber(  )
        if self.pobcountry != 'USA':
            self.naturalizationno = librandbio.naturalizationno(  )
            self.ds1350birthabroadno = librandbio.ds1350birthabroadno(  )
            self.birthabroadno = librandbio.birthabroadno(  )
        self.ssn = librandbio.ssn(  )
        self.ssnformatted = self.ssn[0:3]+'-'+self.ssn[3:5]+'-'+self.ssn[-4:]
        self.passportno = librandbio.passportno(  )
        self.passporttype = librandbio.passporttype(  )

    def details( self ):
        detailsarray = libdetailsarray.create( self )
        open('Output/' + self.fullname + '/Applicant Details.html', 'w').close()
        with open( 'Output/' + self.fullname + '/Applicant Details.html', 'w' ) as thefile:
            thefile.write( '<HTML><HEAD><TITLE>Applicant Details</TITLE></HEAD><BODY>' )
            for x in range( 0, len( detailsarray[0] ) ):
                thefile.write( '<B>' + detailsarray[0][x] + '</B>' + str( detailsarray[1][x] ) + '<BR>' )
            thefile.write( '</BODY></HTML>' )
            
    def print_all( self ):
        os.makedirs( 'output/' + self.fullname )
        if self.pobcountry == 'USA':
            self.print_bc(  )
        self.passport(  )
        self.ssc(  )
        self.dl(  )
        self.i9(  )

    def print_some( self ):
        os.makedirs( 'output/' + self.fullname )
        self.details(  )
        self.i9(  )   # everybody needs an I-9 to work in the US
        chosen = ''
        docs = [ 'license', 'passport', 'ssc' ]
        if self.pobcountry == 'USA':
            docs.append( 'bc' )
        numdocs = choice( range( 2, len( docs ) ) )
        print '-'*10
        print 'name  : ', self.fullname
        print 'pobc  : ', self.pobcountry
        print 'status: ', self.status
        print 'numdocs:',numdocs
        for x in range( 0, numdocs ):
            chosen = choice( docs )
            print 'chosen: ', chosen
            docs.remove( chosen )
            if chosen == 'passport': self.passport(  )
            elif chosen == 'license': self.drivers(  )
            elif chosen == 'ssc': self.ssc(  )
            elif chosen == 'bc': self.bc(  )

    def bc( self  ):
        '''Generate Birth Certificate '''
        if self.pobcountry == 'USA':
            img = Image.open( 'images/birth certificate.png' )
            fnt = ImageFont.truetype("arial.ttf", 45)
            draw = ImageDraw.Draw( img )
            # issue date
            issue = self.dob + timedelta( days=2 )
            # draw document
            draw.text( ( 1300, 400 ), 'State Of '+fromUSPS( self.state ), fill='black', font=ImageFont.truetype("arial.ttf", 100) )
            draw.text( ( 870, 800 ), '( From the Clerk\'s Office of the County Commissioner )', fill='black', font=fnt )
            # state
            draw.text( ( 2150, 1540 ), self.state, fill='black', font=fnt )
            # county 
            draw.text( ( 1630, 1090 ), self.county, fill='black', font=fnt )
            # name
            draw.text( ( 500, 1020 ), self.fullname, fill='black', font=fnt )
            # sex
            draw.text( ( 1860, 1020 ), self.sex, fill='black', font=fnt )
            # POB City
            draw.text( ( 750, 1090 ), self.pobcity, fill='black', font=fnt )
            # day
            draw.text( ( 630, 1170 ), suffix( self.dob.strftime( '%d') ), fill='black', font=fnt )
            # month, year
            draw.text( ( 1015, 1170 ), self.dob.strftime( '%B %Y' ), fill='black', font=fnt )
            # date filed
            draw.text( ( 2065, 1400 ), issue.strftime( '%m/%d/%Y'), fill='black', font=fnt )
            # date filed
            draw.text( ( 1870, 1600 ), suffix( issue.strftime( '%d') ), fill='black', font=fnt )  
            # date filed
            draw.text( ( 1675, 1700 ), issue.strftime( '%B %Y' ), fill='black', font=fnt )
            img.save( 'output/' + self.fullname + '/Birth Certificate.png' )
        else:
            print 'Cannot print Birth Certificate for non-US births'

    def drivers( self ):
        if self.sex.lower(  ) == 'f': img = Image.open( 'images/license_F.png' )
        else: img = Image.open( 'images/license_M.png' )
        fnt = ImageFont.truetype("arial.ttf", 30)
        fnt2 = ImageFont.truetype("arial.ttf", 60)
        draw = ImageDraw.Draw( img )
        # State header
        draw.text( ( 40, 40 ), fromUSPS( self.state )+ '-' + self.state, fill='black', font=fnt2 )
        # DOB
        draw.text( ( 380, 210 ), self.dob.strftime( '%m/%d/%Y' ) , fill='black', font=fnt )
        # Name
        draw.text( ( 318, 260 ), self.fullname, fill='black', font=fnt )
        # Address 1
        draw.text( ( 318, 293 ), self.address[ 0 ], fill='black', font=fnt )
        # Address 2 (city, state, zip)
        draw.text( ( 318, 324 ), self.address[ 1 ] , fill='black', font=fnt )
        # Sex
        draw.text( ( 375, 354 ), self.sex, fill='black', font=fnt )
        # Height in in
        draw.text( ( 586, 354 ), self.height, fill='black', font=fnt )
        # Eye color
        draw.text( ( 770, 354 ), self.eyecolor, fill='black', font=fnt )
        img.save( 'output/' + self.fullname + '/Drivers License.png' )

    def ssc( self ):
        img = Image.open( 'images/social security card.png' )
        fnt = ImageFont.truetype("arial.ttf", 30)
        fnt2 = ImageFont.truetype("arial.ttf", 20)
        draw = ImageDraw.Draw( img )
        # name, centered
        draw.text( ( 285-fnt2.getsize(self.fullname)[0]/2, 210 ), self.fullname, fill='black', font=fnt2 )
        # SSN
        draw.text( ( 195, 145 ), self.ssn[0:3]+'-'+self.ssn[3:5]+'-'+self.ssn[-4:], fill='black', font=fnt )
        img.save( 'output/' + self.fullname + '/Social Security Card.png' )
        
    def i9( self ):
        img = Image.open( 'images/i9.png' )
        fnt = ImageFont.truetype("arial.ttf", 30)
        fnt2 = ImageFont.truetype("arial.ttf", 25)
        draw = ImageDraw.Draw( img )
        # Name - last, suffix, first, middle initial
        name = self.lname
        if self.suffix != '':
            name = name+ ' ' + self.suffix
        name = name + ', ' + self.fname+' '+self.minitial
        draw.text( ( 75, 310 ), name, fill='black', font=fnt )
        # maiden name ( alias lname if present )
        if self.sex.lower(  ) == 'f':
            draw.text( ( 850, 310 ), self.lalias, fill='black', font=fnt )
        else:
            draw.text( ( 850, 310 ), 'N/A', fill='black', font=fnt )
        # address 1 + 2
        draw.text( ( 75, 370 ), self.address[ 0 ] + ' ' + self.address[ 1 ], fill='black', font=fnt )
        # DOB  mm/dd/yyyy
        draw.text( ( 850, 370 ), self.dob.strftime( '%m/%d/%Y' ), fill='black', font=fnt )
        # city, state, zip
        draw.text( ( 75, 425 ), self.city+' '+self.state+' '+self.zipcode, fill='black', font=fnt )
        # ssn
        draw.text( ( 850, 425 ), self.ssnformatted, fill='black', font=fnt )
        # immigration status
        if self.status.lower(  ) == 'citizen': # citizen
            draw.text( ( 558,484 ), 'X', fill='black', font=fnt2 )
        elif self.status.lower(  ) == 'resident': # resident
            draw.text( ( 556, 507 ), 'X', fill='black', font=fnt2 )
            draw.text( ( 895, 500 ), self.anumber, fill='black', font=fnt2 )
        elif self.status.lower(  ) == 'foreigner': # Alien
            draw.text( ( 557, 534 ), 'X', fill='black', font=fnt2 )
            draw.text( ( 772, 558 ), self.anumber, fill='black', font=fnt2 )
        img.save( 'output/' + self.fullname + '/I-9.png' )
        
    def passport( self ):
        if self.citizenship.lower(  ) == 'usa':
            if self.sex.lower(  ) == 'f': img = Image.open( 'images/passport_f.png' )
            else: img = Image.open( 'images/passport_m.png' )
            fnt = ImageFont.truetype("arial.ttf", 32)
            draw = ImageDraw.Draw( img )
            # passport type
            draw.text( ( 575, 1145 ), self.passporttype, fill='black', font=fnt )
            # passport number
            draw.text( ( 1075, 1145 ), self.passportno, fill='black', font=fnt )
            # last name
            draw.text( ( 504, 1220 ), self.lname + ' ' + self.suffix, fill='black', font=fnt )
            # first name
            draw.text( ( 504, 1293 ), self.fname, fill='black', font=fnt )
            # DOB
            draw.text( ( 504, 1450 ), self.dob.strftime( '%d %b %Y'), fill='black', font=fnt )
            # POB state and country or pob country
            if self.pobcountry.lower(  ) == 'usa':
                draw.text( ( 504, 1525 ), fromUSPS(self.pobstate) + ', ' + self.pobcountry, fill='black', font=fnt )
            else:
                draw.text( ( 504, 1525 ), self.pobcountry, fill='black', font=fnt )
            # sex
            draw.text( ( 1220, 1515 ), self.sex, fill='black', font=fnt )
            img.save( 'output/' + self.fullname + '/Passport.png' )
        else:
            if self.sex.lower(  ) == 'f': img = Image.open( 'images/foreign passport f.png' )
            else: img = Image.open( 'images/foreign passport m.png' )
            fnt = ImageFont.truetype("arial.ttf", 22)
            fnt2 = ImageFont.truetype("arial.ttf", 32)
            draw = ImageDraw.Draw( img )
            # issue date
            draw.text( ( 280, 714 ), '24 Sep 2011', fill='black', font=fnt )
            # expiration date
            draw.text( ( 427, 714 ), '25 Sep 2031', fill='black', font=fnt )
            # issuing country
            draw.text( ( 312-fnt2.getsize(self.citizenship)[0]/2, 436 ), self.citizenship, fill='black', font=fnt2 )
            # passport type
            draw.text( ( 255, 480 ), self.passporttype, fill='black', font=fnt )
            # passport country code
            draw.text( ( 370, 480 ), self.country, fill='black', font=fnt )
            # passport number
            draw.text( ( 485, 480 ), self.passportno, fill='black', font=fnt )
            # first name
            draw.text( ( 255, 518 ), self.fname, fill='black', font=fnt )
            # last name
            draw.text( ( 255, 558 ), self.lname + ' ' + self.suffix, fill='black', font=fnt )
            # nationality
            draw.text( ( 255, 594 ), self.citizenship, fill='black', font=fnt )
            # sex
            draw.text( ( 400, 594 ), self.sex, fill='black', font=fnt )
            # DOB
            draw.text( ( 500, 594 ), self.dob.strftime( '%d %b %Y'), fill='black', font=fnt )
            # POB country
            draw.text( ( 280, 632 ), self.pobcountry, fill='black', font=fnt )
            # place of residence
            draw.text( ( 280, 672 ), self.state + ', ' + self.country, fill='black', font=fnt )
            img.save( 'output/' + self.fullname + '/Passport.png' )



print('TelosID TSA Random Record Generator')
prompts = ['How many US-born US-Citizens?','How many Foreign-born US-Citizens?','How many Foreign-born US-Residents?','How many Foreign-born Foreign-Citizens?']
nums    = [0,0,0,0]
types   = [ ['USA','citizen'], ['', 'citizen'], ['', 'resident'], ['', 'foreigner'] ]
for x in prompts:
    print '-'*30
    print x
    try:
        nums[ prompts.index( x ) ] = int(raw_input('?: '))
    except:
        nums[ prompts.index( x ) ] = 0
for t in types:
    for x in range( 0, nums[ types.index(t) ] ):
        p = Person( t[0], t[1] )
        p.print_some(  )

print 'finished'
