# Reel: „Der 10-Sekunden-Nacken-Check"

Fertiges Instagram-Reel für Gerstner Physiotherapie – 1080 × 1920, 28 Sekunden, 30 fps, ohne Ton.
Passend zum bestehenden HWS-Carousel (gleiche Farben, Schriften, Fotos).

| Datei | Was es ist |
|---|---|
| `reel-nacken-check.mp4` | Das fertige Video – direkt hochladbar |
| `cover.png` | Titelbild fürs Raster (in der App unter „Cover" → „Aus Galerie") |
| `reel.html` | Die Animation als Quelle (Texte hier ändern) |
| `build.mjs` | Baut aus `reel.html` wieder ein MP4: `node build.mjs` |

---

## Warum genau dieses Format Reichweite bringt

Reichweite auf Instagram entsteht 2026 fast nur noch über vier Signale. Das Reel ist so
gebaut, dass es jedes einzelne davon bedient:

| Signal | Wie das Reel es auslöst |
|---|---|
| **Hook < 1 Sekunde** | Drei Wörter, riesig, rot: „Ist dein Nacken zu steif?" – eine Ja/Nein-Frage, die fast jeder mit „hm, eigentlich schon" beantwortet. |
| **Watch-Time** | Der Zuschauer *macht mit*. Wer den Kopf dreht, scrollt nicht weiter. „Test 1 / 3" erzeugt zusätzlich den Wunsch, alle drei zu sehen. |
| **Kommentare** | „Schreib L oder R" – eine Antwort, die einen Buchstaben kostet. Die niedrigste Hürde, die es gibt, und trotzdem echte Information für dich. |
| **Speichern & Teilen** | Ein Selbsttest, den man später nochmal machen will (Speichern) und den man dem Kollegen mit dem steifen Nacken schickt (Teilen). Teilen ist das stärkste Signal überhaupt. |

