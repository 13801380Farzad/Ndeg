import streamlit as st
PASSWORD = "Staging2026"  # Passwort ändern nach Wunsch
st.title("Digital Ndeg-Staging Program - Login")
pw = st.text_input("Passwort", type="password")

if pw != PASSWORD:
    st.warning("Falsches Passwort. Zugriff verweigert.")
    st.stop()  # Stoppt die App hier, bis korrektes Passwort eingegeben wird

st.title("Digital Ndeg-Staging Program")
st.header("((Parkinson: LPC and Braak alpha synuclein))")
a1 = st.radio("McKeith Olfactory bulb", [0, 1, 2, 3, 4])
st.header("((🧠:green[Neocortex]))")
a= st.radio("McKeith Gyrus frontalis medius", [0, 1, 2, 3, 4])
b= st.radio("McKeith Lobulus parietalis inferior", [0, 1, 2, 3, 4])
c= st.radio("McKeith Gyrus temporalis superior", [0, 1, 2, 3, 4])
d= st.radio("McKeith Aria striata", [0, 1, 2, 3, 4])
st.header("((🧠:green[Limbic system]))")
e= st.radio("McKeith Gyrus cinguli (0-4)", [0, 1, 2, 3, 4])
f= st.radio("McKeith Amygdala", [0, 1, 2, 3, 4])
g= st.radio("McKeith CA1", [0, 1, 2, 3, 4])
h= st.radio("McKeith CA2", [0, 1, 2, 3, 4])
i= st.radio("McKeith CA3", [0, 1, 2, 3, 4])
j= st.radio("McKeith CA4", [0, 1, 2, 3, 4])
k= st.radio("McKeith Subiculum", [0, 1, 2, 3, 4])
l= st.radio("McKeith Fascia dentata", [0, 1, 2, 3, 4])
n= st.radio("McKeith Entorhinal cortex", [0, 1, 2, 3, 4])
m= st.radio("McKeith Transentorhinal cortex", [0, 1, 2, 3, 4])
o= st.radio("McKeith Piriform cortex", [0, 1, 2, 3, 4])
st.header("((🧠:green[Diencephalon]))")
p= st.radio("McKeith Thalamus", [0, 1, 2, 3, 4])
st.header("((🧠:green[Basal ganglia))")
q= st.radio("McKeith Globus pallidus", [0, 1, 2, 3, 4])
r= st.radio("McKeith Striatum", [0, 1, 2, 3, 4])
st.header("((🧠:green[Brainstem]))")
s= st.radio("McKeith Subtantia nigra", [0, 1, 2, 3, 4])
t= st.radio("McKeith Locus coeruleus", [0, 1, 2, 3, 4])
u= st.radio("McKeith dorsal motor nucleus of vagal nerve (dmX)", [0, 1, 2, 3, 4])
v= st.radio("McKeith Inferior olivary nucleus", [0, 1, 2, 3, 4])
st.header("((🧠:green[Cerebellum]))")
w= st.radio("McKeith Cerebellar molecular layer", [0, 1, 2, 3, 4])
x= st.radio("McKeith Nucleus dentatus", [0, 1, 2, 3, 4])

st.header("((Alzheimer: ABC Staging and Thal))")
st.header("ß-A4+ Plaques, Present or Absent")
aa= st.radio("Gyrus frontalis medius", ["Present", "Absent"])
bb= st.radio("CA1", ["Present", "Absent"])
cc= st.radio("Fascia dentata", ["Present", "Absent"])
dd= st.radio("CA4", ["Present", "Absent"])
ee= st.radio("Cerebellar molecular layer", ["Present", "Absent"])
ff= st.radio("Thalamus", ["Present", "Absent"])
gg= st.radio("Substantia nigra", ["Present", "Absent"])
hh= st.radio("Inferior olivary nucleus", ["Present", "Absent"])
ii= st.radio("Aria striata", ["Present", "Absent"])

st.header("Tau Positive Tangles, Present or Absent")
aaa= st.radio("Gyrus frontalis medius", ["Present", "Absent"], key="radio1")
bbb1= st.radio("Transentorhinal cortex", ["Present", "Absent"])
bbb2= st.radio("Entorhinal cortex", ["Present", "Absent"])
bbb= st.radio("CA1,CA2", ["Present", "Absent"])
ccc= st.radio("CA3,CA4,Subiculum", ["Present", "Absent"])
ddd= st.radio("Aria striata", ["Present", "Absent"], key="radio2")

st.header("CERAD neuritic plaque score")
s1= st.radio("Region: Gyrus temporalis medius/Superior, Gyrus frintalis medius", ["None", "Sparse", "Moderate", "Frequent"])


