Get-ChildItem -Path "z:\Marco\WebProjects\CareOptions\services\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    if ($content -notmatch '<script src="\.\./js/script\.js"></script>') {
        $content = $content -replace '</body>', "<script src=`"../js/script.js`"></script>`r`n</body>"
        Set-Content -Path $_.FullName -Value $content -Encoding UTF8
        Write-Host "Added script to $($_.Name)"
    }
}
