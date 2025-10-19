# whitepy

[![Build Status](https://travis-ci.org/yasn77/whitepy.svg?branch=master)](https://travis-ci.org/yasn77/whitepy)

Whitespace interpreter written in Python3 for my final Open University project (TM470)

### Install and Usage

Once installed, run `whitepycli` with a whitespace source file as an argument.

##### Using pip

```shell
$ pip install whitepy
$ whitepycli --help
Usage: whitepycli [OPTIONS] FILENAME

  Whitespace Interpreter

Options:
  --debug / --no-debug  Enable Debug
  --help                Show this message and exit.
  
$ whitepycli sample_ws/helloworld.ws 
Hello, World!
```

##### From Github

```shell
$ git clone https://github.com/mori-no-anikitachi/whitepy && cd whitepy
$ pip install -r requirements.txt
$ ./whitepycli --help
Usage: whitepycli [OPTIONS] FILENAME

  Whitespace Interpreter

Options:
  --debug / --no-debug  Enable Debug
  --help                Show this message and exit.
  
$ ./whitepycli sample_ws/helloworld.ws 
Hello, World!
```

### What is Whitespace?

Whitespace programming language was originally created by Edwin Brady and Chris Morris at the University of Durham<sup>[1]</sup>, then gained wider exposure when it was reviewed<sup>[2]</sup> April 1st 2003 on [Slashdot](https://slashdot.org) website.

Originally developed as a bit of fun, Whitespace is an attempt to have a programming language that uses characters that are usually ignored by other programming languages, namely `space` (ASCII 32), `tab`(ASCII 9) and `linefeed`(ASCII 10). The by-product being that you could implement Whitespace code in other text (making it possible to write a polygot computer program).

### How to write Whitespace?

Whitespace is an imperative stack based language, with 5 basic commands known as _Instruction Imperative Parameter_ (IMP):

| IMP            | Meaning            |
| -------------- | ------------------ |
| `[Space]`      | Stack Manipulation |
| `[Tab][Space]` | Arithmetic         |
| `[Tab][Tab]`   | Heap access        |
| `[LF]`         | Flow Control       |
| `[Tab][LF]`    | I/O                |

The full list of IMP with commands can be found in the Whitespace tutorial<sup>[3]</sup>. The original tutorial is no longer available, but can be accessed using [Internet Archive:  Wayback machine](http://archive.org/web/).

One of the biggest difficulties in writing Whitespace is that the source code isn't immediately visible in most editors. To get around this, many editors have the ability to represent Whitespace characters as some other character. For example, in `vim` you can use `:set listchars=...` and `:set list`.

### whitepy Implementation

#### Lexer ([`lexer.py`](whitepy/lexer.py))

The whitepy lexerical analysis relies on [`lexerconstants.py`](whitepy/lexerconstants.py), which contains valid IMP that can be used and their valid arguments also other definitions, such as integer representation. These are taken from the [original whitespace tutorial](https://web.archive.org/web/20030414001723/http://compsoc.dur.ac.uk:80/whitespace/tutorial.php).

The lexer takes the whitespace code as an input (`lexer.Lexer(line=lines)`) and when the method `lexer.get_all_tokens()` is called, a list of tokens and arguments is created from the whitespace source file. These tokens are stored in the lexer object and can be retrieved by calling `lexer.tokens`.

Tokenisation process is handled by [`ws_token.py`](whitepy/ws_token.py).

#### Tokeniser ([`ws_token.py`](whitepy/ws_token.py))

The engine that drives the Tokeniser is Pythons `re` library, specifically `re.Scanner`. This is a powerful library that can easily allow splitting of text in to the required tokens. Documentation for `re.Scanner` is not extensive and can be found under section `6.2.5.9` of [Python `re` documentation](https://docs.python.org/3.2/library/re.html#writing-a-tokenizer), however I found some really helpful documentation and examples [here](http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/).

#### Parser ([`parser.py`](whitepy/parser.py))

Once lexical analysis is complete, it is now possible to parse the list of tokens and execute accordingly. At the heart of the parser is a token to method map (`parser.method_map`), this is a `dict` structure that maps tokens to internal methods. I believe this approach helps me to extend the interpreter with possibly my own token implementations and reduces the size of the `parser.parse()` method. This is because it reduces the amount of logic required in `parser.parse()` and instead the method simply looks up keys in a `dict`.

### Helpful links

The following is a list of sites/references I have used to help me develop `whitepy`:

| Title                                    | Link                                     |
| ---------------------------------------- | ---------------------------------------- |
| Writing Compilers and Interpreters: A Software Engineering Approach by Ronald Mak | https://www.amazon.co.uk/Writing-Compilers-Interpreters-Software-Engineering-ebook/dp/B004S82O40) |
| Whitspace Language Tutorial              | https://h0tsh0tt.wordpress.com/2016/07/03/whitespace-language-tutorial/ |
| Whitespace (Wikipedia)                   | https://en.wikipedia.org/wiki/Whitespace_(programming_language) |
| Interpreter Collection for the Whitespace Language | https://github.com/hostilefork/whitespacers/ |
| Online Whitespace Compiler, virtual machine and IDE | https://github.com/vii5ard/whitespace    |
| Let's build a simple interpreter         | https://ruslanspivak.com/lsbasi-part1/   |
| Python `re` module used for tokenising   | http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/ |
| Let's build a compiler                   | http://compilers.iecc.com/crenshaw/      |
| Notes on how Parsers and Compilers work  | http://parsingintro.sourceforge.net/     |

### References

[1] https://web.archive.org/web/20030412201917/http://compsoc.dur.ac.uk:80/whitespace/

[2] https://developers.slashdot.org/story/03/04/01/0332202/New-Whitespace-Only-Programming-Language

[3] https://web.archive.org/web/20030414001723/http://compsoc.dur.ac.uk:80/whitespace/tutorial.php

