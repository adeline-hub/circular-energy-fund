$templates = @{
  "README.md" = @"
# Circular Energy Fund

Repository di progetto per la progettazione e realizzazione di un fondo circolare
per la produzione e distribuzione di energia solare sostenibile in Sicilia.

## Obiettivo
Creare un veicolo di investimento partecipativo (crowdfunding o club di investimento)
per circa 100 soci, finalizzato alla costruzione di un impianto fotovoltaico sostenibile
che non sottragga terreno all’agricoltura e privilegi materiali e fornitori locali.

## Ambito
- Project Management
- Fund Management
- Data Management & Blockchain
- Energy Management

## Periodo
Avvio progetto: 2022
"@

  "docs/01_project_management/project_overview.md" = @"
# Project Overview

## Contesto
Supporto strategico, operativo e tecnologico al Cliente per la creazione
di un fondo circolare energetico in Sicilia.

## Obiettivi di Progetto
- Strutturare il veicolo di investimento
- Garantire compliance normativa
- Progettare architettura dati e modello energetico

## KPI Principali
- Numero soci
- CAPEX impianto
- Produzione annua stimata (kWh)
- Beneficio energetico per socio
"@

  "docs/01_project_management/governance_model.md" = @"
# Modello di Governance

## Principi
- Trasparenza
- Partecipazione dei soci
- Tracciabilità decisionale

## Organi
- Assemblea dei soci
- Comitato di gestione
- Advisor tecnici e legali
"@

  "docs/01_project_management/milestones_definition.md" = @"
# Milestones di Progetto

## M1 – Studio di fattibilità
Analisi tecnica, normativa e finanziaria.

## M2 – Struttura fondo
Definizione modello crowdfunding / club di investimento.

## M3 – Architettura dati ed energia
Progettazione flussi dati e modello di distribuzione energetica.
"@

  "docs/01_project_management/meeting_notes/meeting_notes_template.md" = @"
# Meeting Notes

**Data:**  
**Partecipanti:**  
**Obiettivo incontro:**

## Discussione
- 

## Decisioni
- 

## Azioni
| Azione | Responsabile | Scadenza |
|-------|-------------|----------|
"@

  "docs/02_fund_management/crowdfunding/compliance/regulatory_overview.md" = @"
# Compliance Crowdfunding

## Normativa Applicabile
- Regolamento Europeo ECSP
- Normativa italiana su crowdfunding

## Requisiti Chiave
- Trasparenza informativa
- KYC / AML
- Limiti di investimento

## Impatti sul Progetto
- Struttura del veicolo
- Comunicazione agli investitori
"@

  "docs/02_fund_management/crowdfunding/production/investor_journey.md" = @"
# Investor Journey

## Fasi
1. Informazione e onboarding
2. Investimento
3. Costruzione impianto
4. Produzione e benefici energetici

## Touchpoint
- Piattaforma digitale
- Reportistica periodica
"@

  "docs/03_data_management/production/data_architecture.md" = @"
# Architettura Dati

## Fonti
- Produzione impianto
- Consumi soci
- Transazioni finanziarie

## Principi
- Trasparenza
- Sicurezza
- Auditabilità

## Output
- Dashboard
- Report normativi
"@

  "docs/04_energy_management/production/energy_distribution_model.md" = @"
# Modello di Distribuzione Energia

## Principi
- Equità
- Autoconsumo prioritario
- Riduzione costi energetici

## Metodo
Distribuzione proporzionale all’investimento del socio
con conguaglio periodico.
"@
}

foreach ($file in $templates.Keys) {
  if (Test-Path $file) {
    Set-Content -Path $file -Value $templates[$file] -Encoding UTF8
  }
}
Write-Output "Template Markdown popolati con successo."