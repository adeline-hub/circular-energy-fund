$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "models\financial\financial_model_crowdfunding.xlsx"
$fullPath = Join-Path (Get-Location) $path

$workbook = $excel.Workbooks.Open($fullPath)

$cashflow  = $workbook.Sheets.Item("Cashflow")
$dashboard = $workbook.Sheets.Item("Dashboard")

# =========================
# GRAFICO 1 – CASHFLOW CUMULATO
# =========================

$lastRow = $cashflow.Cells($cashflow.Rows.Count, "A").End(-4162).Row  # xlUp

$chart1 = $dashboard.Shapes.AddChart2(240, 4, 50, 200, 350, 250).Chart
$chart1.ChartType = 65 # xlLine

$chart1.SetSourceData(
    $cashflow.Range("A2:A$lastRow,E2:E$lastRow")
)

$chart1.HasTitle = $true
$chart1.ChartTitle.Text = "Cashflow cumulato nel tempo"

$chart1.Axes(1).HasTitle = $true
$chart1.Axes(1).AxisTitle.Text = "Anno"

$chart1.Axes(2).HasTitle = $true
$chart1.Axes(2).AxisTitle.Text = "€"

# =========================
# GRAFICO 2 – IRR (INDICATORE)
# =========================

# Mini tabella di supporto (nascosta)
$dashboard.Cells.Item(10,1) = "IRR"
$dashboard.Cells.Item(10,2).Formula = "=Cashflow!B24"
$dashboard.Range("A10:B10").Font.ColorIndex = 15

$chart2 = $dashboard.Shapes.AddChart2(240, 51, 420, 200, 300, 200).Chart
$chart2.ChartType = 51 # xlColumnClustered

$chart2.SetSourceData($dashboard.Range("A10:B10"))

$chart2.HasTitle = $true
$chart2.ChartTitle.Text = "IRR progetto"

$chart2.Axes(2).MaximumScale = 0.2
$chart2.Axes(2).MinimumScale = 0

$workbook.Save()
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Grafici automatici creati nella Dashboard."