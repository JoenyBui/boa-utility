# README #

This is a a collection of functions and decorators that I've collected
throughout the years.  Please use it as required.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* Reformat Info

        Non-special chars match themselves.  Exceptions are special characters:
            \       Escape special char or start a sequence.
            .       Match any char except newline, see re.DOTALL
            ^       Match start of the string, see re.MULTILINE
            $       Match end of the string, see re.MULTILINE
            []      Enclose a set of matchable chars
            R|S     Match either regex R or regex S.
            ()      Create capture group, & indicate precedence

        After '[', enclose a set, the only special chars are:
            ]   End the set, if not the 1st char
            -   A range, eg. a-c matches a, b or c
            ^   Negate the set only if it is the 1st char

        Quantifiers (append '?' for non-greedy):
            {m}     Exactly m repetitions
            {m,n}   From m (default 0) to n (default infinity)
            *       0 or more. Same as {,}
            +       1 or more. Same as {1,}
            ?       0 or 1. Same as {,1}

        Special sequences:
            \A  Start of string
            \b  Match empty string at word (\w+) boundary
            \B  Match empty string not at word boundary
            \d  Digit
            \D  Non-digit
            \s  Whitespace, see LOCALE, UNICODE
            \S  Non-whitespace
            \w  Alphanumeric: [0-9a-zA-Z_], see LOCALE
            \W  Non-alphanumeric
            \Z  End of string
            \g<id>  Match prev named or numbered group, '<' & '>' are literal, e.g. \g<0> or \g<name> (not \g0 or \gname)

        -?      an optional -
        [\d.]+  a series of digits or dots (see *1)
        (?:     start non capturing group
          e     "e"
          -?    an optional -
          \d+   digits
        )?      end non-capturing group, make optional


        1. The earliest (leftmost) match wins.
        2. Standard quantifiers are greedy.

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact