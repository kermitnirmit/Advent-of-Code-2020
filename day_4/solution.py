import re
with open("input.txt") as f:
    text = f.read().rstrip()

passports = text.split("\n\n")
valid = 0

for passport in passports:
    fields = re.split(r"\n| ", passport)
    if len(fields) >= 7:
        
        all_Valid = True
        # # need to find all of the fields
        # # each field is of the form asdf:#####

        # # check byr
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
        print(byr, iyr, eyr, hgt, ecl, hcl, pid)
        # print(pid)
        # all but heights have been checked

        if hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76:
            valid += 1
        elif hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193:
            valid += 1
        
        # iyr = [i for i in fields if "iyr:" in i]
        # eyr = [i for i in fields if "eyr:" in i]
        # hgt = [i for i in fields if "hgt:" in i]
        # hcl = [i for i in fields if "hcl:" in i]
        # ecl = [i for i in fields if "ecl:" in i]
        # pid = [i for i in fields if "pid:" in i]
        # print(fields)
        # # byr validation
        # if len(byr) != 1:
        #     all_Valid = False
        #     break
        # byrVal = byr[0].split(":")[1]
        # if not (1920 <= int(byrVal) <= 2002):
        #     all_Valid = False
        
        # # ecl
        # if len(ecl) != 1:
        #     all_Valid = False
        #     break
        # valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        # eclVal = ecl[0].split(":")[1]
        # if eclVal not in valid_ecls:
        #     all_Valid = False
        
        # # hcl
        # if len(hcl) != 1:
        #     all_Valid = False
        #     break
        # hclVal = hcl[0].split(":")[1]
        # if not re.match(r"^#[0-9|a-z]{6}$", hclVal):
        #     all_Valid = False
        
        # #pid
        # if len(pid) != 1:
        #     all_Valid = False
        #     break
        # pidVal = pid[0].split(":")[1]

        # if not re.match(r"^[0-9]{9}$", pidVal):
        #     all_Valid = False
        
        # #iyr

        # if len(iyr) != 1:
        #     all_Valid = False
        # iyrVal = iyr[0].split(":")[1]
        # if not (2010 <= int(iyrVal) <= 2020):
        #     all_Valid = False
        
        # # eyr
        # if len(eyr) != 1:
        #     all_Valid = False
        # eyrVal = eyr[0].split(":")[1]
        # if not (2010 <= int(eyrVal) <= 2020):
        #     all_Valid = False

        # # hgt
        # if len(hgt) != 1:
        #     all_Valid = False
        # hgtVal = hgt[0].split(":")[1]
        # if hgtVal[-2:] == "cm" and not 150 <= int(hgtVal[:-2]) <= 193:
        #     all_Valid = False
        # if hgtVal[-2:] == "in" and not 59 <= int(hgtVal[:-2]) <= 76:
        #     all_Valid = False
        
        # if all_Valid:
        #     valid += 1
print(valid)

# 124 is too low