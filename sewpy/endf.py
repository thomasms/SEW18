from sewpy.numerical import getfloat


LINE_LENGTH         = 80
DATA_ENTRY_LENGTH   = 11
DATA_NENTRY         = 6
DATA_LENGTH         = DATA_NENTRY*DATA_ENTRY_LENGTH
MAT_LENGTH          = 4
MF_LENGTH           = 2
MT_LENGTH           = 3
NS_LENGTH           = 5

assert LINE_LENGTH == DATA_LENGTH + MAT_LENGTH + MF_LENGTH + MT_LENGTH + NS_LENGTH


class ENDFRecordReadError(Exception):
    pass

class ENDFRecord(object):
    """
        Base class for all ENDF record
    """
    def __init__(self):
        self.MAT = 0
        self.MF = 0
        self.MT = 0
        self.NS = 0
    
    def __str__(self):
        return "Mat: {}, MF: {}, MT: {}, NS: {}".format(self.MAT,
                                                        self.MF,
                                                        self.MT,
                                                        self.NS)
    def readLine(self, line):
        """
            Method to be implemented in subclasses
        """
        pass

    def read(self, line):
        if len(line) != LINE_LENGTH:
            raise ENDFRecordReadError("Expected {} character long string, got {}".format(LINE_LENGTH, len(line)))
        
        # metadata - mat, mf, mt, ns
        meta = line[DATA_LENGTH:LINE_LENGTH]
        def getMeta(start, end):
            return int(getfloat(meta[start:end].strip())) if meta[start:end].strip() else 0
        
        self.MAT = getMeta(0,
                           MAT_LENGTH)
        self.MF  = getMeta(MAT_LENGTH,
                           MAT_LENGTH+MF_LENGTH)
        self.MT  = getMeta(MAT_LENGTH+MF_LENGTH,
                           MAT_LENGTH+MF_LENGTH+MT_LENGTH)
        self.NS  = getMeta(MAT_LENGTH+MF_LENGTH+MT_LENGTH,
                           MAT_LENGTH+MF_LENGTH+MT_LENGTH+NS_LENGTH)

        self.readLine(line)


class ENDFTextRecord(ENDFRecord):
    """
        Class for all ENDF text entries
        [MAT, MF, MT/ HL] TEXT
        
        Fortran read:
        READ(LIB,10)HL,MAT,MF,MT,NS
     10 FORMAT(A66,I4,I2,I3,I5)
     
        For example:
        
137CS DECAY 30.04 Y   3                     I(min) = 0.0E+00 %    1809 1451   20
         Ex = 0.0         keV                     1 decay mode(s) 1809 1451   21
                                                                  1809 1451   22
137CS B- DECAY              Q =  1175.6300 keV       0.1700       1809 1451   23
    """
    def __init__(self):
        super(ENDFTextRecord, self).__init__()
        self.text = ""
    
    def __str__(self):
        return "Mat: {}, MF: {}, MT: {}, NS: {}, text: {}".format(self.MAT,
                                                                  self.MF,
                                                                  self.MT,
                                                                  self.NS,
                                                                  self.text)

    def readLine(self, line):
        pass


class ENDFContRecord(ENDFRecord):
    """
        Class for all ENDF CONT records
        [MAT,MF,MT/C1,C2,L1,L2,N1,N2]CONT
        
        Fortran read:
        READ(LIB,10)C1,C2,L1,L2,N1,N2,MAT,MF,MT,NS
     10 FORMAT(2E11.0,4I11,I4,I2,I3,I5)
     
        For example:
        
 9.47990+08 9.46728+05          0          0          6          01809 8457    2
    """
    def __init__(self):
        super(ENDFContRecord, self).__init__()
        self.C1 = 0.0
        self.C2 = 0.0
        self.L1 = 0
        self.L2 = 0
        self.N1 = 0
        self.N2 = 0
    
    def readLine(self, line):
        pass


class ENDFHeadRecord(ENDFRecord):
    """
        Class for all ENDF CONT records
        [MAT,MF,MT/ZA,AWR,L1,L2,N1,N2]CONT
        
        Fortran read:
        READ(LIB,10)ZA,AWR,L1,L2,N1,N2,MAT,MF,MT,NS
     10 FORMAT(2E11.0,4I11,I4,I2,I3,I5)
     
        For example:
        
 9.47990+08 9.46728+05          0          0          6          01809 8457    2
    """
    def __init__(self):
        super().__init__()
        self.ZA = 0.0
        self.AWR = 0.0
        self.L1 = 0.0
        self.L2 = 0.0
        self.N1 = 0.0
        self.N2 = 0.0
    
    def readLine(self, line):
        pass


class ENDFListRecord(object):
    """
        Class for all ENDF list records
        [MAT,MF,MT/ C1, C2, L1, L2, NPL, N2/ Bn] LIST
        
        For Fortran read:
        READ(LIB,10)C1,C2,L1,L2,NPL,N2,MAT,MF,MT,NS
     10 FORMAT(2E11.0,4I11,I4,I2,I3,I5)
        READ(LIB,20)(B(N),N=1,NPL)
     20 FORMAT(6E11.0)
        
        For example:
        
 3.50000+00 1.00000+00          0          0         12          21809 8457    4
 1.00000+00 0.00000+00 1.17563+06 1.70000+02 5.60055-02 0.00000+001809 8457    5
 1.00000+00 1.00000+00 5.13971+05 1.70000+02 9.43995-01 0.00000+001809 8457    6
    """
    def __init__(self):
        # self.listcont.N1 = NPL here
        self.listcont = ENDFContRecord()
        # a list of floats
        self.entries = []

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, index):
        return self.entries[index]
    
    def read(self, lines):
        """
            lines: a list of strings for each line
            
            must have the same MAT, MF, MT numbers
        """
        pass

