from decimal import Decimal
from constants.physics import *


def ohms_law(solve_for, **kwargs):

    def voltage(**kwargs):
        current = Decimal(kwargs.get('current'))
        resistance = Decimal(kwargs.get('resistance')) 
        return (current * resistance) * V
 

    def current(**kwargs):
        voltage = Decimal(kwargs.get('voltage'))
        resistance = Decimal(kwargs.get('resistance'))
        return (voltage / resistance) * A

    
    def resistance(**kwargs):
        voltage = Decimal(kwargs.get('voltage'))
        current = Decimal(kwargs.get('current'))
        return (voltage / current) * Ω    

    methods = {
        'voltage': voltage,
        'current': current,
        'resistance': resistance,
    } 

    result = methods[solve_for](**kwargs)
    return result