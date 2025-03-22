# Testa formulär

## User stories  https://tap-ht24-testverktyg.github.io/form-demo/ 
[U1] Som en besökare vill jag bli påmind med ett vänligt felmeddelande om jag inte skrivit i mitt namn, så att jag fyller i formuläret korrekt.

[U2] Som en besökare vill jag kunna registrera mig genom att klicka på knappen när jag fyllt i alla fält korrekt, så att jag kan använda tjänsten.

[U3] Som en besökare vill jag bli påmind med ett vänligt felmeddelande om jag inte skrivit in mitt födelseår, så att jag fyller i formuläret korrekt.

[U4] Som en besökare vill jag bli påmind med ett vänligt felmeddelande om jag inte skrivit in en korrekt e-postadress, så att jag fyller i formuläret korrekt.

[U5] Som en besökare vill jag bli påmind med ett vänligt felmeddelande om jag inte skrivit in ett lösenord som är minst 4 tecken långt, så att jag fyller i formuläret korrekt.


## Acceptanskriterier
[A1.1] Om namnfältet är tomt, ska det visas ett felmeddelande.
[A1.2] Om namnfältet innehåller minst 1 tecken ska felmeddelandet inte visas.


[A2.1] Knappen ska gå att klicka på när alla fält är korrekt ifyllda.
[A2.2] Knappen ska inte gå att klicka på om minst ett fält är felaktigt ifyllt.

[A3.1] Om födelseårsfältet är tomt, ska det visas ett felmeddelande. 
[A3.2] Om födelseårsfältet innehåller exakt 4 siffror ska felmeddelandet inte visas.

[A4.1] Om e-postfältet är tomt, ska det visas ett felmeddelande. 
[A4.2] Om e-postfältet innehåller en korrekt formaterad e-postadress ska felmeddelandet inte visas.

[A5.1] Om lösenordsfältet är tomt, ska det visas ett felmeddelande. 
[A5.2] Om lösenordsfältet innehåller minst 4 tecken ska felmeddelandet inte visas.

## Testscenarier

[T1] Testa namnfältet
1. Kontrollera att textfältet inte är tomt.
2. Kontrollera att felmeddelandet inte visas.
3. Sudda det som finns i fältet.
4. Kontrollera att felmeddelandet visas.

[T2] Testa registreringsknappen
1. Kontrollera att knappen är avstängd (disabled).
2. Skriv in "password" i lösenordsfältet.
3. Kontrollera att knappen är aktiverad (ej disabled).

[T3] Testa födelseårsfältet
1. Kontrollera att textfältet inte är tomt.
2. Kontrollera att felmeddelandet inte visas.
3. Sudda det som finns i fältet.
4. Kontrollera att felmeddelandet visas.

[T4] Testa e-postfältet
1. Kontrollera att textfältet inte är tomt.
2. Kontrollera att felmeddelandet inte visas.
3. Sudda det som finns i fältet.
4. Kontrollera att felmeddelandet visas.

[T5] Testa lösenordsfältet
1. Kontrollera att textfältet inte är tomt.
2. Kontrollera att felmeddelandet inte visas.
3. Sudda det som finns i fältet.
4. Kontrollera att felmeddelandet visas.




## user stories https://lejonmanen.github.io/timer-vue/ 
[U1] Som en användare vill jag kunna skapa och ta bort widgets (timer och anteckning), så att jag kan anpassa applikationen efter mina behov.

[U2] Som en användare vill jag kunna byta plats på två widgets, så att jag kan organisera dem efter mina preferenser.

[U3]  Som en användare vill jag kunna ändra tidsinställningen på en timer, så att jag kan justera tiden efter behov. 

[U4] Som en användare vill jag kunna starta, pausa och återställa en timer, så att jag kan kontrollera tidtagningen.

[U5] Som en användare vill jag kunna ändra texten i en anteckning, så att jag kan uppdatera mina anteckningar. 

[U6] Som en användare vill jag kunna ändra temafärgen på applikationen, så att jag kan anpassa utseendet enligt mina preferenser.


## Acceptanskriterier
[A1] Skapa och ta bort widgets

[A1.1] Användaren ska kunna skapa en ny timer-widget genom att klicka på en knapp.
[A1.2] Användaren ska kunna skapa en ny anteckning-widget genom att klicka på en knapp.
[A1.3] Användaren ska kunna ta bort en timer-widget genom att klicka på en "ta bort"-knapp.
[A1.4] Användaren ska kunna ta bort en anteckning-widget genom att klicka på en "ta bort"-knapp.


[A2.1] Användaren ska kunna dra och släppa widgets för att byta deras plats.
[A2.2] Widgets ska byta plats i användargränssnittet när användaren drar och släpper dem.

[A3.1] Användaren ska kunna klicka på en knapp eller ett textfält för att ändra tidsinställningen på en timer.
[A3.2] Den nya tiden ska visas korrekt på timer-widgeten efter att den har ändrats.

[A4.1] Användaren ska kunna starta en timer genom att klicka på en "starta"-knapp.
[A4.2] Användaren ska kunna pausa en timer genom att klicka på en "pausa"-knapp.
[A4.3] Användaren ska kunna återställa en timer genom att klicka på en "återställa"-knapp.

[A5.1] Användaren ska kunna klicka på textfältet i anteckning-widgeten för att redigera texten.
[A5.2] Den nya texten ska sparas och visas korrekt i anteckning-widgeten efter att användaren har redigerat den.

[A6.1] Användaren ska kunna välja en ny temafärg från en färgpalett eller färgväljare.
[A6.2] Applikationens utseende ska uppdateras till den valda temafärgen omedelbart.


## Testscenarier

[T1] Skapa och ta bort widgets
1. Kontrollera att en ny timer-widget skapas när användaren klickar på knappen.
2. Kontrollera att en ny anteckning-widget skapas när användaren klickar på knappen.
3. Kontrollera att en timer-widget tas bort när användaren klickar på "ta bort"-knappen.
4. Kontrollera att en anteckning-widget tas bort när användaren klickar på "ta bort"-knappen.


[T2] Byta plats på widgets
1. Kontrollera att användaren kan dra och släppa widgets för att byta deras plats.
2. Kontrollera att widgets byter plats i användargränssnittet när de dras och släpps.

[T3] Ändra tidsinställning på timer
1. Kontrollera att användaren kan klicka på en knapp eller ett textfält för att ändra tidsinställningen på en timer.
2. Kontrollera att den nya tiden visas korrekt på timer-widgeten efter att den har ändrats.

[T4] Starta, pausa, återställa timer
1. Kontrollera att användaren kan starta en timer genom att klicka på "starta"-knappen.
2. Kontrollera att användaren kan pausa en timer genom att klicka på "pausa"-knappen.
3. Kontrollera att användaren kan återställa en timer genom att klicka på "återställa"-knappen.


[T5] Ändra texten för anteckning
1. Kontrollera att användaren kan klicka på textfältet i anteckning-widgeten för att redigera texten.
2. Kontrollera att den nya texten sparas och visas korrekt i anteckning-widgeten efter redigeringen.


[T6] Ändra temafärg
1. Kontrollera att användaren kan välja en ny temafärg från en färgpalett eller färgväljare.
2. Kontrollera att applikationens utseende uppdateras till den valda temafärgen omedelbart.





