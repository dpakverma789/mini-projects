
try:
    from pytube import YouTube
    import platform
except ModuleNotFoundError:
    import os
    import platform
    os.system('pip install pytube')
    from pytube import YouTube

download_path = 'C:\\Users\\DEEPAK-PC\\Desktop' if platform.system() == 'Windows' else '/home/deepak/Downloads'


class VideoInfo:
    @staticmethod
    def default():
        link = input('\n\n\tPaste your youtube Link here : ')
        print('\n\tFetching Info...')
        try:
            media = YouTube(link)
            media_title = media.title
            media_length = media.length
            return media_title, media_length, media
        except:
            print('\n\n\tSomeThing is Wrong With Link!!')

    @staticmethod
    def generate_file_name(char):
        generate_file_name = ''
        for i in char:
            if i == '|':
                break
            else:
                generate_file_name += i
        return generate_file_name


class VideoLengthCalculator:
    def __init__(self, length):
        self.length = length
        
    def video_length(self):
        time = '{0}:{1}'.format(self.length//60, self.length % 60)
        return time


class Comparator:
    def __init__(self, *args):
        self.choice = args[0]
        self.name = args[1]
        self.video = args[2]
        self.downloading = '\nDownloading {}...'.format('Video' if self.choice == 1 else 'Audio')

    def com(self):    
        if self.choice == 1:
            video_filter = self.video.streams.filter(file_extension='mp4', progressive="True")
            video_order = video_filter.order_by('resolution').desc()
            print(self.downloading)
            video_name = info.generate_file_name(self.name).strip()+'.mp4'
            video_order.first().download(download_path, filename=video_name)
            return

        else:
            audio_filter = self.video.streams.filter(only_audio=True)
            audio_order = audio_filter.order_by('bitrate').desc()
            print(self.downloading)
            audio_name = info.generate_file_name(self.name).strip()+'.mp3'
            audio_order.first().download(download_path, filename=audio_name)
            return


if __name__ == '__main__':
    while True:
        print('===='*20)
        print("\nPRESS 1 FOR VIDEO DOWNLOAD \t\t PRESS 2 FOR AUDIO DOWNLOAD")
        choice = int(input("\nENTER YOUR CHOICE HERE :"))
        if choice in (1, 2):
            info = VideoInfo()
            try:
                media_title, media_length, media = info.default()
                media_length = VideoLengthCalculator(media_length)
                print('\nTitle: ', media_title, '\nLength: ', media_length.video_length())
                comp = Comparator(choice, media_title, media)
                comp.com()
                print('\n**** Find Your Downloaded File here "{}" ****\n'.format(download_path))
            except Exception as e:
                print('\n\t**** OOps Went Something Wrong, Downloading Abort!! ****\n', e)
        else:
            print('\n\t\t\tInvalid Operation Input!!')

    



