import lyricsgenius

test = "lMdsrNvLWxMxTXXIGB1tPq1wVZpod-E-_PHhUPNSIfxpVloW38iAxgw2cG8Xptp8"

genius = lyricsgenius.Genius(test)

genius.search_artist("Taylor Swift", max_songs=1, sort="title")