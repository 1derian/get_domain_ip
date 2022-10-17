#!/usr/bin/env python3
import os,time
import textwrap

import dns.resolver
import tldextract
import sys
import argparse


def domain_extract(domain):
    source_domain = tldextract.extract(domain)
    if source_domain.subdomain == '':
        domain = "{}.{}".format(source_domain.domain, source_domain.suffix)
    else:
        domain = "{}.{}.{}".format(source_domain.subdomain, source_domain.domain, source_domain.suffix)
    return domain


def get_record_a(domain):
    try:
        domain = dns.resolver.query(domain, "A")
        iplist = []
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 1:
                    iplist.append(ip.address)
        return iplist
    except Exception:
        return None


def get_record_cname(domain):
    domain_extract(domain)
    try:
        domain = dns.resolver.query(domain, "CNAME")
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 5:
                    return ip.to_text()
    except Exception:
        return None


def get_record_ns(domain):
    domain_extract(domain)
    try:
        domain = dns.resolver.query(domain, "NS")
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 2:
                    return ip.to_text()
    except Exception:
        return None


def get_record_file(file_path, output_path=None):
    start_time = time.time()
    f1 = open(output_path, mode="w", encoding="u8")
    with open(file_path, mode="r", encoding="u8") as f:
        print("{:<40s}{:<40s}{:<40s}{:30s}".format("Domain", "CNAME", "NS", "A"))
        for line in f:
            domain = line.strip("\n")
            domain = domain_extract(domain)
            getcname = get_record_cname(domain)
            getdns = get_record_a(domain)
            getns = get_record_ns(domain)

            if getdns is not None:
                getdns_str = ",".join(f"{x}" for x in getdns)
            else:
                getdns = ""
            if getcname is not None:
                getcname = getcname
            else:
                getcname = ""

            if getns is not None:
                getns = getns
            else:
                getns = ""

            print('{:<40s}{:<40s}{:<40s}{:<40s}'.format(domain, getcname, getns, getdns_str))
            # 写入
            line = "{:<40s}{:<40s}\n".format(domain, getdns_str)
            f1.write(line)
        f1.close()
        print(f"\n\nall done , save in {output_path}, have a nice day!!!")
        print("shutting down at {0} 共耗时{1}秒\n".format(time.strftime("%X"), time.time() - start_time))


def get_record_list(*args):
    if args is None:
        sys.exit(1)
    print("{:<40s}{:<40s}{:<40s}{:30s}".format("Domain", "CNAME", "NS", "A"))
    for key in args:
        for line in key:
            domain = line.strip("\n")
            domain = domain_extract(domain)
            getcname = get_record_cname(domain)
            getdns = get_record_a(domain)
            getns = get_record_ns(domain)

            if getdns is not None:
                getdns = ",".join(f"{x}" for x in getdns)
            else:
                getdns = ""

            if getcname is not None:
                getcname = getcname
            else:
                getcname = ""
            if getns is not None:
                getns = getns
            else:
                getns = ""
            print('{:<40s}{:<40s}{:<40s}{:<40s}'.format(domain, getcname, getns, getdns))


def main():
    banner = """ 
                         _                       _                                     
                      __| | ___  _ __ ___   __ _(_)_ __     __ _ _   _  ___ _ __ _   _ 
                     / _` |/ _ \| '_ ` _ \ / _` | | '_ \   / _` | | | |/ _ \ '__| | | |
                    | (_| | (_) | | | | | | (_| | | | | | | (_| | |_| |  __/ |  | |_| |
                     \__,_|\___/|_| |_| |_|\__,_|_|_| |_|  \__, |\__,_|\___|_|   \__, |
                                                              |_|                |___/ 
                                                                        version: 0.0.1
                                                                        author : mhx
    """
    print(banner)

    parser = argparse.ArgumentParser(description="This is a good domain resolution tool",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
        python3 get_domain_ip -d www.baidu.com
        '''))
    parser.add_argument('-d', '--domain', dest="domain", nargs="+",
                        help="Query single or multiple domain name resolution.")
    parser.add_argument('-df', '--domain_file', dest="domain_file",
                        help="Query multiple domain name resolutions as files.")
    parser.add_argument('-o', '--output', dest="output", default="result.txt",
                        help="Domain name resolutions save in file.")
    args = parser.parse_args()

    if args.domain:
        get_record_list(args.domain)
    if args.domain_file:
        get_record_file(args.domain_file, output_path=args.output)


if __name__ == '__main__':
    main()