st.header("** Staging Results **")


if a>=1 or b>=1 or d>=1:
    st.write("** LPC:Neocortical Type")
elif c>=1 or e>=1 and (a==0 and b==0 and d==0):
    st.write("** LPC:Limbic Type")
elif u>=1 or s>=1 and (a==0 and b==0 and d==0 and c==0 and e==0):
    st.write("** LPC:Brainstem Predominant")
elif f>=1 and a==0 and b==0 and d==0 and c==0 and e==0 and u==0 and s==0:
    st.write("** LPC:Amygdala Predominant")
elif a1>=1 and a==0 and b==0 and d==0 and c==0 and e==0 and u==0 and s==0 and f==0:
    st.write("** LPC:Olfactory only")
else:
    st.write("Not valid input")


#Braak alpha synuclein
if a>=1 and d>=1:
    st.write("** Braak alpha synuclein Stage 6")
elif d==0 and a>=1:
    st.write("** Braak alpha synuclein Stage 5")
elif a==0 and m>=1 or h>=1:
    st.write("** Braak alpha synuclein Stage 4")
elif a==0 and m==0 and h==0 and s>=1:
    st.write("** Braak alpha synuclein Stage 3")
elif a==0 and m==0 and h==0 and s==0 and t>=1:
    st.write("** Braak alpha synuclein Stage 2")
elif a==0 and m==0 and h==0 and s==0 and t==0 and u>=1:
    st.write("** Braak alpha synuclein Stage 1")
elif a==0 and m==0 and h==0 and s==0 and t==0 and u==0:
    st.write("** Braak alpha synuclein Stage 0")
else:
    st.write("Not valid input")


#Thal

if ee == "Present" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 5")
elif ii == "Absent" or aa == "Absent":
    st.write("** Thal Phase 0")
elif (ee == "Absent" and bb == "Absent") and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 1")
elif ff == "Absent" and bb == "Present" and ee == "Absent" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 2")
elif dd == "Absent" and ff == "Present" and bb == "Present" and ee == "Absent" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 3")
elif gg == "Present" and dd == "Present" and ff == "Present" and bb == "Present" and ee == "Absent" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 4")
elif hh == "Present" and gg == "Absent" and dd == "Present" and ff == "Present" and bb == "Present" and ee == "Absent" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 4")
elif hh == "Absent" and gg == "Absent" and dd == "Present" and ff == "Present" and bb == "Present" and ee == "Absent" and (ii == "Present" or aa == "Present"):
    st.write("** Thal Phase 3")
else:
    st.write("Not valid input")


#Braak Tau

if ddd == "Present":
    st.write("** Braak Tau Stage 6")
elif aaa == "Present" and ddd == "Absent":
    st.write("** Braak Tau Stage 5")
elif ddd == "Absent" and aaa == "Absent" and ccc == "Present":
    st.write("** Braak Tau Stage 4")
elif ddd == "Absent" and aaa == "Absent" and ccc == "Absent" and bbb == "Present":
    st.write("** Braak Tau Stage 3")
elif ddd == "Absent" and aaa == "Absent" and ccc == "Absent" and bbb == "Absent" and bbb2 == "Present":
    print("** Braak Tau Stage 2")
elif st.write == "Absent" and aaa == "Absent" and ccc == "Absent" and bbb == "Absent" and bbb2 == "Absent" and bbb1 == "Present":
    st.write("** Braak Tau Stage 1")
else:
    st.write("Not valid input")


#A Stage

A_Stage = None
if aa == "Present" and bb == "Present" and cc == "Present" and dd == "Present":
    A_Stage = "A3"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Absent" and cc == "Absent" and dd == "Absent":
    A_Stage = "A0"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Absent" and cc == "Absent" and dd == "Present":
    A_Stage = "A3"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Absent" and cc == "Present" and dd == "Present":
    A_Stage = "A3"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Present" and cc == "Present" and dd == "Present":
    A_Stage = "A3"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Absent" and cc == "Present" and dd == "Absent":
    A_Stage = "A2"
    st.write(A_Stage)
elif aa == "Present" and bb == "Present" and cc == "Present" and dd == "Absent":
    A_Stage = "A2"
    st.write(A_Stage)
elif aa == "Absent" and bb == "Present" and cc == "Absent" and dd == "Absent":
    A_Stage = "A1"
    st.write(A_Stage)
elif aa == "Present" and bb == "Present" and cc == "Absent" and dd == "Absent":
    A_Stage = "A1"
    st.write(A_Stage)
else:
    st.write("Not valid input")



#B Stage

