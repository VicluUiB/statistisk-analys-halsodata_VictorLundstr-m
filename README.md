# Statistisk analys av hälsodata

Examinerande skoluppgift i statistisk dataanalys med Python.

Författare: Victor Lundström

## Del 1 – Grundläggande analys och statistik

Analysen finns i `analys.ipynb` på branchen `del1` och omfattar:

- Beskrivande statistik för ålder, vikt, längd, systoliskt blodtryck och kolesterol.
- Histogram, boxplot och stapeldiagram.
- Simulering av sjukdomsförekomst.
- Konfidensintervall med normalapproximation och percentil-bootstrap.
- Ensidigt Welch-t-test av om rökare har högre medelblodtryck än icke-rökare.
- Simulering av testets power vid olika antagna skillnader.

Metodförklaringar, resultattolkningar och källhänvisningar finns i notebooken.

## Filer

- `analys.ipynb`: analys, figurer och tolkningar.
- `health_study_dataset.csv`: dataset från kursen.
- `requirements.txt`: paketversioner som användes i analysen.
- `README.md`: projektbeskrivning och körinstruktioner.

## Köra analysen

Analysen har körts med Python 3.14.7 i VS Code.

1. Klona repot och gå in i projektmappen:

   ```bash
   git clone https://github.com/VicluUiB/statistisk-analys-halsodata_VictorLundstr-m.git
   cd statistisk-analys-halsodata_VictorLundstr-m
   git switch del1
   ```

2. Installera paketen i den Python-miljö som ska användas:

   ```bash
   python -m pip install -r requirements.txt
   python -m pip install ipykernel
   ```

3. Öppna projektmappen i VS Code med tilläggen Python och Jupyter installerade.
4. Öppna `analys.ipynb` och välj den Python-miljö där paketen installerades som kernel.
5. Se till att `health_study_dataset.csv` ligger i samma mapp som notebooken.
6. Starta om kernel och välj **Run All** för att köra analysen från början till slut.

## Reproducerbarhet

Slumpsimuleringarna använder fasta seeds. Paketversionerna anges
i `requirements.txt`. Notebooken har kontrollerats genom att starta
om kernel och köra samtliga celler i ordning utan fel.