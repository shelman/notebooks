from typing import List
from functools import reduce
import math

from phasor import Phasor
from sinusoid import Sinusoid


class Element:
    
    def impedance(self, frequency: float) -> Phasor:
        pass
    
    def current(self, voltage: Sinusoid) -> Sinusoid:
        return Sinusoid.from_phasor(
            Phasor.divide(voltage.to_phasor(), self.impedance(voltage.angular_frequency)),
            voltage.angular_frequency,
        )
    
    def voltage(self, current: Sinusoid) -> Sinusoid:
        return Sinusoid.from_phasor(
            Phasor.multiply(current.to_phasor(), self.impedance(current.angular_frequency)), 
            current.angular_frequency,
        )
    

class ParallelCombination(Element):
    
    def __init__(self, elements: List[Element]):
        self.elements = elements
    

class SeriesCombination(Element):
    
    def __init__(self, elements: List[Element]):
        self.elements = elements
        
    def impedance(self, frequency: float) -> Phasor:
        imp = Phasor.from_rect(0, 0)
        for element in self.elements:
            imp = Phasor.add(imp, element.impedance(frequency))
        return imp


class Resistor(Element):
    
    def __init__(self, resistance: float):
        self.resistance = resistance
        
    def impedance(self, frequency: float) -> Phasor:
        return Phasor.from_rect(self.resistance, 0)

    def __repr__(self) -> str:
        return f'Resistor(resistance = {self.resistance})'
    
    
class Inductor(Element):
    
    def __init__(self, inductance: float):
        self.inductance = inductance
        
    def impedance(self, frequency: float) -> Phasor:
        return Phasor.scale(Phasor.from_radius_and_phase(1, math.pi / 2), self.inductance * frequency)
    
    def __repr__(self) -> str:
        return f'Inductor(inductance = {self.inductance})'
    

class Capacitor(Element):
    
    def __init__(self, capacitance: float):
        self.capacitance = capacitance
        
    def impedance(self, frequency: float) -> Phasor:
        return Phasor.reciprocal(Phasor.scale(Phasor.from_radius_and_phase(1, math.pi / 2), self.capacitance * frequency))
        
    def __repr__(self) -> str:
        return f'Capacitor(capacitance = {self.capacitance})'