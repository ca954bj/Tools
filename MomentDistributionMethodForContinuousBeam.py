
# =================================== Length of Each Span (From Left to Right) =================================
Length = [8, 10, 6]

# ================================== Young's Modulus of each span ==============================================
E = [29000, 29000, 29000, 29000, 29000]

# ================================== Moment of Inertia of each span ============================================
I = [4860, 4860, 4860, 4860, 4860]

# ================================== UDL of each span ==========================================================
UDL = [0, -12.6, -20]

# ================================== Concentrated Load (Act on mid-span) =======================================
CL = [-100, 0, 0]

# ================================== Support Type of Start and End =============================================
# Available options are 'fix', 'pin', 'roller'
SP = ['pin', 'fix']

# ================================= Tolerance ==========================
Tol = 0.1

# ======================================================== BEGIN COMPUTATION ===================================

class Element:
    instances = []
    def __init__(self, n, L, E, I, UDL, CL, start=False, end=False):
        self.n = n
        self.stiffness = float(E*I)/L
        self.start = start
        self.end = end
        self.UDL = float(UDL)
        self.CL = float(CL)
        self.L = float(L)
        self.distM1 = []
        self.distM2 = []
        self.CO1 = []
        self.CO2 = []
        if start:
            if SP[0] == 'fix':
                self.FEM1 = 1.0 / 12 * self.UDL * self.L * self.L + 1.0 / 8 * self.CL * self.L
                self.FEM2 = -self.FEM1
            elif SP[0] == 'pin':
                self.FEM1 = 0
                self.FEM2 = -1.0 / 8 * self.UDL * self.L * self.L - 3.0 / 16 * self.CL * self.L
            elif SP[0] == 'roller':
                self.FEM1 = - 1.0 / 6 * self.UDL * self.L * self.L - 1.0 / 8 * self.CL * self.L
                self.FEM2 = - 1.0 / 3 * self.UDL * self.L * self.L - 3.0 / 8 * self.CL * self.L

        elif end:
            if SP[1] == 'fix':
                self.FEM1 = 1.0 / 12 * self.UDL * self.L * self.L + 1.0 / 8 * self.CL * self.L
                self.FEM2 = -self.FEM1
            elif SP[1] == 'pin':
                self.FEM1 = 1.0 / 8 * self.UDL * self.L * self.L - 3.0 / 16 * self.CL * self.L
                self.FEM2 = 0
            elif SP[1] == 'roller':
                self.FEM1 = 1.0 / 3 * self.UDL * self.L * self.L - 1.0 / 8 * self.CL * self.L
                self.FEM2 = 1.0 / 6 * self.UDL * self.L * self.L - 3.0 / 8 * self.CL * self.L

        else:
            self.FEM1 = 1.0 / 12 * self.UDL * self.L * self.L + 1.0 / 8 * self.CL * self.L
            self.FEM2 = -self.FEM1


        Element.instances.append(self)

    def AddDistributionFactor1(self, df1):
        self.df1 = df1

    def AddDistributionFactor2(self, df2):
        self.df2 = df2

    def AddDistributionM1(self, M1):
        self.distM1.append(M1)

    def AddDistributionM2(self, M2):
        self.distM2.append(M2)

    def AddCO(self):
        if self.start:
            if SP[0] == 'pin':
                self.CO1.append(0)
            elif SP[0] == 'roller':
                self.CO1.append(-self.distM2[-1])
            elif SP[0] == 'fix':
                self.CO1.append(self.distM2[-1]*0.5)
        elif self.end:
            if SP[1] == 'pin':
                self.CO2.append(0)
            elif SP[1] == 'roller':
                self.CO2.append(-self.distM1[-1])
            elif SP[1] == 'fix':
                self.CO2.append(self.distM1[-1]*0.5)

        else:
            self.CO1.append(self.distM2[-1]*0.5)
            self.CO2.append(self.distM1[-1]*0.5)

    def FinalMoment(self):
        self.FiM1 = 0
        self.FiM2 = 0
        self.FiM1 += self.FEM1
        self.FiM1 += sum(self.distM1)
        self.FiM1 += sum(self.CO1)
        self.FiM2 += self.FEM2
        self.FiM2 += sum(self.distM2)
        self.FiM2 += sum(self.CO2)

