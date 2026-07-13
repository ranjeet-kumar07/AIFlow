# Expression Parser

## Purpose

Extracts a mathematical expression from a natural language prompt.

Examples

Input:
calculate 25*8

Output:
25*8

Input:
What is (20+5)*3

Output:
(20+5)*3

The parser keeps providers focused on communication with LLMs while isolating parsing logic into a dedicated reusable component.