import os
from datetime import datetime
from rich.console import Console

console = Console()

def save_report(target, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{target}_{timestamp}.html"
    
    os.makedirs("reports", exist_ok=True)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>OSINT Report - {target}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; padding: 30px; }}
        h1 {{ color: #58a6ff; font-size: 28px; }}
        h2 {{ color: #79c0ff; border-bottom: 1px solid #30363d; padding-bottom: 8px; margin-top: 30px; }}
        .section {{ background: #161b22; padding: 20px; margin: 15px 0; border-radius: 8px; border: 1px solid #30363d; }}
        .meta {{ color: #8b949e; font-size: 13px; margin: 4px 0; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; font-size: 13px; line-height: 1.6; }}
    </style>
</head>
<body>
    <h1>OSINT Report</h1>
    <p class="meta">Target: <strong style="color:#58a6ff">{target}</strong></p>
    <p class="meta">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p class="meta">Tool: ByteFortix OSINT Tool V1</p>
    <p class="meta">Contributors: zeo-design | kaifhoda1</p>
    <hr style="border-color:#30363d">
"""

    for section, content in data.items():
        html += f"""
    <div class="section">
        <h2>{section}</h2>
        <pre>{content}</pre>
    </div>
"""

    html += "</body></html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    console.print(f"\n[green]Report saved:[/green] {filename}")
    return filename


def save_simple_report(target, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{target}_{timestamp}.html"

    os.makedirs("reports", exist_ok=True)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>OSINT Report - {target}</title>
    <style>
        body {{ font-family: monospace; background: #0d1117; color: #c9d1d9; padding: 30px; }}
        h1 {{ color: #58a6ff; font-size: 26px; }}
        h2 {{ color: #79c0ff; border-bottom: 1px solid #30363d; padding-bottom: 8px; margin-top: 25px; }}
        .section {{ background: #161b22; padding: 20px; margin: 15px 0; border-radius: 8px; border: 1px solid #30363d; }}
        .meta {{ color: #8b949e; font-size: 13px; margin: 4px 0; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; font-size: 13px; line-height: 1.8; color: #c9d1d9; }}
        hr {{ border-color: #30363d; margin: 20px 0; }}
        .found {{ color: #3fb950; }}
        .notfound {{ color: #f85149; }}
    </style>
</head>
<body>
    <h1>OSINT Report</h1>
    <p class="meta">Target: <strong style="color:#58a6ff">{target}</strong></p>
    <p class="meta">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p class="meta">Tool: ByteFortix OSINT Tool V1</p>
    <p class="meta">Contributors: zeo-design | kaifhoda1</p>
    <hr>
"""

    for section, content in data.items():
        html += f"""
    <div class="section">
        <h2>{section}</h2>
        <pre>{content}</pre>
    </div>
"""

    html += "</body></html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    console.print(f"\n[green]Report saved:[/green] {filename}")
    return filename