class Analysis:
    def __init__(self):
        # =================== Add Elements ===============================
        EleNumber = len(Length)
        for i in range(0, EleNumber):
            if i == 0:
                Element(i + 1, Length[i], E[i], I[i], UDL[i], CL[i], start=True)
            elif i == EleNumber - 1:
                Element(i + 1, Length[i], E[i], I[i], UDL[i], CL[i], end=True)
            else:
                Element(i + 1, Length[i], E[i], I[i], UDL[i], CL[i])

        # =================== Calculate Distribution Factors ============

        print("===================== Distribution Factors ===========================\n")
        for i in range(0, EleNumber - 1):
            k1 = Element.instances[i].stiffness
            k2 = Element.instances[i + 1].stiffness
            if i == 0:
                if SP[0] == 'pin':
                    k1 = 3*k1
                    k2 = 4*k2
                elif SP[0] == 'fix':
                    k1 = 4*k1
                    k2 = 4*k2
            elif i == EleNumber - 2:
                if SP[1] == 'pin':
                    k2 = 3*k2
                    k1 = 4*k1
                elif SP[1] == 'fix':
                    k2 = 4*k2
                    k1 = 4*k1
            else:
                k1 = 4*k1
                k2 = 4*k2

            df1 = k1 / (k1 + k2)
            df2 = k2 / (k1 + k2)
            Element.instances[i].AddDistributionFactor2(df1)
            Element.instances[i + 1].AddDistributionFactor1(df2)
            print("Distribution Factor of Element %d at right side is %f" % (Element.instances[i].n, df1))
            print("Distribution Factor of Element %d at left side is %f\n" % (Element.instances[i + 1].n, df2))


        for i in range(0, EleNumber - 1):
            Ele1 = Element.instances[i]
            Ele2 = Element.instances[i + 1]
            UBM = Ele1.FEM2 + Ele2.FEM1
            Dist1 = -UBM*Ele1.df2
            Dist2 = -UBM*Ele2.df1
            Ele1.AddDistributionM2(Dist1)
            Ele2.AddDistributionM1(Dist2)

        for i in range(0, EleNumber):
            Element.instances[i].AddCO()

        # =======================================
        COMoment = 0
        for i in range(0, EleNumber):
            if len(Element.instances[i].CO1) > 0:
                temp = Element.instances[i].CO1[-1]
                if abs(temp) > COMoment:
                    COMoment = temp
            if len(Element.instances[i].CO2) > 0:
                temp = Element.instances[i].CO2[-1]
                if abs(temp) > COMoment:
                    COMoment = temp

        print("RE = %f" % COMoment)
        iternum = 0

        while abs(COMoment) > Tol:
            iternum += 1
            for i in range(0, EleNumber - 1):
                Ele1 = Element.instances[i]
                Ele2 = Element.instances[i + 1]
                UBM = 0
                if len(Ele1.CO2) > 0:
                    UBM += Ele1.CO2[-1]
                if len(Ele2.CO1) > 0:
                    UBM += Ele2.CO1[-1]
                Dist1 = -UBM * Ele1.df2
                Dist2 = -UBM * Ele2.df1
                Ele1.AddDistributionM2(Dist1)
                Ele2.AddDistributionM1(Dist2)

            for i in range(0, EleNumber):
                Element.instances[i].AddCO()

            COMoment = 0
            for i in range(0, EleNumber):
                if len(Element.instances[i].CO1) > 0:
                    temp = Element.instances[i].CO1[-1]
                    if abs(temp) > COMoment:
                        COMoment = temp
                if len(Element.instances[i].CO2) > 0:
                    temp = Element.instances[i].CO2[-1]
                    if abs(temp) > COMoment:
                        COMoment = temp
            print("RE = %f" % COMoment)

        # ======================================

        for i in range(0, EleNumber - 1):
            Ele1 = Element.instances[i]
            Ele2 = Element.instances[i + 1]
            UBM = 0
            if len(Ele1.CO2) > 0:
                UBM += Ele1.CO2[-1]
            if len(Ele2.CO1) > 0:
                UBM += Ele2.CO1[-1]
            Dist1 = -UBM * Ele1.df2
            Dist2 = -UBM * Ele2.df1
            Ele1.AddDistributionM2(Dist1)
            Ele2.AddDistributionM1(Dist2)


        # ======================== Summation of Moments =============================

        print("Results:")
        for i in range(0, EleNumber):
            Element.instances[i].FinalMoment()
            print(Element.instances[i].FiM1)
            print(Element.instances[i].FiM2)

        # ========================= Show Process ====================================
        print("Process:")
        print("DF")
        for i in range(0, EleNumber):
            if i == 0:
                print(Element.instances[i].df2)
                print('\n')
            elif i == EleNumber - 1:
                print(Element.instances[i].df1)
                print('\n')
            else:
                print(Element.instances[i].df1)
                print(Element.instances[i].df2)
                print('\n')

        print("FEM")
        for i in range(0, EleNumber):
            print(-Element.instances[i].FEM1, -Element.instances[i].FEM2)

        print('Dist')
        for i in range(0, EleNumber):
            print(Element.instances[i].distM1, Element.instances[i].distM2)

        print('CO')
        for i in range(0, EleNumber):
            print(Element.instances[i].CO1, Element.instances[i].CO2)

        print("Iteration Number = %d" % iternum)
Analysis()
