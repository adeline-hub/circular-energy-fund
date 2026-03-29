
# Progetto: Fondo Circolare per Energia Solare Sostenibile (Sicilia)

## Introduzione
Questo repository documenta la progettazione, strutturazione e sviluppo tecnico di un fondo circolare per la produzione e condivisione di energia elettrica tramite impianti solari sostenibili in Sicilia. Il progetto, avviato nel 2022, integra Project Management, Data Engineering e Fund Management. 

L'obiettivo è creare un modello di investimento collettivo replicabile e conforme alle normative vigenti, garantendo ai soci la massima trasparenza attraverso l'utilizzo della tecnologia blockchain.

## Obiettivo per i Soci Azionisti (Cittadini)
Il progetto mira alla creazione di un veicolo di investimento partecipativo per circa 100 soci iniziali. I pilastri dell'iniziativa sono:

- Investimento collettivo nella costruzione di un impianto fotovoltaico sostenibile.
- Tutela del territorio agricolo (utilizzo di impianti agrovoltaici o su superfici non produttive).
- Priorità a materiali e fornitori locali siciliani per massimizzare l'impatto economico sul territorio.
- Ritorni per i soci sotto forma di energia elettrica a prezzo scontato o rendimenti economici indiretti.

Il fondo opera secondo i principi dell'economia circolare: i benefici rimangono all'interno della comunità, i dati sono tracciabili in modo immutabile e la governance è orientata al lungo periodo.

## Stato di Avanzamento e Timeline di Project Management

Il progetto segue un approccio strutturato, dall'ideazione fino alla prototipazione tecnica attuale. Di seguito le fasi principali e lo stato di avanzamento:

### Fase 1: Ideazione e Studio di Fattibilità (Completata - 2022)
- Definizione dell'idea e dei requisiti del Cliente.
- Analisi normativa per la creazione di comunità energetiche e club di investimento.
- Valutazione preliminare dei siti in Sicilia e della capacità produttiva.

### Fase 2: Strutturazione Governance e Fund Management (Completata - 2023)
- Scelta del modello di partecipazione (Crowdfunding vs. Club di Investimento Privato).
- Redazione dei modelli finanziari e delle simulazioni di ritorno per i soci.
- Definizione dei requisiti legali e fiscali.

### Fase 3: Prototipazione Dati e Tecnologia (Stato Attuale - In Corso)
Attualmente ci troviamo nella fase di sviluppo e test degli strumenti di comunicazione e tracciabilità per i soci azionisti. I due deliverable principali di questa fase, presenti in questo repository, sono:
1. White Paper Interattivo: Sviluppato in Python (tramite Marimo), spiega in modo trasparente l'architettura blockchain per la tracciabilità dell'energia e la distribuzione dei dividendi.
2. Dashboard Prototipo: Un'interfaccia utente dedicata ai soci per monitorare la produzione energetica, i rendimenti economici e l'impatto ambientale della propria quota di investimento.

### Fase 4: Sviluppo Impianto e Lancio Operativo (Prossimi Passi)
- Inizio lavori di costruzione dell'impianto solare.
- Onboarding ufficiale dei primi 100 soci sulla piattaforma definitiva.
- Connessione degli smart meter dell'impianto all'infrastruttura blockchain per la generazione in tempo reale dei dati.

## Ambito del Progetto e Struttura del Repository

Gli archivi seguono una logica modulare per garantire tracciabilità, supportare gli audit e facilitare la scalabilità.

### 1. Project Management
Documentazione per la gestione, pianificazione e controllo.
- 1.1 Tools: Roadmap, Gantt, backlog, framework di gestione e reportistica.
- 1.2 Meeting Notes: Verbali con il Cliente, workshop strategici e decisioni chiave.
- 1.3 Milestones: Definizione delle tappe, stato di avanzamento e deliverable.

### 2. Fund, Data & Energy Management

#### 2.1 Fund Management
Gestione della raccolta fondi e della governance.
- 2.1.A Crowdfunding: Struttura dell'offerta, flussi finanziari, ticket di investimento.
- 2.1.B Club Privato: Governance, diritti/doveri dei soci, meccanismi di ingresso/uscita.
- Sottosezioni per entrambi: Compliance (analisi normativa), Benchmark (casi studio europei), Production (modelli finanziari e simulazioni).

#### 2.2 Data Management - Blockchain
Gestione dei dati finanziari ed energetici tramite registri distribuiti per garantire auditabilità.
- Compliance: Gestione dati personali e normative transazioni.
- Benchmark: Soluzioni blockchain nel settore energetico.
- Production: Architettura dati, smart contract per distribuzione token/crediti, pipeline dati. In questa sezione risiedono il White Paper (Marimo) e il codice backend.

#### 2.3 Energy Management
Gestione operativa della produzione e distribuzione fisica.
- Compliance: Normative GSE e autorità competenti.
- Benchmark: Tecnologie fotovoltaiche e modelli di comunità energetiche.
- Production: Stime di produzione, ottimizzazione rendimenti e logica della Dashboard per i soci.

## Valore Generato e Sviluppi Futuri
Questo lavoro trasforma una visione comunitaria in una struttura operativa solida, riducendo i rischi normativi e creando una base dati affidabile per le decisioni. 

I prossimi obiettivi includono il consolidamento del modello pilota, la scalabilità su nuovi impianti in altre aree, l'estensione del numero di soci azionisti e l'automazione avanzata della reportistica attraverso i prototipi attualmente in sviluppo.


# Progetto Fondo Circolare per Energia Solare Sostenibile  
**Avvio progetto: 2022**

## Introduzione

Questo repository documenta il lavoro svolto dalla nostra società di gestione a supporto del Cliente, a partire dal 2022, per la progettazione, strutturazione e avvio di un **fondo circolare per la produzione e condivisione di energia elettrica da impianti solari sostenibili in Sicilia**.

Il progetto integra **Project Management**, **Data Engineering** e **Fund Management**, con l’obiettivo di creare un modello di investimento collettivo **replicabile**, **sostenibile** e **conforme alle normative vigenti**.

---

## Obiettivo del Cliente

L’obiettivo principale del Cliente è la creazione di un **veicolo di investimento partecipativo** che consenta a circa **100 soci** di:

- investire collettivamente nella costruzione di un **impianto fotovoltaico sostenibile**
- non sottrarre terreno all’agricoltura (es. impianti agrovoltaici o su superfici non produttive)
- utilizzare, per quanto possibile, **materiali e fornitori locali (Sicilia)**
- beneficiare dei ritorni dell’investimento sotto forma di:
  - **energia elettrica a prezzo scontato**
  - e/o **rendimenti economici indiretti**

Il fondo è concepito come **circolare**, ovvero:
- i benefici economici ed energetici rimangono all’interno della comunità dei soci
- i dati di produzione, consumo e distribuzione sono tracciabili e verificabili
- la governance è trasparente e orientata al lungo periodo

---

## Ambito del Progetto

Il progetto combina competenze e attività nei seguenti ambiti:

- **Project Management**
  - pianificazione
  - coordinamento degli stakeholder
  - controllo dell’avanzamento e delle milestone

- **Fund Management**
  - crowdfunding
  - club di investimento privato
  - modelli di governance e distribuzione dei ritorni

- **Data Management & Engineering**
  - gestione dei dati energetici, finanziari e di compliance
  - integrazione di tecnologie blockchain per trasparenza e auditabilità

- **Energy Management**
  - analisi della produzione
  - distribuzione dell’energia tra i soci
  - ottimizzazione dei rendimenti energetici

---

## Struttura del Repository

La struttura degli archivi segue una logica modulare, pensata per:

- facilitare la collaborazione del team
- garantire tracciabilità delle decisioni
- supportare audit, compliance e scalabilità futura

### 1. Project Management

Documentazione relativa alla gestione complessiva del progetto.

#### 1.1 Project Management Tools
- strumenti di pianificazione (roadmap, Gantt, backlog)
- framework di gestione (Agile / Waterfall ibrido)
- modelli di reportistica

#### 1.2 Meeting Notes
- verbali degli incontri con il Cliente
- workshop strategici e tecnici
- decisioni chiave e azioni concordate

#### 1.3 Milestones Archives
- definizione delle milestone
- stato di avanzamento
- deliverable associati a ciascuna fase

---

### 2. Fund, Data & Energy Management

#### 2.1 Fund Management

##### 2.1.A Fund Management – Crowdfunding
Gestione del modello di raccolta fondi tramite piattaforme di crowdfunding:
- struttura dell’offerta
- ticket di investimento
- flussi finanziari
- comunicazione verso i soci-investitori

##### 2.1.B Fund Management – Club di Investimento Privato
Strutturazione alternativa o complementare tramite club di investimento:
- governance del club
- diritti e doveri dei soci
- meccanismi di ingresso e uscita

Per entrambe le sezioni (2.1.A e 2.1.B) sono presenti i seguenti sottofolder:

- **compliance**
  - analisi normativa
  - requisiti legali e fiscali
  - documentazione per enti regolatori

- **benchmark**
  - analisi di casi simili (Italia / Europa)
  - confronto dei modelli di rendimento
  - best practice di mercato

- **production**
  - documentazione operativa
  - modelli finanziari
  - simulazioni di ritorno per i soci

---

#### 2.2 Data Management – Blockchain

Gestione dei dati di progetto, finanziari ed energetici con particolare attenzione a:
- trasparenza
- tracciabilità
- auditabilità

Sottofolder:
- **compliance**
  - gestione dei dati personali
  - normative su dati e transazioni
- **benchmark**
  - soluzioni blockchain nel settore energia
- **production**
  - architettura dati
  - smart contract (se applicabili)
  - pipeline di raccolta e validazione dei dati

---

#### 2.3 Energy Management

Analisi e gestione della produzione e distribuzione energetica dell’impianto solare.

Sottofolder:
- **compliance**
  - normative energetiche
  - requisiti GSE e autorità competenti
- **benchmark**
  - confronto tra tecnologie fotovoltaiche
  - modelli di comunità energetiche
- **production**
  - stime di produzione
  - modelli di distribuzione ai soci
  - ottimizzazione dei consumi e dei rendimenti

---

## Valore Generato

Attraverso questo progetto la nostra società ha supportato il Cliente nel:

- trasformare un’idea in una **struttura operativa concreta**
- ridurre i rischi normativi e operativi
- creare una base dati solida a supporto delle decisioni strategiche
- progettare un modello energetico **sostenibile, locale e replicabile**

---

## Prossimi Passi

- consolidamento del modello pilota
- scalabilità su ulteriori impianti
- estensione del numero di soci
- automazione avanzata della reportistica e della governance

---

*Questo repository rappresenta una sintesi strutturata del lavoro svolto ed è concepito come una base viva, aggiornabile e condivisibile con stakeholder interni ed esterni.*

