#!/usr/bin/env python
# coding: utf-8
1. An abstract superclass is one way to provide re-usable code. You can extend the abstract class and inherit the code. This is sometimes more convenient than using static methods or object composition to share code. The abstract class can "fix" parts of the code (by making it final).

2.An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

3. The main reason for always calling base class _init__ is that base class may typically create member variable and initialize them to defaults. So if you don't call base class init, none of that code would be executed and you would end up with base class that has no member variables. Run this code.

4. A more sophisticated way to augment an inherited method involves forwarding. Message forwarding allows you to augment an inherited method in such a way that it can perform its inherited action and some new action

5. Function scope: Variables that are declared inside a function are called local variables and in the function scope. Local variables are accessible anywhere inside the function. Block scope: Variable that is declared inside a specific block & can't be accessed outside of that block.