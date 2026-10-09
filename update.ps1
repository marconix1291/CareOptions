$navReplacement = @"
    <nav class="navbar scrolled" id="navbar">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../images/logo_horizontal.png" alt="Care Options LLC" style="max-height: 50px; width: auto;">
            </a>
            <div class="nav-links">
                <a href="../index.html#home">Home</a>
                <a href="../index.html#about">About</a>
                <a href="../index.html#services">Services</a>
                <a href="../index.html#therapies">Therapies</a>
                <a href="../index.html#contact">Contact</a>
                <a href="http://www.docpay.com/careoptions" target="_blank">Pay Bill</a>
            </div>
            <div class="nav-actions">
                <a href="tel:8068771474" class="btn btn-primary phone_num">806.877.1474</a>
                <button class="hamburger" id="hamburger" aria-label="Toggle Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>
"@

$footerReplacement = @"
    <footer id="contact">
        <div class="footer-content">
            <div class="footer-contact">
                <h3>Drop us a line!</h3>
                <p style="color: var(--clr-secondary-5); margin-bottom: 1rem;">Phone: <a href="tel:8068771474" style="color: white;">806.877.1474</a></p>
            </div>
            <div class="footer-hours">
                <p>Deni Berry, FNP Primary Care Services.</p>
            </div>
        </div>
        <div class="footer-bottom">
            <a href="../index.html" class="logo footer-logo" style="display: block; margin-bottom: 1rem;">
                <img src="../images/logo_horizontal_white.png" alt="Care Options LLC" style="max-height: 50px; width: auto;">
            </a>
            <p>&copy; 2026 Care Options LLC. All rights reserved.</p>
        </div>
    </footer>
"@

Get-ChildItem -Path "z:\Marco\WebProjects\CareOptions\services\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    $content = $content -replace '(?s)<nav class="navbar scrolled" id="navbar">.*?</nav>', $navReplacement
    $content = $content -replace '(?s)<footer id="contact">.*?</footer>', $footerReplacement
    
    Set-Content -Path $_.FullName -Value $content -Encoding UTF8
    Write-Host "Updated $($_.Name)"
}
