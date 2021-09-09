import csv

def opencsv():
    data = []
    with open('ratings.csv') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        for row in reader:
            data.append(row)
        return data 
       
def getMovies(data):       
    movie = []
    for rows in data:
        for j in range(len(rows)):
            if rows[j] == 'movie':
                movie.append(rows)
    return movie

def getHeader(data):
    return data[0]
         
def writecsv(data):
    header = getHeader(data)
    movies = getMovies(data)
    
    with open('imdbratings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for rows in movies:
            writer.writerow(rows)

if __name__ == '__main__':
    data = opencsv()
    writecsv(data)
