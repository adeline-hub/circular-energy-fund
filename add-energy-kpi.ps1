$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "models\financial\financial_model_crowdfunding.xlsx"
$fullPath = Join-Path (Get-Location) $path

$workbook = $excel.Workbooks.Open($fullPath)

# =====================
# CREA / RESET ENERGY MODEL
# =====================
foreach ($s in $workbook.Sheets) {
    if ($s.Name -eq "Energy_Model") {
        $s.Delete()
        break
    }
}

$energy = $workbook.Sheets.Add()
$energy.Name = "Energy_Model"

# =====================
# INPUT ENERGETICI
# =====================
$energy.Cells.Item(1,1) = "Parametro"
$energy.Cells.Item(1,2) = "Valore"
$energy.Cells.Item(1,3) = "Unità"

$energy.Range("A1:C1").Font.Bold = $true

$energy.Cells.Item(2,1) = "Potenza impianto"
$energy.Cells.Item(2,2) = 500
$energy.Cells.Item(2,3) = "kWp"

$energy.Cells.Item(3,1) = "Produzione specifica"
$energy.Cells.Item(3,2) = 1500
$energy.Cells.Item(3,3) = "kWh/kWp"

$energy.Cells.Item(4,1) = "Produzione annua"
$energy.Cells.Item(4,2).Formula = "=B2*B3"
$energy.Cells.Item(4,3) = "kWh"

$energy.Cells.Item(5,1) = "Autoconsumo"
$energy.Cells.Item(5,2) = 0.70
$energy.Cells.Item(5,2).NumberFormat = "0%"
$energy.Cells.Item(5,3) = "%"

$energy.Cells.Item(6,1) = "Energia autoconsumata"
$energy.Cells.Item(6,2).Formula = "=B4*B5"
$energy.Cells.Item(6,3) = "kWh"

$energy.Cells.Item(7,1) = "Energia condivisa"
$energy.Cells.Item(7,2).Formula = "=B4-B6"
$energy.Cells.Item(7,3) = "kWh"

$energy.Cells.Item(8,1) = "Numero soci"
$energy.Cells.Item(8,2) = 100
$energy.Cells.Item(8,3) = "n"

$energy.Cells.Item(9,1) = "Energia per socio"
$energy.Cells.Item(9,2).Formula = "=B7/B8"
$energy.Cells.Item(9,3) = "kWh/socio"

# =====================
# DASHBOARD KPI
# =====================
$dashboard = $workbook.Sheets.Item("Dashboard")

$dashboard.Cells.Item(9,1)  = "Produzione annua (kWh)"
$dashboard.Cells.Item(10,1) = "Autoconsumo (%)"
$dashboard.Cells.Item(11,1) = "Energia per socio (kWh)"

$dashboard.Range("A9:A11").Font.Bold = $true

$dashboard.Cells.Item(9,2).Formula  = "=Energy_Model!B4"
$dashboard.Cells.Item(10,2).Formula = "=Energy_Model!B5"
$dashboard.Cells.Item(11,2).Formula = "=Energy_Model!B9"

$dashboard.Cells.Item(10,2).NumberFormat = "0%"

# =====================
# MINI DATASET PER GRAFICO
# =====================
$energy.Cells.Item(12,1) = "Tipo"
$energy.Cells.Item(12,2) = "kWh"

$energy.Cells.Item(13,1) = "Autoconsumo"
$energy.Cells.Item(13,2).Formula = "=B6"

$energy.Cells.Item(14,1) = "Condivisa"
$energy.Cells.Item(14,2).Formula = "=B7"

# =====================
# GRAFICO ENERGIA
# =====================
$chart = $dashboard.Shapes.AddChart2(240, 51, 420, 420, 300, 220).Chart
$chart.ChartType = 51 # colonne

$chart.SetSourceData($energy.Range("A13:B14"))
$chart.HasTitle = $true
$chart.ChartTitle.Text = "Produzione elettrica – Autoconsumo vs Condivisione"

$workbook.Save()
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Energy KPI e grafico integrati correttamente."