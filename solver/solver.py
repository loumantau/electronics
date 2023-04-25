from scipy.constants import physical_constants

class Solver():
 
    @staticmethod 
    def voltage(**kwargs):
        current = kwargs.get('current')
        resistance = kwargs.get('resistance')
        return current * resistance

    @staticmethod
    def current(**kwargs):
        voltage = kwargs.get('voltage')
        resistance = kwargs.get('resistance')
        return voltage / resistance

    @staticmethod
    def resistance(**kwargs):
        voltage = kwargs.get('voltage')
        current = kwargs.get('current')
        return voltage / current    
     
    @staticmethod
    def ohms_law(solve_for, **kwargs):
        method = {
            'voltage': Solver.voltage,
            'current': Solver.current,
            'resistance': Solver.resistance,
        } 

        result = method[solve_for](**kwargs)

        return result
