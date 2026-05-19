import requests
from rich.console import Console
from rich.table import Table

console = Console()

def geolocate_ip(ip):
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = resp.json()
        
        if data["status"] == "success":
            table = Table(title=f"IP Geolocation: {ip}")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="white")
            
            table.add_row("IP", data.get("query", "N/A"))
            table.add_row("Country", data.get("country", "N/A"))
            table.add_row("Region", data.get("regionName", "N/A"))
            table.add_row("City", data.get("city", "N/A"))
            table.add_row("ISP", data.get("isp", "N/A"))
            table.add_row("Organisation", data.get("org", "N/A"))
            table.add_row("ASN", data.get("as", "N/A"))
            table.add_row("Timezone", data.get("timezone", "N/A"))
            table.add_row("Latitude", str(data.get("lat", "N/A")))
            table.add_row("Longitude", str(data.get("lon", "N/A")))
            
            console.print(table)
        else:
            console.print(f"[red]Could not geolocate {ip}[/red]")
            
    except Exception as e:
        console.print(f"[red]Geolocation failed: {e}[/red]")

def geolocate_domain_ips(ips):
    console.print(f"\n[bold blue]IP Geolocation Results[/bold blue]\n")
    for ip in ips:
        geolocate_ip(ip)