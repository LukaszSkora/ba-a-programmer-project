import csv
import re
import os


def replace_domain(email, new_domain):
    new_email = re.sub(r'@.+', r'@' + new_domain, email)
    return new_email


def main():
    csv_file = "csv.csv"
    new_domain = "gmail.com"

    with open(csv_file, "r") as f:
        old_list = csv.reader(f)
        new_list = []

        for i in old_list:
            n = i[0].strip()
            e = i[1]
            e = replace_domain(e, new_domain).strip()
            l = [n, e]
            new_list.append(l)
        f.close()
        print(new_list)

        with open("new.csv", 'w') as ff:
            writer = csv.writer(ff)
            writer.writerows(new_list)
            ff.close()

main()
