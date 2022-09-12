# slice-match
Simple class, that simplify usage of slices in `__getitem__`.

# Requirements
Python 3.10 and newer

# Description
It's just a little trick, that allows you to do:

```python
class custom_indexed:
    def __getitem__(self, index):  
        match index:    
            case int(s):      
                print('this is "me[0]"-like expression')        
            case Slice(int(s)):      
                print('this is "me[0:]"-like expression')        
            case Slice(int(start), int(stop)):      
                print('this is "me[0:5]"-like expression')        
            case Slice(int(start), int(stop), int(stride)):      
                print('this is "me[0:5:2]"-like expression')        
            case Slice(start, None, stride):      
                print('this is "me[<Any>::<Any>]"-like expression')
```

# Performance drop

For testing purpose, special class created:

```python
class gg:
    def __class_getitem__(cls, index):
        return index
```

Tested constructions:

```python
%%timeit
match gg[:12]:
    case slice() as x if x.start is None and isinstance((y := x.stop), int) and x.step is None:
        i = y
    case _:
        i = -1
```
Result:
`740 ns ± 83 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)`

```python
%%timeit
match gg[:12]:
    case slice() as x:
        match x.start, x.stop, x.step:
            case None, int(y), None:
                i = y
    case _:
        i = -1
```
Result:
`2.02 µs ± 251 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)`

```python
%%timeit
match gg[:14]:
    case Slice(None, int(y), None):
        i = y
    case _:
        i = -1
```
Result:
`3.33 µs ± 436 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)`

So, readability improved (over 9000% ;) ), but performance slightly drops (+2.5 µs for each Slice in match-case)
