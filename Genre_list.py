songs = [
("Pink Floyd,The Dark Side Of The Moon" ,1973, "progressive rock " , "43:00"),
("Britney Spears", "Baby One More Time,1999", "pop" , "42:20" ),
("The Beatles" , "Revolver" , 1966 , "rock" , "34:43" ),
("Deep Purple" , "Machine Head" , 1972 , "hard rock" , "37:25"),
("Old Timers" , "Old Time" , 966 , "ancient", "123:45"),
("Pink Floyd" , "Wish You Were Here" , 1975 , "progressive rock", "44:28"),
("Boston" , "Boston", 1976 , "hard rock" , "37:41"),
("Monika Brodka" , "Granada" , 2010 , "pop" , "37:42"),
("David Bowie" , "Low" , 1977 , "rock", "38:26"),
("rock" , "rock" , 966 , "pop" , "13:37"),
("Massive Attack" , "Blue Lines" , 1991 , "hip hop", "45:02")
]
genre = lambda genre: genre[3]
songs.sort (key = genre , reverse = True)
print("               Band name                  :           Song name        ;     Year      :     Genre    :     Minutes    : ")
for items in songs:
    print( ":",items[0]," "*(38-len(items[0])) , ':' )