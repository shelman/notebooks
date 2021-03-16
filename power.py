import math

from phasor import Phasor
from sinusoid import Sinusoid


class Power:
    
    @classmethod
    def average_power(cls, voltage: Sinusoid, current: Sinusoid) -> float:
        return 0.5 * voltage.amplitude * current.amplitude * math.cos(voltage.phase - current.phase)
    
    @classmethod
    def instantaneous_power(cls, voltage: Sinusoid, current: Sinusoid, time: float) -> float:
        return cls.average_power(voltage, current) + (0.5 * voltage.amplitude * current.amplitude * 
                                                      math.cos(2.0 * voltage.angular_frequency * time + voltage.phase + current.phase))

    @classmethod
    def max_average_power_transfer(cls, source_voltage: Phasor, source_impedance: Phasor) -> float:
        return (source_voltage.radius * source_voltage.radius) / (8.0 * source_impedance.real)



