from qiskit import QuantumCircuit,transpile
import random
import numpy as np
from qiskit.providers.fake_provider import ConfigurableFakeBackend
import math    

pi=math.pi




def     random_circuit(num_qubits, depth, base_gates):
    """
    Generates a random quantum circuit with the specified number of qubits,
    depth, and base gates.
    """
    
    backend= ConfigurableFakeBackend('custom',6, version=1,coupling_map= [[0,1], [1,0], [1,2], [2,1], [2,3], [3,2],[3,4],[1,4],[4,1],[4,3],[4,5],[5,4]],basis_gates=base_gates)
    #creating a custom fake backend 

    qc = QuantumCircuit(num_qubits)#creating Quantum Circuit qc
    qct=transpile(qc,backend)
    d= qct.depth()# using the tranpiled circuit to include the backend information
    
    while (d<depth):#if depth in any of the qubits surpasses the required depth loop stops
        
        gate = random.choice(base_gates)#choosing random gate
        q=random.randint(0,num_qubits-1)#choosing random Qubit q
        
        #single qubit gates
        if gate == 'u1':
            qc.u(0,0,2*pi*random.random(),q)
        elif gate == 'u2':
            qc.u(pi/2,2*pi*random.random(),2*pi*random.random(),q)
        elif gate == 'u3':
            qc.u(pi*random.random(),2*pi*random.random(),2*pi*random.random(),q)
        elif gate== 'id':
            qc.u(0,0,0,q)
        elif gate == 'h':
            qc.h(q)
        elif gate == 'x':
            qc.x(q)
        elif gate == 'y':
            qc.y(q)
        elif gate == 'z':
            qc.z(q)
        elif gate == 's':
            qc.s(q)  
        elif gate == 'sdg':
            qc.sdg(q)
        elif gate == 't':
            qc.t(q)
        elif gate == 'tdg':
            qc.tdg(q)
        
        #two Qubit gates   
        elif gate == 'cx':
            # Choose a random target qubit for the CNOT gate
            target_qubit = random.choice([t for t in range(num_qubits) if q != t])
            qc.cx(q, target_qubit)
        elif gate == 'cy':
            # Choose a random target qubit for the CY gate
            target_qubit = random.choice([t for t in range(num_qubits) if q != t])
            qc.cy(q, target_qubit)
        elif gate == 'cz':
            # Choose a random target qubit for the CZ gate
            target_qubit = random.choice([t for t in range(num_qubits) if q != t])
            qc.cz(q, target_qubit)
        elif gate == 'ch':
            # Choose a random target qubit for the ch gate
            target_qubit = random.choice([t for t in range(num_qubits) if q != t])
            qc.ch(q, target_qubit)
        elif gate == 'swap':
            # Choose a random target qubit for the swap gate
            target_qubit = random.choice([t for t in range(num_qubits) if q != t])
            qc.swap(q, target_qubit)
         
        else:
            raise ValueError(f"Invalid base gate: {gate}")#for any other unsuported gate
        
        qct=transpile(qc,backend)
        d= qct.depth()#itirating depth
    return qc

qc=random_circuit(6,7,['u1','u2','u3','cx','id'])
#genrating a random circuit by calling the function with some random basis gates
qc.draw('mpl')#drawing the circuit
