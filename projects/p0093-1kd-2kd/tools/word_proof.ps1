$ErrorActionPreference = 'Stop'
$projectPath = Split-Path $PSScriptRoot -Parent
$proofLog = Join-Path $projectPath 'production/word_proof.log'
$wordApp = $null
$wordDocument = $null
try {
  'Starting Word COM' | Set-Content -LiteralPath $proofLog
  $wordApp = New-Object -ComObject Word.Application
  $wordApp.Visible = $false
  $wordApp.DisplayAlerts = 0
  'Word created' | Add-Content -LiteralPath $proofLog
  $docxPath = Join-Path $projectPath 'production/P0093_Prototype.docx'
  $wordDocument = $wordApp.Documents.Open($docxPath, $false, $true)
  'Document opened' | Add-Content -LiteralPath $proofLog
  $wordDocument.Repaginate()
  ('Pages: ' + $wordDocument.ComputeStatistics(2)) | Add-Content -LiteralPath $proofLog
  $pdfPath = Join-Path $projectPath 'production/P0093_WordProof.pdf'
  $wordDocument.ExportAsFixedFormat($pdfPath, 17)
  'SUCCESS' | Add-Content -LiteralPath $proofLog
} catch {
  $_.Exception.Message | Add-Content -LiteralPath $proofLog
  exit 1
} finally {
  if ($null -ne $wordDocument) { $wordDocument.Close(0) }
  if ($null -ne $wordApp) { $wordApp.Quit() }
}
