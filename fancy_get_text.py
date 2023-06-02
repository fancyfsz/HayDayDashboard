import os
import gettext

_ = gettext.gettext

LOCALE_DIR = os.path.abspath("locale")

def fancy_bind_text_domain(domain):
	gettext.bindtextdomain(domain, LOCALE_DIR)
	gettext.textdomain(domain)

fancy_bind_text_domain("item")