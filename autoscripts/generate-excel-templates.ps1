$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

function Ensure-Folder {
    param ([string]$FilePath)
    $folder = Split-Path $FilePath
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
    }
}

function New-ExcelFile {
    param (
        [string]$Path,
        [hashtable]$Sheets
    )

    Ensure-Folder $Path

    $workbook = $excel.Workbooks.Add()

    # Usa il primo foglio
    $baseSheet = $workbook.Sheets.Item(1)
    $baseSheet.Name = ($Sheets.Keys | Select-Object -First 1)

    $headers = $Sheets[$baseSheet.Name]
    for ($i = 0; $i -lt $headers.Count; $i++) {
        $baseSheet.Cells.Item(1, $i + 1) = $headers[$i]
        $baseSheet.Cells.Item(1, $i + 1).Font.Bold = $true
    }
    $baseSheet.Columns.AutoFit() | Out-Null

    # Altri fogli
    foreach ($sheetName in ($Sheets.Keys | Select-Object -Skip 1)) {
        $sheet = $workbook.Sheets.Add()
        $sheet.Name = $sheetName

        $headers = $Sheets[$sheetName]
        for ($i = 0; $i -lt $headers.Count; $i++) {
            $sheet.Cells.Item(1, $i + 1) = $headers[$i]
            $sheet.Cells.Item(1, $i + 1).Font.Bold = $true
        }
        $sheet.Columns.AutoFit() | Out-Null
    }

    # ✅ SAVE CORRETTO
    $fullPath = Join-Path (Get-Location) $Path
    $workbook.SaveAs($fullPath)
    $workbook.Close()
}

# ===========================
# GENERAZIONE FILE EXCEL
# ===========================

New-ExcelFile "models\financial\roadmap_milestones.xlsx" @{
    "Timeline"    = @("Fase","Inizio","Fine","Responsabile","Stato")
    "Deliverable" = @("Deliverable","Milestone","Owner","Data","Note")
}

New-ExcelFile "models\financial\risk_register.xlsx" @{
    "Rischi" = @("ID","Descrizione","Categoria","Probabilità","Impatto","Mitigazione","Owner","Stato")
}

New-ExcelFile "models\financial\financial_model_crowdfunding.xlsx" @{
    "Assunzioni" = @("Parametro","Valore","Note")
    "CAPEX"      = @("Voce","Costo","Fornitore")
    "OPEX"       = @("Voce","Costo annuo")
    "Ricavi"     = @("Fonte","Importo annuo")
    "Cashflow"   = @("Anno","Cash In","Cash Out","Netto")
}

New-ExcelFile "models\energy\pv_production_estimate.xlsx" @{
    "Impianto"          = @("Parametro","Valore")
    "Produzione"        = @("Mese","kWh stimati")
    "DistribuzioneSoci" = @("Socio","Quota %","kWh assegnati")
}

New-ExcelFile "data\benchmarks\energy_fund_benchmark.xlsx" @{
    "CasiStudio" = @("Nome","Paese","Tecnologia","Numero Soci","ROI stimato")
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ File Excel creati correttamente."