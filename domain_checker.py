import whois
import dns.resolver
import sys

def check_domain(domain_name): 
    """Check the registration details and DNS information of a domain."""
    try:
        domain_info = whois.whois(domain_name)
        print(f"Domain {domain_name} is registered.")
        expiration_date = domain_info.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        print(f"Registration expires on: {domain_info.expiration_date}")

        nameservers = domain_info.name_servers
        if isinstance(nameservers, list):
            nameservers = ', '.join(nameservers)
        print(f"Name Servers: {nameservers}")
    except Exception as e: 
        print(f"Domain {domain_name} is not registered or error: {e}")

    try:
        answers = dns.resolver.resolve(domain_name, 'NS')
        print("Name Servers retrieved using dnspython:")
        for server in answers: 
            print(server.target)
    except Exception as e:
        print(f"Failed to retrieve DNS information: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_domain(sys.argv[1])
    else:
        print("Please provide a domain name.")
    
