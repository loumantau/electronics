class Solver():
 
    @staticmethod 
    def voltage(current, resistance):
        return current * resistance

    @staticmethod
    def current(voltage, resistance):
        return voltage / resistance

    def resistance(voltage, current):
        return voltage / current    
     
    @staticmethod
    def ohms_law(solve_for, voltage=None, current=None, resistance=None):
        method = {
            'voltage': Solver.voltage,
            'current': Solver.current,
            'resistance': Solver.resistance,
        } 

        def solve(solve_for):
            method[solve_for](solve_for, voltage=None, current=None, resistance=None)   

        result = solve(solve_for)

        return result