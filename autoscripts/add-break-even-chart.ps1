$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "models\financial\financial_model_crowdfunding.xlsx"
$fullPath = Join-Path (Get-Location) $path

$workbook = $excel.Workbooks.Open($fullPath)

$cashflow  = $workbook.Sheets.Item("Cashflow")
$dashboard = $workbook.Sheets.Item("Dashboard")

# =========================
# DATI BREAK-EVEN
# =========================

$lastRow = $cashflow.Cells($cashflow.Rows.Count, "A").End(-4162).Row  # xlUp

# Colonna di supporto per linea zero (F)
$cashflow.Cells.Item(1,6) = "Linea Zero"

for ($i = 2; $i -le $lastRow; $i++) {
    $cashflow.Cells.Item($i,6) = 0
}

# =========================
# GRAFICO BREAK-EVEN
# =========================

$chart = $dashboard.Shapes.AddChart2(240, 4, 50, 470, 650, 280).Chart
$chart.ChartType = 65 # xlLine

$chart.SetSourceData(
    $cashflow.Range("A2:A$lastRow,E2:E$lastRow,F2:F$lastRow")
)

$chart.HasTitle = $true
$chart.ChartTitle.Text = "Break-even – Cashflow cumulato"

# Assi
$chart.Axes(1).HasTitle = $true
$chart.Axes(1).AxisTitle.Text = "Anno"

$chart.Axes(2).HasTitle = $true
$chart.Axes(2).AxisTitle.Text = "€"

# Formattazione linea zero
$seriesZero = $chart.SeriesCollection(2)
$seriesZero.Format.Line.ForeColor.RGB = 255
$seriesZero.Format.Line.DashStyle = 2

# Evidenzia area negativa
$chart.Axes(2).MinimumScale = $cashflow.Range("E2:E$lastRow").Min() * 1.1

$workbook.Save()
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Break-even chart creato correttamente."
