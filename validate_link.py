import urllib.request


def validate_link(url):

    try:
        html = urllib.request.urlopen(url)
        # print(html.read().decode())
        s = html.read().decode()
        s = s.replace('\n', '')

        video_not_available = s.find('"playabilityStatus":{"status":"ERROR"')
        private_video = s.find('"playabilityStatus":{"status":"LOGIN_REQUIRED"')
        video_unplayable = s.find('"playabilityStatus":{"status":"UNPLAYABLE"')

        # print('Not available', video_not_available)
        # print('Private', private_video)
        # print('No playable', video_unplayable )

        if video_not_available > 0 or private_video > 0 or video_unplayable > 0:
            # Video not available
            return 1
        else:
            # Video available
            return 0

    except Exception:
        print('Not valid link')
        return 1


#result = validate_link('https://www.youtube.com/watch?v=1G4isFylg')

#print(result)