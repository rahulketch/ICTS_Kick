import numpy as np 
def bbh_recoil_HLZ_aligned_components(q, chi1para, chi2para):
    """ 
    Calculate the magnitude of the recoil of the final BH resulting from the 
    merger of two black holes with aligned spins using the RIT
    group's fit given in Eqs. (2A), (12), (17), and (18) (and parameter values from Table VI) of Healy, Lousto, and Zlochower, PRD 90, 104004 (2013).

    q: mass ratio (here m1/m2--the code automatically converts to the q < 1 convention required by the fit)
    chi1para: the component of the dimensionless spin of the *lighter* black hole along the angular momentum (z)
    chi2para: the component of the dimensionless spin of the *heavier* black hole along the angular momentum (z)
    """

    # Check that the spins are at most extremal

    if abs(chi1para) > 1:
        print("WARNING: aligned component of spin 1 has a magnitude of %3f\n > 1" %abs(chi1para))
    if abs(chi2para) > 1:
        print("WARNING: aligned component of spin 2 has a magnitude of %3f\n > 1" %abs(chi2para))

    # First compute eta and then convert the mass ratio to the \leq 1 convention used in the fit, if it's not already in it. Also reverse the spins to correspond to this convention, if necessary
    eta = q/(1.+q)**2. 
    if q > 1.:
        q = 1./q
    chi2para, chi1para = chi1para, chi2para
    dm = (q -1.)/(q + 1.) # dm is \delta m

    dm2 = dm*dm
    dm3 = dm2*dm

    # Now compute the spin combinations used in the fit
    Stpara = (chi2para + chi1para*q**2.)/(1. + q)**2.
    Deltatpara = (chi2para - q*chi1para)/(1. + q)

    Stpara2 = Stpara*Stpara
    Stpara3 = Stpara2*Stpara

    Deltatpara2 = Deltatpara*Deltatpara
    Deltatpara3 = Deltatpara2*Deltatpara

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Compute the magnitude of the recoil 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # Define the relevant constants from the fit
    Am = 12000.
    Bm = -0.93
    H = 7367.250029 # \pm 66.122336
    H2a = -1.626094 # \pm 0.053888
    H2b = -0.578177 # \pm 0.055790
    H3a = -0.717370 # \pm 0.077605
    H3b = -2.244229 # \pm 0.137982
    H3c = -1.221517 # \pm 0.176699
    H3d = -0.002325 # \pm 0.021612
    H3e = -1.064708 # \pm 0.133021
    H4a = -0.579599 # \pm 0.297351
    H4b = -0.455986 # \pm 0.302432
    H4c =  0.010963 # \pm 0.174289
    H4d =  1.542924 # \pm 0.274459
    H4e = -4.735367 # \pm 0.430869 
    H4f = -0.284062 # \pm 0.174087

    a   =  2.611988 # \pm 0.028327
    b   =  1.383778 # \pm 0.092915
    c   =  0.549758 # \pm 0.113300

    # Compute the cosine of xi

    cxi = np.cos(a + b*Stpara + c*dm*Deltatpara)
    
    # Compute the sine of xi
    sxi = np.sin(a + b*Stpara + c*dm*Deltatpara)

    # Compute the two contributions to the recoil. Here we take H_S = 0, since there's not a value given in the paper.

    Vm = Am*eta**2.*((1.-q)/(1.+q))*(1 + Bm*eta)

    VperpH2 = H2a*Stpara*dm + H2b*Deltatpara*Stpara
    VperpH3 = H3a*Deltatpara2*dm + H3b*Stpara2*dm + H3c*Deltatpara*Stpara2 + H3d*Deltatpara3 + H3e*Deltatpara*dm2
    VperpH4 = H4a*Stpara*Deltatpara2*dm + H4b*Stpara3*dm + H4c*Stpara*dm3 + H4d*Deltatpara*Stpara*dm2 + H4e*Deltatpara*Stpara3 + H4f*Stpara*Deltatpara3

    Vperp = H*eta**2*(Deltatpara + VperpH2 + VperpH3 + VperpH4)
    
    #returns the 3 componenents of the kick
    return np.array([Vm + Vperp * cxi, Vperp * sxi, 0])
    #return (Vm**2. + 2.*Vm*Vperp*cxi + Vperp**2.)**0.5



