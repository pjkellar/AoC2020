<#
$x = 0

# Part One
Get-Content .\data.txt | % {
    $password = $_.Substring($_.IndexOf(":") + 2,$_.Length - $_.IndexOf(":") -2)
    $char = $_.SubString($_.IndexOf(":")-1,1)
    $lowerLimit = $_.Substring(0,$_.IndexOf('-'))
    $upperLimit = $_.Substring($_.IndexOf('-')+1,($_.IndexOf(" ")-$_.IndexOf('-')))
    $charCount = ($password.ToCharArray() -match $char)
    if(($charCount.Count -ge $lowerLimit) -and ($charCount.Count -le $upperLimit)){
        $x++
    }
}
Write-Host $x
#>

$x = 0
# Part Two
Get-Content .\data.txt | % {
    $password = $_.Substring($_.IndexOf(":") + 2,$_.Length - $_.IndexOf(":") -2)
    $char = $_.SubString($_.IndexOf(":")-1,1)
    $lowerLimit = $_.Substring(0,$_.IndexOf('-'))
    $upperLimit = $_.Substring($_.IndexOf('-')+1,($_.IndexOf(" ")-$_.IndexOf('-')))
    $charArray = $password.ToCharArray() 
    #write-host $charArray[$lowerLimit-1]
    #write-host $charArray[$upperLimit-1]
    if(($charArray[$lowerLimit-1] -eq $char) -xor ($charArray[$upperLimit-1] -eq $char)){
        $x++
    }
}
Write-Host $x