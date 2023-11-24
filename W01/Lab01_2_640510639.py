milliseconds = int(input('Input milliseconds: '))

day = int(milliseconds/86400000)
milliseconds = milliseconds%86400000

hour = int(milliseconds/3600000)
milliseconds = milliseconds%3600000

minute = int(milliseconds/60000)
milliseconds = milliseconds%60000

second = int(milliseconds/1000)
milliseconds = milliseconds%1000

print('%d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)'
      %(day, hour, minute, second, milliseconds))