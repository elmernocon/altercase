# altercase

Convert strings into different cases.


## Installation

```shell
pip install altercase
```

## Usage

```shell
altercase --help
```
```text
Usage: altercase [OPTIONS] CASE INPUT

  Convert strings into different cases. (version: x.x.x)

Options:
  -h/--help   Show this message and exit.

Arguments:
  CASE        Accepts one of ('camel', 'pascal', 'snake', 'hazard', 'kebab', 'train', 'title', 'sentence').
  INPUT       String(s) to convert.
```

---

```shell
altercase title theQuickBrownFoxJumpsOverTheLazyDog
```
```text
The Quick Brown Fox Jumps Over The Lazy Dog
```

---

```shell
altercase kebab Foobar2000 'HTTP/2 Protocol'
```
```text
foobar-2000
http-2-protocol
```

---

```shell
echo IEEE802.3EthernetStandard PCIe4.0Interface | altercase hazard
```
```text
IEEE_802_3_ETHERNET_STANDARD
PCI_E_4_0_INTERFACE
```

### Case conversion

#### Camel case

`theQuickBrownFoxJumpsOverTheLazyDog`

Spaces and punctuation are removed and the first word will be in lowercase.
Other words will have their first letter be capitalized. Abbreviation
capitalization is always preserved.

```python
import altercase

                                            # ['API', 'v2', 'Parser']
                                            #   ↓↓↓    ↓
                                            # ['api', 'V2', 'Parser']
print(altercase.camel_case("APIv2Parser"))  # apiV2Parser
```

#### Pascal case

`TheQuickBrownFoxJumpsOverTheLazyDog`

Spaces and punctuation are removed and the first letter of each word is
capitalized. Abbreviation capitalization is always preserved.

```python
import altercase

                                             # ['API', 'v2', 'Parser']
                                             #          ↓
                                             # ['API', 'V2', 'Parser']
print(altercase.pascal_case("APIv2Parser"))  # APIV2Parser
```

#### Snake case

`the_quick_brown_fox_jumps_over_the_lazy_dog`

Spaces and punctuation are replaced by single underscores (`_`). All letters
will be lowercase.

```python
import altercase

                                            # ['API', 'v2', 'Parser']
                                            #   ↓↓↓          ↓
                                            # ['api', 'v2', 'parser']
print(altercase.snake_case("APIv2Parser"))  # api_v2_parser
```

#### Hazard case (Screaming Snake case)

`THE_QUICK_BROWN_FOX_JUMPS_OVER_THE_LAZY_DOG`

Spaces and punctuation are replaced by single underscores (`_`). All letters
will be in uppercase.

```python
import altercase

                                             # ['API', 'v2', 'Parser']
                                             #          ↓      ↓↓↓↓↓
                                             # ['API', 'V2', 'PARSER']
print(altercase.hazard_case("APIv2Parser"))  # API_V2_PARSER
```

#### Kebab case

`the-quick-brown-fox-jumps-over-the-lazy-dog`

Spaces and punctuation are replaced by single hyphens (`-`). All letters will
be in lowercase.

```python
import altercase

                                            # ['API', 'v2', 'Parser']
                                            #   ↓↓↓          ↓
                                            # ['api', 'v2', 'parser']
print(altercase.kebab_case("APIv2Parser"))  # api-v2-parser
```

#### Train case

`THE-QUICK-BROWN-FOX-JUMPS-OVER-THE-LAZY-DOG`

Spaces and punctuation are replaced by single hyphens (`-`). All letters will
be in uppercase.

```python
import altercase

                                            # ['API', 'v2', 'Parser']
                                            #          ↓      ↓↓↓↓↓
                                            # ['API', 'V2', 'PARSER']
print(altercase.train_case("APIv2Parser"))  # API-V2-PARSER
```

#### Title case

`The Quick Brown Fox Jumps Over The Lazy Dog`

Punctuations are removed and the first letter of each word is capitalized.
Abbreviation capitalization is always preserved.

```python
import altercase

                                            # ['API', 'v2', 'Parser']
                                            #          ↓
                                            # ['API', 'V2', 'Parser']
print(altercase.title_case("APIv2Parser"))  # API V2 Parser
```

#### Sentence case

`The quick brown fox jumps over the lazy dog`

Punctuations are removed and the first letter of the first word is capitalized.
Other words will be in lowercase. Abbreviation capitalization is always
preserved.

```python
import altercase

                                               # ['API', 'v2', 'Parser']
                                               #          ↓     ↓
                                               # ['API', 'v2', 'parser']
print(altercase.sentence_case("APIv2Parser"))  # API v2 parser
```

### String splitting

```text
1st Pass
- separate the input string into 'words' whenever it switches from lowercase, uppercase, or digits;
  while ignoring non-alphanumeric chars

  'Foo'         → ['F', 'oo']
  'Foobar2000'  → ['F', 'oobar', '2000']
  'JWTToken'    → ['JWTT', 'oken']
  'WiFi'        → ['W', 'i', 'F', 'i']
  'APIv2Parser' → ['API', 'v', '2', 'P', 'arser']

2nd Pass
- if the previous word (is uppercase) and the current word (length > 1), (is lowercase)
  then take the last char from the previous word and insert it in front of the current word

  'Foo'         → ['F', 'oo']                     → ['Foo']
  'Foobar2000'  → ['F', 'oobar', '2000']          → ['Foobar', '2000']
  'JWTToken'    → ['JWTT', 'oken']                → ['JWT', 'Token']
  'APIv2Parser' → ['API', 'v', '2', 'P', 'arser'] → ['API', 'v', '2', 'Parser']

- if the previous word (length == 1), (is uppercase) and the current word (length == 1), (is lowercase)
  then move the char from the previous word and insert it in front of the current word

  'WiFi'        → ['W', 'i', 'F', 'i']   → ['Wi', 'Fi']

- if the previous word (length == 1), (is either 'v' or 'V') and the current word (is digit)
  then move the char from the previous word and insert it in front of the current word

  'APIv2Parser' → ['API', 'v', '2', 'P', 'arser'] → ['API', 'v', '2', 'Parser'] → ['API', 'v2', 'Parser']
```

```python
import altercase

print(altercase.split_string("APIv2Parser"))  # ['API', 'v2', 'Parser']
```

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or
bug reports, please
[create an issue](https://github.com/elmernocon/altercase/issues) or submit a
pull request.

## License

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
