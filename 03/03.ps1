$map = Get-Content .\data.txt

<#
$trees = [int]0
$linesToSkip = 1
$xPosition = 3
for($i = 0; $i -lt $map.Length; $i++){
    $line = $map[$i+$linesToSkip]
    $loopPosition = ($xPosition % 11)
    if($line[$loopPosition] -eq "#"){
        $trees++
    }
    $xPosition + 4
}
Write-host "There are $($trees) in your way! Be careful"
#>

$trees = 0
$iterations = @{
    '0' = '1:1'
    '1' = '3:1'
    '2' = '5:1'
    '3' = '7:1'
    '4' = '1:2'
}

foreach($pair in $iterations.Values){
    $right = 0
    $down = 0
    $positions = $pair.Split(":")
    for($i = 0; $i -lt $map.Length - 1; $i++){
        $right += $positions[0]
        $down += $positions[1]
        $line = $map[$down]
        if($line.Length -gt 0){
            $char = $line[$right % $line.Length]
            if($char -eq "#"){
                $trees++
            }
        }
    }
    write-host "$($pair): tree count = $trees"
    $trees = 0 
}