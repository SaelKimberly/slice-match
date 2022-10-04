# slice-match

Simple class, that simplify usage of slices in `__getitem__`.

**Available on PyPi**: <https://pypi.org/project/slice-match/>

## Installation

Install with pip:

```powershell
pip install -U slice-match
```

## Requirements

Python 3.10 and newer

## Description

It's just a little trick, that allows you to do:

```python
class custom_indexed:
    def __getitem__(self, index):  
        match index:    
            case int(s):      
                print('this is "me[0]"-like expression')        
            case Slice(int(s)):
                # note, this also matches "me[0:<Any>:<Any>]"-like
                print('this is "me[0:]"-like expression')        
            case Slice(int(start), int(stop)):      
                # note, this also matches "me[0:5:<Any>]"-like
                print('this is "me[0:5]"-like expression')        
            case Slice(int(start), int(stop), int(stride)):      
                print('this is "me[0:5:2]"-like expression')        
            case Slice(start, None, stride):      
                print('this is "me[<Any>::<Any>]"-like expression')
            case Slice(start=12):
                print('this is "me[12:<Any>:<Any>]"-like expression')
```

## Performance drop

Using `Slice` cause ~2x performance drop, compared with using `slice`.

Simple benchmark notebook can be found here: <https://github.com/SaelKimberly/slice-match/blob/main/slice-match.ipynb>

So, readability improved (over 9000% ;) ), but performance slightly drops.
