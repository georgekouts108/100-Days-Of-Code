from prettytable import PrettyTable

movies = PrettyTable()

movies.add_column('title',['Lights Out','Terrifier 2', 'White Christmas', 'The Wizard of Oz','The Conjuring'],'c')
movies.add_column('year', [2016,2022,1954,1939,2013],'c')
movies.add_column('director', ['David F. Sandburg','Damien Leone','Michael Curtiz','Victor Fleming','James Wan'],'c')
print(movies)

songs = PrettyTable()


songs.add_column('title',['Thinking Out Loud', 'Shape of You', 'Havana', 'Moves Like Jagger', 'I Knew You Were Trouble'])
songs.add_column('artist',['Ed Sheeran', 'Ed Sheeran', 'Camilla Cabello ft. Young Thug', 'Maroon 5', 'Taylor Swift'])
songs.align = 'l'
# songs.add_column()
print(songs)