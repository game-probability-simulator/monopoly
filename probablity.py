import chance

board = ["Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
         "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Conneticuit Avenue",
         "Jail", "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue",
         "Pensylvania Railroad", "St. James Place", "Community Chest", "Tenesee Avenue", "New York Avenue",
         "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
         "B & O Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens",
         "Go to Jail", "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pensylvania Avenue",
         "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"]

matrix = [[

]]

def matmul(x, y):
    output = []
    for row in x:
        nrow = []
        for col in zip(*y):
            nrow += [sum(a*b for a, b in zip(row, col))]
        output += [nrow]
