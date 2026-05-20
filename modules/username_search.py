import requests
from rich.console import Console
from rich.table import Table
from concurrent.futures import ThreadPoolExecutor, as_completed

console = Console()

PLATFORMS = {
    "GitHub":       "https://github.com/{}",
    "Twitter":      "https://twitter.com/{}",
    "Instagram":    "https://www.instagram.com/{}",
    "Reddit":       "https://www.reddit.com/user/{}",
    "TikTok":       "https://www.tiktok.com/@{}",
    "Pinterest":    "https://www.pinterest.com/{}",
    "Tumblr":       "https://www.tumblr.com/{}",
    "Twitch":       "https://www.twitch.tv/{}",
    "YouTube":      "https://www.youtube.com/@{}",
    "LinkedIn":     "https://www.linkedin.com/in/{}",
    "Snapchat":     "https://www.snapchat.com/add/{}",
    "Telegram":     "https://t.me/{}",
    "Medium":       "https://medium.com/@{}",
    "Gitlab":       "https://gitlab.com/{}",
    "Pastebin":     "https://pastebin.com/u/{}",
    "Keybase":      "https://keybase.io/{}",
    "HackerNews":   "https://news.ycombinator.com/user?id={}",
    "ProductHunt":  "https://www.producthunt.com/@{}",
    "Dev.to":       "https://dev.to/{}",
    "Replit":       "https://replit.com/@{}",
}

headers = {"User-Agent": "Mozilla/5.0"}

def check_platform(platform, url):
    try:
        resp = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
        if resp.status_code == 200:
            return platform, "FOUND", url
        else:
            return platform, "NOT FOUND", url
    except Exception:
        return platform, "ERROR", url

def search_username(username):
    if " " in username:
        console.print("[red]Username cannot contain spaces. Try 'elonmusk' not 'elon musk'[/red]")
        return

    console.print(f"\n[bold blue]Username Search: {username}[/bold blue]\n")
    console.print("[dim]Searching all platforms simultaneously...[/dim]\n")

    table = Table(title=f"Results for '{username}'")
    table.add_column("Platform", style="cyan", width=15)
    table.add_column("Status", width=12)
    table.add_column("URL", style="white")

    found = []
    not_found = []
    results = []

    urls = {platform: url.format(username) for platform, url in PLATFORMS.items()}

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_platform, p, u): p for p, u in urls.items()}
        for future in as_completed(futures):
            platform, status, url = future.result()
            results.append((platform, status, url))

    results.sort(key=lambda x: x[0])

    for platform, status, url in results:
        if status == "FOUND":
            table.add_row(platform, "[green]FOUND[/green]", url)
            found.append((platform, url))
        elif status == "NOT FOUND":
            table.add_row(platform, "[red]NOT FOUND[/red]", url)
            not_found.append(platform)
        else:
            table.add_row(platform, "[yellow]ERROR[/yellow]", url)

    console.print(table)
    console.print(f"\n[green]Found on {len(found)} platforms[/green]")
    console.print(f"[red]Not found on {len(not_found)} platforms[/red]")