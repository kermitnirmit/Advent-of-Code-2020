import re
with open("input.txt") as f:
    text = f.read().rstrip()

passports = text.split("\n\n")
valid1 = valid2 = 0

for passport in passports:
    fields = re.split(r"\n| ", passport)
    if len(fields) == 8 or len(fields) == 7 and len([i for i in fields if "cid" in i]) == 0:
        valid1 += 1
    if len(fields) >= 7:
        all_Valid = True
        try:
            byr = [int(i[4:]) for i in fields if "byr:" in i and 1920 <= int(i[4:]) <= 2002][0]
            iyr = [int(i[4:]) for i in fields if "iyr:" in i and 2010 <= int(i[4:]) <= 2020][0]
            eyr = [int(i[4:]) for i in fields if "eyr:" in i and 2020 <= int(i[4:]) <= 2030][0]
            hgt = [i[4:] for i in fields if "hgt:" in i and i[-2:] in ["in", "cm"]][0]
            ecl = [i[4:] for i in fields if "ecl:" in i and i[4:] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]][0]
            hcl = [i[4:] for i in fields if "hcl:" in i and re.match(r"^#[0-9a-f]{6}$", i[4:])][0]
            pid = [i[4:] for i in fields if "pid:" in i and re.match(r"^[0-9]{9}$", i[4:])][0]
        except:
            continue
        if hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76:
            valid2 += 1
        elif hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193:
            valid2 += 1

print(valid1)
print(valid2)
