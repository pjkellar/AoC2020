$file = (Get-Content .\sample.txt) -split [Environment]::NewLine
$fields = 'byr','iyr','eyr','hgt','hcl','ecl','pid'
$answer = 0

function isValid($passport){
    foreach($f in $fields){
        if($passport.IndexOf($f) -eq $false){
            return $false
        }
    }    
    return $true
}

$passport = ''
for($x=0; $x -le $file.Count; $x++){
    if($file[$x].length -ne 0){
        $passport += " $($file[$x])"
    } else {
        if(isValid $passport){
            $answer++
        }
        $passport = ''
    }
}

$answer
<#
foreach($passport in $collection){
    $pairs = $passport.Trim().Split(" ")
    foreach($p in $pairs){
        $key = $p.Trim().Split(":")[0]
        if($fields -contains $key){
            $valid = $true
        } else {
            $valid = $false
        }

    }
    if($valid){
        $answer++
    }
}

$answer

#>

<#
I could not get this working and from what I can see it has to do with how I am splitting
the passport up. In the interest of time I've switched to try using Python to solve this problem.
See 04.py for more information.
#>