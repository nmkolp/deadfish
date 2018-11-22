# Deadfish~ Interpreter in Python3

## Deadfish Language Features

| cmd | xkdc | Description |
| --- | --- | --- |
| i | x | Increments the accumulator |
| d | d | Decrements the accumulator |
| s | k | Squares the accumulator |
| o | c | Outputs the accumulator |

Accumulator becomes zero if and only if its value is -1 or 256.

### Samples

Hello world! ASCII values
```
>> iisiiiisiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddodddddddddddddddddddddsddoddddddddoiiioddddddoddddddddoddddddddd
ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo
```

Example of Deadfish arithmetic
```
>> iissso
0
```

Another example
```
>> diissisdo
288
```

## Deadfish~ Language Features

| cmd | xkdc | Description |
| --- | --- | --- |
| i | x | Increments the accumulator |
| d | d | Dcrements the accumulator |
| s | k | Squares the accumulator |
| o | C | Outputs the accumulator |
| c | c | Outputs the accumulator as an ASCII character |
| { } | X D* | Instructions inside the braces are executed ten times |
| ( ) | x D* | If accumulator is not 0 then execute instructions inside the parentheses |
| h | D* | Halt |
| w | K | Prints 'Hello, World!' |

&nbsp;*&nbsp;'D' command closes brackets in correct order, if no brackets left then program halts

### Samples

Hello world!
```
>> iisiiiisiiiiiiiiciiiiiiiiiiiiiiiiiiiiiiiiiiiiiciiiiiiicciiicdddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddcdddddddddddddddddddddsddcddddddddciiicddddddcddddddddcddddddddd
ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddc
Hello world!
>> w
Hello world!
```

Alphabet
```
>> iisiiiis{ic}{ic}icicicicicic
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Let the world know what you think of Deadfish~
```
>> iisiiiisiiiiiiiiciiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiciii{c}dddddddddcdddddddciiiiiiiiiicdddddddc
Horrrrrrrrrrible
```

## Startup Arguments

-p: Execute program<br />
&nbsp;&nbsp;&nbsp;&nbsp; program code<br />

-v: Set Deadfish variant<br />
&nbsp;&nbsp;&nbsp;&nbsp; o : Original Deadfish<br />
&nbsp;&nbsp;&nbsp;&nbsp; t : Deadfish~ [default]<br />

-c: Set command style<br />
&nbsp;&nbsp;&nbsp;&nbsp; o : Original (i, d, s, o, ...) [default]<br />
&nbsp;&nbsp;&nbsp;&nbsp; x : xkdc (x, d, k, c, ...)<br />

-w: Set wimpmodes<br />
&nbsp;&nbsp;&nbsp;&nbsp; e : Output error and abort on invalid character<br />
&nbsp;&nbsp;&nbsp;&nbsp; o : Output error and abort on overflow<br />
&nbsp;&nbsp;&nbsp;&nbsp; O : Use correct overflow rule (<0 and > 255)<br />
&nbsp;&nbsp;&nbsp;&nbsp; r : Add reset command 'r'<br />

## More Info

https://esolangs.org/wiki/Deadfish <br />
https://esolangs.org/wiki/Deadfish%7E <br />
https://esolangs.org/wiki/Deadfish/Constants
