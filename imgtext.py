import Image, ImageDraw, ImageFont, csv
from datetime import datetime, timedelta
from random import choice
import randombiographic

sex = ''
name = ''
ssn = ''
dob = ''
phone = ''
address = ''
state = ''
county = ''
zipcode = ''
POBCountry = ''
citizenship = ''
visatype = ''

def create_person(  ):
    sex = choice( [ 'M', 'F' ] )
    name = randombiographic.name( sex )
    ssn = randombiographic.ssn(  )
    dob = randombiographic.rDateBetween(  )
    phone = randombiographic.phonenumber( 2 )
    address = randombiographic.address(  )
    state = randombiographic.state(  )
    county = randombiographic.county( state )
    zipcode = randombiographic.zipcode( choice( [ 5,9,10 ] ), state )
    POBCountry = choice( [ 'USA', 'USA', randombiographic.country(  ) ] )
    if POBCountry == 'USA':
        citizenship = 'USA'
    else:
        citizenship = choice( [ POBCountry, 'USA', randombiographic.country(  ) ] )
        visatype = randombiographic.visatype(  )
    

def fill_in_bc( text ):
    img = Image.open( 'images/birth certificate.png' )
    fnt = ImageFont.truetype("arial.ttf", 45)
    draw = ImageDraw.Draw( img )
    # create date object for DOB
    d = datetime.strptime( text[8], '%m/%d/%Y' )
    d2 = datetime.strptime( text[8], '%m/%d/%Y' )+timedelta(days=2)
    # construct joined name
    if text[1] == '': name = text[0]+' '+text[2]
    else: name = text[0]+' '+text[1]+' '+text[2]
    if text[3] != '': name = name+' '+text[3]
    # Add state name (multiple)
    draw.text( ( 1300, 400 ), 'State Of '+state(text[10]), fill='black', font=ImageFont.truetype("arial.ttf", 100) )
    draw.text( ( 870, 800 ), '( From the Clerk\'s Office of the County Commissioner )', fill='black', font=fnt )
    draw.text( ( 2135, 1540 ), state(text[10]), fill='black', font=fnt )
    draw.text( ( 1630, 1090 ), text[12], fill='black', font=fnt )# Add county name
    draw.text( ( 500, 1020 ), name, fill='black', font=fnt )   # Name
    draw.text( ( 1860, 1020 ), text[13], fill='black', font=fnt )   # Sex
    draw.text( ( 750, 1090 ), text[11], fill='black', font=fnt )   # POB City
    draw.text( ( 630, 1170 ), str( suffix( text[8][3:5] ) ), fill='black', font=fnt )   # day
    draw.text( ( 1015, 1170 ), d.strftime( '%B %Y' ), fill='black', font=fnt )   # month, year
    draw.text( ( 2065, 1400 ), d2.strftime( '%m/%d/%Y'), fill='black', font=fnt )   # date filed
    draw.text( ( 1870, 1600 ), str( suffix( text[8][3:5] ) ), fill='black', font=fnt )   # date filed again
    draw.text( ( 1675, 1700 ), d2.strftime( '%B %Y' ), fill='black', font=fnt )   # date filed again
    img.save( 'output/' + name + '-bc.png' )

def fill_in_dl( text ):
    if text[13] == 'F': img = Image.open( 'images/license_F.png' )
    else: img = Image.open( 'images/license_M.png' )
    fnt = ImageFont.truetype("arial.ttf", 30)
    fnt2 = ImageFont.truetype("arial.ttf", 60)
    # construct joined name
    if text[1] == '': name = text[0]+' '+text[2]
    else: name = text[0]+' '+text[1]+' '+text[2]
    if text[3] != '': name = name+' '+text[3]
    draw = ImageDraw.Draw( img )
    # create date object for DOB
    d = datetime.strptime( text[8], '%m/%d/%Y' )
    # State header
    draw.text( ( 40, 40 ), state(text[23])+ '-' + text[23], fill='black', font=fnt2 )
    # DOB
    draw.text( ( 380, 210 ), d.strftime( '%m/%d/%Y'), fill='black', font=fnt )
    # Name
    draw.text( ( 318, 260 ), name, fill='black', font=fnt )
    # Address 1
    draw.text( ( 318, 293 ), ' '.join( text[ 19:22 ] ), fill='black', font=fnt )
    # Address 2 (city, state, zip)
    draw.text( ( 311, 324 ), ' '.join( text[ 21:25 ] ), fill='black', font=fnt )
    # Sex
    draw.text( ( 366, 358 ), text[13], fill='black', font=fnt )
    # Height in in
    draw.text( ( 586, 358 ), text[18], fill='black', font=fnt )
    # Eye color
    draw.text( ( 770, 358 ), text[17], fill='black', font=fnt )
    img.save( 'output/' + name + '-dl.png' )
