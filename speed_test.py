import speedtest
from time import sleep
from datetime.datetime import now

while True:
    now = now()
    if now.minute == 14 or now.minute == 30:
        file_loc = 'C:/Users/Jerem/Documents/projects/speed_test/speed_test.txt'
        with open(file_loc, 'a') as file:
            time = now.strftime('%H:%M')
            try:
                st = speedtest.Speedtest()
                download = st.download()
                upload = st.upload()
                ping = st.get_servers([])
                ping = st.results.ping
            except speedtest.ConfigRetrievalError:
                download = 'error'
                upload = 'error'
                ping = 'error'
            line = time + '\t' + str(download) + '\t' + str(upload) + '\t' + str(ping)
            file.write(line)
        sleep(60)