Der Schluss („Nochmal ansehen und mitmachen") lädt zum Loop ein – das Reel startet nach
28 Sekunden automatisch neu, was die durchschnittliche Wiedergabezeit weiter hebt.

**Ehrliche Erwartung:** Viralität kann niemand garantieren, auch keine perfekte Datei. Was
man steuern kann, ist die Trefferwahrscheinlichkeit – über Format, Hook, Timing und
Konsistenz. Ein Praxis-Account mit lokalem Einzugsgebiet wächst realistisch über *viele*
solide Reels, nicht über einen Zufallstreffer. Der Nacken-Check ist bewusst ein Format zum
Wiederholen: dieselbe Mechanik funktioniert für Schulter, Hüfte, LWS, Knie und Sprunggelenk.

---

## Vor dem Posten: 4 Handgriffe in der App

1. **Audio drauflegen.** Das Video ist stumm. Reels ohne Ton werden schlechter ausgespielt.
   In der App beim Hochladen ein Audio aus der Instagram-Bibliothek wählen – ruhiger,
   treibender Beat, keine Lyrics, die vom Text ablenken. Kein Musik-Upload von außen:
   Nur die In-App-Bibliothek ist lizenzrechtlich sauber.
   *Hinweis:* Business-Konten sehen eine kleinere Auswahl an Trending-Sounds als
   Creator-Konten. Wenn die Auswahl mager wirkt, lohnt der Wechsel auf „Creator".
2. **Cover setzen.** `cover.png` als Titelbild hochladen, damit das Profilraster ordentlich bleibt.
3. **Ort taggen.** „Sand am Main" bzw. die Praxisadresse. Lokale Signale bringen bei einer
   Praxis mehr als jeder Reichweiten-Hashtag – Menschen aus 200 km Entfernung werden nie Patient.
4. **Als Reel *und* in die Story.** In der Story mit Umfrage-Sticker: „Welche Seite ist
   steifer? L / R". Story-Interaktionen ziehen das Reel mit hoch.

---

## Caption zum Kopieren

```
Steifer Nacken? Dieser Check dauert 10 Sekunden.

Die Halswirbelsäule soll sich in alle Richtungen frei bewegen können:
✔️ ca. 80° Drehung pro Seite
✔️ ca. 45° Seitneigung pro Seite
✔️ Kinn locker nach hinten schiebbar

Spannend ist selten die absolute Zahl – spannend ist der Seitenunterschied.
Wenn eine Seite deutlich weniger weit kommt, hat das immer einen Grund:
Muskelspannung, Gelenkfunktion, Haltung oder eine alte Überlastung.

Genau das schauen wir uns in der Untersuchung an – und behandeln dann die Ursache,
nicht nur den Schmerz.

💬 Welche Seite ist bei dir steifer? Schreib einfach L oder R in die Kommentare.
📌 Speichern, wenn du den Check in vier Wochen nochmal machen willst.

Wichtig: Der Check ersetzt keine Untersuchung. Bei Schwindel, Übelkeit,
Taubheitsgefühl oder starken Schmerzen bitte abbrechen und ärztlich abklären lassen.

📍 Gerstner Physiotherapie · Zeiler Str. 20 · Sand am Main · 09524 5297
```

### Hashtags (unter die Caption oder in den ersten Kommentar)

```
#nackenschmerzen #hws #physiotherapie #verspannungen #kopfschmerzen #beweglichkeit
#physiosandammain #sandammain #haßberge #schweinfurt #bamberg #physiopraxis
#rückengesundheit #büroalltag #selbsttest
```

Mischung mit Absicht: 6 Themen-Tags (was), 5 lokale Tags (wo), 4 Verhaltens-Tags (wer).
Nicht mehr als ~15 – darüber hinaus bringt es nichts. Die lokalen Tags sind für eine Praxis
die wertvollsten, auch wenn sie kleiner sind.

---

## Hook-Varianten zum Testen

Das erste Textbild entscheidet über 80 % der Reichweite. In `reel.html` steht es in den drei
`<h1>`-Zeilen der Hook-Szene. Für A/B-Tests über mehrere Wochen:

| Variante | Text | Wirkt bei |
|---|---|---|
| A (aktuell) | „Ist dein Nacken zu steif?" | breit, niedrigschwellig |
| B | „90 % schaffen Test 2 nicht." | Neugier + Ehrgeiz |
| C | „Kopfschmerzen? Teste zuerst deinen Nacken." | Symptom-Sucher |
| D | „Dein Nacken knackt? Mach das hier, bevor du weiterknackst." | konkretes Ärgernis |

Immer nur *eine* Variable ändern und mindestens 5 Reels vergleichen – sonst misst man Zufall.

---

## Wenn ihr es selbst dreht (empfohlen, sobald Zeit ist)

Ein Gesicht schlägt Grafik. Dieses Reel funktioniert als Vorlage – dieselbe Struktur, nur
mit euch vor der Kamera. Handy hochkant, Fenster im Rücken der Kamera (nicht hinter euch),
Behandlungsliege oder heller Praxisflur als Hintergrund.

| Zeit | Bild | Was gesagt/gezeigt wird |
|---|---|---|
| 0–3 s | Nah, direkt in die Kamera | „Ist dein Nacken zu steif? Zehn Sekunden, drei Tests – mach mit." |
| 3–9 s | Halbtotale, seitlich | Rotation vormachen: „Kinn Richtung Schulter, erst rechts, dann links." Beide Seiten zeigen. |
| 9–14 s | Halbtotale, frontal | Seitneigung: „Ohr zur Schulter – Schulter bleibt unten." |
| 14–19 s | Nah, Profil | Doppelkinn: „Kinn gerade nach hinten, Blick geradeaus." |
| 19–24 s | Nah, direkt in die Kamera | „Seitenunterschied? Ziehen? Kopfschmerzen? Das gehört angeschaut." |
| 24–28 s | Nah, lächeln, Praxis im Hintergrund | „Schreib L oder R in die Kommentare." |

Untertitel in der App aktivieren – der Großteil schaut ohne Ton.
Erste drei Sekunden ohne Begrüßung, ohne Logo-Intro, ohne „Hallo, ich bin…". Direkt rein.

---

## Die ersten 60 Minuten nach dem Posten

Instagram testet ein Reel zuerst an einer kleinen Gruppe. Was in der ersten Stunde passiert,
entscheidet über den Rest.

- Posten, wenn eure Leute am Handy sind: **werktags 17–20 Uhr** oder **sonntags ab 18 Uhr**.
  (Nach vier Wochen in den Insights nachsehen, wann eure Follower wirklich aktiv sind.)
- Direkt danach die Story mit dem Umfrage-Sticker.
- **Jeden Kommentar in der ersten Stunde beantworten** – am besten mit einer Rückfrage
  („Seit wann merkst du das?"). Jede Antwort ist ein zusätzliches Signal.
- Nicht nach 20 Minuten die Insights checken und enttäuscht sein. Reels bauen sich über
  48–72 Stunden auf, gute laufen wochenlang nach.

---

## Fachlich & rechtlich

- **Keine Heilversprechen.** Die Texte sagen bewusst „kann begünstigen", „wir schauen uns an,
  woher es kommt" – nicht „wir machen dich schmerzfrei". Das ist nicht nur ehrlicher,
  sondern beim Heilmittelwerbegesetz auch die sichere Seite. Vorher-Nachher-Bilder von
  Behandlungen und Patienten-Erfolgsgeschichten sind heikel – im Zweifel vorher juristisch prüfen lassen.
- **Sicherheitshinweis bleibt drin.** Die Einblendung zu Schwindel/Übelkeit/Taubheit ist nicht
  nur Deko: Die getesteten Bewegungen sind endgradige HWS-Bewegungen. Der Hinweis gehört
  in jedes Video mit Selbsttest, auch in die Caption.
- **Bildrechte.** Die verwendeten Fotos stammen aus dem HWS-Carousel dieser Praxis. Für jede
  abgebildete Person sollte eine schriftliche Einwilligung zur Social-Media-Nutzung vorliegen.

---

## Nachschub: 8 Reels nach demselben Bauplan

Format kopieren, Thema tauschen – so entsteht eine Serie, die Leute abonnieren:

1. **Schulter-Check** – Hand hinter den Kopf, Hand hinter den Rücken, Seitenvergleich.
2. **Hüft-Check** – im Sitzen Bein über Bein: Wo klemmt es?
3. **Sprunggelenk-Check** – Knie über Zehen bei fersenkontakt, cm messen.
4. **„3 Fehler beim Nackendehnen"** – Mythos-Format, hoher Share-Wert.
5. **„Knacken im Nacken – gefährlich oder nicht?"** – Frage, die viele googeln.
6. **Arbeitsplatz in 30 Sekunden richtig einstellen** – hoher Save-Wert.
7. **„Was passiert in der ersten Behandlung?"** – nimmt Hemmschwellen, bringt Termine.
8. **Ein Tag in der Praxis** – Gesichter zeigen. Menschen buchen bei Menschen.

Rhythmus schlägt Perfektion: 2 Reels pro Woche über drei Monate bringen mehr als
zehn perfekte Videos in einer Woche und dann Stille.

---

## Video neu bauen

Texte in `reel.html` ändern, dann:

```bash
cd social-media/reel-nacken-check
node build.mjs
```

Das rendert 840 Einzelbilder mit Chromium und encodiert sie zu `reel-nacken-check.mp4`
(H.264, yuv420p, 30 fps, stumme Tonspur für maximale Upload-Kompatibilität).
Die Zeitachse steht am Ende von `reel.html` im `render(t)`-Block – jede Szene hat
`data-in` / `data-out` in Sekunden, jedes Element ein `data-d` (Verzögerung ab Szenenstart).
