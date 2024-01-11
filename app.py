from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import ForeignKey, Column, Integer, String 

 # A declarative Base for Inheritance
Base = declarative_base()
class User(Base):
# Table name
    __tablename__ = 'users'
# Columns(T.attributes)
    id = Column (Integer(), primary_key= True)
    userName = Column(String())
    email = Column(String())
    dateOfBirth = Column(Integer())
    # users = relationship ('User', backref=backref('budget'))
# respresentation of class objects as strings
    def __repr__(self):
        return f'userName= {self.userName}'
           
class Artist(Base):
    __tablename__ = 'artists'
    id = Column (Integer(), primary_key=True)
    song_id = Column(Integer())
    artistName = Column(String())
    creationDate = Column(Integer())
    # artists = relationship('Artist', backref=backref('song'))
    def __repr__(self):
        return f'Artist(id = {self.id})'+\
           f'artistName ={self.artistName}'
    
class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer(), primary_key= True)
    artist_id = Column(Integer(), ForeignKey('artists.id'))
    song_title = Column(String())
    duration = Column(Integer())
    def __repr__(self):
        return f'Song(id = {self.id})'+\
           f'song_titlr= {self.song_title}'
    
class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column (Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    song_id = Column(Integer(), ForeignKey('songs.id'))
    timestamp = Column(Integer())
    def __repr__(self):
        return f'Favorite(id = {self.id})'+\
           f'user_id={self.user_id}'
        


if __name__ == '__main__':
    engine = create_engine('sqlite:///tracker.db')
    Base.metadata.create_all(engine)
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
# User Instances
    user1 = User(
        userName = "Alvin",
        email = "alvinbee@gmail.com",
        dateOfBirth = "2/2/2010"
        )
    user2 = User(
        userName = "Alvin",
        email = "alvinbee@gmail.com",
        dateOfBirth = "2/2/2010"
        )
    user3 = User(
        userName = "Alvin",
        email = "alvinbee@gmail.com",
        dateOfBirth = "2/2/2010"
        )
   
    # Create Artist(Instances)
    artist1 = Artist(
        song_id = 1,
        artistName = "Alvin",
        creationDate = "12/03/2004"
        )
    artis2 = Artist(
        song_id = 1,
        artistName = "Alvin",
        creationDate = "12/03/2004"
        )
   
    # Create Song(Instances)
    song1 = Song(
        artist_id = 1,
        song_title = "Can I be Him ",
        duration = 10,
        )
    song2 = Song(
        artist_id = 1,
        song_title = "Can I be Him ",
        duration = 10,
        )
    # Create Favorites(Instances)
    favorite1 = Favorite(
        user_id = 1,
        song_id = 1,
        timestamp = "6/09/2023",
        )

    favorite2 = Favorite(
        user_id = 1,
        song_id = 2,
        timestamp = "6/09/2023",
        )

#Saving  the session in the database and applying the committed modifications
    session.add_all([user1,user2,user3])
    session.add_all([artist1,artis2])
    session.add_all([song1,song2])
    session.add_all([favorite1,favorite2])
    session.commit()


def create_playlist(songs):
        print("Create a Favorites Playlist")
        playlist_name = input("Enter the name of your favorites playlist: ")
        playlist = []

        while True:
            print("Add songs to your favorites playlist  (Enter 'done' to finish):")
            song_title = input("Enter the name of the song: ")
            if song_title.lower() == 'done':
                break
            for song in songs:
                if song_title in song:
                    playlist.append(song)
            else:
                print("Song not found in library.")

        with open(f"{playlist_name}.txt", 'w') as playlist_file:
            for song in playlist:
                playlist_file.write(",".join(song) + "\n")
        print(f"{playlist_name} playlist created!")                        


def main ():
    # initialize music list
    # trackerList = []

    choice = 0
    while choice !=7:
        print("**<<KARIBU||WELCOME TO BOOMBOX MUSIC LIBRARY>>**")
        print("1) Add Song")
        print("2) Search Song ")
        print("3) Create a Favorites playlist")
        print("4) Display Songs")
        print("5) Display Artist")
        # print("6) Display limit 10000 and above")
        print("7) Quit program")
        choice = int(input())


#   Adds song details
        if choice == 1:
            print("**<<Adding a Song...>>**")
            song_title = input("Enter the name of the song....")
            duration= input("Enter the duration of the song....")
            Song.append([song_title, duration])

#   Search for a song
        elif choice == 2:
            print("**<<Searching for a song...>>**")
            keyword = input("Enter name....")   
            for song in Song:
                if keyword in song:
                    print(song)
                else:
                    print("Song not found!")  

#   Lookup Expenses
#   Prints a Tuple
        elif choice == 3:
            print("**<<Creating a Favourites Playlist...>>**")
            create_playlist(Song)

#  prints average limit
        elif choice == 4:
            print("**<<Displaying Songs...>>**")
            for i in range(len(Song)):
                 print(Song[i])

#  prints limit below 10000
        elif choice == 5:
            budgets = session.query(Budget).filter(Budget.limit < 10000)
            for budget in budgets:
                print("**<<Displaying Artists...>>**")
                print(budget.budgetName)
    
# #  prints limit 10000 and above
#         elif choice == 6:
#             budgets = session.query(Budget).filter(Budget.limit >= 10000)
#             for budget in budgets:
#                 print("**<<Printing limit 10000 and above>>**")
#                 print(budget.budgetName)
       
#  Quiting program
        elif choice == 7:
                print("**<<You are no longer on the main menu.>>**")
                print("**<<Thank you for choosing BOOMBOX MUSIC LIBRARY.>>**")
                print("**<<Run the program again to get back to the main menu.>>**")

#  Unrecognized input and validates user's input
        else:
                print("*<<Incorrect Input.>>**")
                
                
# Calling the function
if __name__ == "__main__":
    main()