def bbh_recoil_HLZ_aligned(q, chi1para, chi2para):
    """ 
    Calculate the magnitude of the recoil of the final BH resulting from the 
    merger of two black holes with aligned spins using the RIT
    group's fit given in Eqs. (2A), (12), (17), and (18) (and parameter values from Table VI) of Healy, Lousto, and Zlochower, PRD 90, 104004 (2013).

    q: mass ratio (here m1/m2--the code automatically converts to the q < 1 convention required by the fit)
    chi1para: the component of the dimensionless spin of the *lighter* black hole along the angular momentum (z)
    chi2para: the component of the dimensionless spin of the *heavier* black hole along the angular momentum (z)
    """

    # Check that the spins are at most extremal

    if abs(chi1para) > 1:
        print("WARNING: aligned component of spin 1 has a magnitude of %3f\n > 1" %abs(chi1para))
    if abs(chi2para) > 1:
        print("WARNING: aligned component of spin 2 has a magnitude of %3f\n > 1" %abs(chi2para))

    # First compute eta and then convert the mass ratio to the \leq 1 convention used in the fit, if it's not already in it. Also reverse the spins to correspond to this convention, if necessary
    eta = q/(1.+q)**2. 
    if q > 1.:
        q = 1./q
    chi2para, chi1para = chi1para, chi2para
    dm = (q -1.)/(q + 1.) # dm is \delta m

    dm2 = dm*dm
    dm3 = dm2*dm

    # Now compute the spin combinations used in the fit
    Stpara = (chi2para + chi1para*q**2.)/(1. + q)**2.
    Deltatpara = (chi2para - q*chi1para)/(1. + q)

    Stpara2 = Stpara*Stpara
    Stpara3 = Stpara2*Stpara

    Deltatpara2 = Deltatpara*Deltatpara
    Deltatpara3 = Deltatpara2*Deltatpara

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Compute the magnitude of the recoil 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # Define the relevant constants from the fit
    Am = 12000.
    Bm = -0.93
    H = 7367.250029 # \pm 66.122336
    H2a = -1.626094 # \pm 0.053888
    H2b = -0.578177 # \pm 0.055790
    H3a = -0.717370 # \pm 0.077605
    H3b = -2.244229 # \pm 0.137982
    H3c = -1.221517 # \pm 0.176699
    H3d = -0.002325 # \pm 0.021612
    H3e = -1.064708 # \pm 0.133021
    H4a = -0.579599 # \pm 0.297351
    H4b = -0.455986 # \pm 0.302432
    H4c =  0.010963 # \pm 0.174289
    H4d =  1.542924 # \pm 0.274459
    H4e = -4.735367 # \pm 0.430869 
    H4f = -0.284062 # \pm 0.174087

    a   =  2.611988 # \pm 0.028327
    b   =  1.383778 # \pm 0.092915
    c   =  0.549758 # \pm 0.113300

    # Compute the cosine of xi

    cxi = np.cos(a + b*Stpara + c*dm*Deltatpara)

    # Compute the two contributions to the recoil. Here we take H_S = 0, since there's not a value given in the paper.

    Vm = Am*eta**2.*((1.-q)/(1.+q))*(1 + Bm*eta)

    VperpH2 = H2a*Stpara*dm + H2b*Deltatpara*Stpara
    VperpH3 = H3a*Deltatpara2*dm + H3b*Stpara2*dm + H3c*Deltatpara*Stpara2 + H3d*Deltatpara3 + H3e*Deltatpara*dm2
    VperpH4 = H4a*Stpara*Deltatpara2*dm + H4b*Stpara3*dm + H4c*Stpara*dm3 + H4d*Deltatpara*Stpara*dm2 + H4e*Deltatpara*Stpara3 + H4f*Stpara*Deltatpara3

    Vperp = H*eta**2*(Deltatpara + VperpH2 + VperpH3 + VperpH4)

    return (Vm**2. + 2.*Vm*Vperp*cxi + Vperp**2.)**0.5


