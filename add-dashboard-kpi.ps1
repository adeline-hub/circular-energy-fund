$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "models\financial\financial_model_crowdfunding.xlsx"
$fullPath = Join-Path (Get-Location) $path

$workbook = $excel.Workbooks.Open($fullPath)

# =====================
# FOGLI
# =====================
$cashflow = $workbook.Sheets.Item("Cashflow")
$capex    = $workbook.Sheets.Item("CAPEX")

# Se esiste Dashboard, la cancella
foreach ($s in $workbook.Sheets) {
    if ($s.Name -eq "Dashboard") {
        $s.Delete()
        break
    }
}

$dashboard = $workbook.Sheets.Add()
$dashboard.Name = "Dashboard"

# =====================
# TITOLO
# =====================
$dashboard.Cells.Item(1,1) = "Dashboard KPI – Fondo Energetico Circolare"
$dashboard.Range("A1:E1").Merge()
$dashboard.Range("A1").Font.Bold = $true
$dashboard.Range("A1").Font.Size = 16

# =====================
# KPI LABELS
# =====================
$dashboard.Cells.Item(3,1) = "IRR"
$dashboard.Cells.Item(4,1) = "NPV"
$dashboard.Cells.Item(5,1) = "ROI"
$dashboard.Cells.Item(6,1) = "CAPEX Totale"
$dashboard.Cells.Item(7,1) = "Cashflow Finale"

$dashboard.Range("A3:A7").Font.Bold = $true

# =====================
# KPI VALUES (LINK)
# =====================
$dashboard.Cells.Item(3,2).Formula = "=Cashflow!B24"
$dashboard.Cells.Item(4,2).Formula = "=Cashflow!B25"
$dashboard.Cells.Item(5,2).Formula = "=Cashflow!B26"
$dashboard.Cells.Item(6,2).Formula = "=SUM(CAPEX!B:B)"
$dashboard.Cells.Item(7,2).Formula = "=MAX(Cashflow!E:E)"

# =====================
# FORMATTAZIONE
# =====================
$dashboard.Cells.Item(3,2).NumberFormat = "0.00%"
$dashboard.Cells.Item(5,2).NumberFormat = "0.00%"

$dashboard.Columns.AutoFit() | Out-Null

# Evidenzia KPI
$dashboard.Range("A3:B7").Borders.LineStyle = 1
$dashboard.Range("A3:B7").Interior.ColorIndex = 36

$workbook.Save()
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Dashboard KPI creata correttamente."