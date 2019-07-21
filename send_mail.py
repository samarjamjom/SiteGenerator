import sys
import optparse


parser = optparse.OptionParser( "Usage string" )
parser.add_option( "--text", dest="mail_text", type="string", help="blah blah" )
parser.add_option( "--recipients", dest="recipients",
    type="string", help="Comma-separated list of recipient email addresses" )

(options, args) = parser.parse_args()

#print(str(options))
print(options.recipients)

#print(sys.argv)
#print(sys.argv[0])