'''
def fill_in_ssc( text ):
   img = Image.open( 'images/social security card.png' )
   fnt = ImageFont.truetype("arial.ttf", 30)
   fnt2 = ImageFont.truetype("arial.ttf", 20)
   draw = ImageDraw.Draw( img )
   name = ''
   # Name
   if text[1] == '': name = text[0]+' '+text[2]
   else: name = text[0]+' '+text[1]+' '+text[2]
   if text[3] != '': name = name+' '+text[3]
   draw.text( ( 285-fnt2.getsize(name)[0]/2, 210 ), name, fill='black', font=fnt2 )
   # SSN
   draw.text( ( 195, 145 ), text[15][:3]+'-'+text[15][3:5]+'-'+text[15][5:], fill='black', font=fnt )
   img.save( 'output/' + ' '.join( text[ :4 ] ) + '-ssc.png' )
    '''
def fill_in_ssc(  ):
   img = Image.open( 'images/social security card.png' )
   fnt = ImageFont.truetype("arial.ttf", 30)
   fnt2 = ImageFont.truetype("arial.ttf", 20)
   draw = ImageDraw.Draw( img )
   draw.text( ( 285-fnt2.getsize(name)[0]/2, 210 ), name, fill='black', font=fnt2 )
   # SSN
   draw.text( ( 195, 145 ), ssn, fill='black', font=fnt )
   img.save( 'output/' + ' '.join( name ) + '-ssc.png' )
   
def fill_in_i9( text ):
   img = Image.open( 'images/i9.png' )
   fnt = ImageFont.truetype("arial.ttf", 30)
   fnt2 = ImageFont.truetype("arial.ttf", 25)
   draw = ImageDraw.Draw( img )
   name = ''
   if text[3] == '': name = text[2]+', '+text[0]
   else: name = text[2]+' '+text[3]+', '+text[0]
   if text[1] != '': name = name + ', ' + text[1][0] + '.'
   alias = ''
   if text[6] != '': alias = text[6]
   # create date object for DOB
   d = datetime.strptime( text[8], '%m/%d/%Y' )
   # Name - last, suffix, first, middle initial
   draw.text( ( 75, 310 ), name, fill='black', font=fnt )
   # maiden name ( alias lname if present )
   draw.text( ( 850, 310 ), alias, fill='black', font=fnt )
   # address 1 + 2
   draw.text( ( 75, 370 ), text[20]+' '+text[21], fill='black', font=fnt )
   # DOB  mm/dd/yyyy
   draw.text( ( 850, 370 ), d.strftime( '%m/%d/%Y' ), fill='black', font=fnt )
   # city, state, zip
   draw.text( ( 75, 425 ), text[22]+' '+text[23]+' '+text[24], fill='black', font=fnt )
   # ssn
   draw.text( ( 850, 425 ), text[15], fill='black', font=fnt )
   # immigration status
   if text[ 32 ] == 'USA': # citizen
      draw.text( ( 558,484 ), 'X', fill='black', font=fnt2 )
   else: # not citizen
      if choice[ TRUE, FALSE ] == TRUE: # resident, or on visa
         draw.text( ( 556, 507 ), 'X', fill='black', font=fnt2 )
         draw.text( ( 895, 500 ), text[ 42 ], fill='black', font=fnt2 )
      else:
         draw.text( ( 557, 534 ), 'X', fill='black', font=fnt2 )
         draw.text( ( 772, 558 ), text[ 42 ], fill='black', font=fnt2 )
   img.save( 'output/' + ' '.join( text[ :4 ] ) + '-i9.png' )
   
