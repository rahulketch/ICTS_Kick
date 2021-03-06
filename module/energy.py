import harmonics
import numpy as np

def getRemnantMass(Sim):
	de = 0
	for l in range(2,9):
		for m in range(-l,l+1):
			de = de + Sim.ALM(l,m)*np.conj(Sim.ALM(l,m))
	E = np.cumsum(de*Sim.dt)/(16*np.pi) 
	Radiated_Energy = E[-1] 
	final_mass = np.real(Sim.metadata.initial_mass - Radiated_Energy) 
	return final_mass

def getRemnantSpin(Sim):
	def f(l,m):
		return np.sqrt((l-m)*(l+m+1))
	djx = (0+0j)
	djy = djx
	djz = djx
	for l in range(2,9):
		for m in range(-l,l+1):
			djx = djx + np.imag(Sim.Hcomp(l,m)*(f(l,m)*np.conj(Sim.ALM(l,m+1)) + f(l,-m)*np.conj(Sim.ALM(l,m-1))))
			djy = djy - np.real(Sim.Hcomp(l,m)*(f(l,m)*np.conj(Sim.ALM(l,m+1)) - f(l,-m)*np.conj(Sim.ALM(l,m-1))))
			djz = djz + np.imag(m*Sim.Hcomp(l,m)*np.conj(Sim.ALM(l,m)))
	JX = np.real(np.cumsum(djx*Sim.dt)/(32*np.pi))
	JY = np.real(np.cumsum(djy*Sim.dt)/(32*np.pi))
	JZ = np.real(np.cumsum(djz*Sim.dt)/(16*np.pi))
	J = np.array([JX,JY,JZ])
	Radiated_J = np.array([JX[-1],JY[-1],JZ[-1]])
	final_spin = Sim.metadata.initial_j - Radiated_J
	return final_spin	

def getKick(Sim):
	def norm(vector):
		return np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])
	speed_of_light = 299792.458
	def a(l,m):
		return np.sqrt((1.0+0.0j)*(l-m)*(l+m+1.0))/(l*(l+1.0))
	def b(l,m):
		return (np.sqrt((1+0.0j)*(l-2.0)*(l+2.0)*(l+m)*(l+m-1.0)/(2.0*l-1.0)/(2.0*l+1.0)))/(2.0*l)
	def c(l,m):
		return 2.0*m/(l*(l+1.0))
	def d(l,m):
		return (np.sqrt((1.0+0.0j)*(l-2.0)*(l+2.0)*(l-m)*(l+m)/(2.0*l-1.0)/(2.0*l+1)))/l

	dp_plus = (0.0+0.0j)
	dp_z = dp_plus
	for l in range(2,9):
		for m in range(-l,l+1):
			dp_plus = dp_plus+Sim.ALM(l,m)*(a(l,m)*np.conj(Sim.ALM(l,m+1)) + b(l,-m)*np.conj(Sim.ALM(l-1,m+1)) - b(l+1,m+1)*np.conj(Sim.ALM(l+1,m+1)))
			dp_z = dp_z + Sim.ALM(l,m)*(c(l,m)*np.conj(Sim.ALM(l,m)) + d(l,m)*np.conj(Sim.ALM(l-1,m)) + d(l+1,m)*np.conj(Sim.ALM(l+1,m)))
	p_plus = np.cumsum(dp_plus*Sim.dt)/(8*np.pi)
	PZ = np.real(np.cumsum(dp_z*Sim.dt)/(16*np.pi))
	PX = np.real(p_plus)
	PY = np.imag(p_plus)
	P = np.array([PX,PY,PZ])
	Radiated_P = np.array([PX[-1],PY[-1],PZ[-1]])
	Kick = -1 * Radiated_P/Sim.metadata.remnant_mass * speed_of_light
	return norm(Kick)

