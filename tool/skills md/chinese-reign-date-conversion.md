# Chinese Reign-Date Conversion

## Purpose

Use this skill when a Chinese source contains dates written with a reign-period name and Chinese numerals, such as:

```text
乾隆五十一年十二月十日
```

The project convention is to preserve the original Chinese date and append the Gregorian date in parentheses:

```text
乾隆五十一年十二月十日（1787/1/28）
```

## Required Authority

Use Academia Sinica Sinocal as the conversion authority:

```text
https://sinocal.sinica.edu.tw
```

If Sinocal is unreachable, do not pretend the conversion has been verified there. Either:

- wait and retry Sinocal later, or
- add only conversions that are already known from verified project context, and mark the limitation in processing notes.

## Conversion Rules

- Preserve the original Chinese date exactly.
- Append the Gregorian date immediately after the Chinese date in full-width parentheses.
- Use slash format: `YYYY/M/D`.
- Do not pad month or day with leading zeroes.
- Do not convert partial dates unless the missing part is clearly supplied by context and recorded.
- Do not silently normalize `初十` to `十日` in the source text. Preserve the source form and append the same Gregorian date if verified.
- Convert every full reign-date occurrence in cleaned text, including dates in:
  - metadata lines,
  - body text,
  - final-date lines,
  - notes or imperial replies if present.

## Pattern To Look For

Full dates usually contain:

```text
年
月
日
```

and begin with a reign-period name such as:

```text
康熙
雍正
乾隆
嘉慶
道光
咸豐
同治
光緒
宣統
```

Project-specific non-standard era labels such as `天運` may appear. Convert these only if Sinocal or another explicitly accepted authority supports the date.

## Example

Input:

```text
乾隆五十一年十二月十日
```

Output:

```text
乾隆五十一年十二月十日（1787/1/28）
```

If the source writes:

```text
乾隆五十一年十二月初十日
```

and Sinocal verifies that it is the same date, output:

```text
乾隆五十一年十二月初十日（1787/1/28）
```

## Quick Reference: Repeated Qianlong Years

Use this only as a year-level aid. Exact month/day conversion must still be checked with Sinocal because Chinese lunar years do not align exactly with Gregorian calendar years.

| Chinese reign year | Arabic reign year | Approx. Gregorian year |
| --- | ---: | ---: |
| 乾隆四十九年 | 乾隆49年 | 1784 |
| 乾隆五十年 | 乾隆50年 | 1785 |
| 乾隆五十一年 | 乾隆51年 | 1786 |
| 乾隆五十二年 | 乾隆52年 | 1787 |
| 乾隆五十三年 | 乾隆53年 | 1788 |
| 乾隆五十四年 | 乾隆54年 | 1789 |
| 乾隆五十五年 | 乾隆55年 | 1790 |
| 乾隆五十六年 | 乾隆56年 | 1791 |
| 乾隆五十七年 | 乾隆57年 | 1792 |
| 乾隆五十八年 | 乾隆58年 | 1793 |
| 乾隆五十九年 | 乾隆59年 | 1794 |
| 乾隆六十年 | 乾隆60年 | 1795 |

Example of the boundary issue:

```text
乾隆五十一年十二月十日
```

is in the lunar twelfth month of Qianlong 51 and converts to:

```text
乾隆五十一年十二月十日（1787/1/28）
```

So the year-level table is only a quick guide; the full converted date may fall in the next Gregorian year.

## Documentation Requirement

When applying conversions to a source:

1. Record the converted file path in the source processing notes.
2. Record whether Sinocal was reached successfully.
3. If any conversion was inserted from prior project context rather than a live Sinocal check, state that clearly.
4. Leave uncertain dates unconverted rather than guessing.
