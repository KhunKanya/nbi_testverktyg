#1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:
 Fiskarna som jag fångade var 55 cm långa.

.*\d+\w+\d+.*

#1b Denna gången vill vi veta om det finns två längder.
.*\d+(\w|\s)+\d+.*

# 1c Längderna ska vara samma enhet.
\D+?\d+\scm\D+\d+\scm.*

# 2 Skriv ett regex som matchar ett svenskt postnummer.
# Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"

\d{3}\s\d{2}

# 3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601,
# alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.

^\d{4}-\d{2}-\d{2}

# 4 Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:
# 200 kr
# 12,50 kr
# 0,35 kr

^\d+,?\d+?\s?kr

# 5a Skriv ett regex som matchar en e-postadress (användarnamn@server.domän) enligt följande icke kompletta regler.
# användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck
# server kan innehålla samma sorts tecken
# domän kan innehålla bokstäver och siffror

(\w|[\.\-])+@\w+\.\w+

# 5b Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:
# What is a valid email address format

[a-zA-Z0-9]+[\.-_]?([a-zA-Z0-9]+[\.-_])?@[a-zA-Z0-9]+[\.-_]?[a-zA-Z]+\.[a-zA-Z0-9]+



