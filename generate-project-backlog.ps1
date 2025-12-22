$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$path = "docs\01_project_management\project_backlog.xlsx"
$fullPath = Join-Path (Get-Location) $path

# Crea cartella se non esiste
$folder = Split-Path $fullPath
if (!(Test-Path $folder)) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

$workbook = $excel.Workbooks.Add()
$sheet = $workbook.Sheets.Item(1)
$sheet.Name = "Backlog"

$headers = @(
    "ID","Area","Descrizione","Priorità","Milestone",
    "Owner","Stato","Data Inizio","Data Fine","Note"
)

for ($i = 0; $i -lt $headers.Count; $i++) {
    $sheet.Cells.Item(1, $i + 1) = $headers[$i]
    $sheet.Cells.Item(1, $i + 1).Font.Bold = $true
}

# Esempi realistici
$data = @(
    @("PM-01","Project Management","Avvio studio di fattibilità","Alta","M1","Società di gestione","Done","01/03/2022","30/04/2022",""),
    @("FUND-01","Fund Management","Definizione modello crowdfunding","Alta","M2","Società di gestione","In Progress","","",""),
    @("ENERGY-01","Energy Management","Stima produzione impianto fotovoltaico","Media","M3","Team tecnico","","","","")
)

$row = 2
foreach ($item in $data) {
    for ($col = 0; $col -lt $item.Count; $col++) {
        $sheet.Cells.Item($row, $col + 1) = $item[$col]
    }
    $row++
}

$sheet.Columns.AutoFit() | Out-Null

# Foglio legenda
$legend = $workbook.Sheets.Add()
$legend.Name = "Legenda"

$legend.Cells.Item(1,1) = "Stato"
$legend.Cells.Item(1,2) = "Significato"
$legend.Cells.Item(1,1).Font.Bold = $true
$legend.Cells.Item(1,2).Font.Bold = $true

$legend.Cells.Item(2,1) = "To Do"
$legend.Cells.Item(2,2) = "Attività pianificata"

$legend.Cells.Item(3,1) = "In Progress"
$legend.Cells.Item(3,2) = "Attività in corso"

$legend.Cells.Item(4,1) = "Done"
$legend.Cells.Item(4,2) = "Attività completata"

$workbook.SaveAs($fullPath)
$workbook.Close()

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Output "✅ Project backlog Excel creato correttamente."