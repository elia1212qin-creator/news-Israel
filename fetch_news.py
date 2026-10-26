import feedparser
import json
import datetime

# רשימת מקורות חדשות אמיתיים מישראל (RSS Feeds)
SOURCES = {
    'Ynet': 'https://www.ynet.co.il/Integration/StoryRss2.xml',
    'Walla': 'https://rss.walla.co.il/feed/1',
    'N12': 'https://mako.co.il/rss/31750a2610f26110VgnVCM1000004b01a8c0RCRD.xml',
    'Geektime': 'https://www.geektime.co.il/feed/'
}

def get_real_news():
    all_news = []
    
    for source_name, url in SOURCES.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:8]: # 8 הכתבות האחרונות מכל מקור
                news_item = {
                    'title': entry.title,
                    'link': entry.link,
                    'source': source_name,
                    'published': getattr(entry, 'published', str(datetime.datetime.now())),
                    'summary': getattr(entry, 'summary', '')
                }
                all_news.append(news_item)
        except Exception as e:
            print(f"Error fetching from {source_name}: {e}")

    # שמירת כל החדשות האמיתיות לקובץ JSON
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_real_news()
