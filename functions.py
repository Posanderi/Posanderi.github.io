def party_cmap(party):
    '''
    A function that returns a color value according to what finnish political party was given as an input.
    
    input:
    Party: The short name of the party. The parties with unique colors are SDP, PS, KOK, KESK, VIHR, VAS and RKP.
    Other inputs return the same colorvalue.
    
    output: Color name as a string
    '''
    if party=="SDP":
        return "red"
    elif party=="PS":
        return "turquoise"
    elif party=="KOK":
        return "blue"
    elif party=="KESK":
        return "darkgreen"
    elif party=="VIHR":
        return "lime"
    elif party=="VAS":
        return "darkred"
    elif party=="RKP":
        return "yellow"
    else:
        return "slategrey"
        
def find_winner(row):
    '''
    Return the party with the most amount of votes in the district.
    
    input:
    row: Pandas series with cells containing the amount of votes to each party with party name as the index
    
    output:
    row: Pandas series with a newly added cell "winner" containing the index (party name) of the largest cell (most votes).
    '''
    row["winner"]=None
    row["winner"]=row[2:22].idxmax()
    return row

def code_extract(row, code, city_code, area):
    
    '''
    Extract the district and city codes from the full name of the district in unemployment and education dataframes.
    
    input:
    row: Pandas series containing the full code of the district
    code: empty cell for the district code
    city_code: empty cell for the city code
    area: cell containing the full name of the district with district and city codes
    
    output:
    row:Pandas series with newly added cells containing the district code "code" and city codes "city_code"
    '''
    row[code]=row[area].split(" ")[1].lstrip("0")
    row[city_code]=row[area].split(" ")[0]
    return row
    
def sep_code(row):
    '''
    Extract the right district code according to the city. In Vantaa ("092") the district code is in the index "TILA"
    and in other cities "PIEN"
    
    input:
    row: Pandas series of the district
    
    output:
    row: Pandas series with a newly added cell "code" containing the district code
    '''
    if row["KUNTA"]=="092":
        row["code"]=row["TILA"]
    else:
        row["code"]=row["PIEN"]
    return row