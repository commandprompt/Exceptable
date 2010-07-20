import re

def __factory__(regex):
    
    class Exceptable(object):
        
        def __init__(self, wraps, mappings):
            """
            * wraps -  is the base exception type to wrap.
            * mappings - the dict of strings to mappings that represent the Exceptable chain.
                         Strings will be searched for in the base exception string using the regex
                         ^[a-zA-Z0-9]{1,}::[\w]{0,}$
            """
            
            self.wraps = wraps
            self.mappings = mappings
            self.regex = re.compile(regex)
            self.regex_base = regex
            
        def __call__(self, func):
            def decorates(*args,**kwargs):
                try:
                    return func(*args,**kwargs)
                except self.wraps, e:
                    msg = str(e)
                    if self.regex is not None:
                        g = self.regex.match(msg)
                        
                        if g:
                            # We have a group match. Woot.
                            if g.group('type') in self.mappings.keys():
                                curr = g.group('type')
                                msg = g.group('msg')
                                raise self.mappings[curr](msg)
                        else:
                            # We don't have a match. Re-raise
                            raise e
                    else:
                        raise e # Why is this even happening?
            return decorates
        def add(self, mappings):
            
            for key, val in mappings.items():
                # Allows for easy overrides
                self.mappings[key] = val
                
        def remove(self, key):
            if key in self.mappings:
                del self.mappings[key]
            
    return Exceptable
    
# Except = fact('^(?P<type>[a-zA-Z]{1,})::(?P<msg>[a-zA-Z\. ]{0,})$')
# System = fact('^(?P<type>[a-zA-Z \.]{1,}) for (?P<msg>[a-zA-Z]{1,} [a-zA-Z]{1,})+$')
r = __factory__('^(?P<type>[a-zA-Z \.]{1,}) for (?P<msg>[a-zA-Z]{1,} [a-zA-Z_ ]{1,})+$')
class System(r):
    """System
    Curently know to catch the "permission denied for relation <foo>" errors.
    Unknown if this works with other db-specific fucntions at this time.
    """
    pass

r = __factory__('^(?P<type>[a-zA-Z]{1,})::(?P<msg>[a-zA-Z\. ]{0,})$')
class Except(r):
    """Except
    User-defined exception trapping. Traps all DB-level exceptions in the 
    format of Except::Message
    This type can be extended using the .add mechanism.
    """
    pass
    

        
"""
 Use via:

excepts = Except(ProgrammingError, {"PermissionError":PermissionError})

@excepts
def someFunc():
    
    db_operation()
"""
