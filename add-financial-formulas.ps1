$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "models\financial\financial_model_crowdfunding.xlsx"
$fullPath = Join-Path (Get-Location) $path

$workbook = $excel.Workbooks.Open($fullPath)

# =====================
# ASSUNZIONI
# =====================
$assumptions = $workbook.Sheets.Item("Assunzioni")
$assumptions.Cells.Item(1,1) = "Parametro"
$assumptions.Cells.Item(1,2) = "Valore"

$assumptions.Cells.Item(2,1) = "Tasso di sconto"
$assumptions.Cells.Item(2,2) = 0.06
$assumptions.Cells.Item(2,2).NumberFormat = "0.00%"

# =====================
# CASHFLOW
# =====================
$cashflow = $workbook.Sheets.Item("Cashflow")

$cashflow.Cells.Item(1,1) = "Anno"
$cashflow.Cells.Item(1,2) = "Cash In"
$cashflow.Cells.Item(1,3) = "Cash Out"
$cashflow.Cells.Item(1,4) = "Netto"
$cashflow.Cells.Item(1,5) = "Cumulato"

# Anno 0
$cashflow.Cells.Item(2,1) = 0
$cashflow.Cells.Item(2,2) = 0
$cashflow.Cells.Item(2,3) = 500000

# Anni 1–20
for ($i = 3; $i -le 22; $i++) {
    $cashflow.Cells.Item($i,1) = $i - 2
    $cashflow.Cells.Item($i,2) = 70000
    $cashflow.Cells.Item($i,3) = 10000
}

# Formule
for ($i = 2; $i -le 22; $i++) {
    $cashflow.Cells.Item($i,4).Formula = "=B$i-C$i"
    $cashflow.Cells.Item($i,5).Formula = "=SUM(D`$2:D$i)"
}

# =====================
# KPI FINANZIARI (ROBUSTI - INGLESE)
# =====================

$cashflow.Cells.Item(24,1) = "IRR"
$cashflow.Cells.Item(24,2).Formula = "=IRR(D2:D22)"

$cashflow.Cells.Item(25,1) = "NPV"
$cashflow.Cells.Item(25,2).Formula = "=NPV(Assumptions!B2,D3:D22)+D2"

$cashflow.Cells.Item(26,1) = "ROI"
$cashflow.Cells.Item(26,2).Formula = "=(SUM(B2:B22)-SUM(C2:C22))/SUM(C2:C22)"

$cashflow.Columns.AutoFit() | Out-Null

$workbook.Save()
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Formule IRR / NPV / ROI inserite correttamente."