def fill_in_us_passport( text ):
   if text[ 13 ] == 'F': img = Image.open( 'images/passport_f.png' )
   else: img = Image.open( 'images/passport_m.png' )   
   fnt = ImageFont.truetype("arial.ttf", 32)
   draw = ImageDraw.Draw( img )
   # passport type
   draw.text( ( 575, 1145 ), text[ 36 ], fill='black', font=fnt )
   # passport number
   draw.text( ( 1075, 1145 ), text[ 35 ], fill='black', font=fnt )
   # last name
   draw.text( ( 504, 1220 ), text[ 2 ] + ' ' + text[ 3 ], fill='black', font=fnt )
   # first name
   draw.text( ( 504, 1290 ), text[ 0 ], fill='black', font=fnt )
   # DOB
   draw.text( ( 504, 1450 ), datetime.strptime( text[8], '%m/%d/%Y' ).strftime( '%d %b %Y'), fill='black', font=fnt )
   # POB state and country
   draw.text( ( 504, 1525 ), state(text[ 10 ]) + ',' + text[ 9 ], fill='black', font=fnt )
   # sex
   draw.text( ( 1220, 1515 ), text[ 13 ], fill='black', font=fnt )
   img.save( 'output/' + ' '.join( text[ :4 ] ) + '-pass.png' )

def fill_in_other_passport( text ):
   if text[ 13 ] == 'F': img = Image.open( 'images/foreign passport f.png' )
   else: img = Image.open( 'images/foreign passport m.png' )   
   fnt = ImageFont.truetype("arial.ttf", 22)   
   fnt2 = ImageFont.truetype("arial.ttf", 32)
   draw = ImageDraw.Draw( img )
   # issuing country
   draw.text( ( 312-fnt2.getsize(text[32])[0]/2, 436 ), text[32], fill='black', font=fnt2 )
   # passport type
   draw.text( ( 255, 480 ), text[ 36 ], fill='black', font=fnt )
   # passport number
   draw.text( ( 485, 480 ), text[ 35 ], fill='black', font=fnt )
   # first name
   draw.text( ( 255, 518 ), text[ 0 ], fill='black', font=fnt )
   # last name
   draw.text( ( 255, 558 ), text[ 2 ] + ' ' + text[ 3 ], fill='black', font=fnt )
   # nationality
   draw.text( ( 255, 594 ), text[ 32 ], fill='black', font=fnt )
   # sex
   draw.text( ( 400, 594 ), text[ 13 ], fill='black', font=fnt )
   # DOB
   draw.text( ( 500, 594 ), datetime.strptime( text[8], '%m/%d/%Y' ).strftime( '%d %b %Y'), fill='black', font=fnt )
   # POB state and country
   draw.text( ( 280, 632 ), state(text[ 10 ]) + ',' + text[ 9 ], fill='black', font=fnt )
   # place of residence
   draw.text( ( 280, 672 ), text[ 23 ] + ', ' + text[ 25 ], fill='black', font=fnt )
   img.save( 'output/' + ' '.join( text[ :4 ] ) + '-pass.png' )
   
def suffix(d):
   if d == 1: return d+'st'
   elif d == 2: return d+'nd'
   elif d == 3: return d+'rd'
   else: return d+'th'

def state(s):
   states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
   return states[s]

'''   
with open( 'test.txt', 'rb' ) as csvfile:
   reader = csv.reader( csvfile )
   for row in reader:
      fill_in_other_passport( row )
      if row[ 9 ] == 'USA':   # POB country
         fill_in_bc( row )
      if row[ 32 ] == 'USA':  # Citizenship
         fill_in_ssc( row )
         fill_in_us_passport( row )
      else:
         fill_in_i9( row )
      fill_in_dl( row )
'''

create_person(  )
fill_in_ssc(  )
print 'Finished'
