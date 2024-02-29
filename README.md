# jp-weekends-and-holidays

## Prerequisites

```bash
pip install -r requirements.txt
```

## Example

```bash
 % python jp_weekends_and_holidays.py 2024 1
2024-01-01
2024-01-06
2024-01-07
2024-01-08
2024-01-13
2024-01-14
2024-01-20
2024-01-21
2024-01-27
2024-01-28
```

### multiple months output

```bash
% head yyyy-mm.list
2020 10
2020 11
2020 12
2021 01
2021 02
2021 03
2021 04
2021 05
2021 06
2021 07

while read year_month;do python jp_weekends_and_holidays.py ${year_month%% *} ${year_month#* } | perl -ne '/202\d-\d+-(\d+)/ and print "$1,"' | perl -pe 's/,$/\n/';done < yyyy-mm.list | pbcopy
```

### Change date output to CSV

```bash
 % python jp_weekends_and_holidays.py 2024 02
2024-02-03
2024-02-04
2024-02-10
2024-02-11
2024-02-12
2024-02-17
2024-02-18
2024-02-23
2024-02-24
2024-02-25
```

```bash
 % python jp_weekends_and_holidays.py 2024 02 | perl -ne '/202\d-\d+-(\d+)/ and print "$1,"' | perl -pe 's/,$/\n/'
03,04,10,11,12,17,18,23,24,25
```
