from modules.domain_recon import domain_recon
from modules.email_intel import email_intel
from modules.dorking import generate_dorks
from modules.subdomains import enumerate_subdomains, SUBDOMAINS
from modules.ip_geo import geolocate_ip
from modules.username_search import search_username, PLATFORMS
from report_generator import save_simple_report
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import whois
import dns.resolver

console = Console()

def show_banner():
    console.print(Panel.fit(
        "[bold cyan]OSINT Tool V1[/bold cyan]\n"
        "[dim]Domain Recon | Email Intel | Dorking | Subdomains | IP Geo | Username[/dim]\n"
        "[red]For authorized and legal use only.[/red]",
        border_style="cyan"
    ))

def main():
    show_banner()

    console.print("\n[bold]Select Module:[/bold]")
    console.print("  [cyan]1[/cyan] - Domain Recon")
    console.print("  [cyan]2[/cyan] - Email Intelligence")
    console.print("  [cyan]3[/cyan] - Google Dorking")
    console.print("  [cyan]4[/cyan] - Subdomain Enumeration")
    console.print("  [cyan]5[/cyan] - IP Geolocation")
    console.print("  [cyan]6[/cyan] - Username Search")
    console.print("  [cyan]7[/cyan] - Run All + Save Report\n")

    choice = input("Enter choice (1-7): ").strip()

    if choice == "1":
        domain = input("Enter domain (e.g. google.com): ").strip()
        domain_recon(domain)

    elif choice == "2":
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        domain = input("Company domain: ").strip()
        email_intel(first, last, domain)

    elif choice == "3":
        domain = input("Enter domain: ").strip()
        generate_dorks(domain)

    elif choice == "4":
        domain = input("Enter domain: ").strip()
        enumerate_subdomains(domain)

    elif choice == "5":
        ip = input("Enter IP address: ").strip()
        geolocate_ip(ip)

    elif choice == "6":
        username = input("Enter username: ").strip()
        search_username(username)

    elif choice == "7":
        domain = input("Enter domain: ").strip()
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        username = input("Enter username to search: ").strip()

        console.print("\n[bold yellow]Running full recon in sequence...[/bold yellow]\n")

        report_data = {}

        console.print("[dim]Collecting WHOIS data...[/dim]")
        try:
            w = whois.whois(domain)
            report_data["WHOIS"] = (
                f"Registrar: {w.registrar}\n"
                f"Creation Date: {w.creation_date}\n"
                f"Expiry Date: {w.expiration_date}\n"
                f"Name Servers: {w.name_servers}\n"
                f"Emails: {w.emails}"
            )
        except Exception as e:
            report_data["WHOIS"] = f"Failed: {e}"

        console.print("[dim]Collecting DNS records...[/dim]")
        try:
            dns_data = ""
            for record in ["A", "MX", "NS", "TXT"]:
                try:
                    resolver = dns.resolver.Resolver()
                    resolver.nameservers = ["8.8.8.8"]
                    answers = resolver.resolve(domain, record)
                    for ans in answers:
                        dns_data += f"{record}: {ans}\n"
                except:
                    pass
            report_data["DNS Records"] = dns_data
        except Exception as e:
            report_data["DNS Records"] = f"Failed: {e}"

        console.print("[dim]Enumerating subdomains...[/dim]")
        found_subs = []
        for sub in SUBDOMAINS:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = ["8.8.8.8"]
                resolver.timeout = 3
                resolver.lifetime = 3
                answers = resolver.resolve(f"{sub}.{domain}", "A")
                for ans in answers:
                    found_subs.append(f"{sub}.{domain} -> {ans}")
                    break
            except:
                pass
        report_data["Subdomains"] = "\n".join(found_subs) if found_subs else "None found"

        console.print("[dim]Geolocating IP...[/dim]")
        try:
            resp = requests.get(f"http://ip-api.com/json/{domain}", timeout=10)
            geo = resp.json()
            report_data["IP Geolocation"] = (
                f"IP: {geo.get('query')}\n"
                f"Country: {geo.get('country')}\n"
                f"City: {geo.get('city')}\n"
                f"ISP: {geo.get('isp')}\n"
                f"Organisation: {geo.get('org')}\n"
                f"ASN: {geo.get('as')}\n"
                f"Timezone: {geo.get('timezone')}"
            )
        except Exception as e:
            report_data["IP Geolocation"] = f"Failed: {e}"

        console.print("[dim]Generating email formats...[/dim]")
        f_lower = first.lower()
        l_lower = last.lower()
        f_init = f_lower[0]
        emails = [
            f"{f_lower}.{l_lower}@{domain}",
            f"{f_lower}{l_lower}@{domain}",
            f"{f_init}{l_lower}@{domain}",
            f"{f_lower}@{domain}",
            f"{f_lower}_{l_lower}@{domain}",
            f"{l_lower}.{f_lower}@{domain}",
        ]
        report_data["Email Intelligence"] = "\n".join(emails)

        console.print("[dim]Searching username across platforms...[/dim]")
        found_users = []
        not_found_users = []
        headers = {"User-Agent": "Mozilla/5.0"}

        def check(platform, url):
            try:
                r = requests.get(url, headers=headers, timeout=5)
                return platform, "FOUND" if r.status_code == 200 else "NOT FOUND", url
            except:
                return platform, "ERROR", url

        urls = {p: u.format(username) for p, u in PLATFORMS.items()}
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(check, p, u): p for p, u in urls.items()}
            for future in as_completed(futures):
                platform, status, url = future.result()
                if status == "FOUND":
                    found_users.append(f"FOUND - {platform}: {url}")
                else:
                    not_found_users.append(f"NOT FOUND - {platform}")

        report_data["Username Search"] = (
            "\n".join(sorted(found_users)) +
            "\n\n" +
            "\n".join(sorted(not_found_users))
        )

        console.print("[dim]Generating dork queries...[/dim]")
        from modules.dorking import DORKS
        dork_text = ""
        for category, template in DORKS.items():
            dork = template.replace("{domain}", domain)
            dork_text += f"{category}: {dork}\n"
        report_data["Google Dorking"] = dork_text

        save_simple_report(domain, report_data)

        console.print("\n[bold yellow]Running live terminal scan...[/bold yellow]\n")
        domain_recon(domain)

        console.print("\n[bold green]Full recon complete. Report saved.[/bold green]")

    else:
        console.print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    main()