# Mini-BlackJack-Spiel in Python

## Projektbeschreibung
Dieses Projekt implementiert ein vereinfachtes BlackJack-Spiel in Python, basierend auf einem Tutorial. Es simuliert ein textbasiertes Kartenspiel, bei dem der Spieler gegen den Dealer antritt. Ziel ist es, ein grundlegendes Spiel mit Python zu erstellen, das sowohl Spaß macht als auch als Lernprojekt für Anfänger dient.

---

## Ziel des Projekts
Das Projekt zielt darauf ab:
- **Grundlagen der Programmierung** zu vertiefen, einschließlich Schleifen, Bedingungen und Funktionen.
- **Zufallselemente** in Spielen zu verstehen, z. B. das Ziehen von Karten.
- **Benutzerinteraktion** im Terminal zu ermöglichen.

---

## Spielregeln
1. Der Spieler und der Dealer starten mit jeweils zwei Karten.
2. Der Spieler kann:
   - **Hit**: Eine zusätzliche Karte ziehen.
   - **Stand**: Den aktuellen Punktestand halten.
3. Der Dealer zieht Karten, bis er mindestens 17 Punkte hat.
4. Ziel:
   - Komme so nah wie möglich an 21, ohne diese Punktzahl zu überschreiten.
   - Gewinne gegen den Dealer, indem du näher an 21 bist.

---

## Funktionsübersicht
### Hauptfunktionen:
- **`deal_card()`**:
  - Zieht zufällig eine Karte aus einem simulierten Deck.
- **`calculate_score(hand)`**:
  - Berechnet die Punktzahl der Hand und behandelt die spezielle Rolle des Asses (1 oder 11).
- **`compare(player_score, dealer_score)`**:
  - Vergleicht die Punktzahl des Spielers und des Dealers, um den Gewinner zu ermitteln.
- **`play_game()`**:
  - Führt die Spielschritte aus: Karten verteilen, Spielerentscheidungen und Dealerlogik.

---

## Technische Details
- **Programmiersprache:** Python 3.x
- **Benötigte Bibliotheken:** `random` (integriert in Python)
- **Benutzeroberfläche:** Textbasiert (Terminal)

---
