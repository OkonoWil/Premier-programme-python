
def countVoyelle(chain:str) -> int:
    voyelle = ["a","e","i","o","u","A","E","I","O","U"]
    ans = 0
    for voy in voyelle:
        ans += chain.count(voy) 
    return ans


print(countVoyelle("OKONO Wilfried"))