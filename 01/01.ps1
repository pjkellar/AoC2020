$array = Get-Content .\data.txt

<#foreach ($num in $list){
    $check = ($target - $num)
    $new = $check | Where-Object { $list -Contains $_}
    if($new.length -gt 0){
        write-host "$($num) and $($new) are the numbers"    
    }
}#>

#Part 2
for($i=0; $i -lt $array.Length; $i++){
    for($j=$i+1; $j -lt $array.Length; $j++){
        for($k=$j+1; $k -lt $array.Length; $k++){
            if(([int]$array[$i] + [int]$array[$j] + [int]$array[$k]) -eq 2020){
                write-host ([int]$array[$i] * [int]$array[$j] * [int]$array[$k])
            }
        }
    }   
}