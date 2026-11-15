$files = @(
    @{
        Docx = "c:\Users\mathi\OneDrive\Escritorio\technoload-responsability\upc-pre-202620-1asi0730-8093-technoload-course-plan-performance.docx"
        Pdf  = "c:\Users\mathi\OneDrive\Escritorio\technoload-responsability\upc-pre-202620-1asi0730-8093-technoload-course-plan-performance.pdf"
    },
    @{
        Docx = "c:\Users\mathi\OneDrive\Escritorio\technoload-responsability\upc-pre-202620-1asi0730-8093-technoload-course-plan.docx"
        Pdf  = "c:\Users\mathi\OneDrive\Escritorio\technoload-responsability\upc-pre-202620-1asi0730-8093-technoload-course-plan.pdf"
    }
)

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    foreach ($item in $files) {
        Write-Output "Converting $($item.Docx) to $($item.Pdf)..."
        $doc = $word.Documents.Open($item.Docx)
        $doc.SaveAs([ref]$item.Pdf, [ref]17)
        $doc.Close([ref]$false)
        Write-Output "Successfully converted: $($item.Pdf)"
    }
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
} catch {
    Write-Error "Error in Word COM conversion: $_"
}
