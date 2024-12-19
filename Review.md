Review.md

1) Code Review für WellBee - Max Feldmann & Schweinberger
   
Korrektheit
•	Der Code ist soweit korrekt formuliert, dass die gewünschten Funktionen angezeigt bzw. ausgeführt werden.
•	Die Anwendung ist dennoch nur eingeschränkt nutzbar, da einige Funktionen (die Eingabe für Kalorien, die Eingabe für Wasser sowie der Button zum Beenden der Anwendung) auf kleinen Screens (getestet mit 14 Zoll) nicht angezeigt werden.
[Die beschriebenen Teile werden daher in diesem Review nicht geprüft!]
•	Der Code bzw. die Anwendung ist somit nicht auf allen Geräten nutzbar und kann in diesem Fall auch nicht ordnungsgemäß bedient werden.
•	Der Code bzw. die Anwendung kann auf diesen Geräten weiters nicht sinnvoll genutzt werden, da sie nicht beendet und die Wochendaten daher nicht vollständig angezeigt werden können.
•	Die für den Code benötigten Module können problemlos installiert werden um den Code korrekt auszuführen.
•	Der Code ist soweit korrekt formuliert, dass trotz nicht funktionierender Teile die restlichen Teile problemlos laufen
Lesbarkeit
•	Der Code für die Funktionen ist gut lesbar und beschrieben.
•	Auch der Code für Buttons und Bilder ist trotz des größeren Umfanges gut beschrieben und strukturiert.
•	Der Code ist insbesondere auch dahingehend gut lesbar, dass aufgrund der Screengröße nicht angezeigte Funktionen trotzdem nachvollziehbar waren und das Testing großteils auch so möglich war.
Effizienz
•	Die Funktionen sind kompakt und übersichtlich formuliert, besonders komplexe Formulierungen werden vermieden.
•	Die Zeit vom Start der Anwendung bis zum vollständigen öffnen ist kurz, was weiters auf effizienten Code hindeutet.
•	Die Button-Erstellung besteht Großteils aus Duplikaten und kann vereinfacht werden.
•	Die verwendeten Bilder werden mehrmals konvertiert und könnten über eine Library einfacher abgelegt und wiederverwendet werden.
Wartbarkeit
•	Die einzelnen Teile des Code sind klar von einander getrennt und beschrieben, wodurch eine einfache Wartung möglich gemacht wird.
•	Die Kommentare sind grundsätzlich gut gewählt und ausreichend.
Fehlerbehandlung
•	Auf Fehlermeldungen die den Ablauf der Anwendung grundsätzlich verhindern würden wird verzichtet.
•	Fehlermeldungen für Usereingaben sind Großteils, allerdings nicht überall, vorhanden.
(Fehlt z.B. bei Tracking der Trainingszeit)
Sicherheit
•	Die Sicherheit der eingegebenen Daten kann im Rahmen dieser Anwendung nicht überprüft werden.
•	Eine Abänderung des Codes über die Anwendung war nicht möglich, der Code scheint sicher zu sein.
Einhaltung von Standards
•	Der Code befolgt die gängigen Coding Standards weitgehend, insbesondere im Bezug auf Konsistenz und Aufbau.
•	Einzelne Teile (z.B. Buttons) können noch weiter zusammengefasst bzw. schlanker gestaltet werden, um dem Grundsatz den Code so simpel wie möglich zu gestalten, gerecht zu werden.
Skalierbarkeit
•	Der Code ist durch den Einsatz einiger Module (PIL module, panda module, plyer module) nicht gut skalierfähig – insbesondere auch weil diese Module nicht in Standard-Packages enthalten sind und gesondert installiert werden müssen.
•	Damit eine weitere Skalierung möglich ist, muss weiters das Problem der Anzeige auf kleinen Bildschirmen gelöst werden.
•	In der aktuellen Umsetzung ist daher keine Skalierung möglich.


2) Code Review für Blackjack - Almir, Lea, Tamara

