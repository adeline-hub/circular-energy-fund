\# Contributing Guidelines



Questo repository documenta un progetto professionale avviato nel 2022 per la

progettazione, strutturazione e sviluppo di un \*\*fondo circolare per la produzione

e condivisione di energia solare sostenibile in Sicilia\*\*.



Il repository integra attività di \*\*Project Management\*\*, \*\*Fund Management\*\*,

\*\*Data Management\*\* ed \*\*Energy Management\*\* ed è concepito come una base

strutturata, tracciabile e auditabile.



---



\## Principi Generali



\- Tutte le modifiche devono essere \*\*tracciabili\*\*

\- Le decisioni progettuali devono essere \*\*documentate\*\*

\- I modelli finanziari ed energetici devono essere \*\*riproducibili\*\*

\- Il repository deve rimanere \*\*presentabile per clienti e stakeholder\*\*



---



\## Struttura del Repository



Il repository è organizzato in moduli tematici:



\- `docs/`  

&nbsp; Documentazione di progetto, governance e meeting notes



\- `models/`  

&nbsp; Modelli finanziari ed energetici (Excel)



\- `data/`  

&nbsp; Dataset di benchmark e simulazioni



\- `governance/`  

&nbsp; Materiale di compliance, legale e regolatorio



Ogni contributo deve rispettare questa struttura.



---



\## Regole di Collaborazione



\### Branching



\- `main`  

&nbsp; Contiene solo versioni \*\*stabili\*\*, validate e presentabili a clienti o investitori



\- `develop`  

&nbsp; Contiene il lavoro operativo in corso



\- Branch tematici per nuove attività:

&nbsp; - `feature/finance-\*`

&nbsp; - `feature/energy-\*`

&nbsp; - `feature/data-\*`

&nbsp; - `docs/\*`



Le modifiche \*\*non devono mai\*\* essere fatte direttamente su `main`.



---



\## Commit Message



I commit devono essere \*\*chiari, concisi e descrittivi\*\*.



Formato consigliato:





Esempi:

\- `\[DOCS] Update README and project scope`

\- `\[FINANCE] Revise financial assumptions and KPIs`

\- `\[ENERGY] Update energy production model`

\- `\[DATA] Improve blockchain data architecture`



---



\## Modelli Excel (.xlsx)



I file Excel rappresentano modelli critici del progetto.



Regole:

\- Un file = un modello

\- Evitare dati sensibili o personali

\- Le formule devono essere \*\*trasparenti e documentate\*\*

\- Le modifiche strutturali devono essere descritte nel commit



Quando possibile:

\- mantenere i nomi dei fogli in inglese

\- evitare celle nascoste o protette senza documentazione



---



\## Documentazione (.md)



\- Usare Markdown per documentare:

&nbsp; - decisioni

&nbsp; - assunzioni

&nbsp; - architettura

&nbsp; - meeting notes

\- Ogni documento deve avere:

&nbsp; - titolo chiaro

&nbsp; - contesto

&nbsp; - data o periodo di riferimento (se rilevante)



---



\## Versioning



Il progetto segue un versioning semantico adattato:







\- \*\*MAJOR\*\* → nuove fasi di progetto o cambi strutturali

\- \*\*MINOR\*\* → nuove funzionalità o modelli

\- \*\*PATCH\*\* → correzioni e miglioramenti minori



Le versioni devono essere taggate su `main`.



---



\## Compliance e Dati Sensibili



\- Non caricare dati personali dei soci

\- Non caricare documenti legali confidenziali senza autorizzazione

\- Usare placeholder o dati simulati per modelli e dashboard



---



\## Qualità e Revisione



Prima di integrare modifiche su `main`:

\- verificare la coerenza con il modello esistente

\- assicurarsi che i file siano leggibili e completi

\- verificare che i modelli Excel funzionino correttamente



---



\## Obiettivo del Repository



Questo repository non è solo un archivio tecnico, ma uno strumento per:

\- supportare decisioni strategiche

\- garantire trasparenza

\- facilitare la collaborazione

\- documentare un modello replicabile di fondo energetico circolare



---



\*Seguendo queste linee guida, il repository rimane coerente, professionale e

utilizzabile nel tempo da team interni, partner e stakeholder esterni.\*



