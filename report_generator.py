import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

def save_report(target, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{target}_{timestamp}.html"
    
    os.makedirs("reports", exist_ok=True)
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>OSINT Report - {target}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }}
        h1 {{ color: #58a6ff; }}
        h2 {{ color: #79c0ff; border-bottom: 1px solid #30363d; padding-bottom: 5px; }}
        .section {{ background: #161b22; padding: 15px; margin: 10px 0; border-radius: 8px; border: 1px solid #30363d; }}
        .found {{ color: #3fb950; }}
        .not-found {{ color: #f85149; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; }}
        .meta {{ color: #8b949e; font-size: 12px; }}
    </style>
</head>
<body>
    <h1>OSINT Report</h1>
    <p class="meta">Target: {target}</p>
    <p class="meta">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p class="meta">Tool: ByteFortix OSINT Tool V1</p>
    <hr>
"""
    
    for section, content in data.items():
        html += f"""
    <div class="section">
        <h2>{section}</h2>
        <pre>{content}</pre>
    </div>
"""
    
    html += """
</body>
</html>
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    
    console.print(f"\n[green]Report saved:[/green] {filename}")
    return filename