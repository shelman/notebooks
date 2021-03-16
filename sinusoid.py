from __future__ import annotations

import math
from phasor import Phasor


class Sinusoid:
    
    @classmethod
    def sine_to_cosine(cls, s: Sinusoid) -> Sinusoid:
        return Sinusoid(s.amplitude, s.angular_frequency, s.phase - (math.pi / 2))
    
    @classmethod
    def cosine_to_sine(cls, s: Sinusoid) -> Sinusoid:
        return Sinusoid(s.amplitude, s.angular_frequency, s.phase + (math.pi / 2))
    
    @classmethod
    def from_phasor(self, phasor: Phasor, angular_frequency: float) -> Sinusoid:
        return Sinusoid(phasor.radius, angular_frequency, phasor.phase)
    
    def __init__(self, amplitude: float, angular_frequency: float, phase: float):
        self.amplitude = amplitude
        self.angular_frequency = angular_frequency
        self.phase = phase
        
    def frequency(self) -> float:
        return self.angular_frequency / (2.0 * math.pi)
    
    def period(self) -> float:
        return 1.0 / self.frequency()
        
    def to_phasor(self) -> Phasor:
        return Phasor.from_radius_and_phase(self.amplitude, self.phase)
    
    def __repr__(self) -> str:
        return f'Sinusoid(amplitude = {self.amplitude}, angular_frequency = {self.angular_frequency}, phase = {round(math.degrees(self.phase), 4)} degrees)'