Code Review: Ausführlicher Bericht
Korrektheit
•	Der Code funktioniert wie erwartet und erfüllt die grundlegenden Anforderungen eines Blackjack-Spiels.
•	Alle zentralen Spielregeln sind korrekt implementiert, einschließlich der Behandlung von Assen (A) als 1 oder 11, je nach Hand-Summe.
•	Die Karten werden korrekt gemischt, ausgeteilt, und die Spielzüge des Dealers und des Spielers verlaufen regelkonform.
Lesbarkeit
•	Insgesamt ist der Code gut lesbar und die Struktur konsistent.
•	Eine Ausnahme ist die Funktion print_hand. Der Name könnte verwirrend sein, da "print" meist mit der Python-eigenen print()-Funktion assoziiert wird. Vorschlag: Umbenennen in show_hand, um den Zweck klarer zu machen.
•	Mehr und ausführlichere Kommentare würden besonders Anfängern helfen, den Code besser zu verstehen, z. B. bei der Regelung der Asse oder dem Ablauf des Dealer-Zugs.
•	Die Darstellung der Karten in ASCII-Art ist sehr hilfreich und trägt zur besseren Spielbarkeit und Verständlichkeit bei.
Effizienz
•	Der Code ist effizient und verzichtet auf unnötig komplexe Algorithmen.
•	Die Berechnung der Hand-Summe in calculate_total ist gut gelöst und berücksichtigt Sonderfälle wie mehrere Asse.
•	Verbesserungspotential:
o	Vermeidung redundanter Berechnungen: Die Hand-Summe (calculate_total) wird in einigen Fällen mehrfach für dieselbe Hand berechnet. Hier könnte Zwischenspeichern helfen.
Wartbarkeit
•	Der Code ist modular aufgebaut, was die Wartbarkeit erleichtert. Die Funktionen sind klar voneinander getrennt und auf spezifische Aufgaben fokussiert.
•	Mehr Kommentare, insbesondere für komplexere Logik wie die Regelung der Asse, würden die Wartbarkeit weiter erhöhen.
•	Der Umgang mit ungeplanten Benutzereingaben (z. B. falsche Eingabe bei "ziehen" oder "bleiben") ist nicht berücksichtigt und könnte die Robustheit des Codes beeinträchtigen.
Fehlerbehandlung
•	Es wurden keine Fehler im grundlegenden Ablauf gefunden.
•	Verbesserungspotential:
o	Fehlende Validierung von Benutzereingaben (z. B. falsche oder ungültige Eingaben während der Spieleraktion). Hier könnten spezifische Fehlermeldungen oder Wiederholungsaufforderungen ergänzt werden.
Sicherheit
•	Sicherheit ist bei einem einfachen Kartenspiel nicht von zentraler Bedeutung.
•	Eingaben des Benutzers sollten jedoch validiert werden, um potenzielle unerwartete Fehler zu vermeiden (z. B. durch Tippfehler).
Einhaltung von Standards
•	Der Code folgt weitgehend den akzeptierten Coding-Standards (PEP 8):
o	Funktionen sind modular und konsistent gestaltet.
o	Die Namenskonventionen für Variablen und Funktionen sind verständlich.
•	Verbesserungspotential:
o	Einheitlichere Verwendung von Anführungszeichen (' und " wechseln an einigen Stellen).
o	Längere Codezeilen könnten für bessere Lesbarkeit umgebrochen werden.
Skalierbarkeit
•	Der Code ist nicht direkt skalierbar, da er auf eine einzelne Spieler-Hand und einen Dealer ausgelegt ist.
•	Vorschläge zur Skalierung:
o	Unterstützung mehrerer Spieler im selben Spiel.
o	Integration in eine größere Spiele-App, die Blackjack als eines von mehreren Kartenspielen anbietet.
________________________________________
Zusammenfassung der Verbesserungsvorschläge
1.	Lesbarkeit:
o	Umbenennung der Funktion print_hand in show_hand.
o	Ergänzung ausführlicherer Kommentare, z. B. zur Ass-Regelung und zur Dealer-Logik.
2.	Fehlerbehandlung:
o	Robustere Validierung von Benutzereingaben.
o	Klare Fehlermeldungen und Wiederholungsaufforderungen bei ungültigen Eingaben.
3.	Effizienz:
o	Reduzierung redundanter Berechnungen durch Zwischenspeichern von Summen.
4.	Standards:
o	Einheitlichere Verwendung von Anführungszeichen.
o	Umbruch langer Zeilen für bessere Lesbarkeit.
5.	Skalierbarkeit:
o	Unterstützung für mehrere Spieler oder Integration in eine Spiele-App.
Mit diesen Verbesserungen wird der Code robuster, skalierbarer und einsteigerfreundlicher gestaltet.




