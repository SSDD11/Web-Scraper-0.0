"""Goal:
Reduce the time consumed in searching for and finding industry news online.
Estimated time saved: 60+ minutes per day.
Method:  Scan industry websites for pertinent information, return pertinent information as links and summaries.
Websites include, but not limited to:  (techcrunch.com, reddit.com/r/robotics, /r/futurology, robohub.org, theverge.com, others.)
Website article titles and introductions will be scanned for words such as 'robotics', 'recognition', 'AI' etc.
Relevant articles will be returned as links AND summaries to .txt file or email.
Steps:
1Iterate over list of websites.XFor each website, provide HTML data of article titles and attenuant links.
2Iterate over each title.XFor each title, filter for keywords.
3Print keyword-bearing titles and links.
4For each link, follow to attenuant text.
5Print text to .txt file.
6Run each text through summary/paraphraser.
7Print each text to .txt file with title and link.
8Profit!"""

  
import urllib
import re
class sites(object):
    
    
    
    def __init__(self, urlsite, post_title, pref, keywords):
        self.urlsite = urlsite
        self.post_title = post_title
        self.pref = pref
        self.keywords = keywords
        
        
        
    def scraper(self):
        regex = self.post_title
        pattern = re.compile(regex)
        htmlfile = urllib.urlopen(self.urlsite)
        htmltext = htmlfile.read()
        titles = re.findall(pattern, htmltext)
        scraped = []
        x = 0
        for item in titles:
            x += 1
        print self.pref + str(x) + " total titles"
        if isinstance(titles, str) == True:
            titlestring = titles
        else:
            titlestring = str(titles)
        if "-" in titlestring or "/" in titlestring:
            titleslist = titlestring.split("-")
            titleslist = titlestring.split("/")
        else: 
            titleslist = titlestring.split(" ")
        
        for word in self.keywords:
            for t in titleslist:
                if word in t and t not in scraped:
                    scraped.append(t)
                    print "\n" + self.pref + t + "\n"
                
        if len(scraped) == 0:
            print self.pref + "No Relevant Titles"
        else:
            print self.pref + str(len(scraped)) + " relevant titles returned"
        return
class sites2(object):
    def __init__(self, urlsite, post_title, pref, keywords):
        self.urlsite = urlsite
        self.post_title = post_title
        self.pref = pref
        self.keywords = keywords
        
    def scraper(self):
            regex = self.post_title
            pattern = re.compile(regex)
            htmlfile = urllib.urlopen(self.urlsite)
            htmltext = htmlfile.read()
            titles = re.findall(pattern, htmltext)
            scraped = []
            titlestring = titles
            titleslist = titlestring
            x = 0
            for item in titles:
                x += 1
            if len(titleslist) < 1:
                print self.pref + "No Titles Found"
            else:
                print self.pref + " " + str(x) + "Titles found"
            for title in titleslist:
                for word in self.keywords:
                    if word in title:
                        if title not in scraped:
                            scraped.append(title)
                            print self.pref + title + "\n"""
            if len(scraped) == 0:
                print self.pref + "No Relevant Titles"
            else:
                print self.pref + str(len(scraped)) + " relevant titles returned"
            return

t_c = sites("http://techcrunch.com", 'data-omni-sm="gbl_river_headline,(.+?)</h2>', 'techcrunch----',\
    ['Machine','Robot','Vision','A.I.','Learning','Chat','Recognition','Robotics','AI','Neural','Assistant'] )

r_hub = sites("http://robohub.org", '<a href="(.+?)">', 'robohub----',\
    ['Machine','Consumer','Vision','A.I.','AI','Smarthome','Neural'])
    
sp_ieee = sites2("http://spectrum.ieee.org", '<h3 class="article-title">(.+?)</h3>', 'ieee spectrum----', \
    ['Machine','Learning','Vision','Chat','Recognition','A.I.','Social','Neural'])

live_sci = sites("http://www.livescience.com/topics/robots/",'<div class="section_asset white_box animated_appear content_container article_content">(.+?)</div>','livescience----',\
    ["article","Robots","robot","Machine",'Emotion','A.I.','Learning','Chat','Recognition','Vision','Intelligence','Social']),

techrev = sites("http://technologyreview.com/c/robotics/",'<a class="grid-tz__title--link" href="(.+?)</a>','MIT tec review----',\
    ["Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Chip','Neural'])
        
sing_hub = sites("http://singularityhub.com/",'<article class="(.+?)"</article>','SingularityHub----',\
    ["Machine",'Learning','Vision','Chat','Recognition','A.I.','AI','Social','Intelligence'])  

physorg = sites("http://phys.org/technology-news/robotics/",'<a href="http://phys.org/news/(.+?)</a>','PhysOrg----',\
    ["Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Neural'])   

popsci = sites("http://www.popsci.com/find/robotics",'<a href="(.+?)</a>','PopSci----',\
    ["Chip","Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Neural'])

disnews = sites("http://news.discovery.com/tech/robotics",'<a href=(.+?)</a>','DiscoveryNews----',\
    ["Chip","Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Neural'])

newsci = sites("https://www.newscientist.com/subject/technology/",'<h2(.+?)</h2>','NewScientist----',\
    ["Turing","Chip","Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Neural'])
        
stack_cloud = sites("https://thestack.com",'<a href="(.+?)" style="height: 71px;">','TheStack----',\
    ["AI","Chip","Machine",'Learning','Vision','Chat','Recognition','A.I.','Social','Intelligence','Neural'])

t_c.scraper()
r_hub.scraper()
sp_ieee.scraper() 
techrev.scraper()

physorg.scraper()
popsci.scraper()
disnews.scraper()
newsci.scraper()
#stack_cloud.scraper()
#live_sci.scraper()
#sing_hub.scraper()
