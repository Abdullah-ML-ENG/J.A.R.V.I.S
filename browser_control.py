import webbrowser
import subprocess
import os
from urllib.parse import quote

class BrowserControl:
    """Handles browser control, app launching, and web searches - Windows Only"""
    
    # Popular websites mapping
    WEBSITES = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'github': 'https://www.github.com',
        'gmail': 'https://www.gmail.com',
        'linkedin': 'https://www.linkedin.com',
        'reddit': 'https://www.reddit.com',
        'twitter': 'https://www.twitter.com',
        'facebook': 'https://www.facebook.com',
        'instagram': 'https://www.instagram.com',
        'netflix': 'https://www.netflix.com',
        'spotify': 'https://www.spotify.com',
        'stack overflow': 'https://www.stackoverflow.com',
        'wikipedia': 'https://www.wikipedia.com',
        'medium': 'https://www.medium.com',
        'discord': 'https://www.discord.com',
    }
    
    # Windows application paths
    WINDOWS_APPS = {
        'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'chromium': 'C:\\Program Files\\Chromium\\Application\\chrome.exe',
        'firefox': 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
        'edge': 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'word': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
        'excel': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'powerpoint': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE',
        'vlc': 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe',
        'spotify': 'C:\\Users\\' + os.getenv('USERNAME') + '\\AppData\\Roaming\\Spotify\\Spotify.exe',
        'discord': 'C:\\Users\\' + os.getenv('USERNAME') + '\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe',
        'telegram': 'C:\\Users\\' + os.getenv('USERNAME') + '\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe',
        'visual studio code': 'C:\\Program Files\\Microsoft VS Code\\Code.exe',
        'vs code': 'C:\\Program Files\\Microsoft VS Code\\Code.exe',
        'cmd': 'cmd.exe',
        'powershell': 'powershell.exe',
        'file explorer': 'explorer.exe',
    }
    
    @staticmethod
    def search_google(query):
        """Search on Google"""
        search_url = f'https://www.google.com/search?q={quote(query)}'
        webbrowser.open(search_url)
        return f"Searching Google for {query}"
    
    @staticmethod
    def search_youtube(query):
        """Search on YouTube"""
        search_url = f'https://www.youtube.com/results?search_query={quote(query)}'
        webbrowser.open(search_url)
        return f"Searching YouTube for {query}"
    
    @staticmethod
    def search_wikipedia(query):
        """Search on Wikipedia"""
        search_url = f'https://en.wikipedia.org/wiki/{quote(query)}'
        webbrowser.open(search_url)
        return f"Searching Wikipedia for {query}"
    
    @staticmethod
    def open_website(website_name):
        """Open a popular website"""
        website_name = website_name.lower()
        if website_name in BrowserControl.WEBSITES:
            url = BrowserControl.WEBSITES[website_name]
            webbrowser.open(url)
            return f"Opening {website_name}"
        return f"Website {website_name} not found"
    
    @staticmethod
    def open_app(app_name):
        """Open a Windows application"""
        app_name = app_name.lower()
        
        # Check if app exists in dictionary
        if app_name in BrowserControl.WINDOWS_APPS:
            app_path = BrowserControl.WINDOWS_APPS[app_name]
            
            # Check if file exists before launching
            if os.path.exists(app_path):
                try:
                    subprocess.Popen(app_path)
                    return f"Opening {app_name}"
                except Exception as e:
                    return f"Error opening {app_name}: {e}"
            else:
                # Try to launch anyway - Windows might find it in PATH
                try:
                    os.startfile(app_path)
                    return f"Opening {app_name}"
                except Exception as e:
                    return f"{app_name} not found on your system"
        
        return f"Application {app_name} not recognized"
    
    @staticmethod
    def open_url(url):
        """Open a custom URL"""
        if not url.startswith('http'):
            url = 'https://' + url
        webbrowser.open(url)
        return f"Opening {url}"
    
    @staticmethod
    def add_custom_app(app_name, app_path):
        """Add a custom application to the apps dictionary"""
        BrowserControl.WINDOWS_APPS[app_name.lower()] = app_path
        return f"Added {app_name} to applications"
    
    @staticmethod
    def list_available_apps():
        """List all available applications"""
        return list(BrowserControl.WINDOWS_APPS.keys())
    
    @staticmethod
    def list_available_websites():
        """List all available websites"""
        return list(BrowserControl.WEBSITES.keys())
