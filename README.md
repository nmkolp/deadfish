# Deadfish~ Interpreter in Python3

## Deadfish Language Features

| cmd | xkdc | Description |
| --- | --- | --- |
| i | x | This increments the accumulator |
| d | d | This decrements the accumulator |
| s | k | Squares the value in the accumulator |
| o | c | Outputs the accumulator |

## Deadfish~ Language Features

| cmd | xkdc | Description |
| --- | --- | --- |
| i | x | This increments the accumulator |
| d | d | This decrements the accumulator |
| s | k | Squares the value in the accumulator |
| o | C | Outputs the accumulator |
| c | c | Outputs the accumulator as an ASCII character |
| {} | XD | Instructions inside the curly braces loop ten times |
| () | xD | If accumulator is not 0 then execute the statement inside once |
| h | D | Halt |
| w | K | Prints 'Hello, World!' |

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
https://esolangs.org/wiki/Deadfish%7E
