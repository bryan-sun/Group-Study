import ldap
import sys

# Connect to UIUC ActiveDirectory over StartTLS
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
ldap.set_option(ldap.OPT_REFERRALS, 0)

def login(user,passw):

	l = ldap.initialize("ldap://ad.uillinois.edu")
	l.set_option(ldap.OPT_REFERRALS, 0)
	l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
	l.set_option(ldap.OPT_X_TLS,ldap.OPT_X_TLS_DEMAND)
	l.set_option( ldap.OPT_X_TLS_DEMAND, True )
	l.set_option( ldap.OPT_DEBUG_LEVEL, 255 )
	l.start_tls_s()

	username = 'CN=' + user + ',OU=People,DC=ad,DC=uillinois,DC=edu'
	password = passw

	try: 
		l.simple_bind_s(username, password)
	except ldap.INVALID_CREDENTIALS:
		# -1 means the username or password was incorrect
		l.unbind_s();
		return "-1"
	except ldap.LDAPError, e:
		# -2 means there was some other error
		print(e)
		l.unbind_s();
		return "-2"
	# 0 means login successful
	l.unbind_s();
 	return "0"

