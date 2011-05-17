#!/usr/bin/env python
# -*- coding: utf-8 -*-

   
class Tag():
    AND    = 256
    BASIC  = 257
    BREAK  = 258
    DO     = 259
    ELSE   = 260
    EQ     = 261
    FALSE  = 262
    GE     = 263
    ID     = 264
    IF     = 265
    INDEX  = 266
    LE     = 267
    MINUS  = 268
    NE     = 269
    NUM    = 270
    OR     = 271
    REAL   = 272
    TEMP   = 273
    TRUE   = 274
    WHILE  = 275

class Token():
    def __init__(self,t):
        self.tag = int()
        self.tag = t
    def toString(self):
        return str(self.tag)

class Num(Token):
    value = int()
    def __init__(self,v):
        Token.__init__(self,Tag.NUM)
        value = v
    def toString(self): 
        return str(value)

class Real(Token):
    value = float()
    def __init__(self,v):
        Token.__init__(self,Tag.REAL)
        value = v
    def toString(self):
        return str(value)



class Word(Token):
    def __init__(self,s,tag):
        Token.__init__(self,tag)
        self.lexeme = str()
        self.lexeme = s
    def toString():
        return self.lexeme

Word.AND    = Word("&&",    Tag.AND)
Word.OR     = Word("||",    Tag.OR)
Word.EQ     = Word("==",    Tag.EQ)
Word.NE     = Word("!=",    Tag.NE)
Word.LE     = Word("<=",    Tag.LE)
Word.GE     = Word(">=",    Tag.GE)
Word.MINUS  = Word("minus", Tag.MINUS)
Word.TRUE   = Word("true",  Tag.TRUE)
Word.FALSE  = Word("false", Tag.FALSE)
Word.TEMP   = Word("t",     Tag.TEMP)

class Type(Word):
    def __init__(self,s,tag,w):
        Word.__init__(self,s,tag)
        self.width = int(w)
    def numeric(self,p):
        if p == Type.CHAR or p == Type.INT or p == Type.FLOAT:
            return True
        else:
            return False
    def max(self,p1,p2):
        if not self.numeric(p1) or not self.numeric(p2):
            pass
        elif p1 == Type.FLOAT or p2 == Type.FLOAT:
            return Type.FLOAT
        elif p1 == Type.INT or p2 == Type.INT:
            return Type.INT
        else:
            return Type.CHAR


Type.INT   = Type("int",    Tag.BASIC, 4)
Type.FLOAT = Type("float",  Tag.BASIC, 8)
Type.CHAR  = Type("char",   Tag.BASIC, 1)
Type.BOOL  = Type("bool",   Tag.BASIC, 1)

class lexer():
    words = dict()
    line = 1
    def reserve(self,w):
        self.words[w.lexeme] = w
    def __init__(self):
        self.peek = ' '
        f = open('test1','r+')
        self.haha = f.read()
        f.close()

        tmp = list()
        tmp.append(Word("if",    Tag.IF))
        tmp.append(Word("else",  Tag.ELSE))
        tmp.append(Word("while", Tag.WHILE ))
        tmp.append(Word("do",    Tag.DO ))
        tmp.append(Word("break", Tag.BREAK ))
        tmp.append(Word.TRUE)
        tmp.append(Word.FALSE)
        tmp.append(Type.INT)
        tmp.append(Type.CHAR)
        tmp.append(Type.BOOL)
        tmp.append(Type.FLOAT)

        for i in tmp:
            self.reserve(i)
    def readch(self,c=None):
        if self.haha:
            self.peek = self.haha[0]
            self.haha = self.haha[1:]
        else:
            raise Exception('End of file reached') 
        if c is not None:
            if c == self.peek:
                return False
            else:
                self.peek = ' '
                return True
    def scan(self):
        while(True):
            if self.peek == '\n':
                self.line += 1
                self.readch()
                continue
            elif self.peek == ' ' or self.peek == '\t':
                self.readch()
                continue
            else:
                break

        if self.peek == '&':
            if self.readch('&'):
                return Word.AND
            else:
                return Token('&')
        elif self.peek == '|':
            if self.readch('|'):
                return Word.OR
            else:
                return Token('|')
        elif self.peek == '=':
            if self.readch('='):
                return Word.EQ
            else:
                return Token('=') 
        elif self.peek == '!':
            if self.readch('='):
                return Word.NE
            else:
                return Token('!')
        elif self.peek == '<':
            if self.readch('='):
                return Word.LE
            else:
                return Token('<')
        elif self.peek == '>':
            if self.readch('='):
                return Word.GE
            else:
                return Token('>')
               
        if self.peek.isdigit():
            v = int(0)
            while self.peek.isdigit():
                v = 10*v + int(self.peek)
                self.readch()
            if not self.peek == '.':
                return Num(v)
            x = float(v)
            d = float(10)
            while(True):
                self.readch()
                if not self.peek.isdigit():
                    break
                x = x + (int(self.peek)/d)
                d = d * 10
            return Real(x)
        if self.peek.isalpha():
            b = str()
            while(self.peek.isalpha() or self.peek.isdigit()):
                b += str(self.peek)
                readch()
            s = b
            w = words[s]
            if w:
                return w
            w = Word(s, Tag.ID)
            words[s] = w
            return w

                
            
 
def main():
    mylexer = lexer()
    try:
        while(True):
            t = Token(mylexer.scan())
            print t.toString() 
    except Exception as inst:
        print inst           # __str__ allows args to printed directly
        
if __name__ == '__main__':
    main()

