import HTML

# open een HTML bestand waarin de output moet worden gezet
HTMLFILE = 'IPFIT5.html'
f = open(HTMLFILE, 'w')

# Het opmaken van het html document
titel = 'IFPIT5 HTML rapport'
f.write(titel)
f.write('<p>')
f.write('<title> Ipfit5 Html rapport </title>') # voegt pagina titel toe

# voegt een afbeelding van het rapport of onderzoeksbureau toe.
f.write('<img src="http://www.forensischonderzoeksbureau.nl/images/recherchebureaus.jpg" alt="Hier moet een afbeelding">') 
f.write('<p>')
f.write('<body bgcolor="#E6E6FA">') # Voegt een achtergrond kleur toe aan het rapport

# genereer case data vanuit sleutel
casenaam = 'test'
casenr = '1' 
onderzoeker = 'Dylan Bragonje'

# printen van de casedata naar het html bestand in een tabel maar kan ook naar plaintext worden omgezet
case_data = [
        ['Case',   casenaam],
        ['Casenummer', casenr],
        ['Onderzoeker' , onderzoeker]]
casedata = HTML.table(case_data)
f.write(casedata)
f.write('<p>')
f.write('<hr>')
print '-'*79

#Inladen van bewijs materiaal
case_materiaal = [
	['1', 'test', 'testbestand', '01-01-2014', 'Dylan Bragonje']
]
casemateriaal = HTML.table(case_materiaal,
	header_row = ['Bewijsstuk', 'Naam', 'Beschrijving', 'toegevoegd op', 'toegevoegd door'],
	col_width = ['','20%','10%','10%','10%]'])
f.write(casemateriaal + '<p>\n')
