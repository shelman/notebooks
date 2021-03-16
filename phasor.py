from __future__ import annotations

import math


class Phasor:
    
    @classmethod
    def from_rect(cls, real: float, imaginary: float) -> Phasor:
        return cls(real, imaginary, math.sqrt(real*real + imaginary*imaginary), math.atan(imaginary/real) if real != 0 else math.pi / 2)
    
    @classmethod
    def from_radius_and_phase(cls, radius: float, phase: float) -> Phasor:
        return cls(radius * math.cos(phase), radius * math.sin(phase), radius, phase)
        
    @classmethod
    def unit_imaginary(cls) -> Phasor:
        return cls.from_radius_and_phase(1.0, math.pi / 2.0)
    
    @classmethod
    def add(cls, p1: Phasor, p2: Phasor) -> Phasor:
        return cls.from_rect(p1.real + p2.real, p1.imaginary + p2.imaginary)
    
    @classmethod
    def subtract(cls, p1: Phasor, p2: Phasor) -> Phasor:
        return cls.from_rect(p1.real - p2.real, p1.imaginary - p2.imaginary)
    
    @classmethod
    def multiply(cls, p1: Phasor, p2: Phasor) -> Phasor:
        return cls.from_radius_and_phase(p1.radius * p2.radius, p1.phase + p2.phase)
    
    @classmethod
    def divide(cls, p1: Phasor, p2: Phasor) -> Phasor:
        return cls.from_radius_and_phase(p1.radius / p2.radius, p1.phase - p2.phase)
    
    @classmethod
    def reciprocal(cls, p: Phasor) -> Phasor:
        return cls.from_radius_and_phase(1.0 / p.radius, -1.0 * p.phase)
    
    @classmethod
    def sqrt(cls, p: Phasor) -> Phasor:
        return cls.from_radius_and_phase(math.sqrt(p.radius), p.phase / 2.0)
    
    @classmethod
    def complex_conjugate(cls, p: Phasor) -> Phasor:
        return cls.from_rect(p.real, -1.0 * p.imaginary)
    
    @classmethod
    def scale(cls, p: Phasor, factor: float) -> Phasor:
        return cls.from_radius_and_phase(p.radius * factor, p.phase)
    
    def __init__(self, real: float, imaginary: float, radius: float, phase: float):
        self.real = real
        self.imaginary = imaginary
        self.radius = radius
        self.phase = phase
        
    def __repr__(self) -> str:
        return f'Phasor(real = {round(self.real, 4)}, imaginary = {round(self.imaginary, 4)}, radius = {round(self.radius, 8)}, phase = {round(math.degrees(self.phase), 4)} degrees)'