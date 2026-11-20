# Statistisk analys av hälsodata

Examinerande skoluppgift i statistisk dataanalys med Python.

Författare: Victor Lundström

## Del 1 – Grundläggande analys och statistik

Inlämningsversionen finns på branchen `del1` och omfattar:

- Beskrivande statistik för ålder, vikt, längd, systoliskt blodtryck och kolesterol.
- Histogram, boxplot med individpunkter och stapeldiagram.
- Simulering av sjukdomsstatus för 1000 personer med observerad sjukdomsandel som sannolikhet.
- Jämförelse av konfidensintervall med normalapproximation och percentil-bootstrap.
- Ensidigt Welch-t-test av om rökare har högre medelblodtryck än icke-rökare.
- Power-simulering vid olika antagna skillnader mellan gruppernas medelvärden.

## Del 2 – Fördjupning och pipeline

Inlämningsversionen finns på branchen `del2`. Den bygger vidare på
del 1 i samma notebook och omfattar:

- Återanvändbar kod i modulen `health_analyzer.py`.
- Klassen `HealthAnalyzer` med metoder för statistik, visualisering och regression.
- Enkel linjär regression med ålder som förklarande variabel.
- Multipel linjär regression med ålder och vikt som förklarande variabler.
- Matris- och vektorberäkningar med NumPy och minsta kvadratmetoden.
- Residualgraf för granskning av den multipla regressionsmodellen.

Metodmotiveringar, resultattolkningar och källhänvisningar finns
i notebooken. Klassen och funktionerna dokumenteras med docstrings.
Regressionerna beskriver samband i datasetet; prediktionsförmågan
på nya observationer har inte utvärderats.

## Filer

- `analys.ipynb`: analys, figurer, metodförklaringar och tolkningar.
- `health_analyzer.py`: klass med analys- och visualiseringsmetoder.
- `health_study_dataset.csv`: dataset från kursen med 800 observationer.
- `requirements.txt`: paketversioner som användes i analysen.
- `README.md`: projektbeskrivning och körinstruktioner.

## Köra analysen

Analysen har körts med Python 3.14.7 i VS Code.

1. Klona repot och gå in i projektmappen:

   ```bash
   git clone https://github.com/VicluUiB/statistisk-analys-halsodata_VictorLundstr-m.git
   cd statistisk-analys-halsodata_VictorLundstr-m
   ```

2. Välj den del som ska granskas:

   ```bash
   git switch del1
   ```

   eller:

   ```bash
   git switch del2
   ```

3. Installera paketen i den Python-miljö som ska användas:

   ```bash
   python -m pip install -r requirements.txt
   python -m pip install ipykernel
   ```

4. Öppna projektmappen i VS Code med tilläggen Python och Jupyter installerade.
5. Öppna `analys.ipynb` och välj miljön där paketen installerades som kernel.
6. Se till att `health_study_dataset.csv` och `health_analyzer.py` ligger i samma mapp som notebooken.
7. Starta om kernel och välj **Run All** för att köra samtliga celler i ordning.

## Reproducerbarhet

Slumpsimuleringarna använder fasta seeds. Paketversionerna anges
i `requirements.txt`. Relativa filsökvägar används så att analysen
inte är beroende av en specifik sökväg på författarens dator.