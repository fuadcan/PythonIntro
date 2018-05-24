import requests,re,bs4
import sqlite3
from time import sleep
from random import uniform
import json, os


class DarkLyricsCrawler(object):
    
    class song(object):
        def __init__(self, name,lyrics,artist,genre,album,year,source):
            self.name   = name
            self.lyrics = lyrics
            self.artist = artist
            self.genre  = genre
            self.album  = album
            self.year   = year
            self.source = source
            
    def url_extractor(self,band_name,genre):
        band_name = band_name.replace(' ','').lower()
        first_letter = band_name[0]
        url  = 'http://www.darklyrics.com/%s/%s.html' % (first_letter,band_name)
        soup = bs4.BeautifulSoup(requests.get(url).content,'html.parser')
        url_list = [album.find('a').get('href') for album in soup.find_all('div', class_='album')]
        url_list = [re.sub('#1|\.\./','',url) for url in url_list]
        url_list = ['http://www.darklyrics.com/' + url for url in url_list]
        print('[LOG]: Scraped %i urls for %s' % (len(url_list),band_name))
        return((url_list,genre))

    def album_scraper(self,url,genre):
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.content,'html.parser')
        # Meta info extraction
        metainfo    = [soup.find('h1').text,soup.find('h2').text]
        metainfo[0] = metainfo[0].replace(' LYRICS','').capitalize()
        metainfo.append(''.join(re.findall('\(([0-9]{4})\)',metainfo[1])))
        if not metainfo[2]:
            metainfo[2] == None
            metainfo[1] == None
        else:
            metainfo[2] = int(metainfo[2])
            metainfo[1] = re.search('"(.*)"',metainfo[1]).groups()[0]
        # lyric extraction
        lyrics     = soup.find('div', class_='lyrics')
        tagnames   = [child.name for child in list(lyrics.children)]
        begins     = [i for i,x in enumerate(tagnames) if x=='h3']
        ends       = [i-1 for i in begins][1:] + [len(tagnames)]
        # song name and lyrics
        songnames  = [list(lyrics.children)[i].text for i in begins]
        songlyrics = [list(lyrics.children)[(x+1):(ends[i]+1)] for i,x in enumerate(begins)]
        songlyrics = [[line.strip() for line in lyric if type(line) is bs4.element.NavigableString] for lyric in songlyrics]
        songlyrics = [' '.join(lyric) for lyric in songlyrics]
        #
        # Creation of song and Album (songs list)
        songs = []
        for i,x in enumerate(songnames):
            songs.append(self.song(x,songlyrics[i],metainfo[0],genre,metainfo[1],metainfo[2],'Darklyrics'))
            print('Scraped %s of %s, %s' % (x,metainfo[0],metainfo[1]))
        sleep(uniform(4,10))
        return(songs)

    def db_creator(self, dbpath, dbname):
        conn = sqlite3.connect(dbpath + '/' + dbname)
        cur  = conn.cursor()
        cur.execute('''CREATE TABLE lyrics
                     (name TEXT, lyrics TEXT, artist TEXT, genre TEXT, album TEXT,year INTEGER, source TEXT)''')
        cur.execute('''CREATE UNIQUE INDEX id ON lyrics (name, artist, album)''')

        conn.commit()    
        conn.close()

    def jsonwriter(self,song_info_list,dbpath):
        if not os.path.isdir(dbpath + '/json'): os.mkdir(dbpath + '/json')
        filename = '%s/%s_%s.json' % (dbpath + '/json',
                                      re.sub('[\s\'\.,~^+%&/)(=\?]','',song_info_list[0].artist),
                                      re.sub('[\s\'\.,~^+%&/)(=\?]','',song_info_list[0].album))
        with open(filename, 'w') as fh:
            fh.write('[')
            for song in song_info_list:
                fh.write('\n')
                json.dump(song.__dict__, fh)
                fh.write(',')
            # Son iterasyonda eklenen gereksiz virgül'ü sil
            fh.seek(fh.tell()-1)
            fh.truncate()
            # Bir satır aşağıya
            fh.write('\n]')
        print('[LOG] Written songs for %s - %s to JSON' % (song_info_list[0].album, song_info_list[0].artist))
    
    def album_writer(self, song_info_list,dbdest):
        conn = sqlite3.connect(dbdest)
        cur  = conn.cursor()

        for s in song_info_list:
            # Yazma
            cur.execute("INSERT OR IGNORE INTO lyrics VALUES (?,?,?,?,?,?,?)", 
                        (s.name,s.lyrics,s.artist,s.genre,s.album,s.year,s.source))
            print('[LOG] Written songs for %s - %s' % (s.album, s.artist))
        conn.commit()    
        conn.close()