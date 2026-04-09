# ============================================================
# Regex (Reguläre Ausdrücke) in Python
# ============================================================
# Regex = ein Suchmuster für Text
# Damit kannst du: suchen, prüfen, ersetzen, aufteilen
#
# import re  ← das Modul muss importiert werden
# ============================================================

import re


# ────────────────────────────────────────────────────────────
# 1. GRUNDBEFEHLE
# ────────────────────────────────────────────────────────────

text = "Python ist super"

# re.match() → Sucht NUR am ANFANG des Strings
print(re.match(r"Python", text))   # → Match! (Text fängt mit "Python" an)
print(re.match(r"ist", text))      # → None   ("ist" steht nicht am Anfang)

# re.search() → Sucht ÜBERALL im String (erster Treffer)
print(re.search(r"ist", text))     # → Match! (findet "ist" in der Mitte)

# re.findall() → Findet ALLE Treffer, gibt Liste zurück
zahlen_text = "Ich habe 3 Katzen und 2 Hunde"
print(re.findall(r"\d+", zahlen_text))  # → ['3', '2']


# ────────────────────────────────────────────────────────────
# 2. WICHTIGE ZEICHEN (Cheatsheet)
# ────────────────────────────────────────────────────────────
#   \d     = eine Ziffer (0-9)
#   \D     = KEINE Ziffer
#   \w     = Buchstabe, Ziffer oder _ (Wortzeichen)
#   \W     = kein Wortzeichen
#   \s     = Leerzeichen, Tab, Newline
#   .      = ein beliebiges Zeichen (außer Newline)
#
#   +      = 1 oder mehr davon        \d+  = "123"
#   *      = 0 oder mehr davon        \d*  = "" oder "123"
#   ?      = 0 oder 1 davon           \d?  = "" oder "5"
#   {N}    = genau N davon            \d{3} = "123"
#   {N,M}  = zwischen N und M davon   \d{2,4} = "12" bis "1234"
#
#   [abc]  = a, b oder c              [aeiou] = ein Vokal
#   [a-z]  = Kleinbuchstabe           [A-Z]   = Großbuchstabe
#   [0-9]  = Ziffer (wie \d)
#   ^      = Anfang des Strings
#   $      = Ende des Strings


# ────────────────────────────────────────────────────────────
# 3. re.split() → Text an Muster aufteilen
# ────────────────────────────────────────────────────────────
# Wie str.split(), aber mit Regex-Power

daten = "Apfel,Birne;Banana Kirsche"

# Aufteilen an Komma ODER Semikolon ODER Leerzeichen
# [,; ]+ = eines oder mehrere dieser Zeichen
liste = re.split(r"[,; ]+", daten)
print(liste)  # → ['Apfel', 'Birne', 'Banana', 'Kirsche']


# ────────────────────────────────────────────────────────────
# 4. re.sub() → Suchen und Ersetzen
# ────────────────────────────────────────────────────────────
# re.sub(muster, ersatz, text)

text = "Meine Nummer ist 123-4567"

# Jede Ziffer durch X ersetzen
geheim = re.sub(r"\d", "X", text)
print(geheim)  # → Meine Nummer ist XXX-XXXX


# ────────────────────────────────────────────────────────────
# 5. PRAXIS: E-Mail-Adresse prüfen
# ────────────────────────────────────────────────────────────
# Muster Schritt für Schritt:
#   [a-zA-Z0-9._%+-]+    = Benutzername (Buchstaben, Zahlen, Punkte...)
#   @                     = das @-Zeichen
#   [a-zA-Z0-9.-]+       = Domain-Name (z.B. "gmail", "bbq")
#   \.                    = ein Punkt (\ weil . sonst "beliebiges Zeichen" heißt)
#   [a-zA-Z]{2,}         = Endung mit mindestens 2 Buchstaben (de, com, org)

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

test_emails = ["jan.dus@bbq.de", "nicht-gueltig@", "test@web.com"]

for email in test_emails:
    if re.match(email_pattern, email):
        print(f"{email} → Gültig!")
    else:
        print(f"{email} → Ungültig!")
# → jan.dus@bbq.de → Gültig!
# → nicht-gueltig@ → Ungültig!
# → test@web.com   → Gültig!


# ============================================================
# MERKSATZ
# ============================================================
# re.match()   → sucht nur am ANFANG
# re.search()  → sucht ÜBERALL (erster Treffer)
# re.findall() → findet ALLE Treffer (als Liste)
# re.split()   → aufteilen an Muster
# re.sub()     → suchen & ersetzen
#
# r"..." → Raw-String: Backslashes werden nicht interpretiert
#          Immer r"..." bei Regex verwenden!
# ============================================================
