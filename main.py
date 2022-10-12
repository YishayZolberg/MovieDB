from EHAB import TMDBDownloader
def main():
    a = TMDBDownloader()
    a.getURL()
    print(a)
    a.getposterURL()
    a.download_image(a.getname())

if __name__ == '__main__':
    main()