if aaa == "Present" and (bbb == "Present" or bbb1 == "Present" or bbb2 == "Present") and ccc == "Present" and ddd == "Present":
    B_Stage="B3"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Absent" or bbb1 == "Absent" or bbb2 == "Absent") and ccc == "Absent" and ddd == "Absent":
    B_Stage = "B0"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Absent" or bbb1 == "Absent" or bbb2 == "Absent") and ccc == "Absent" and ddd == "Present":
    B_Stage = "B3"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Absent" or bbb1 == "Absent" or bbb2 == "Absent") and ccc == "Present" and ddd == "Present":
    B_Stage = "B3"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Present" or bbb1 == "Present" or bbb2 == "Present") and ccc == "Present" and ddd == "Present":
    B_Stage = "B3"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Absent" or bbb1 == "Absent" or bbb2 == "Absent") and ccc == "Present" and ddd == "Present":
    B_Stage = "B2"
    st.write(B_Stage)
elif aaa == "Present" and (bbb == "Present" or bbb1 == "Present" or bbb2 == "Present") and ccc == "Present" and ddd == "Absent":
    B_Stage = "B2"
    st.write(B_Stage)
elif aaa == "Absent" and (bbb == "Present" or bbb1 == "Present" or bbb2 == "Present") and ccc == "Absent" and ddd == "Absent":
    B_Stage = "B1"
    st.write(B_Stage)
elif aaa == "Present" and (bbb == "Present" or bbb1 == "Present" or bbb2 == "Present") and ccc == "Absent" and ddd == "Absent":
    B_Stage = "B1"
    st.write(B_Stage)
else:
    st.write("Not valid input")

#C Stage

if s1 == "None":
    C_Stage="C0"
    st.write(C_Stage)
elif s1 == "Sparse":
    C_Stage = "C1"
    st.write(C_Stage)
elif s1 == "Moderate":
    C_Stage = "C2"
    st.write(C_Stage)
elif s1 == "Frequent":
    C_Stage = "C3"
    st.write(C_Stage)
else:
    st.write("Not valid input")


#AD Change

if A_Stage == "A0" and B_Stage in ["B0","B1","B2","B3"] and C_Stage == "C0":
    st.write("** AD Neuropathologic Change:Not AD")
elif A_Stage =="A1" and B_Stage in ["B0","B1","B2","B3"] and C_Stage in ["C0","C1"]:
    st.write("** AD Neuropathologic Change:Low")
elif A_Stage =="A1" and B_Stage in ["B0","B1"] and C_Stage in ["C2","C3"]:
    st.write("** AD Neuropathologic Change:Low")
elif A_Stage =="A1" and B_Stage in ["B2","B3"] and C_Stage in ["C2","C3"]:
    st.write("** AD Neuropathologic Change:Intermediate")
elif A_Stage =="A2" and B_Stage in ["B0","B1"] and C_Stage in ["C0","C1","C2","C3"]:
    st.write("** AD Neuropathologic Change:Low")
elif A_Stage =="A2" and B_Stage in ["B2","B3"] and C_Stage in ["C0","C1","C2","C3"]:
    st.write("** AD Neuropathologic Change:Intermediate")
elif A_Stage =="A3" and B_Stage in ["B0","B1"] and C_Stage in ["C0","C1"]:
    st.write("** AD Neuropathologic Change:Low")
elif A_Stage =="A3" and B_Stage in ["B2","B3"] and C_Stage in ["C0","C1"]:
    st.write("** AD Neuropathologic Change:Intermediate")
elif A_Stage =="A3" and B_Stage in ["B0","B1"] and C_Stage in ["C2","C3"]:
    st.write("** AD Neuropathologic Change:Low")
elif A_Stage =="A3" and B_Stage == "B2" and C_Stage in ["C2","C3"]:
    st.write("** AD Neuropathologic Change:Intermediate")
elif A_Stage =="A3" and B_Stage == "B3" and C_Stage in ["C2","C3"]:
    st.write("** AD Neuropathologic Change:High")
else:
    st.write("Not valid input")


st.markdown("**CAA Maximum Severity Staging**")
d1= st.radio("CAA Aria striata", ["NONE", "MILD", "MODERATE", "SEVERE"])
e1= st.radio("CAA Gyrus cinguli", ["NONE", "MILD", "MODERATE", "SEVERE"])
j1= st.radio("CAA Hippocampus", ["NONE", "MILD", "MODERATE", "SEVERE"])
severity = {
    "NONE": 0,
    "MILD": 1,
    "MODERATE": 2,
    "SEVERE": 3
}
values = [severity[d1], severity[e1], severity[j1]]
max_value = max(values)
stage_names = ["NONE", "MILD", "MODERATE", "SEVERE"]
st.write("** CAA Severity:", stage_names[max_value])
